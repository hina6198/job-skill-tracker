# 📊 Job Skill Tracker

A full-stack web application that collects remote job postings, stores them in a SQLite database, analyzes the most in-demand technical skills, and displays the results through an interactive React dashboard.

---

## 🚀 Features

- Fetches remote job postings automatically
- Stores job data in SQLite
- Analyzes job descriptions using Pandas
- Counts the most in-demand technical skills
- FastAPI REST API backend
- Interactive React dashboard
- Role-based job filtering
- Responsive user interface
- Data visualization using Recharts

---

## 🛠️ Tech Stack

### Frontend
- React
- Vite
- Tailwind CSS
- Axios
- Recharts

### Backend
- Python
- FastAPI
- SQLAlchemy

### Database
- SQLite

### Data Analysis
- Pandas

### Version Control
- Git
- GitHub

---

## 📂 Project Structure

```
job-skill-tracker/
│
├── backend/
│   ├── app/
│   ├── data/
│   ├── scripts/
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   └── package.json
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## ⚙️ How It Works

1. Python fetches remote job postings.
2. Job data is stored in a SQLite database.
3. Pandas processes the job descriptions and counts technical skills.
4. FastAPI provides REST APIs.
5. React fetches API data.
6. Recharts displays skill statistics.

---

## 📡 API Endpoints

### Get Jobs

```
GET /jobs
```

Returns all job postings.

---

### Get Skills

```
GET /skills
```

Returns skill frequency data.

---

### Get Roles

```
GET /roles
```

Returns available job roles.

---

## 💾 Database

SQLite database contains the following fields:

- id
- title
- company
- role
- location
- tags
- description
- url
- date

---

## 📊 Dashboard

The dashboard includes:

- Total Jobs
- Skills Analysis
- Role Filter
- Interactive Bar Chart
- Latest Job Listings

---

## 📦 Installation

### Clone Repository

```bash
git clone https://github.com/hina6198/job-skill-tracker.git
```

---

### Backend

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Backend runs on

```
http://127.0.0.1:8000
```

---

### Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend runs on

```
http://localhost:5173
```

---

## 📈 Skills Used

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pandas
- React
- Tailwind CSS
- Axios
- Recharts
- Git
- GitHub

---

## 🔮 Future Improvements

- Resume upload and skill matching
- Advanced search and filtering
- Authentication
- Multiple job sources
- PostgreSQL support
- Cloud deployment

---

## 👨‍💻 Author

**Hina Qazi**

BS Computer Science Student

