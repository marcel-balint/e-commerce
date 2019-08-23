## The Shopper - Ecommerce (full stack web application)

A live demo can be found [here](https://the-shopper120.herokuapp.com/).

This is a fictional ecommerce site built for Code Institute as a part of Full Stack Software Development Diploma course. Project was build with using semantic HTML5, CSS3,
JavaScript (jQuery) along with Python framework Django 1.11.4.


## UX

#### User Stories
Users are able to:
  - access the site using their preferred device (mobile, tablet, desktop) without any loss of functionality.
  - sing up so that he/she can have his/her own account.
  - login so that he/she can buy clothes from the site.
  - log out.
  - make purchases online.
  - add and remove products in a shopping cart.
  - see a summary of the cart so that he/she can easily see all purchases.
  - see a summary of the cart so that he/she can easily remove items.
  - have intuitive access to the checkout page so that he/she can easily proceed with the payment.
  - change the credit card linked his/her account.
  

The wireframes for this website can be seen [here](https://github.com/marcel-balint/e-commerce/tree/master/wireframes).

## Features

- **Navbar**, located at the top of the website page, has a background color of silver(`#e8e8e8`). Contains six links:
   - **Home** - links to home page: on hover, the border bottom transitions into black color;
   - **Contact** - links to a page with a form where a user can send a contact message.
   - **Products** - links to a page where a user can find all the products from which he/she can choose which to buy. Once clicked on a product, the user will be taken to a page where more details about that product are displayed, and a button to _add_ or _remove_ the product from the shopping cart.
   - **Shopping cart icon** - links to the shopping cart. In the shopping cart the user can see a list of all purchases and can easily remove items. At the bottom of the shopping list there is a *checkout* button, when clicked:
      - if not logged in, the user will be presented with two choices: to login or to countinue the checkout process as a guest. If he/she chooses to continue as a guest, will have to enter an email address, then, two forms will be displayed, one where the user must type the _shipping address_ and one for _billing address_.
      After that a page will be presented, where a payment card can be added and the user will be redirected to the _**finalize checkout**_ page where there is a summary of all products from the _**shopping cart:**_ the _**shipping address**_, the _**billing address**_, the _**payment method**_, the _**cart total**_, the _**shipping fee**_ and the _**order total**_ (the _**cart total**_ is the sum of the _**the order total**_ + _**shipping fee**_).
      Next to where the payment method is listed, there is a link where the user has the option to change the card. If clicked on _**checkout**_ button, located at the bottom of the summary list, the payment will be processed and a message of thanks will be displayed.
      - if logged in, the user will have to fill in the _shipping address_ and the _billing address_ then, will be redirected to the finalize checkout page where there is a summary of all products from the _**shopping cart:**_ the _**shipping address**_, the _**billing address**_, the _**payment method**_, the _**cart total**_, the _**shipping fee**_ and the _**order total**_ (the _**cart total**_ is the sum of the _**order total**_ + _**shipping fee**_). 
      Next to where the payment method is listed, there is a link where the user has the option to change the card. If clicked on _**checkout**_ button, located at the border of the summary list, the payment will be processed and a message of thanks will be displayed.         
   - **Register** - links to a page with a form where users can register by typing a unique _username_, an _email address_ and a _password_ which must be confirmed. At the bottom of the register form there is a link which links to the _login_ page for users who already have an account.
   - **Login** - links to a page with a form where registered users can login by typing their _username_ and _password_. At the bottom of the login form there is a link which links to the _register_ page for users who do not have an account yet.

- On the _home page_ there is a background image with introduction text and a button which links to the _products_ page - The aim of this section is to introduce the user to the website;
- **Footer** - contain a link to the _Contact_ page and four social media links with a hover effect of `scale(1.3);`.


#### Features Left to Implement

- Pagination 

## Technologies Used

* [Cloud9 IDE](https://aws.amazon.com/cloud9/) - Used to build this project.
* [GitHub](https://github.com/) - Used as remote storage of my code online.

#### Front-End Technologies

* [HTML5](https://en.wikipedia.org/wiki/HTML) - Used as the base for markup text.
* [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) - Used as the base for cascading styles.
* [JQuery](https://code.jquery.com/jquery/) - Used as the primary JavaScript functionality.
* [Bootstrap](https://getbootstrap.com/) - Used as the front-end framework for layout and design.
* [Stripe API ](https://stripe.com/docs/api?lang=python) - Used to make secured payments.
* [Amazon AWS S3](https://aws.amazon.com/) - Used to store staticfiles and media folder and files.

#### Back-End Technologies

* [Python](https://www.python.org/) - Used as the back-end programming language.
* [Django 1.11.4](https://docs.djangoproject.com/en/1.11/) -  Used as my Python web framework.
* [Heroku](https://www.heroku.com/) - Hosts the deployed version of this project.
* [PostgreSQL](https://www.postgresql.org/) - Used as relational SQL database plugin via Heroku.


## Testing
All pages have been tested on all screen sizes. This has been done via Google Chrome developer tools and by testing on my own personal phone and ipad.
Also all features of the page are scaling as intended in tablet and mobile devices.

I checked the _register_ form to see if an error occurred when entering an existing username and email, and the form validations reacts as expected..
Also, if the _confirmation password_ does not match the _password_, it will cause an error. I made sure that the _login_ form
will cause an error if the username and password entered are not registered in the database.

I also checked to see if the number next to the cart is updated when a product is added or removed. While testing the checkout process, 
I made sure that a new customer who does not have a payment card attached to his account will have to add a card to complete the checkout process.
The _change card_ functionality on the _finalize checkout_ page has been tested to make sure it is working correctly and redirects back as intended.


All links and forms are verified to be working correctly via manual testing.



#### Validators
- **HTML** 

   Passing the HTML code from all templates into the [W3C Markup Validator](https://validator.w3.org/) generates numerous errors, but these are expected as the validator is unable to understand the Django template tags. 
- **CSS**
    
  The CSS code passes [W3C CSS Validation Service ](https://jigsaw.w3.org/css-validator/)without errors.

- **JavaScript**
  
  The JavaScript code passes trough [JSHint](https://jshint.com/) without errors.

- **Python**
 
  The Python code was passed through the [PEP8 Online validator](http://pep8online.com/) and is fully PEP8 compliant.
   
 The project was tested to ensure full usability across the following browsers:

  * Google Chrome

  * Mozilla Firefox

  * Microsoft Edge
  
###### Chrome's DevTools Audit Report

![Audit Report]()
