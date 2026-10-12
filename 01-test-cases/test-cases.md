# Task 1: Appointment Booking Test Cases

## Feature

Book an appointment with an in-network provider.

## Scope

Verify appointment eligibility, booking dates and times, appointment limits, cancellation rules, and booking confirmations.

## Test Cases

| ID | Title | Preconditions | Steps | Test data | Expected result | Priority |
|---|---|---|---|---|---|---|
| TC-01 | Book an appointment successfully | Member has an active policy, an in-network provider is available, and the member has no upcoming appointments. | 1. Log in as the member. 2. Select an in-network provider. 3. Select an available slot within the permitted booking period. 4. Confirm the booking. | Active policy; in-network provider; available slot today at 10:00. | The appointment is booked, an in-app confirmation is displayed, and an SMS confirmation is sent. | High |
| TC-02 | Reject booking when the member's policy is inactive | Member has an inactive policy and an available provider slot exists. | 1. Log in as the member. 2. Select an in-network provider. 3. Attempt to book an available slot. | Inactive policy; available slot today at 10:00. | The appointment is not booked because the member does not have an active policy. | High |
| TC-03 | Reject booking with an out-of-network provider | Member has an active policy and an out-of-network provider is available. | 1. Log in as the member. 2. Attempt to select or book the out-of-network provider. | Active policy; out-of-network provider. | The member cannot complete a booking with an out-of-network provider. | High |
| TC-04 | [BVA] Book an appointment today | Member has an active policy and an in-network provider has an available slot today. | 1. Log in. 2. Select the provider. 3. Select an available slot today. 4. Confirm the booking. | Today's date; available slot at 10:00. | The appointment is booked successfully, and both confirmation methods are triggered. | High |
| TC-05 | [BVA] Book an appointment 30 days ahead | Member has an active policy and an in-network provider has an available slot exactly 30 days ahead. | 1. Log in. 2. Select the provider. 3. Navigate to the date 30 days ahead. 4. Select an available slot. 5. Confirm the booking. | Appointment date = today + 30 days. | The appointment is bookable if the 30-day limit is inclusive. Confirm inclusivity with the product manager. | High |
| TC-06 | [BVA] Reject an appointment 31 days ahead | Member has an active policy and the booking calendar allows navigation beyond 30 days. | 1. Log in. 2. Select the provider. 3. Navigate to 31 days ahead. 4. Attempt to select or book a slot. | Appointment date = today + 31 days. | The appointment cannot be booked because it falls outside the permitted booking period. | High |
| TC-07 | [BVA] Verify the earliest appointment time | Member has an active policy and an in-network provider has an available slot at the start of the booking day. | 1. Log in. 2. Select the provider. 3. View the available slots. 4. Select 08:00 and confirm the booking. | Slot start time = 08:00. | The 08:00 slot is available and can be booked if it is otherwise eligible. | High |
| TC-08 | [BVA] Verify the latest appointment time | Member has an active policy and an in-network provider has an available slot at the end of the permitted daily schedule. | 1. Log in. 2. Select the provider. 3. View the final available slot. 4. Attempt to book it. | Candidate final slot: 16:30–17:00. | A 30-minute appointment ending at 17:00 is bookable if 17:00 is the end of the booking window. Confirm the intended interpretation with the product manager. | High |
| TC-09 | Verify appointment slot duration | Member has an active policy and an in-network provider has available slots. | 1. Log in. 2. Select the provider. 3. Inspect the start and end times of an available slot. | Slot duration = 30 minutes. | Each available appointment slot lasts exactly 30 minutes. | Medium |
| TC-10 | Book a third upcoming appointment | Member has an active policy and already has two upcoming appointments. | 1. Log in. 2. Select an in-network provider. 3. Select an eligible available slot. 4. Confirm the booking. | Existing upcoming appointments = 2. | The third upcoming appointment is booked successfully, and both confirmations are triggered. | High |
| TC-11 | Reject a fourth upcoming appointment | Member has an active policy and already has three upcoming appointments. | 1. Log in. 2. Select an in-network provider. 3. Attempt to book another eligible slot. | Existing upcoming appointments = 3. | The fourth upcoming appointment is not created because the member has reached the limit. | High |
| TC-12 | [BVA] Cancel an appointment exactly two hours before it starts | Member has a confirmed upcoming appointment. | 1. Open the appointment details. 2. Initiate cancellation exactly two hours before the appointment starts. 3. Confirm cancellation. | Appointment starts at 12:00; cancellation at 10:00. | The appointment is cancelled without a cancellation charge, based on the stated two-hour rule. | High |
| TC-13 | [BVA] Cancel an appointment more than two hours before it starts | Member has a confirmed upcoming appointment. | 1. Open the appointment details. 2. Initiate cancellation more than two hours before the appointment. 3. Confirm cancellation. | Appointment starts at 12:00; cancellation at 09:59. | The appointment is cancelled without a cancellation charge. | High |
| TC-14 | [BVA] Cancel an appointment less than two hours before it starts | Member has a confirmed upcoming appointment. | 1. Open the appointment details less than two hours before the start time. 2. Attempt to cancel the appointment. | Appointment starts at 12:00; cancellation at 10:01. | The system applies the cancellation rule for requests made less than two hours before the appointment. Whether cancellation is blocked or charged requires clarification. | High |
| TC-15 | Verify both booking confirmations | Member has an active policy and an in-network provider has an available slot. | 1. Book an eligible appointment. 2. Check the in-app confirmation. 3. Check whether the SMS confirmation is sent. | Eligible booking; valid SMS recipient configured for the test member. | An in-app confirmation is displayed and an SMS confirmation is sent for the booking. | High |

## Questions for the Product Manager

1. **Booking date boundary:** Is the 30-day limit inclusive, and which time zone determines the booking date and the start of a new day?

2. **Daily time boundary:** Does 17:00 represent the latest appointment start time or the end of the appointment window? Can the final 30-minute slot run from 16:30 to 17:00?

3. **Cancellation boundary:** What should happen when a member attempts to cancel less than two hours before the appointment: should cancellation be blocked, or should a charge apply? Is cancellation exactly two hours before always free?

