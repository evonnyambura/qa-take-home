# BUG-SQL-01: Claim Approved After Member's Policy End Date

## Bug Details

- **Bug ID:** BUG-SQL-01
- **Title:** Claim Approved After Member's Policy End Date
- **Module:** Claims Management
- **Severity:** High-potential financial risk
- **Priority:** High
- **Status:** New

## Environment Details

- **Testing Tool:** DB Fiddle
- **Database:** SQLite
- **Operating System:** Ubuntu 24.04.5 LTS
- **Browser:** Google Chrome 153.0.8010.36 (Official Build) (x86_64)
- **Screen Resolution:** 1920 × 1200 pixels
- **Browser Viewport:** 1280 × 800 pixels
- **Test Data:** Task 4 sample data

## Preconditions

- The SQL setup script has executed successfully.
- The `members` and `claims` tables contain the provided sample data.

## Steps to Reproduce

1. Open DB Fiddle in Google Chrome.
2. Select SQLite as the database engine.
3. Execute the provided setup script to create and populate the tables.
4. Run the following SQL query:

```sql
SELECT
    claims.id,
    members.name,
    members.policy_end,
    claims.submitted_on,
    claims.amount,
    claims.status
FROM claims
JOIN members ON claims.member_id = members.id
WHERE claims.submitted_on > members.policy_end;
```

5. Review the query results.
6. Compare the claim's submission date with the member's policy end date and claim status.

## Expected Result

Claims submitted after a member's policy end date should be flagged for eligibility review. The claim's eligibility should be checked against the applicable policy rules and the date the medical service was provided before confirming whether approval was appropriate.

## Actual Result

The query returns one claim submitted after the member's policy end date that has an `approved` status.

| Field | Result |
|---|---|
| Claim ID | 4 |
| Member Name | Wanjiru Kamau |
| Policy End Date | 2026-06-30 |
| Submission Date | 2026-07-15 |
| Claim Amount | 8,000 |
| Claim Status | approved |

The claim was submitted **15 days after the member's policy end date**, but its status is `approved`.

## Evidence

The screenshot below shows the SQL query and its output identifying the claim submitted after the member's policy end date.

![Question 4 SQL evidence](./bug-evidence/query%204.png)

**Screenshot file:** `query 4.png`

Save the screenshot in the `bug-evidence` folder.

## Severity and Priority Justification

**Severity: High**

There is a potential financial risk if the claim was approved despite the member being ineligible for coverage. Further investigation is needed to confirm whether a policy violation occurred.

**Priority: High**

The claim should be reviewed promptly to verify eligibility, particularly if payment has not yet been made.

## Recommended Action

1. Verify the member's coverage and the date the medical service was provided.
2. Check the applicable policy rules to determine whether the claim was eligible.
3. If the claim was incorrectly approved, correct its status and take the appropriate action.
4. Review the claims eligibility checks to determine whether additional validation is needed.

## Limitations

The dataset does not include the date the medical service was provided. Therefore, the submission date alone does not prove that the claim was incorrectly approved. The claim requires further investigation before it can be confirmed as a defect in the claims approval process.

This report identifies a **potential eligibility issue based on the available data**, not a confirmed system defect.





# BUG-SQL-02: Possible Duplicate Claims

## Bug Details

- **Bug ID:** BUG-SQL-02
- **Title:** Possible Duplicate Claims for the Same Member, Provider, Amount, and Submission Date
- **Module:** Claims Management
- **Severity:** Medium — requires investigation
- **Priority:** Medium
- **Status:** New

## Environment Details

- **Testing Tool:** DB Fiddle
- **Database:** SQLite
- **Operating System:** Ubuntu 24.04.5 LTS
- **Browser:** Google Chrome 153.0.8010.36 (Official Build) (x86_64)
- **Screen Resolution:** 1920 × 1200 pixels
- **Browser Viewport:** 1280 × 800 pixels
- **Test Data:** Task 4 sample data

## Preconditions

- The SQL setup script has executed successfully.
- The `claims`, `members`, and `providers` tables contain the provided sample data.

## Steps to Reproduce

1. Open DB Fiddle in Google Chrome.
2. Select SQLite as the database engine.
3. Execute the provided setup script to create and populate the tables.
4. Run the following SQL query:

```sql
SELECT
    claims.member_id,
    claims.provider_id,
    claims.amount,
    claims.submitted_on,
    COUNT(*) AS duplicate_count
FROM claims
GROUP BY
    claims.member_id,
    claims.provider_id,
    claims.amount,
    claims.submitted_on
HAVING COUNT(*) > 1;
```

5. Review the query results.
6. Compare the matching claims to determine whether they may represent duplicate submissions.

## Expected Result

Claims with matching member, provider, amount, and submission date should be flagged for further review to establish whether they relate to the same medical service.

## Actual Result

The query identifies two claims with matching details.

| Field | Result |
|---|---|
| Claim IDs | 5 and 6 |
| Member Name | Hassan Ali |
| Provider Name | Uhai Clinic |
| Claim Amount | 3,000 per claim |
| Submission Date | 2026-09-01 |
| Claim Status | submitted for both |
| Matching Record Count | 2 |

Both claims have the same member, provider, amount, and submission date. This indicates a possible duplicate submission that requires investigation.

## Evidence

The screenshot below shows the SQL query and its output identifying claims with matching details.

![Question 5 SQL evidence](./bug-evidence/query%205.png)

**Screenshot file:** `query 5.png`

Save the screenshot in the `bug-evidence` folder.

## Severity and Priority Justification

**Severity: Medium**

Potential duplicate claims may result in duplicate payments if both claims relate to the same service and are processed separately. The available data does not confirm that a duplicate has occurred.

**Priority: Medium**

The matching claims should be reviewed against supporting records before they are processed further.

## Recommended Action

1. Compare the claims against invoices, service dates, and other supporting records.
2. Confirm whether both claims relate to the same medical service.
3. If the claims are confirmed as duplicates, investigate why both submissions were accepted and take the appropriate corrective action.
4. Consider additional duplicate-detection checks using available claim identifiers and service details.

## Limitations

The dataset does not include invoice numbers or service dates. Matching member, provider, amount, and submission date alone does not prove that the claims relate to the same service.

This report identifies **possible duplicate claims based on the available data**, not confirmed duplicate submissions.