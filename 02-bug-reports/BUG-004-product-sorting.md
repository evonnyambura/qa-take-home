# BUG-004: Product Sorting Does Not Apply the Selected Order

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
3. Locate the product sorting dropdown.
4. Select **Name (A to Z)**.
5. Observe the order of the product names.
6. Repeat with the other available sorting options.
7. Compare the displayed product order with the selected sorting option.

## Expected Result
The product list should be reordered according to the selected sorting option. For example, **Name (A to Z)** should display product names in alphabetical ascending order.

## Actual Result
The product does not respond to clicks on the all the ranges from A to Z and Z to A and also from the lowest to the highest price.

## Severity
**Major** — Unresponsive sorting makes it harder for users to locate and compare products.

## Priority
**Medium** — Product discovery is affected, although users may still be able to browse and purchase products.

## Evidence
- **Screenshot:** `bug-04.png`
- The screenshot shows the selected sorting option and the resulting product order. 