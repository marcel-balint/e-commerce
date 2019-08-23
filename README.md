## The Shopper - Ecommerce (full stack web application)

A live demo can be found [here](https://easy-recipes.herokuapp.com/).

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
  

The wireframes for this website can be seen [here](https://github.com/marcel-balint/easy-recipes/tree/master/static/wireframes).

## Features

- **Navbar**, located at the top of the website page, has a background color of silver(`#e8e8e8`). Contains five links:
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