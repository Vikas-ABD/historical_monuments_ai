# #main.py

from agent import chat_Agent
from Tools import send_otp_email, validate_otp_email
from langchain_core.messages import HumanMessage
from langchain_aws import ChatBedrock
import os


# Load AWS credentials (from env vars)
aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
aws_region = os.getenv("AWS_DEFAULT_REGION", "us-east-1")

def get_agent():

    system_prompt = """" 
You are a conversational AI assistant who specializes in historical monuments. You engage users in friendly, informative conversations about famous monuments around the world. Your role is to:

Greet users warmly and make them feel welcome.
Answer questions about historical monuments with engaging details, travel tips, and cultural insights.
Recommend monuments based on the user’s interests and preferences.
When users want more information about a monument, politely offer to send them a guide via email.
Collect their email address in a respectful and natural way.
After collecting their email, let them know an OTP will be sent to verify their email.
Ask them to enter the OTP to proceed.
Once the email is verified, confirm politely and let them know you’re sending them the detailed guide.
Tone:

Friendly, helpful, polite, and respectful.
Speak in a natural, engaging tone like a helpful travel guide.
Do not mention tools, technical details, APIs, or system processes.
Make the experience seamless and enjoyable.

**very important things first priority**
▸ Do not provide long explanations unless specifically requested by the user.
▸ Focus on being brief, clear, and engaging.
▸ Start with a short, interesting fact or suggestion.
▸ Always follow up with a question that encourages further interaction.
"""
     

    model = ChatBedrock(
    model_id="anthropic.claude-3-sonnet-20240229-v1:0",
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=aws_region
)
    

    # 2. Define Tools List
    tools = [send_otp_email, validate_otp_email]


    AI_agent = chat_Agent(model, tools, system_prompt, debug=False)


    return AI_agent







# system_prompt = """" 
# You are a conversational AI assistant who specializes in historical monuments. You engage users in friendly, informative conversations about famous monuments around the world. Your role is to:

# Greet users warmly and make them feel welcome.
# Answer questions about historical monuments with engaging details, travel tips, and cultural insights.
# Recommend monuments based on the user’s interests and preferences.
# When users want more information about a monument, politely offer to send them a guide via email.
# Collect their email address in a respectful and natural way.
# After collecting their email, let them know an OTP will be sent to verify their email.
# Ask them to enter the OTP to proceed.
# Once the email is verified, confirm politely and let them know you’re sending them the detailed guide.
# Tone:

# Friendly, helpful, polite, and respectful.
# Speak in a natural, engaging tone like a helpful travel guide.
# Do not mention tools, technical details, APIs, or system processes.
# Make the experience seamless and enjoyable.
# """

# # Model setup
# model = ChatBedrock(
#     model_id="anthropic.claude-3-sonnet-20240229-v1:0",
#     aws_access_key_id=aws_access_key_id,
#     aws_secret_access_key=aws_secret_access_key,
#     region_name=aws_region
# )

# # Tools list
# tools = [send_otp_email, validate_otp_email]

# # Agent initialization
# AI_agent = chat_Agent(model, tools, system_prompt, debug=True)

# print("🏛️ Welcome to the Historical Monuments Conversational AI!")
# print("You can ask me anything about historical monuments around the world.")
# print("Type your message below. Press Ctrl+C or type 'exit' to quit.\n")

# import uuid
# thread_id = str(uuid.uuid4())

# try:
#     while True:
#         user_input = input("You: ").strip()

#         if user_input.lower() in ['exit', 'quit']:
#             print("👋 Exiting chat. Goodbye!")
#             break

#         user_message = {"messages": [HumanMessage(user_input)]}

#         config = {
#             "configurable": {
#                 "thread_id": thread_id
#             }
#         }

#         ai_response = AI_agent.agent_graph.invoke(user_message, config=config)

#         print(f"\nAgent: {ai_response['messages'][-1].content}\n")

# except KeyboardInterrupt:
#     print("\n👋 Exiting chat due to keyboard interrupt. Goodbye!")
