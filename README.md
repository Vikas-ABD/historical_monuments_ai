# 🤖 Conversational AI Bot - Streamlit App

This is a **Conversational AI Bot** built with **Streamlit**. The bot provides interactive conversations about **historical monuments** and **travel recommendations**. It engages users in a friendly and informative dialogue and can even **send a detailed guide via email**, using **Gmail SMTP**.

---

## ✨ Features
- Interactive chat interface powered by Streamlit.
- Talks about famous historical monuments and destinations.
- Sends detailed travel guides to users via email.
- Clean and simple UI for an enjoyable experience.

---

## 🚀 Example Chat Flow

**Bot:** Hey, I am a historical agent AI. You can ask me anything about historical monuments!  
**User:** Hey, I am traveling to Noida next month for official work. Can you suggest something to visit?  
**Bot:** Have you visited the Taj Mahal in Agra before?  
**User:** No, this is my first visit to India.  
**Bot:** Great! You must visit the Taj Mahal in Agra. Agra is around 200 km from Noida, and you can easily take a cab.  
**User:** Thanks.  
**Bot:** If you share your email, I can send you detailed information about the Taj Mahal.  
**User:** No thanks, I’m in a hurry. Later.  
**Bot:** There are many places around Agra worth visiting. Since you’re leaving, I suggest sharing your email, and I’ll send you a list of places to visit.  
**User:** Thanks, my email is abc@xyz.com.  
**Bot:** Thanks! I’ve sent a 6-digit code to your email. Please confirm the code.  
**User:** Sure, it’s 992812.  
**Bot:** Sorry, that’s incorrect. Can you please check again?  
**User:** Sorry, typo! It’s 982812.  
**Bot:** Great, thanks! You’ll receive the email shortly. Take care!

---

## 🛠️ Installation & Setup (Run Locally)

### 1. Clone the Repository
```bash
git clone https://github.com/Vikas-ABD/historical_monuments_ai.git
cd historical_monuments_ai

python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate


pip install --upgrade pip
pip install -r requirements.txt


```


### Run the Streamlit App

'''bash

streamlit run app.py

'''

### 👉 By default, the app runs on http://localhost:8501. Open this link in your browser!



# Historical Monuments AI Chatbot

## ⚙️ Environment Variables Setup (Required for Email Functionality)

Create a `.env` file in the project root directory with the following content:

SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your_gmail@gmail.com
SMTP_PASSWORD=your_gmail_app_password

✅ Important:

Use a Google App Password instead of your Gmail password

Enable "Less Secure Apps" or App Passwords in your Google Account settings

�🐳 Run with Docker Compose (Optional)

1. Build and Start Containers

docker-compose up --build

This will:

Build your Streamlit app image

Expose it on port 8501 (default Streamlit port)

2. Access the Application
Open your browser and visit:
http://localhost:8501



📦 Docker Compose Overview
The docker-compose.yml file handles:

Running the Streamlit app container

Managing environment variables from .env

Exposing the app on port 8501


🔥 Concurrent Usage Behavior
Each user gets an independent Streamlit session

The bot runs as single process (suitable for light usage)

Production recommendation: Deploy on AWS ECS/Fargate with Auto Scaling and Application Load Balancer in future



✅ Next Steps
Connect with backend API (FastAPI/Flask) for scalable processing

Implement chat history storage (Redis/Database)

Add authentication & user dashboards

Enhance conversation capabilities


🙌 Acknowledgments
Built with Streamlit for rapid prototyping

Powered by LangChain for conversational AI

Email integration using Gmail SMTP



📄 License
This project is licensed under the MIT License - see LICENSE file for details.



📧 Contact
For questions or feedback:

📩 Email: vikachelluru@gmail.com

🌐 GitHub: https://github.com/Vikas-ABD/historical_monuments_ai