# BUG-003: Remove Button Does Not Remove Product from Cart

## Environment
- **OS:** Ubuntu 24.04.5 LTS
- **Browser:** Google Chrome 153.0.8010.36 (Official Build) (x86_64)
- **Screen resolution:** 1920 × 1200 pixels
- **Browser viewport:** 1280 × 800 pixels
- **Test account:** `problem_user`
- **Application URL:** https://www.saucedemo.com/

## Preconditions
- The user is logged in with the `problem_user` test account.
- A product has been successfully added to the cart.
- The user opens that product's details page.

## Steps to Reproduce
1. Open https://www.saucedemo.com/.
2. Log in using the `problem_user` test account.
3. Add a product to the cart using a product whose Add to cart button works.
4. Open that product's details page.
5. Click **Remove**.
6. Observe the button state and cart badge.
7. Open the cart and check whether the product is still listed.

## Expected Result
The selected product should be removed from the cart. The button should change back to **Add to cart**, the cart badge should decrease, and the product should no longer appear in the cart.

## Actual Result
On the product details page, clicking **Remove** does not appear to remove the product, and the cart badge does not decrease.

## Severity
**Major** — Users cannot reliably remove unwanted products from their cart.

## Priority
**High** — The issue affects cart management and can interfere with correcting an order before checkout.

## Evidence
- **Screenshot:** `bug-03.png`
- The screenshot shows the product details page showing the Remove button and cart badge. 