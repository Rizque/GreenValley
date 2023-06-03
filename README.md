# Green Valley Django App

The Green Valley Django App is a web application built with Django framework that allows users to browse and review products from various farms.

## Features
- User registration and authentication
- Browse and search for agricultural products
- Product details page with ratings and reviews
- Submit and update product reviews
- Different user roles: Clients and Farms
- Responsive design using Bootstrap 5

## Installation

### 1. Clone the repository:

git clone

### 2. Change to the project directory:

cd GreenValley

### 3. Install and create a virtual environment:

pip install virtualenv

python -m venv env

### 4. Activate the virtual environment:

On Windows:

env\Scripts\activate

On macOS and Linux:

source env/bin/activate

### 5. Install the required dependencies:

pip install -r requirements.txt

### 6. Apply database migrations:

python manage.py migrate

### 7. Create a superuser (admin) account:

python manage.py createsuperuser

### 8. Start the development server:

python manage.py runserver

### 9. Open your web browser and visit http://localhost:8000 to access the app.

## Configuration

The Green Valley Django App uses environment variables for configuration. Create a .env file in the root directory of the project and set the following variables:

SECRET_KEY=your-secret-key
DEBUG=
PASSWORD=
DATABASE_URL=your-database-url
