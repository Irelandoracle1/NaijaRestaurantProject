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

Built using the *Django framework* with *SQLite (at development) and PostgreSQL (at production), and authenticated via **Django-Allauth. The UI leverages **Bootstrap 5* for responsive and fast front-end development. The project followed Agile practices, using *user stories* managed on a [Kanban Board](https://en.wikipedia.org/wiki/Kanban_board), with features prioritized via a MoSCoW backlog to support incremental builds with constant validation.

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
* All functionality must be tested manually.

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

* *Menu* 
  * Holds item names, descriptions, prices.
  * Displayed on "Menu" page for customers.

Views handle listing, creating, updating, and deleting bookings with proper access control.

---

## Templates

* base.html – Website shell with navbar & footer.
* home.html – Hero image, intro, call-to-action.
* menu_list.html – Static menu display with items and descriptions.
* Auth Pages – Bootstrap-styled login/signup overriding Django-Allauth defaults.
* Booking pages – Responsive forms and CRUD views for customers.

---

## Wireframes 🖼

- *Home Page Wireframe*  
  ![Home Wireframe](https://github.com/Irelandoracle1/NaijaRestaurantProject/blob/main/images/restaurantbookingsection.jpg)
  
  - *Registration Page Wireframe*  
  ![Booking Wireframe](https://github.com/Irelandoracle1/NaijaRestaurantProject/blob/main/images/registrationpage.jpg)

- *Login Page Wireframe*  
  ![Booking Wireframe](https://github.com/Irelandoracle1/NaijaRestaurantProject/blob/main/images/loginpage.jpg)

- *Menu Page Wireframe*  
  ![Menu Wireframe](https://github.com/Irelandoracle1/NaijaRestaurantProject/blob/main/images/menupage.jpg)

- *Booking Page Wireframe*  
  ![Booking Wireframe](https://github.com/Irelandoracle1/NaijaRestaurantProject/blob/main/images/bookingpage.jpg)

- ** manage Booking Page Wireframe**  
  ![Booking Wireframe](https://github.com/Irelandoracle1/NaijaRestaurantProject/blob/main/images/managebookingspage.jpg)

---

## Snapshots 📸

- *Homepage Preview*  
  ![Homepage](https://github.com/Irelandoracle1/NaijaRestaurantProject/blob/main/images/naijarestauranthomepage.png)

- *Menu Page Preview*  
  ![Menu Preview](https://github.com/Irelandoracle1/NaijaRestaurantProject/blob/main/images/menupic1.png)

  - *Sign up Page Preview*  
  ![Sign Up Page Preview](https://github.com/Irelandoracle1/NaijaRestaurantProject/blob/main/images/signuppic.png)

  - *Login Page Preview*  
  ![Login Page Preview](https://github.com/Irelandoracle1/NaijaRestaurantProject/blob/main/images/signinpic.png)

- *Booking Page Preview*  
  ![Booking Preview](https://github.com/Irelandoracle1/NaijaRestaurantProject/blob/main/images/bookingspic.png)
  
---

## Testing

Includes:

* Form validation tests (e.g., double-booking prevention).
* View tests to ensure correct behavior for booking create, update, and delete.
* Template rendering tests for key pages like home, menu, booking list.

---

## Deployment

The *Naija Restaurant* application was developed using VS Code, and deployed to *GitHub* with the following steps:

### Save & Commit Changes
1. Save your files as usual.
2. To commit changes:
   bash
   git add .
   git commit -m "summarise changes"
`

3. Push changes to GitHub:

   bash
   git push
   

---

### Deploy Locally

To run the project locally:

bash
python manage.py runserver


Then select *Open in Browser* from the popup.

---

### Prior to Deployment

1. If static files have changed, collect them:

   bash
   python3 manage.py collectstatic
   

   Enter *yes* if prompted to overwrite existing files.
2. In settings.py, set:

   python
   DEBUG = False
   

   for production.
3. Add, commit, and push changes to GitHub.

---

### Heroku Deployment

The project is deployed on *Heroku*.

1. Log in to [Heroku](https://heroku.com), or create an account.

2. To create a new app:

   * Navigate to the dashboard → *New* → *Create new app*.
   * Provide a unique app name (use hyphens instead of spaces).
   * Select your region → *Create app*.

3. In the app settings:

   * Navigate to *Reveal Config Vars*.
   * Add:

     * DATABASE_URL → value of your PostgreSQL database.
     * SECRET_KEY → your secret key (from env.py).

4. Navigate to the *Deployment* tab:

   * Connect to your GitHub repository.
   * Optionally enable automatic deployment.
   * Click *Deploy Branch* to deploy the project.

5. To update deployments:

   * Push changes to GitHub.
   * On Heroku, navigate to the deployment tab and click *Deploy Branch*.

---

### Live App

The deployed app is available at the Heroku URL below...


https://naijarestaurantbookingsys-5ad47925ea27.herokuapp.com/


---

## Technologies Used

* *Python, **Django, **Django-Allauth*
* *Bootstrap 5* (via CDN)
* SQLite(Local Development) and PostgreSQL(Production)
* Cloudinary (for image hosting in advanced iterations)

---

## Credits

* Readme File inspired by Code Institute’s Blue Boar Inn project
* Images via *Pexels*
* Auth UI built with Django-Allauth, styled with Bootstrap