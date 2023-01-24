- [Contents](#contents)
- [Mahir Store](#mahir-store)
  * [UX](#ux)
  * [Purpose](#purpose)
  * [User Stories](#user-stories)
    + [User Stories for in ths project:](#user-stories-for-in-ths-project:)
  * [Wireframes](#wireframes)
    + [Home page](#home-page)
    + [All Products](#all-products)
    + [Product details](#product-details)
    + [Profile app](#profile-app)
  * [Agile Methodology](#agile-methodology)
    + [Canban board](#canban-board)
  * [Existing Features](#existing-features)
    + [Navbar and Footer](#navbar-and-footer)
    + [Footer](#footer)
    + [Shop](#shop)
    + [User authentication](#user-authentication)
  * [Future Features](#future-features)
    + [Google places API to fetch address data](#google-places-api-to-fetch-address-data)
    + [Current stock](#current-stock)
    + [Javascript validation on input](#javascript-validation-on-input)
    + [Success page after question is submitted](#success-page-after-question-is-submitted)
    + [Secured view to unsubscribe](#secured-view-to-unsubscribe)
    + [Dashboard for superuser](#dashboard-for-superuser)
    + [search option in questions](#search-option-in-questions)
  * [Search Engine Optimalization](#search-engine-optimalization)
  * [Web Marketing](#web-marketing)
    + [Newsletter](#newsletter)
    + [Facebook](#facebook)
  * [Technologies Used](#technologies-used)
    + [Languages Used](#languages-used)
    + [Technologies and Programs Used:](#technologies-and-programs-used-)
    + [Frameworks Libraries and Programs Used](#frameworks-libraries-and-programs-used)
  * [Code Validation](#code-validation)
    + [HTML beautify](#html-beautify)
    + [HTML valiation](#html-valiation)
    + [CSS validation](#css-validation)
    + [JavaScript validation](#javascript-validation)
    + [Python beautify](#python-beautify)
    + [Python validator](#python-validator)
  * [Tests](#tests)
    + [Automated tests](#automated-tests)
    + [Lighthouse](#lighthouse)
  * [Project Bugs and Solutions:](#project-bugs-and-solutions-)
    + [Grid with filtering and sorting icons](#grid-with-filtering-and-sorting-icons)
    + [Button In trolley on all trees view](#button-in-trolley-on-all-trees-view)
    + [Checkbox not in line with label for some screen widths](#checkbox-not-in-line-with-label-for-some-screen-widths)
    + [Addressing email to the registered user](#addressing-email-to-the-registered-user


# Mahir Store

[![showpiece home page](readme_docs/showpices/Home-page.png)](https://mahir-store.herokuapp.com/)

Click [here](https://mahir-store.herokuapp.com/) to live site.  
------

## UX

Mahir Store is designed in e-commerce based. Color background and light cards are used. The user is given different kind of choices which way to get to the shop from the home page. 

To make a purchase user can pay with a credit card as checkout page features stripe payments.

The user can also sign up and subscribe to the newsletter via email.

## Purpose

The app is designed as a e-commerce application that encourages the users to make a purchase

## User Stories

### User Stories for in ths project:

| id  |  content |
| ------ | ------ |
|  [#1](https://github.com/mamuzaan/portfolio_p5_store/issues/1) | As a Shopper I want to be able to View a list of products So that Select some to purchase |
|  [#2](https://github.com/mamuzaan/portfolio_p5_store/issues/2) | As a shopper I want to be able to view individual product details So that identify the price description, product rating, product image and available sizes |
|  [#3](https://github.com/mamuzaan/portfolio_p5_store/issues/3) | As a Shopper I want to be able to quickly identify deals clearance, items and special offers So that take advantage of special savings on products I'd like to purchase |
|  [#4](https://github.com/mamuzaan/portfolio_p5_store/issues/4) | As a shopper I want to be able to easily see what I've searched for and the number of results so that quickly decide whether the product I want is available |
|  [#5](https://github.com/mamuzaan/portfolio_p5_store/issues/5) | As a shopper I want to be able to sort the list of available products so that I can easily identify the best rated, best priced and category based sorted products |
|  [#6](https://github.com/mamuzaan/portfolio_p5_store/issues/6) | As a shopper I want to be able to search for a product by name or description so that I can find a specific product I'd like to purchase |
|  [#7](https://github.com/mamuzaan/portfolio_p5_store/issues/7) | As a shopper I want to be able to sort a specific category of product so that I can find the best priced or best rated product in a specific category or sort the products in that category by name |
|  [#8](https://github.com/mamuzaan/portfolio_p5_store/issues/8) | As a shopper I want to be able to view items in my bag to be purchased so that I can identify the total cost of my purchase and all items I will receive |
|  [#9](https://github.com/mamuzaan/portfolio_p5_store/issues/9) | As a shopper I want to be able to adjust the quantity of individual items in my bag so that I can easily make changes to my purchase before checkout |
|  [#10](https://github.com/mamuzaan/portfolio_p5_store/issues/10) | As a shopper I want to be able to view an order confirmation after checkout so that I can verify that I haven't made any mistakes |
|  [#11](https://github.com/mamuzaan/portfolio_p5_store/issues/11) | As a shopper I want to be able to easily enter my payment so that I can checkout quickly and with no hassies |
|  [#12](https://github.com/mamuzaan/portfolio_p5_store/issues/12) | As a shopper I want to be able to feel my personal and payment information is safe and secure so that I can confidently provid the needed information to make a purchase |
|  [#13](https://github.com/mamuzaan/portfolio_p5_store/issues/13) | As a shopper I want to be able to receive an email confirmation after checking out so that I can keep the confirmation of what I have purchased for my records |
|  [#14](https://github.com/mamuzaan/portfolio_p5_store/issues/14) | As a site user I want to be able to have a personalized user profile so that I can view my personal order history and order confirmations, and save my payment information |
|  [#15](https://github.com/mamuzaan/portfolio_p5_store/issues/15) | As a shopper I want to be able to easily view the total of my purchases at any time So that avoid spending too much |
|  [#16](https://github.com/mamuzaan/portfolio_p5_store/issues/16) | As a shopper I want to be able to easily select the size and quantity of a product when purchasing it so that ensure I don't accidentally select the wrong product quantity or size |
|  [#17](https://github.com/mamuzaan/portfolio_p5_store/issues/17) | As a shopper I want to be able to sort multiple categories of products simultaneously so that I can find the best priced or best rated products across board categories such as 'shirt' or 'pants' |
|  [#18](https://github.com/mamuzaan/portfolio_p5_store/issues/18) | As a site user I want to be able to easily register for an account so that have a personal account and be able to view my profile |
|  [#19](https://github.com/mamuzaan/portfolio_p5_store/issues/19) | As a site user I want to be able to easily login or logout so that I can access my personal account information |
|  [#20](https://github.com/mamuzaan/portfolio_p5_store/issues/20) | As a site user I want to be able to easily recover my password in case I forget it so that I can recover access to my account |
|  [#21](https://github.com/mamuzaan/portfolio_p5_store/issues/21) | As a site user I want to be able to receive an email confirmation after registering so that I can verify my account registration was successful |
|  [#22](https://github.com/mamuzaan/portfolio_p5_store/issues/22) | As a Store owner I want to be able to add a product so that I can add new items to my store |
|  [#23](https://github.com/mamuzaan/portfolio_p5_store/issues/23) | As a Store owner I want to be able to Edit Update a product so that I can change product prices, descriptions, images and other product criteria |
|  [#24](https://github.com/mamuzaan/portfolio_p5_store/issues/24) | As a Store owner I want to be able to delete a product so that I can remove items that are no longer for sale |

## Wireframes 

The general structure of the page on this project and many of it's features. Wireframes were created with [Balsamiq](https://balsamiq.com/wireframes/?gclid=Cj0KCQiAubmPBhCyARIsAJWNpiMYzrk_0rLzl3vgYKRLXwnX7rpqyQiUFdyt3xHGpRiHlZlozwO_pvcaAvUFEALw_wcB). 

### Home page

![wireframes of home page](readme_docs/wireframe/home-page.png)

The design of this page is heavily inspired by bootstrap example. This design was than further individualised to match the overal style of the page.

Home page is divided into two main sections: carousele and product images. This aims to give the user a feeling of dealing with real people.

### All Products

![wireframes of all products](readme_docs/wireframe/all-product.png)

The design of this page is products of all categories. This design was than further individualised to match the overal style of the page.

This page is divided for all type of product images.

### Product details

![wireframes of product details page](readme_docs/wireframe/product-details.png)

The design of this page is products for details of this product. This page is divided for details of product like images, size, price, category, desctiption and more.

### Profile app

![wireframes of user profile apps page](readme_docs/wireframe/profile-page.png)

The design of this page is user profile. This page is divided for details of Users name, address, state, county, postcode, country and history of products already user shop.

## Agile Methodology

### Canban board

![Screenshot of the canban board](readme_docs/canban-board/kanban-board.png)


Github issues were used to create the User stories and group. Link to the project with live issues can be found [here](https://github.com/users/mamuzaan/projects/5).

