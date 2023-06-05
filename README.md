# Green Valley Django App

The Green Valley Django App is a web application built with Django framework that allows users to browse and review products from various farms.

## Deployment

The application is deployed and can be accessed online at [https://greenvalley.herokuapp.com/](https://greenvalley.herokuapp.com/). Feel free to visit the site and explore the available features.


## Features
- User registration and authentication
- Browse and search for agricultural products
- Product details page with ratings and reviews
- Submit and update product reviews
- Different user roles: Clients and Farms
- Responsive design using Bootstrap 5

## Installation

### 1. Clone the repository:

`git clone`

### 2. Change to the project directory:

`cd GreenValley`

### 3. Install and create a virtual environment:

`pip install virtualenv`

`python -m venv env`

### 4. Activate the virtual environment:

On Windows:

`env\Scripts\activate`

On macOS and Linux:

`source env/bin/activate`

### 5. Install the required dependencies:

`pip install -r requirements.txt`

### 6. Apply database migrations:

`python manage.py migrate`

### 7. Create a superuser (admin) account:

`python manage.py createsuperuser`

### 8. Start the development server:

`python manage.py runserver`

### 9. Open your web browser and visit http://localhost:8000 to access the app.

## Configuration

The Green Valley Django App uses environment variables for configuration. Create a .env file in the root directory of the project and set the following variables:

For production version:

- CLIENT_ID=                  Google client ID for authentication.
- SECRET=                     Secret key for securing sensitive information.

For development version:

- SECRET_KEY=                 Secret key for Django application.
- AWS_ACCESS_KEY_ID=          AWS access key ID for development.
- AWS_SECRET_ACCESS_KEY=      AWS secret access key for development.
- AWS_STORAGE_BUCKET_NAME=    Name of the AWS S3 bucket for file storage.

## Usage
- Create a farm account to add and manage products.
- Create a client account to browse and review products.
- Use the search functionality to find specific products or farms.
- Click on a product to view its details, ratings, and reviews.
- Submit reviews for products.



## Technologies Used

This Django project utilizes the following technologies:

- Python: The programming language used for the development of the project.
- Django: The web framework used for building the application.
- Virtual Environment: A tool used to create isolated Python environments for project dependencies.
- HTML: The markup language used for creating the structure and content of web pages.
- CSS: The styling language used for applying visual styles to the web pages.
- Bootstrap: Front-end framework used for creating responsive and visually appealing web pages.
- JavaScript: The programming language used for client-side interactivity and dynamic behavior.
- Google Maps: Mapping service used for generating maps and displaying location data.
- SQLite: The relational database management system used for storing and retrieving data.
- Django AllAuth: Authentication framework used for user authentication and registration, including integration with Google.
- Amazon Web Services (AWS): Cloud services used for file storage and hosting assets.
- AWS S3: Storage service provided by AWS for storing and retrieving static and media files.
- Heroku: Cloud platform used for deploying and hosting web applications.
- Git: Version control system used for tracking changes and collaboration among developers.

## Web Author

The Green Valley Django App was developed by Ritvars Vjakse.

For any inquiries or further information, please feel free to reach out via email at ritvarsvjakse@gmail.com.

## Contributing
Contributions to the Green Valley Django App are welcome! If you find any issues or would like to suggest improvements, please submit a GitHub issue or pull request.

## License
The Green Valley Django App is open-source software licensed under the MIT License.
