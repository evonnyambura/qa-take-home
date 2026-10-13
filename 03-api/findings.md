# Findings: Restful Booker API

Reproduce any finding with `python -m pytest --runxfail -v` (the xfail markers are switched off, so the real response is shown).

| ID | Endpoint | Request | Actual | Expected | Severity | Test |
|----|----------|---------|--------|----------|----------|------|
| F-01 | POST /booking | Body `{"firstname":"Jane"}` (required fields missing) | 500 with body `Internal Server Error` | 400 Bad Request with a validation message | High: a server error on bad client input, with no message telling the client what is wrong | test_07 |
| F-02 | POST /booking | `totalprice` sent as text `"abc"` | 200, booking created with `totalprice` stored as `null` (the invalid value is silently dropped) | 400 Bad Request | High: bad data is accepted and silently corrupted, so a booking is saved without its price | test_08 |
| F-03 | PUT /booking/999999999 | Valid token, booking does not exist | 405 with body `Method Not Allowed` | 404 Not Found | Medium: a misleading error, because PUT is allowed on this endpoint and the real problem is the missing booking | test_10 |
| F-04 | DELETE /booking/{id} | Valid token, existing booking | 201 with body `Created` | 200 or 204 (201 is documented, but "Created" for a deletion is poor design) | Low: confusing, but documented | test_06 |

## Checked and behaves correctly
- GET on a booking that does not exist returns 404 `Not Found` (test_09).
- PUT with no token returns 403 `Forbidden`, and the booking is unchanged (test_11).
- DELETE with a wrong token returns 403 `Forbidden`, and the booking still exists (test_12).

## Notes
- Tests 07, 08 and 10 assert the correct behaviour and are marked `xfail`. In a normal run they show as 3 xfailed, which confirms the API does not behave as expected there.
- Error responses are plain text (`Forbidden`, `Not Found`), not JSON.
- One early run measured 2.406 s for `POST /auth` on a cold connection (shared free server). It did not recur once a warm-up request was added.
- Because of F-02, `test_08` creates a real booking on the shared site each run (for example booking 727), and nothing deletes it until the API is fixed.