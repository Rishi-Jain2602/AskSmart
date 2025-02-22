# AskSmart: A RAG-Powered Intelligent Query System


**AskSmart** is a powerful document retrieval system that allows you to upload and process various formats such as **PDF, DOCX, JSON, and TXT**. Our advanced AI technology retrieves relevant information and generates context-aware responses to your queries.

**Supported Formats: PDF, DOCX, JSON, TXT**

****
## Installation

1. Clone the Repository
   
``` bash
git clone https://github.com/Rishi-Jain2602/AskSmart.git
```

2. Create Virtual Environment

```bash
cd backend
virtualenv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On macOS/Linux
```

3. Install the Project dependencies

- 3.1 Navigate to the **Backend** Directory and install Python dependencies:

```bash
cd backend
pip install -r requirements.txt
```
- 3.2 Navigate to the **Frontend** Directory and install Node.js dependencies:
```bash
cd frontend
npm install
```

4. Run the React App

Start the React app with the following command:

```bash
cd frontend
npm start
```

5. Run the Backend (FastAPI App)

Open a new terminal and run the backend:

```bash
cd backend
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
****

## Note
1. Make sure you have Python 3.x installed
2. It is recommended to use a virtual environment to avoid conflict with other projects.
3. If you encounter any issue during installation or usage please contact rishijainai262003@gmail.com or rj1016743@gmail.com
