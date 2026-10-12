# BUG-002: Add to Cart Does Not Work for Some Products

## Environment
- **OS:** Ubuntu 24.04.5 LTS
- **Browser:** Google Chrome 153.0.8010.36 (Official Build) (x86_64)
- **Screen resolution:** 1920 × 1200 pixels
- **Browser viewport:** 1280 × 800 pixels
- **Test account:** `problem_user`
- **Application URL:** https://www.saucedemo.com/

## Preconditions
- The user is logged in with the `problem_user` test account.
- The Products page is displayed.

## Steps to Reproduce
1. Open https://www.saucedemo.com/.
2. Log in using the `problem_user` test account.
3. Click **Add to cart** for the first product.
4. Repeat for the second product.
5. Attempt to add the third product to the cart.
6. Attempt to add the fourth product to the cart.
7. Attempt to add the last product to the cart.
8. Observe the button labels and cart badge after each attempt.

## Expected Result
Clicking **Add to cart** should add the selected product to the cart. The button should change to **Remove**, and the cart badge should reflect the updated number of items.

## Actual Result
The first, second, and last products can be added to the cart. The third and fourth products cannot be added successfully.

## Severity
**Major** — Users cannot add certain products to their cart, preventing them from purchasing those products through the normal shopping flow.

## Priority
**High** — The issue affects core shopping functionality.

## Evidence
- **Screenshot:** `bug-02.png`
- The screenshot shows an unsuccessful Add to cart attempt with the product and button state visible. 