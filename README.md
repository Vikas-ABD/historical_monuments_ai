🏛️ Historical Monuments AI Chatbot
A conversational AI chatbot built with Streamlit and LangChain, designed to assist travelers with historical monument information, travel suggestions, and email-based guide sharing via Gmail SMTP.

🚀 Getting Started
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/Vikas-ABD/historical_monuments_ai.git
cd historical_monuments_ai
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
👉 By default, the app runs on:

arduino
Copy
Edit
http://localhost:8501
Open this link in your browser!

⚙️ Environment Variables Setup (Required for Email Functionality)
Create a .env file in the project root directory and add the following:

ini
Copy
Edit
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your_gmail@gmail.com
SMTP_PASSWORD=your_gmail_app_password
✅ Important Notes:

Use a Google App Password instead of your regular Gmail password.
Enable App Passwords in your Google Account Settings.
🐳 Run with Docker Compose (Optional)
1. Build and Start the Containers
bash
Copy
Edit
docker-compose up --build
This will:

Build your Streamlit app Docker image.
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
The bot runs as a single process, suitable for light concurrent usage.
For production use, deploy on AWS ECS/Fargate with:

Auto Scaling
Application Load Balancer
This ensures better concurrency handling.

💡 How It Works
When a user visits the app, a short example of the chat follows:

vbnet
Copy
Edit
Bot: Hey, I am a historical agent AI. You can ask anything around it.
User: Hey, I am travelling to Noida next month for official work. Can you suggest me something to visit?
Bot: Hey, have you visited the Taj Mahal in Agra before?
User: No, this is my first visit to India.
Bot: Great! I think you must visit the Taj Mahal in Agra. Agra is around 200Km from Noida and one can easily take a cab from Noida to Agra.
User: Thanks.
Bot: If you can share your email, I can send a few details related to the Taj Mahal.
User: No thanks, I am in a hurry. Later.
Bot: There are many places around Agra which one should visit. Since you are leaving, I suggest you share your email and I can share a lot of places to visit around.
User: Thanks, my email is abc@xyz.com
Bot: Thanks! I have sent a 6-digit code to your email. Can you please confirm it with the code?
User: Sure, it's 992812
Bot: Sorry, it's incorrect. Can you please check again?
User: Sorry, typo. It's 982812.
Bot: Great! Thanks. I’ll shoot you the email soon. Take care.
✅ What's Next?
Connect with a backend API (FastAPI/Flask) for scalable chatbot processing.
Store chat history in Redis or a database.
Add authentication and user dashboards!
🙌 Acknowledgments
Built with Streamlit for quick prototyping.
Powered by LangChain for conversational AI capabilities.
Email functionality enabled by Gmail SMTP.
📄 License
This project is licensed under the MIT License.
See the LICENSE file for details.

📧 Contact
For questions or feedback, feel free to reach out:
📩 your_email@example.com
🌐 GitHub Repo