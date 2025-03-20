# Total Life Take Home Project


## Overview
___
This project is a full-stack web application designed to manage patients, clinicians, and appointments. It consists of a **Django REST API** backend and a **React frontend**. The backend provides CRUD operations for clinicians, patients, and appointments, while the frontend displays the appointment data.

## Features
___
### **Backend** /total_life (Django REST Framework) 
- Models for **Clinician**, **Patient**, and **Appointment**
- CRUD operations for all resources
- SQLite database for data storage
- API validation for **NPI numbers** (using [NPI Registry API](https://npiregistry.cms.hhs.gov/api-page))
- Django REST Framework 

### **Frontend** /frontend (React + Tailwind CSS) 
- Fetches and displays appointments from the backend
- Allows filtering by appointment time
- Styling using **Tailwind CSS**



## Installation & Setup
---

### Prerequisites
- **Python 3.x**
- **Node.js & npm**
- **Git** (optional but recommended)

### Backend Setup (Django)
1. **Clone the repository:**
   ```sh
   git clone https://github.com/woopy098/total-life.git
   cd total-life
   ```
2. **Create and activate a virtual environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # (Mac/Linux)
   venv\Scripts\activate  # (Windows)
   ```
3. **Install dependencies:**
   ```sh
   cd total_life
   pip install -r requirements.txt
   ```
4. **Apply migrations:**
   ```sh
   python manage.py makemigrations api
   python manage.py migrate
   ```
5. **Create a superuser (optional for admin panel access):**
   ```sh
   python manage.py createsuperuser
   ```
6. **Start the backend server:**
   ```sh
   python manage.py runserver
   ```
   The API will be available at: `http://127.0.0.1:8000/api/`

### Frontend Setup (React)
1. **Navigate to the frontend directory:**
   ```sh
   cd frontend
   ```
2. **Install dependencies:**
   ```sh
   npm install
   ```
3. **Start the frontend server:**
   ```sh
   npm start
   ```
   The frontend will be available at: `http://localhost:3000`


## Backend Structure
___
The backend consists of three core models:

### 1. **Clinician Model** (`Clinician`)
This model represents medical professionals who provide healthcare services.

#### **Fields:**
- `first_name` *(CharField, max_length=50)* - First name of the clinician.
- `last_name` *(CharField, max_length=50)* - Last name of the clinician.
- `state` *(CharField, max_length=2)* - The state where the clinician is licensed (e.g., "NY").
- `npi_number` *(CharField, max_length=10, unique=True)* - A unique **National Provider Identifier (NPI)** number.

#### **Relationships:**
- This model is **referenced in the `Appointment` model** since an appointment is associated with a clinician.

#### **Validation:**
When a clinician is created, their `npi_number` is validated against the **NPI Registry API** to ensure legitimacy.

---

### 2. **Patient Model** (`Patient`)
This model represents individuals receiving medical care.

#### **Fields:**
- `first_name` *(CharField, max_length=50)* - First name of the patient.
- `last_name` *(CharField, max_length=50)* - Last name of the patient.
- `date_of_birth` *(DateField)* - The patient’s date of birth.

#### **Relationships:**
- This model is **referenced in the `Appointment` model**, as a patient can have multiple appointments.

---

### 3. **Appointment Model** (`Appointment`)
This model stores details about patient appointments.

#### **Fields:**
- `patient` *(ForeignKey → Patient)* - The patient who booked the appointment.
- `clinician` *(ForeignKey → Clinician)* - The clinician attending the appointment.
- `appointment_time` *(TimeField)* - The scheduled time of the appointment.
- `status` *(CharField, choices=["pending", "completed", "cancelled"], default="pending")* - The current status of the appointment.

#### **Relationships:**
- **`patient` ForeignKey** → Links each appointment to a patient.
- **`clinician` ForeignKey** → Links each appointment to a clinician.

#### **Constraints:**
- The appointment status is **limited to three choices** (`pending`, `completed`, `cancelled`).
- **Deletion Policy:** If a patient or clinician is deleted, their associated appointments are also removed (**CASCADE delete**).


## API Endpoints
---
## **Clinicians**
| Method | Endpoint               | Description |
|--------|------------------------|-------------|
| GET    | `/api/clinicians/`     | List all clinicians |
| GET    | `/api/clinicians/{id}/`| List a Specific clinician|
| POST   | `/api/clinicians/`     | Create a clinician (validates NPI number) |
| PUT    | `/api/clinicians/{id}/`| Update a Specific clinician|
| DELETE    | `/api/clinicians/{id}/`| Delete a Specific clinician|


### Create a Clinician (with NPI validation)
```sh
curl -X POST "http://127.0.0.1:8000/api/clinicians/" \
     -H "Content-Type: application/json" \
     -d '{
           "first_name": "John",
           "last_name": "Doe",
           "state": "NY",
           "npi_number": "1234567893"
         }'
```
### Get all Clinician
```sh
curl -X GET "http://127.0.0.1:8000/api/clinicians/"
```

### Get a specific Clinician
```sh
curl -X GET "http://127.0.0.1:8000/api/clinicians/{id}/"
```

### Update a specific Clinician
```sh
curl -X PUT "http://127.0.0.1:8000/api/clinicians/{id}/" \
     -H "Content-Type: application/json" \
     -d '{
           "first_name": "John",
           "last_name": "Doe",
           "state": "NY",
           "npi_number": "1234567893"
         }'
```
### Delete a specific Clinician
```sh
curl -X DELETE "http://127.0.0.1:8000/api/clinicians/{id}/"
```

## **Patients**
| Method | Endpoint               | Description |
|--------|------------------------|-------------|
| GET    | `/api/patients/`       | List all patients |
| GET    | `/api/Patients/{id}/`  | List a Specific patients|
| POST   | `/api/patients/`       | Create a patient |
| PUT    | `/api/patients/{id}/`   | Update a patient |
| DEL    | `/api/patients/{id}/`   | Delete a patient |



### Create a Patient
```sh
curl -X POST "http://127.0.0.1:8000/api/patients/" \
     -H "Content-Type: application/json" \
     -d '{
           "first_name": "Alice",
           "last_name": "Smith",
           "date_of_birth": "1990-05-20"
         }'
```
### Get all Patients
```sh
curl -X GET "http://127.0.0.1:8000/api/clinicians/"
```

### Get a specific Patient
```sh
curl -X GET "http://127.0.0.1:8000/api/clinicians/{id}/"
```

### Update a specific Patient
```sh
curl -X PUT "http://127.0.0.1:8000/api/clinicians/{id}/" \
     -H "Content-Type: application/json" \
     -d '{
           "first_name": "Alice",
           "last_name": "Smith",
           "date_of_birth": "1990-05-20"
         }'
```
### Delete a specific Patient
```sh
curl -X DELETE "http://127.0.0.1:8000/api/clinicians/{id}/"
```



## **Appointments**
| Method | Endpoint               | Description |
|--------|------------------------|-------------|
| GET    | `/api/appointments/`   | List all appointments |
| GET    | `/api/appointments/{id}/`  | List a Specific appointments|
| POST   | `/api/appointments/`   | Create an appointment |
| PUT    | `/api/appointments/{id}/` | Update an appointment |
| DEL    | `/api/appointments/{id}/` | Delete an appointment |


### Create an Appointment
```sh
curl -X POST "http://127.0.0.1:8000/api/appointments/" 
     -H "Content-Type: application/json" \
     -d '{
           "patient": {patient_id},
           "clinician": {clinician_id},
           "appointment_time": "15:30:00",
           "status": "pending"
         }'
```
### Get all Patients
```sh
curl -X GET "http://127.0.0.1:8000/api/appointments/"
```

### Get a specific Patient
```sh
curl -X GET "http://127.0.0.1:8000/api/appointments/{id}/"
```

### Update a specific Patient
```sh
curl -X PUT "http://127.0.0.1:8000/api/appointments/{id}/" \
     -H "Content-Type: application/json" \
     -d '{
           "patient": {patient_id},
           "clinician": {clinician_id},
           "appointment_time": "15:30:00",
           "status": "pending"
         }'
```
### Delete a specific Patient
```sh
curl -X DELETE "http://127.0.0.1:8000/api/appointments/{id}/"
```

 
---



## Future Enhancements
- Add authentication using Django and JWT
- Improve UI with additional filters and appointment creation forms
- Implement logging for API requests

