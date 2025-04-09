# Fitness Tracker API

Welcome to the **Fitness Tracker API**! This API allows users to track and manage their fitness activities such as running, cycling, and weightlifting. It provides a secure, easy-to-use interface to log, update, delete, and view fitness activities, as well as track key metrics like calories burned, distance, and duration.

The goal of this project is to offer users a way to easily monitor their progress and stay motivated in their fitness journey.

---

## Features

- **User Management**: Users can register, log in, and manage their activities.
- **Activity Management**: Users can create, update, and delete fitness activities.
- **Activity History**: Users can view their past activities, filtered by date or activity type.
- **Activity Metrics**: Users can view total distance, total calories burned, and activity duration over time.
- **Authentication**: The API uses token-based authentication to ensure user data is secure.

---

## Getting Started

Follow the instructions below to get the Fitness Tracker API up and running on your local machine.

### Prerequisites

- Python 3.x
- Django 3.x+
- Django Rest Framework
- SQLite (for local development) or PostgreSQL (for production)
- Git

### Installation

1. **Clone the repository**

   Start by cloning the repository to your local machine:

   ```bash
   git clone https://github.com/Rozthegray/Fitness-Tracker-API
   cd fitness-tracker-api

2   Set up a virtual environment

Create a virtual environment to isolate the project dependencies:

python -m venv venv


3 Activate the virtual environment

On Windows:

.\venv\Scripts\activate
On macOS/Linux:

source venv/bin/activate

4 Install dependencies

Install the required packages:

pip install -r requirements.txt


5 Run database migrations

Set up the database:

py manage.py migrate


6 Create a superuser
Create a superuser to access the Django admin panel:

py manage.py createsuperuser
Follow the prompts to create your admin account.

7 Start the development server
Now you're ready to run the server:

py manage.py runserver
