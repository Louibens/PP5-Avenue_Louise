Go back to [README.md](/README.md)

# Testing
- [Code Validation](#code-validation)
    - [HTML](#html)
    - [CSS](#css)
    - [JavaScript](#JavaScript)
    - [Python](#python)
- [Responsiveness](#Responsiveness)
- [Browser Compatibility](#browser-compatibility)
- [Lighthouse](#Lighthouse)
- [Manual Testing](#manual-testing)
- [User Story Testing](#user-story-testing)

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

![Add a Product](documentation/images/)
</details>

<details>
    <summary>Add a Workshop</summary>

![Add a Workshop](documentation/images/)
</details>

<details>
    <summary>Add a Testimonial</summary>

![Add a Testimonial](documentation/images/)
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
