# eastvantage-technical_exam
Technical assessment for Eastvantage

Address Book API

Features
- Create address
- Get all addresses
- Get address by ID
- Update address
- Delete address
- Retrieve nearby address using latitude, longitude, and distance

Tech Stack
- FastAPI
- SQLAlchemy (ORM)
- SQLite

Libraries
- Pydantic (validation)
- Geopy (distance calculation)

How to Run
1) Clone repository via cmd
git clone https://github.com/Jliung033/eastvantage-technical_exam.git 
cd eastvantage-technical_exam

2) Install dependencies
python -m pip install -r requirements.txt

3) Run application
python -m uvicorn main:app --reload --app-dir .

4) Open API docs
http://127.0.0.1:8000/docs

Example Usage
Create Address:
{ 
    "name": "Home", 
    "latitude": 14.5995, 
    "longitude": 120.9842 
}
