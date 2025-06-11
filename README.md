**Data Agent**

This is a Django-based application for processing CSV files and interacting with the Gemini LLM to answer questions based on the uploaded data.

Features
CSV Upload: Users can upload CSV files, which are processed to extract data.

Question Answering: After uploading a CSV, users can ask questions about the data, and the agent (powered by Gemini LLM) will provide answers.

MongoDB Integration: Stores uploaded CSVs and logs in MongoDB.

History Logging: Saves user questions and agent responses, accessible for future reference.

Requirements
Before running the application, make sure to install the required dependencies:

1. Python version:
Python 3.10 or higher.

2. Dependencies:
Create a virtual environment and install dependencies with:

bash
Copy
pip install -r requirements.txt
The required packages are:

Django: Web framework used for the backend.

Pandas: Used for data manipulation and processing CSV files.

Pymongo: MongoDB client for Python to interact with the database.

python-dotenv: Loads environment variables from .env for sensitive keys.

langchain-experimental: Integrates Gemini LLM for question answering.

langchain-google-genai: Provides access to Gemini via Google APIs.

3. MongoDB Atlas Setup:
You need a MongoDB Atlas account and a cluster.

Create a database data_agent_db and a collection agent_age to store logs and data.

Set up your environment variables in a .env file (see below for an example).

Setup
1. Clone the repository:
Clone the project to your local machine:

bash
Copy
git clone https://github.com/BBHUVANESHWARAN/Data_Agent.git
2. Set up a virtual environment:
Create and activate a virtual environment:

bash
Copy
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
3. Install dependencies:
Install the required dependencies:

bash
Copy
pip install -r requirements.txt
4. Create .env file:
In the project root, create a .env file with the following environment variables:

env
Copy
MONGO_URI="mongodb+srv://<username>:<password>@dataagent.qvscvry.mongodb.net/data_agent_db?retryWrites=true&w=majority"
GOOGLE_API_KEY="<your-google-api-key>"
Replace <username>, <password>, and <your-google-api-key> with your actual MongoDB credentials and Google API key.

Running the Project Locally
1. Apply migrations:
bash
Copy
python manage.py migrate
2. Run the development server:
bash
Copy
python manage.py runserver
Visit http://127.0.0.1:8000/ in your browser to access the app.

3. Upload CSV:
Upload a CSV file, and the app will process it. You can then ask questions related to the CSV data.

Deployment
Deploy to Vercel
Push your project to GitHub.

Go to Vercel.

Create a new project by selecting your GitHub repository.

Vercel will automatically detect and deploy your Django app.

Set Environment Variables on Vercel
Go to Vercel Dashboard → Project Settings → Environment Variables, and add the following variables:

MONGO_URI

GOOGLE_API_KEY

Directory Structure
plaintext
Copy
Data_Agent/
├── backend/                   # Django backend
│   ├── core/                   # Core Django app
│   ├── manage.py               # Django's entry point
│   ├── requirements.txt        # Python dependencies
│   └── .env                    # Environment variables (not pushed to GitHub)
│
├── media/                      # User-uploaded files (like CSVs)
├── frontend/                   # Frontend (if any)
│   └── static/                 # Static files like CSS/JS
├── vercel.json                 # Vercel deployment config
└── README.md                   # This file
