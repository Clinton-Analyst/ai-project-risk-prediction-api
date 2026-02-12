#  AI-Powered Project Risk Prediction API + Dashboard

An end-to-end AI system that predicts project risk levels using machine learning, FastAPI, MySQL, and Streamlit.
The API Accepts project data (budget, duration, labor count, weather risk)
•	Predicts:
        o	Delay probability
        o	Budget overrun risk
        o	Risk score


---

##  Project Overview

This system allows project managers to:

- Predict project risk (Low / Medium / High)
- Store predictions in MySQL database
- Visualize analytics in a dashboard
- Access API documentation via Swagger UI



## System Architecture

User → Streamlit Dashboard → FastAPI Backend → ML Model → MySQL Database

                 ┌──────────────────────┐
                 │      Web Dashboard   │		(streamlit)
                 └──────────┬───────────┘
                        	  │ HTTP
                 ┌──────────▼───────────┐
                 │      FastAPI API     │		(prediction API)
                 └──────────┬───────────┘
                    	   │
                 ┌──────────▼───────────┐
                 │  ML Model (.pkl)     │
                 └──────────┬───────────┘
                           	  │
                 ┌──────────▼───────────┐
                 │        MySQL DB      │
                 └──────────────────────┘


---

## Technologies Used

- Python
- FastAPI
- Streamlit
- Scikit-learn
- MySQL
- SQLAlchemy
- Uvicorn

---

## Project Structure

```
project_risk_system/
│
├── app/
│   ├── database.py
│   ├── main.py
│   ├── ml_model.py
│   ├── schemas.py
├── dashboard/
│   └── dashboard.py
├── data/
|   ├── cost_model.py
│   ├── delay_model.py
│   ├── generate_dataset.py
│   ├── project_data.csv
|   ├── train_model.py
├── Documentation/
|   ├── PROJECT_EXPERIENCE.md
│   ├── README.me
├── model/
|   ├── cost_model.py
│   ├── delay_model.py
│   ├── generate_dataset.py
│   ├── project_data.csv
|   ├── train_model.py

|── env

```



##  Installation & Setup

###  Clone Repository

```bash
git clone <your-repo-link>
cd project
```

###  Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

###  Install Dependencies

```in vs code terminal install dependencies
pip install fastapi, uvicorn, scikit-learn, pandas, numpy, sqlalchemy, psycopg2-binary, streamlit, python-dotenv

```

###  Configure Database (MySQL)

Update database URL in `database.py`:

```python
DATABASE_URL = "mysql+pymysql://username:password@127.0.0.1/project_db"
```
Replace username, password and project_db with your corresponding credentials

Make sure MySQL server is running.


##  Run the Backend

``` In VS Code open terminal and run the code  below. Ensure you are on pjoject root directory.
uvicorn main:app --reload
```

Open: in a browser

```
http://127.0.0.1:8000/docs
```


##  Run Dashboard

```open a new terminal in vs code and run this. Ensure the other terminal is also running.
   To stop the server from learning click [ctrl+c] in the terminal that API is running.
streamlit run dashboard.py
```


##  API Endpoint

POST `/predict`

Example JSON:

```json
{
  "budget": 50000,
  "team_size": 5,
  "duration": 6,
  "complexity": 7
}
```

Response:

```json
{
  "risk_level": "High"
}
```


##  Features

- ML-based risk prediction
- Database storage of predictions
- Interactive dashboard
- Swagger API documentation
- Real-time analytics


## Learning Objectives

- Build REST APIs using FastAPI
- Integrate ML models into backend
- Connect MySQL database
- Create interactive dashboards
- Handle debugging and performance issues


## OWNER

Clinton Munene  
AI Enthusiast, Data Scientist & Data Analyst  
