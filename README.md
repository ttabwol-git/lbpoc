# LBPOC: FastAPI Proof of Concept for Landbot
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/67108534cd784c1bb5c7d47af9bf2adf)](https://app.codacy.com/gh/ttabwol-git/lbpoc/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
[![Known Vulnerabilities](https://snyk.io/test/github/ttabwol-git/lbpoc/badge.svg)](https://snyk.io/test/github/ttabwol-git/lbpoc)

## 1. Description
This project serves as a demonstration of FastAPI capabilities, created specifically for Landbot as part of the application process for the Senior Software Engineer role.
- Job details → [here](https://jobs.landbot.io/o/senior-software-engineer-2)
- Backend challenge → [here](https://github.com/hello-umi/backend-challenge)

## 2. Installation
Developed and tested on Python [3.12.3](https://www.python.org/downloads/release/python-3123/)
```bash
git clone https://github.com/ttabwol-git/lbpoc.git
cd lbpoc
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
Don't forget to set up your environment variables in `config/local.env`:
```
AUTH0_DOMAIN='your.domain.auth0.com'
AUTH0_API_AUDIENCE='https://your-audience'
AUTH0_ISSUER='https://your.domain.auth0.com/'
AUTH0_ALGORITHMS='RS256'

SLACK_API_TOKEN='your-slack-api-token'
SLACK_CHANNEL='#your-slack-channel'
SLACK_BOT_NAME='your-slack-bot-name'

EMAIL_TO_ADDR='your@email.address'
EMAIL_TO_NAME='Your Name'
MAILJET_API_KEY='your-mailjet-api-key'
MAILJET_API_SECRET='your-mailjet-api-secret'
```
And set the auth0 bearer token for the tests in `config/pytest.env`:
```
BEARER_TOKEN='your-auth0-bearer-token'
```

## 3. Usage
Run the API locally:
```bash
uvicorn main:app
```
```
INFO:     Started server process [8808]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

Run the unit tests:
```bash
pytest --cov=api
```
```
========================= test session starts ========================
platform darwin -- Python 3.12.3, pytest-8.2.2, pluggy-1.5.0
rootdir: /Users/ttabwol/Projects/lbpoc
plugins: cov-5.0.0, anyio-4.4.0
collected 5 items

tests/test_topics.py .....                                      [100%]

---------- coverage: platform darwin, python 3.12.3-final-0 ----------
Name                           Stmts   Miss  Cover
--------------------------------------------------
api/engine/__init__.py             0      0   100%
api/engine/topics_engine.py       23      4    83%
api/managers/__init__.py           0      0   100%
api/managers/auth.py              30      9    70%
api/managers/config.py            30      0   100%
api/managers/mailjet.py           11      0   100%
api/managers/slack.py             13      2    85%
api/routers/__init__.py            0      0   100%
api/routers/topics_router.py      18      2    89%
--------------------------------------------------
TOTAL                            125     17    86%


========================= 5 passed in 0.59s =========================
```

## 4. API Endpoints
- **POST** `/api/topics/submit` → Submit a topic

Find full API documentation at [Postman](https://documenter.getpostman.com/view/36001241/2sA3QzZTez)
