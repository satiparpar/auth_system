# Django Authentication and Authorization System

This repository contains a comprehensive authentication and authorization system built using Django. The system supports multiple user roles, allowing for fine-grained control over user access and permissions.

## Features

- **User Roles**: The system includes six types of users:
  - **Superusers**: Full access to all aspects of the system.
  - **Staff Users**: Can manage site content and users, but with limited access compared to superusers.
  - **Golden Users**: Special privileges for trusted users.
  - **Silver Users**: Standard users with some additional permissions.
  - **Normal Users**: Basic access for general users.
  - **Not Registered Users**: Users who have not yet created an account.

- **Role-Based Access Control**: Customize user access based on their assigned roles, ensuring that users can only access the resources and functionalities appropriate to their permissions.

## Customization

This authentication and authorization system is designed to be flexible and can be further customized to fit the specific needs of your website. You can modify user roles, permissions, and access controls as necessary.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/satiparpar/auth_system.git
   cd auth_system
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
