# Task 3: API testing (Restful Booker, pytest)

## Run
From inside the `03-api/` folder:

```bash
pip install -r requirements.txt
cp .env.example .env
python -m pytest -v
```

Expected result: 9 passed, 3 xfailed (the 3 xfails are known API bugs, see `findings.md`).