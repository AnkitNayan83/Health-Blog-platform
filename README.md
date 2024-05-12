# Health Blog Platform

This is a Django Rest Framework application for a health blog platform where users can create articles on health-related topics and other users can comment on them. It also features authentication using JWT (JSON Web Tokens).

## Setup

### Prerequisites

- Python 3.x installed on your system
- pip package manager
- PostgreSQL or SQLite database (PostgreSQL recommended for production)

### Installation

1. Clone the repository:

``` git clone https://github.com/your_username/health-blog-platform.git ```

2. Navigate to the project directory:

```cd health-blog-platform```

3. Install dependencies:

```pip install -r requirements.txt```


### Configuration

1. Create a `.env` file and add the following variables:

```
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=your_database_url
```

2. Create the database tables:

``` python manage.py migrate ```


### Running the Application

1. Start the development server:

```  python manage.py runserver ```


2. The application will be accessible at `http://localhost:8000/`

### Usage

1. To create a new article, you can make a POST request to `/api/articles/` with the required fields.

2. To comment on an article, make a POST request to `/api/comments/` with the article ID and comment text.

### Authentication

- Authentication is handled using JWT (JSON Web Tokens).
- To obtain a token, make a POST request to `/api/token/` with your username and password.
- Include the token in the Authorization header of subsequent requests as `Bearer your_token`.

### Deployment

- For production deployment, update `DEBUG=False` in your `.env` file.
- Configure a production-ready web server (e.g., Nginx or Apache) to serve the application.
- Set up Gunicorn or uWSGI to serve the Django application.
- Consider using a service like Heroku or AWS for hosting.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/improvement`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/improvement`).
5. Create a new Pull Request.


