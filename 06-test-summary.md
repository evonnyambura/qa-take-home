# Test Summary: Sauce Demo Release Readiness

**Date:** 2026-10-13

## What I Tested

| Area | Method | Scope |
|---|---|---|
| Sauce Demo UI | Manual and exploratory testing | Product images, add to cart, remove from cart, product sorting, About page navigation, and user persona comparison |
| Sauce Demo UI | Playwright automation using Chromium | Login, locked-out user, adding two items to cart, and checkout |
| Restful Booker API | Pytest | Authentication, create, read, PUT, PATCH, delete, and negative test cases |
| Restful Booker load testing | k6 with up to 10 virtual users | `GET /booking` |

The API and load tests targeted Restful Booker, a separate system. Their results do not establish Sauce Demo's readiness.

## Test Results

| Area | Results | Findings |
|---|---|---|
| Manual UI testing | 5 bugs documented; 0 passed functional verifications recorded | Five issues identified and documented |
| Automated UI testing | 4 passed, 0 failed | All four automated tests passed |
| API testing | 12 tests reported; 9 passed, 3 failures reported | See `03-api/findings.md` for findings F-01 to F-04 |
| Load testing | 487 requests; 487 returned HTTP 200; p95 = 700.85 ms; 0% failed | Both configured thresholds were met for the tested endpoint |

Manual testing focused on documenting bugs. Zero recorded passed verifications does not mean every functional check failed.

## Functional Testing Findings

| Bug ID | Issue | Impact |
|---|---|---|
| BUG-001 | Product Images | Broken or misaligned images affect product browsing. |
| BUG-002 | Add to Cart | Adding multiple units may fail or provide insufficient feedback. |
| BUG-003 | Remove from Cart | Removing items may fail or leave cart counters inconsistent. |
| BUG-004 | Product Sorting | Sorting by price or name may not rearrange products correctly. |
| BUG-005 | About Page Navigation | A broken link leads to a 404 page. |

Evidence is stored in `02-bug-reports/bug-evidence/bug-01.png` through `bug-05.png`. The user persona comparison is documented in `02-bug-reports/user-comparison.md`.

## Top Three Risks

1. **Cart functionality:** The reported add-to-cart and remove-from-cart issues may affect users' ability to manage their items. Their severity and impact on checkout need confirmation.
2. **Limited automated coverage:** Four Playwright tests cover selected workflows in Chromium. Other user personas and application features may contain undetected defects.
3. **Unverified application performance:** The load test targeted Restful Booker, so Sauce Demo's performance under load remains untested.

## Recommendation

**HOLD pending confirmation of the cart defects' severity and status.**

The reported cart issues affect a core shopping workflow. Confirm their reproducibility, severity, and whether they remain unresolved before making a final release decision. If either defect blocks cart or checkout functionality, resolve and retest it before release.

## What I Would Test Next

- Reproduce the five reported bugs and confirm their severity and current status.
- Test adding and removing multiple items and verify cart contents and counters.
- Test `error_user`, `visual_user`, and `performance_glitch_user`.
- Test checkout validation, sorting, logout, and cart persistence.
- Add automated regression tests for the reported bugs after fixes.
- Test additional browsers, mobile screen sizes, accessibility, and protected-page access.
- Run a performance test against Sauce Demo if the environment permits it.

