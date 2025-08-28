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

Built using the *Django framework* with *SQLite (at development) and PostgreSQL (at production), and authenticated via **Django-Allauth. The UI leverages **Bootstrap 5* for responsive and fast front-end development. The project followed Agile practices, using *user stories* managed on a [Kanban Board](https://github.com/users/Irelandoracle1/projects/5), with features prioritized via a MoSCoW backlog to support incremental builds with constant validation.

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

## Wireframes 

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

## Snapshots 

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

Manual test was used in the testing of the programme.

## Manual Tests

| Function      | Test                                                                 | Pass |
|---------------|----------------------------------------------------------------------|------|
| General       | Index page fully renders with all content visible                    | ✓    |
| General       | All links routed to correct pages                                    | ✓    |
| General       | Menu page fully renders with all content visible                     | ✓    |
| General       | Header collapses to dropdown on small screens                        | ✓    |
| General       | Footer minimised on small screens                                    | ✓    |
| General       | Latest version deployed to Heroku                                   | ✓    |
| Access        | Users able to login with username and email                          | ✓    |
| Access        | User given feedback as to if they are logged in or not               | ✓    |
| Access        | Log in feedback links to register and log in pages                   | ✓    |
| Access        | Users unable to access admin page without proper permissions         | ✓    |
| Bookings  | Bookings only visible when logged in                             | ✓    |
| Bookings  | User can only view Bookings they have made                       | ✓    |
| Bookings  | Logged in user can make a Bookings                                | ✓    |
| Bookings  | Logged in user can edit a Bookings                                | ✓    |
| Bookings  | Logged in user can Cancel a Bookings                              | ✓    |
| Bookings  | Logged in staff/superuser can make a Bookings                     | ✓    |
| Bookings  | Logged in staff/superuser can edit a Bookings                     | ✓    |
| Bookings  | Logged in staff/superuser can cancel a Bookings                   | ✓    |
| Bookings  | Datepicker prevents user booking date prior to current date          | ✓    |
| Bookings  | Bookings form cannot be submitted without all fields being completed | ✓ |
| Menu          | Menu page fully renders all content to correct sections              | ✓    |
| Menu          | Logged in staff/superuser can add menu items                         | ✓    |
| Menu          | Logged in staff/superuser can edit menu items                        | ✓    |
| Menu          | Logged in staff/superuser can delete menu items                      | ✓    |
| Menu          | Menu items can only be created, edited and deleted through admin panel | ✓  |


# HTML Validation

The below pages were put through the [W3C validator](https://validator.w3.org/) 
As the validator doesn't understand Django template syntax, the URL of each page was entered into the validator.

| Page                     | Pass |
|--------------------------|------|
| base.html   | ✓    |
| home.html   | ✓    |
| booking_form.html | ✓ |
| booking_list.html  | ✓ |
| menu_list.html   | ✓    |
| booking_confirm_delete.html | ✓    |
| logout.html              | ✓    |
| login.html               | ✓    |
| password_reset.html      | ✓    |
| signup.html              | ✓    |

Includes:

* Form validation tests (e.g., double-booking prevention).
* View tests to ensure correct behavior for booking create, update, and delete.
* Template rendering tests for key pages like home, menu, booking list.

---

# CSS Validation

The below pages were put through the [W3C validator](https://jigsaw.w3.org/css-validator/#validate_by_input)

| Page                  | Pass | Message                                                                 |
|-----------------------|------|-------------------------------------------------------------------------|
| static/css/style.css  | ✓    | Congratulations! No Error Found.|

*Note:*  
The single CSS style sheet passes without error, with the message listed above.  


# PEP8 Validation

The below pages were put through the [PEP8 validator](https://pep8ci.herokuapp.com/#) and returned no errors:

| Page                        | Pass |
|-----------------------------|------|
| booking/admin.py               | ✓    |
| booking/apps.py                | ✓    |
| booking/models.py              | ✓    |
| booking/tests.py          | ✓    |
| booking/urls.py                | ✓    |
| booking/views.py               | ✓    |
| booking/forms.py               | ✓    |
| naijarestaurant/urls.py        | ✓    |
| naijarestaurant/asgi.py          | ✓    |
| naijarestaurant/urls.py          | ✓    |
| naijarestaurant/settings.py      | ✓   |
| naijarestaurant/wsgi.py          | ✓    |

---

### Notes on Errors
- No errors, all fixed.
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
* Images via [Pexels](https://pexels.com)
* Auth UI built with Django-Allauth, styled with Bootstrap