# Naija Restaurant – Django Booking System 🍽

*A simple, elegant restaurant reservation app built with Django, Django-Allauth, and Bootstrap 5.*

---

## Table of Contents

* [Overview](#overview)
* [Strategy](#strategy)
* [Scope](#scope)
  * [Epics](#epics)
  * [Must Have](#must-have)
  * [Should Have](#should-have)
  * [Could Have](#could-have)
  * [Won't Have](#wont-have-for-this-iteration)
* [Project Structure](#project-structure)
* [Authentication](#authentication)
* [Models & Views](#models--views)
* [Templates](#templates)
* [Wireframes](#wireframes)
* [Snapshots](#snapshots)
* [Testing](#testing)
* [Deployment](#deployment)
* [Technologies Used](#technologies-used)
* [Credits](#credits)

---

## Overview

The goal of *Naija Restaurant* is to create a user-friendly system where customers can register, log in, and manage their own bookings. Admins handle overall reservation management. This project mirrors a full-stack development process with a focus on clarity and simplicity.

---

## Strategy

Built using the *Django framework* with *SQLite or PostgreSQL, and authenticated via **Django-Allauth. The UI leverages **Bootstrap 5* for responsive and fast front-end development. The project followed Agile practices, with features prioritized via a MoSCoW backlog to support incremental builds with constant validation.

---

## Scope

### Epics

* Build a Django-based booking system.
* Support admin CRUD of bookings.
* Allow authenticated users to CRUD their bookings via frontend.
* Display a static menu.
* Include customer-facing, responsive UI.
* Maintain a beautiful and well-documented codebase.

### Must Have

* Admin can create/edit/delete bookings via the admin panel.
* Authenticated users can register, log in, and manage bookings.
* Prevent double bookings by enforcing unique date+time.
* All functionality must be tested with unit tests.

### Should Have

* Display menu items to users without requiring login.
* Validate against past bookings.
* Provide intuitive UI/UX with feedback messages.
* Clear navigation header and footer.

### Could Have

* Email notifications/post-booking reminders.
* Responsive animations.

### Won’t Have (for this iteration)

* Table assignments or capacity logic.
* Real-time availability syncing.
* Image uploads for menu items.

---


---

## Authentication

* Managed using *Django-Allauth* for registration, login, logout.
* Two user roles:
  * *External Users (Customers)* – front-end booking.
  * *Admin Users* – full access via Django admin.
* Templates for login/signup are customized with Bootstrap.

---

## Models & Views

* *Booking*
  * Fields: user (FK), date, time, guests, menu_choice, timestamps.
  * Constraints: Unique date+time to prevent double bookings.
  * Validation: Prevent bookings in the past.

* *Menu* (optional or static)
  * Holds item names, descriptions, prices.
  * Displayed on "Menu" page for customers.

Views handle listing, creating, updating, and deleting bookings with proper access control.

---

## Templates

* base.html – Website shell with navbar & footer.
* home.html – Hero image, intro, call-to-action.
* menu.html – Static menu display with items and descriptions.
* Auth Pages – Bootstrap-styled login/signup overriding Django-Allauth defaults.
* Booking pages – Responsive forms and CRUD views for customers.

---

## Wireframes 🖼

- *Home Page Wireframe*  
  ![Home Wireframe](https://via.placeholder.com/600x400.png?text=Home+Wireframe)

- *Menu Page Wireframe*  
  ![Menu Wireframe](https://via.placeholder.com/600x400.png?text=Menu+Wireframe)

- *Booking Page Wireframe*  
  ![Booking Wireframe](https://via.placeholder.com/600x400.png?text=Booking+Wireframe)

---

## Snapshots 📸

- *Homepage Preview*  
  ![Homepage](https://via.placeholder.com/800x450.png?text=Homepage+Preview)

- *Menu Page Preview*  
  ![Menu Preview](https://via.placeholder.com/800x450.png?text=Menu+Page+Preview)

- *Booking Page Preview*  
  ![Booking Preview](https://via.placeholder.com/800x450.png?text=Booking+Page+Preview)

---

## Testing

Includes:

* Form validation tests (e.g., double-booking prevention).
* View tests to ensure correct behavior for booking create, update, and delete.
* Template rendering tests for key pages like home, menu, booking list.

---

## Deployment

1. Run python manage.py migrate
2. Collect static files via python manage.py collectstatic
3. Set DEBUG=False for production
4. Deploy steps can be for platforms like Heroku / Render / Vercel:
   * Create app
   * Configure environment variables (SECRET_KEY, DB)
   * Push changes from GitHub

---

## Technologies Used

* *Python, **Django, **Django-Allauth*
* *Bootstrap 5* (via CDN)
* Optional: SQLite or PostgreSQL
* Optional: Cloudinary (for image hosting in advanced iterations)

---

## Credits

* Layout and logic inspired by Code Institute’s Blue Boar Inn project
* Placeholder images via *Picsum.photos*
* Auth UI built with Django-Allauth, styled with Bootstrap