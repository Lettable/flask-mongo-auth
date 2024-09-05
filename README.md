# Flask Auth App 

A simple Flask application demonstrating user authentication with MongoDB. Includes features for user signup, login, and session management with secure password hashing.

## Features

- **User Signup:** Allows new users to register with a username, email, and password.
- **User Login:** Authenticates users with their credentials.
- **MongoDB Integration:** Stores user data securely in MongoDB.
- **Password Hashing:** Utilizes hashing for password storage to enhance security.

## Prerequisites

Before running the project, make sure you have the following installed:

- Python 3.x
- Flask
- Flask-PyMongo
- Flask-Bcrypt
- MongoDB (Running locally or remotely)

You can install the required Python packages using pip:

```bash
pip install Flask Flask-PyMongo Flask-Bcrypt pymongo
```

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Lettable/flask-mongo-auth.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd flask-mongo-auth
   ```

3. **Set up MongoDB:**

   Ensure MongoDB is running. You can use a local MongoDB server or a cloud-based service. Update the MongoDB connection string in the `app.py` file if necessary.

4. **Run the Flask application:**

   ```bash
   python app.py
   ```

   By default, the Flask application will run on `http://127.0.0.1:5000`.

## File Structure

- `app.py`: The main Flask application file.
- `templates/`: Directory containing HTML templates for signup and login pages.
- `static/`: Directory containing static files like CSS and JavaScript and Images.
- 
## Usage

1. **Signup:**

   Navigate to `http://127.0.0.1:5000/signup` to create a new account. Provide a username, email, and password.

2. **Login:**

   Navigate to `http://127.0.0.1:5000/login` to log in with your credentials.

## Code Overview

- **Flask App Setup:** `app.py` sets up the Flask application, routes, and connects to MongoDB.
- **User Registration:** Users are registered with hashed passwords for security.
- **User Authentication:** Login functionality verifies credentials and manages user sessions.
- **MongoDB:** User data is stored and managed using MongoDB collections.

## Contributing

Feel free to fork the repository and submit pull requests. If you find any issues or have suggestions, please open an issue or contact me.

## Contact

For any questions or feedback, you can reach me at [Mirzya](tg://openmessage?user_id=6404281440).
