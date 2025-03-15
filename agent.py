from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver
from typing import TypedDict, Annotated
import operator
from langchain_core.messages import AnyMessage, SystemMessage,ToolMessage

#An Agent State class that keep state of the agent while it answers a query
class chat_Agent_State(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]

#-----------------------------------------------------------------------------
#An agent class that manages all agentic interactions
class chat_Agent:

    #Setup the agent graph, tools and memory
    def __init__(self, model, tools, system_prompt, debug):
        
        self.system_prompt=system_prompt
        self.debug=debug

        #Setup the graph for the agent manually
        agent_graph=StateGraph(chat_Agent_State)
        agent_graph.add_node("llm",self.call_llm)
        agent_graph.add_node("tools",self.call_tools)
        agent_graph.add_conditional_edges(
            "llm",
            self.is_tool_call,
            {True: "tools", False: END }
        )
        agent_graph.add_edge("tools","llm")
        #Set where there graph starts
        agent_graph.set_entry_point("llm")

        #Add chat memory
        self.memory=MemorySaver()
        #compile the graph
        self.agent_graph = agent_graph.compile(checkpointer=self.memory)

        #Setup tools
        self.tools = { tool.name : tool for tool in tools }
        if self.debug:
            print("\nTools loaded :", self.tools)
            
        #attach tools to model
        self.model=model.bind_tools(tools)


    #Call the LLM with the messages to get next action/result
    def call_llm(self, state: chat_Agent_State):
        messages = state["messages"]

        # Add system prompt only if it's not already in the messages
        if self.system_prompt and not any(isinstance(msg, SystemMessage) for msg in messages):
            messages = [SystemMessage(content=self.system_prompt)] + messages

        # Invoke the model with the message history
        result = self.model.invoke(messages)
        if self.debug:
            print(f"\nLLM Returned : {result}")

        # Return the LLM output
        return {"messages": [result]}
    
    #Check if the next action is a tool call.
    def is_tool_call(self, state:chat_Agent_State):
        last_message = state["messages"][-1]
        #print("Last result from LLM : ", last_message)
        #If tool action is requested
        if len(last_message.tool_calls) > 0 :
            return True
        else:
            return False

    #Execute the tool requested with the given parameters
    def call_tools(self, state: chat_Agent_State):
        #Get the last message from the LLM
        tool_calls = state["messages"][-1].tool_calls
        results = []

        if self.debug:
           print(f"\nTool Calls: {tool_calls}")

        # Process all tool calls
        for tool in tool_calls:
            if tool["name"] not in self.tools:
                print(f"Unknown tool name {tool}")
                result = "Invalid tool found. Please retry"
            else:
                # Call the tool and collect results
                result = self.tools[tool["name"]].invoke(tool["args"])

            # Append results to the list of tool results
            results.append(ToolMessage(
                tool_call_id=tool['id'],
                name=tool['name'],
                content=str(result)
            ))

        if self.debug:
            print(f"\nTools returned {results}")

        # Return all tool results
        return {"messages": results}

#-----------------------------------------------------------------------------