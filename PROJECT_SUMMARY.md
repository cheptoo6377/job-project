# Flask Job Board Application - Project Summary

## Overview
A web-based job board platform built with Flask, supporting user registration, authentication, and role-based access (admin/applicant). The system allows job posting, application, and management for both administrators and applicants.

## Key Features
- **User Authentication:** Secure login, registration, and logout using Flask-Security.
- **Role-Based Dashboards:**
  - **Admin Dashboard:** View user/job stats, manage jobs, see recent users.
  - **Applicant Dashboard:** View available jobs, apply to jobs, see applied jobs.
- **Job Management:**
  - Admins can create, edit, and delete jobs.
  - Applicants can browse and apply for jobs.
- **Job Application Tracking:** Users can view jobs they have applied to.
- **CSRF Protection:** All forms and API endpoints are protected.
- **RESTful API:** Jobs can be managed via API endpoints.

## Technical Stack
- **Backend:** Flask, Flask-SQLAlchemy, Flask-Security, Flask-WTF, Flask-RESTful
- **Database:** SQLite (default, can be swapped)
- **Frontend:** Jinja2 templates, Bootstrap for styling

## Database Models
- **UserModel:** Stores user info, roles, and applications.
- **RoleModel:** Defines user roles (admin, applicant).
- **JobModel:** Stores job postings.
- **JobApplication:** Tracks which users applied to which jobs.

## Security
- Passwords are hashed.
- Role-based access control for admin/applicant.
- CSRF protection on all forms and APIs.

## Usage Flow
1. **Registration/Login:** Users register and select a role.
2. **Dashboard:** Redirected to admin or applicant dashboard based on role.
3. **Job Management:** Admins manage jobs; applicants browse and apply.
4. **Application Tracking:** Applicants see their applied jobs.

## Extensibility
- Easily add more roles or permissions.
- Can integrate with other databases or authentication providers.
- RESTful API endpoints allow for future mobile or frontend integrations.
