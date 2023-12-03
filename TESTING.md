Go back to [README.md](/README.md)

# Testing
- [Code Validation](#code-validation)
    - [HTML](#html)
    - [CSS](#css)
    - [JavaScript](#JavaScript)
    - [Python](#python)
- [Responsiveness](#Responsiveness)
- [Lighthouse](#Lighthouse)
- [Accessability](#Accessability)
- [Stripe](#Stripe)
- [Manual Testing](#manual-testing)
- [Additional Testing Comments](#additional-testing-comments)


## Code Validation
### HTML

W3C Validator flagged 
- “The type attribute is unnecessary for JavaScript resources.”. Updated where necessary
- "The value of the for attribute of the label element must be the ID of a non-hidden form control." Updated the checkout page

<details>
    <summary>Homepage</summary>

![Homepage](documentation/HTML/Homepage.png)
</details>

<details>
    <summary>Products</summary>

![Products](documentation/HTML/products.png)
</details>

<details>
    <summary>Product Details</summary>

![Product Details](documentation/HTML/product_details.png)
</details>

<details>
    <summary>Workshops</summary>

![Workshops](documentation/HTML/workshops.png)
</details>

<details>
    <summary>Workshop Details</summary>

![Workshop Details](documentation/HTML/workshop_details.png)
</details>

<details>
    <summary>About Us</summary>

![About Us](documentation/HTML/about_us.png)
</details>

<details>
    <summary>Contact Us</summary>

![Contact Us](documentation/HTML/contact_us.png)
</details>

<details>
    <summary>My Profile</summary>

![My Profile](documentation/HTML/profile.png)
</details>

<details>
    <summary>Add a Product</summary>

![Add a Product](documentation/HTML/add_product.png)
&nbsp;

HTML validation flagged an issue with a duplicated id (id="id_image"). Following investigation this is being generated in the custom_clearable_file_input.html file. Further research required to fix
</details>

<details>
    <summary>Add a Workshop</summary>

![Add a Workshop](documentation/HTML/add_workshop.png)
</details>

<details>
    <summary>Add a Testimonial</summary>

![Add a Testimonial](documentation/HTML/add_testimonial.png)
</details>

<details>
    <summary>Edit a Product</summary>

![Edit a Product](documentation/HTML/edit_product.png)
&nbsp;

HTML validation flagged an issue with a duplicated id (id="id_image"). Following investigation this is being generated in the custom_clearable_file_input.html file. Further research required to fix
</details>

<details>
    <summary>Edit a Workshop</summary>

![Edit a Workshop](documentation/HTML/edit_workshop.png)
</details>

<details>
    <summary>Bag</summary>

![Bag](documentation/HTML/bag.png)
</details>

<details>
    <summary>Checkout</summary>

![Checkout](documentation/HTML/checkout.png)
</details>

<details>
    <summary>Checkout Success</summary>

![Checkout Success](documentation/HTML/checkout_success.png)
</details>

### CSS

Jigsaw CSS validator - no issues flagged

<details>
    <summary>base.css</summary>

![base.css](documentation/CSS/base.css.png)
</details>

<details>
    <summary>checkout.css</summary>

![checkout.css](documentation/CSS/checkout.css.png)
</details>

### JavaScript

JSHint flagged one undefined variable which cannot be changed as it is required for Stripe. Any missing semi-colons have been added where required.

<details>
    <summary>stripe_elements.js</summary>

![stripe_elements.js](documentation/images/javascript.png)
</details>

<details>
    <summary>scroll to top</summary>

![scroll to top](documentation/images/scroll_top.png)
</details>

<details>
    <summary>remove item</summary>

![remove item](documentation/images/remove_item.png)
</details>

### Python

Issues flagged during python code validation were mainly lines too long or blank spaces. All of the flagged issues have been resolved.

- avenue_louise project app

<details>
    <summary>settings.py</summary>

![settings.py](documentation/python/avelou_settings.py.png)
</details>

<details>
    <summary>urls.py</summary>

![urls.py](documentation/python/avelou_urls.py.png)
</details>

<details>
    <summary>views.py</summary>

![views.py](documentation/python/avelou_views.py.png)
</details>
&nbsp;

- bag app

<details>
    <summary>bag_contexts.py</summary>

![bag_contents.py](documentation/python/bag_contexts.py.png)
</details>

<details>
    <summary>urls.py</summary>

![urls.py](documentation/python/bag_urls.py.png)
</details>

<details>
    <summary>views.py</summary>

![views.py](documentation/python/bag_views.py.png)
</details>
&nbsp;

- checkout app

<details>
    <summary>admin.py</summary>

![admin.py](documentation/python/checkout_admin.py.png)
</details>

<details>
    <summary>forms.py</summary>

![forms.py](documentation/python/checkout_forms.py.png)
</details>

<details>
    <summary>models.py</summary>

![models.py](documentation/python/checkout_models.py.png)
</details>

<details>
    <summary>signals.py</summary>

![signals.py](documentation/python/checkout_signals.py.png)
</details>

<details>
    <summary>urls.py</summary>

![urls.py](documentation/python/checkout_urls.py.png)
</details>

<details>
    <summary>views.py</summary>

![views.py](documentation/python/checkout_views.py.png)
</details>

<details>
    <summary>webhook_handler.py</summary>

![webhook_handler.py](documentation/python/checkout_webhook_handler.py.png)
</details>

<details>
    <summary>webhooks.py</summary>

![webhooks.py](documentation/python/checkout_webhooks.py.png)
</details>
&nbsp;

- home app

<details>
    <summary>admin.py</summary>

![admin.py](documentation/python/home_admin.py.png)
</details>

<details>
    <summary>forms.py</summary>

![forms.py](documentation/python/home_forms.py.png)
</details>

<details>
    <summary>models.py</summary>

![models.py](documentation/python/home_models.py.png)
</details>

<details>
    <summary>urls.py</summary>

![urls.py](documentation/python/home_urls.py.png)
</details>

<details>
    <summary>views.py</summary>

![views.py](documentation/python/home_views.py.png)
</details>
&nbsp;

- products app

<details>
    <summary>admin.py</summary>

![admin.py](documentation/python/products_admin.py.png)
</details>

<details>
    <summary>forms.py</summary>

![forms.py](documentation/python/products_forms.py.png)
</details>

<details>
    <summary>models.py</summary>

![models.py](documentation/python/products_models.py.png)
</details>

<details>
    <summary>urls.py</summary>

![urls.py](documentation/python/products_urls.py.png)
</details>

<details>
    <summary>views.py</summary>

![views.py](documentation/python/products_views.py.png)
</details>

<details>
    <summary>widgets.py</summary>

![widgets.py](documentation/python/products_widgets.py.png)
</details>
&nbsp;

- profiles app

<details>
    <summary>forms.py</summary>

![forms.py](documentation/python/profiles_forms.py.png)
</details>

<details>
    <summary>models.py</summary>

![models.py](documentation/python/profiles_models.py.png)
</details>

<details>
    <summary>urls.py</summary>

![urls.py](documentation/python/profiles_urls.py.png)
</details>

<details>
    <summary>views.py</summary>

![views.py](documentation/python/profiles_views.py.png)
</details>
&nbsp;

- testimonials app

<details>
    <summary>admin.py</summary>

![admin.py](documentation/python/testimonials_admin.py.png)
</details>

<details>
    <summary>forms.py</summary>

![forms.py](documentation/python/testimonials_forms.py.png)
</details>

<details>
    <summary>models.py</summary>

![models.py](documentation/python/testimonials_models.py.png)
</details>

<details>
    <summary>urls.py</summary>

![urls.py](documentation/python/testimonials_urls.py.png)
</details>

<details>
    <summary>views.py</summary>

![views.py](documentation/python/testimonials_views.py.png)
</details>
&nbsp;

- workshops app

<details>
    <summary>admin.py</summary>

![admin.py](documentation/python/workshops_admin.py.png)
</details>

<details>
    <summary>forms.py</summary>

![forms.py](documentation/python/workshops_forms.py.png)
</details>

<details>
    <summary>models.py</summary>

![models.py](documentation/python/workshops_models.py.png)
</details>

<details>
    <summary>urls.py</summary>

![urls.py](documentation/python/workshops_urls.py.png)
</details>

<details>
    <summary>views.py</summary>

![views.py](documentation/python/workshops_views.py.png)
</details>


## Responsiveness

The site has been fully tested on different screen sizes to ensure users get an optimal experience whether accessing the site from a mobile or on a desktop computer. Bootstrap grid system is used to reposition elements depending on screensize. 

<details>
    <summary>Mobile Homepage</summary>

![Mobile Homepage](documentation/mobile/home-mob.jpg)
</details>

<details>
    <summary>Mobile Products</summary>

![Mobile Products](documentation/mobile/products-mob.jpg)
</details>

<details>
    <summary>Mobile Product Details</summary>

![Mobile Product Details](documentation/mobile/product-details-mob.jpg)
</details>

<details>
    <summary>Mobile Workshops</summary>

![Mobile Workshops](documentation/mobile/workshops-mob.jpg)
</details>

<details>
    <summary>Mobile Workshops Details</summary>

![Mobile Workshops Details](documentation/mobile/workshop_details-mob.jpg)
</details>

<details>
    <summary>Mobile About Us</summary>

![Mobile About Us](documentation/mobile/about-mob-bug.jpg)
</details>

<details>
    <summary>Mobile Contact Us</summary>

![Mobile Contact Us](documentation/mobile/contact-mob.jpg)
</details>

## Lighthouse

I used Lighthouse within the Chrome Developer Tools to allow me to test the performance, accessibility, best practices and SEO of the website.
Images have been compressed using tinypng and converted to webp using convertio however performance could still be improved.

 - Desktop

 ![Desktop](documentation/images/lighthouse_desktop.png)

 - Mobile

 ![Desktop](documentation/images/lighthouse-mobile.png)

## Accessability

The site was tested for accessability using the wave accessability tool (https://wave.webaim.org/). Any errors or contract errors have been resolved to ensure the site is optimised for individuals with disabilities.

 ![Wave](documentation/images/wave.png)


## Stripe

- Stripe webhooks functioning successfully

    ![Manual Testing](documentation/images/stripe.png)

## Manual Testing

- The below table details the 65 test cases that were used and the results and relates back to the website Features
- There is also a "FAILED tests now fixed" section outlining the tests that failed and how they were fixed
- Click the table to enlarge for better readability
- These tests were carried out on desktop and mobile devices

    <details>
    <summary>Manual Testing Table</summary>

    ![Manual Testing](documentation/images/testing-al.png)
    </details>

### Additional Testing Comments

- Testing has been carried out on the following browsers :

    - Chrome Version 119.0.6045.200 (Official Build) (64-bit)
    - Firefox Version 120.0.1 (64-bit)
    - Edge Version 119.0.2151.97 (Official build) (64-bit)

- Testing has also been carried out on desktop, laptop and smartphone for a variety of screen sizes.

- 1 issue has been identified when testing on a couple of iphones. A couple of the images are being rotated. Further investigation and research is required to get this issue resolved.
![Manual Testing](documentation/images/iphone.jpg)


Go back to [README.md](/README.md)