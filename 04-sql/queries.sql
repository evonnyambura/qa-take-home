-- Question 1: List every claim with the member's name, provider's name, amount and status, newest first

SELECT
    members.name AS member_name,
    providers.name AS provider_name,
    claims.amount,
    claims.status,
    claims.submitted_on
FROM claims
JOIN members ON claims.member_id = members.id
JOIN providers ON claims.provider_id = providers.id
ORDER BY claims.submitted_on DESC;

-- Question 2: Show the total amount of approved claims for each employer

SELECT
    employers.name AS employer_name,
    SUM(claims.amount) AS total_approved_amount
FROM employers
JOIN members ON employers.id = members.employer_id
JOIN claims ON members.id = claims.member_id
WHERE claims.status = 'approved'
GROUP BY employers.name;

-- Question 3: Find members who have never submitted a claim

SELECT
    members.name
FROM members
WHERE members.id NOT IN (
    SELECT claims.member_id
    FROM claims
);

-- Question 4: Find claims submitted after the member's policy had ended

SELECT
    claims.id AS claim_id,
    members.name AS member_name,
    claims.submitted_on,
    members.policy_end
FROM claims
JOIN members ON claims.member_id = members.id
WHERE claims.submitted_on > members.policy_end;

-- Question 5: Find possible duplicate claims with the same member, provider, amount and date

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