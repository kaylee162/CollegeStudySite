**College Study Site**
---
College Study Site is a full-stack Django web application designed to connect students and tutors through location-based tutoring sessions. Tutors can create and manage sessions with custom tags and mapped locations, while students can search, filter, and join sessions that fit their needs. The platform supports real-time communication through SMS and email to make coordination easy.

**Features**
---
**Students**  
Search for tutoring sessions using filters and tags  
View session locations on an interactive map  
Message tutors and other students via SMS or email  
Manage a personalized student profile  

**Tutors**  
Create and manage tutoring sessions  
Add custom tags to sessions (subject, level, format, etc.)  
Set session locations using Google Maps  
Message students and other tutors  
Manage a personalized tutor profile  

**Core Functionality**
---
Full authentication system with role-based access    
Location-based session discovery using the Google Maps API    
Filtered search for sessions (tags, location, and other criteria)    
Role-specific profiles for students and tutors  
SMS and email messaging powered by Twilio  
Clean, responsive UI built with Django templates  

**Tech Stack**
---
Backend: Django, Python  
Frontend: HTML, CSS, JavaScript, Django Templates  
Database: SQLite (development)  

**APIs & Services:**  
Google Maps API (location and session discovery)  
Twilio (SMS and email messaging)  
Version Control: Git, GitHub  

**Project Structure**
```bash
college-study-site/
│
├── accounts/        # Authentication and user roles
├── profiles/        # Student and tutor profiles
├── sessions/        # Tutoring session creation and discovery
├── messaging/       # Twilio SMS and email integration
├── templates/       # HTML templates
├── static/          # CSS, JS, and assets
├── manage.py
└── requirements.txt
```
**Getting Started**
---
**Prerequisites**  
Python 3.10+  
pip  
Virtual environment (recommended)  
Google Maps API key  
Twilio account and credentials  

**Installation**  
Clone the repository:  
```bash
git clone https://github.com/your-username/college-study-site.git
```

```bash
cd college-study-site
```
Create and activate a virtual environment:  
```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```
**Install dependencies:**
```bash
pip install -r requirements.txt
```
Create a .env file and add the required environment variables:  
```bash
SECRET_KEY=your_django_secret_key
GOOGLE_MAPS_API_KEY=your_google_maps_api_key
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=your_twilio_phone_number
```
Run migrations:
```bash
python manage.py migrate
```
Start the development server:
```bash
python manage.py runserver
```
Visit the app at:
```bash
http://127.0.0.1:8000/
```
**Usage:**  
Create an account and select a role (student or tutor)  
Tutors can create sessions with locations and tags  
Students can browse and filter sessions using the map and search tools  
Users can message each other via SMS or email directly from the platform  

**Project Context**
---
This project was developed as part of a computer science course and focuses on:  
Full-stack web development  
API integration  
Role-based application design  
Real-world features like messaging and location services  

**Future Improvements**  
---
Advanced search and recommendation logic  
In-app messaging dashboard  
Reviews and ratings for tutors  
Deployment to a production environment  
Enhanced security and permissions  
