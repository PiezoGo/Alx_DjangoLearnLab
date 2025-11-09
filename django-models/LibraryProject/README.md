Objective

The goal of this project is to gain familiarity with Django by setting up a Django development environment and creating a basic Django project named LibraryProject.
This serves as an introduction to Django’s workflow, including project setup, running a development server, and exploring the framework’s default structure.

Task Description

This task involves:

Installing Django.

Creating a new Django project called LibraryProject.

Running the development server.

Exploring the project’s default files and structure to understand how Django organizes settings, URLs, and commands.

To run it 
Navigate to the Project Directory
cd LibraryProject

Run the Development Server
Start the local server using:

python manage.py runserver


Visit the following URL in your browser to view the default Django welcome page:
 http://127.0.0.1:8000/

 Project Structure Overview

After creating the project, the following files and directories are generated:

LibraryProject/
├── LibraryProject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── manage.py
└── README.md

Key Files:

manage.py – A command-line utility for interacting with the Django project (e.g., running the server, migrations, creating apps).

settings.py – Contains configuration settings such as installed apps, middleware, databases, and templates.

urls.py – Acts as the “table of contents” for your Django site, mapping URLs to views.

asgi.py / wsgi.py – Used for deploying the application on servers.

