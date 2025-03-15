# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

# # Sender and receiver details
# sender_email = "vikaschelluru@gmail.com"
# receiver_email = 'vikas.c20@iiits.in'

# # Gmail App Password (NOT your regular Gmail password)
# app_password = "**********************" # Paste your 16-character app password

# # Email content
# subject = 'Test Email from Python'
# body = 'Hello there! This is a test email sent using Python and Gmail SMTP.'

# # Create a MIME message
# message = MIMEMultipart()
# message['From'] = sender_email
# message['To'] = receiver_email
# message['Subject'] = subject

# # Attach the email body
# message.attach(MIMEText(body, 'plain'))

# try:
#     # Connect to Gmail's SMTP server
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.starttls()  # Secure the connection

#     # Login using the app password
#     server.login(sender_email, app_password)

#     # Send the email
#     server.send_message(message)

#     print('✅ Email sent successfully!')

# except Exception as e:
#     print(f'❗ Failed to send email: {e}')

# finally:
#     server.quit()


###################################################################################################################333

# ✅ Call the LLM (Handles streaming and non-streaming)
    # def call_llm(self, state: chat_Agent_State) -> Dict[str, List[AIMessage]]:
    #     messages = state["messages"]

    #     # Ensure system prompt is included once at the start
    #     if self.system_prompt and not any(isinstance(msg, SystemMessage) for msg in messages):
    #         messages = [SystemMessage(content=self.system_prompt)] + messages

    #     final_message = None

    #     if hasattr(self.model, "stream"):
    #         if self.debug:
    #             print("\n🚀 Streaming LLM response...")

    #         response_chunks = self.model.stream(messages)
    #         full_response = ""

    #         for chunk in response_chunks:
    #             content_list = chunk.content or []

    #             for item in content_list:
    #                 text_piece = item.get("text", "")
    #                 if text_piece:
    #                     print(text_piece, end="", flush=True)
    #                     full_response += text_piece

    #         final_message = AIMessage(content=full_response)

    #     else:
    #         if self.debug:
    #             print("\n🚀 Calling LLM...")

    #         response = self.model.invoke(messages)

    #         if isinstance(response, str):
    #             final_message = AIMessage(content=response)
    #         elif isinstance(response, AIMessage):
    #             final_message = response
    #         else:
    #             raise ValueError(f"Unexpected LLM response type: {type(response)}")

    #     if self.debug:
    #         print(f"\n✅ LLM Returned: {final_message.content}")

    #     return {"messages": [final_message]}


##############################################################################################################################################################################

