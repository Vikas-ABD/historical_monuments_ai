# 🤖 Conversational AI Bot - Streamlit App

This is a **Conversational AI Bot** built with **Streamlit**. The bot provides interactive conversations about **historical monuments** and **travel recommendations**. It engages users in a friendly and informative dialogue and can even **send a detailed guide via email**, using **Gmail SMTP**.

---

## ✨ Features
- Interactive chat interface powered by Streamlit.
- Talks about famous historical monuments and destinations.
- Sends detailed travel guides to users via email.
- Clean and simple UI for an enjoyable experience.

---

## 🚀 A Short Example of the Chat Follows:
Bot: Hey I am a historical agent AI, You can ask anything around it. 
User: Hey, I am travelling to Noida next month for official work, can you suggest me something to visit? Bot: Hey, have you visited Taj Mahal in Agra before? User: No, this is my first visit to India. 
Bot: Great, I think you must visit Taj Mahal in Agra! Agra is around 200Km from Noida and one can easily take a cab from Noida to Agra. 
User: Thanks. Bot: If you can share your email, I can send few details related to Taj Mahal. User: No Thanks, I am in a hurry. Later. 
Bot: There are many places around Agra which one should visit. Since you are leaving, I suggest you share your email and I can send lots of places to visit around. 
User: Thanks, my email is abc@xyz.com Bot: Thanks, I have sent a 6-digit code to your email. Can you please confirm the code? 
User: Sure, it's 992812. 
Bot: Sorry, it's incorrect. Can you please check again? 
User: Sorry, typo! It's 982812. 
Bot: Great, thanks. I’ll shoot you an email soon. Take care.


## 🛠️ Installation & Setup (Run Locally)

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/conversational-ai-bot.git
cd conversational-ai-bot
2. Create a Virtual Environment (Optional but Recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
3. Install Python Dependencies
bash
Copy
Edit
pip install --upgrade pip
pip install -r requirements.txt
4. Run the Streamlit App
bash
Copy
Edit
streamlit run app.py
👉 By default, the app runs on http://localhost:8501. Open this link in your browser!

⚙️ Environment Variables Setup (Required for Email Functionality)
Create a .env file in the project root directory and add the following:

ini
Copy
Edit
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your_gmail@gmail.com
SMTP_PASSWORD=your_gmail_app_password
✅ Important:

Use a Google App Password instead of your Gmail password.
Enable "Less Secure Apps" or App Passwords in your Google Account settings.
🐳 Run with Docker Compose (Optional)
1. Build and Start the Containers
bash
Copy
Edit
docker-compose up --build
This will:

Build your Streamlit app image.
Expose it on port 8501 (default Streamlit port).
2. Access the App
Open your browser and visit:

arduino
Copy
Edit
http://localhost:8501
📦 Docker Compose Overview
Your docker-compose.yml file handles:

Running the Streamlit app container.
Managing environment variables from .env.
Exposing the app on port 8501.
🔥 What Happens When Multiple Users Connect?
Each user gets an independent session in Streamlit.
The bot runs a single process, suitable for light concurrent usage.
For production use, deploy on AWS ECS/Fargate with Auto Scaling and Application Load Balancer for better concurrency.
✅ What's Next?
Connect with a backend API (FastAPI/Flask) for scalable chatbot processing.
Store chat history in Redis or a database.
Add authentication and user dashboards!
🙌 Acknowledgments
Built with Streamlit for quick prototyping.
