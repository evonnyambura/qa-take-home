# k6 load test results: GET /booking (Restful Booker)

Script: `load-test.js` (ramp up to 10 virtual users over 30 s, hold 1 min, ramp down over 10 s).
Run date: 2026-10-13.

## k6 summary output

```
     ✓ status is 200

     checks.........................: 100.00% 487 out of 487
     data_received..................: 23 MB   224 kB/s
     data_sent......................: 120 kB  1.2 kB/s
     http_req_blocked...............: avg=9.7ms    min=4.81µs   med=8.03µs   max=555.57ms p(90)=9.84µs   p(95)=10.82µs 
     http_req_connecting............: avg=4.8ms    min=0s       med=0s       max=321.84ms p(90)=0s       p(95)=0s      
   ✓ http_req_duration..............: avg=663.05ms min=445.12ms med=672.5ms  max=804.77ms p(90)=691.85ms p(95)=700.85ms
       { expected_response:true }...: avg=663.05ms min=445.12ms med=672.5ms  max=804.77ms p(90)=691.85ms p(95)=700.85ms
   ✓ http_req_failed................: 0.00%   0 out of 487
     http_req_receiving.............: avg=435.34ms min=222.25ms med=446.19ms max=541.37ms p(90)=458.25ms p(95)=466.55ms
     http_req_sending...............: avg=135.76µs min=54.26µs  med=130.88µs max=466.41µs p(90)=183.18µs p(95)=205.49µs
     http_req_tls_handshaking.......: avg=4.66ms   min=0s       med=0s       max=236.06ms p(90)=0s       p(95)=0s      
     http_req_waiting...............: avg=227.57ms min=221.54ms med=225.21ms max=266.24ms p(90)=236.2ms  p(95)=240.21ms
     http_reqs......................: 487     4.810067/s
     iteration_duration.............: avg=1.67s    min=1.44s    med=1.67s    max=2.22s    p(90)=1.69s    p(95)=1.7s    
     iterations.....................: 487     4.810067/s
     vus............................: 1       min=1          max=10
     vus_max........................: 10      min=10         max=10

running (1m41.2s), 00/10 VUs, 487 complete and 0 interrupted iterations
```


## What it shows

| Check | Result | Limit | Outcome |
|---|---|---|---|
| p95 response time | 700.85 ms | under 1,000 ms | Passed |
| Failed requests | 0 of 487 (0.00%) | under 1% | Passed |
| Responses with status 200 | 487 of 487 | all | Passed |
| Peak virtual users | 10 | 10 or fewer | Within limit |

- **Both thresholds passed:** the p95 response time was 700.85 ms (limit 1,000 ms) and no request failed.
- **Every response was status 200,** across 487 requests during the full ramp-up, hold and ramp-down.
- **Typical speed:** the average response took 663 ms, and the slowest took 805 ms.
- **What surprised me:** the server's own time was low and steady (about 228 ms), but receiving the response took about 435 ms, roughly two thirds of the total, because `GET /booking` returns a large list (about 47 kB per response).
- **Notes:** the ramp-down lasted 10 seconds, and results on a shared public site can vary with other people's traffic.