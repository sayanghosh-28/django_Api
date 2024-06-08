# django_Api
Crypto Scraper API
This Django REST framework API allows users to start scraping cryptocurrency data for specified coins and check the status of the scraping jobs. The API leverages Celery for asynchronous task management and Redis as the message broker and result backend.

**Requirements**
Python 3.8+
Django 3.2+
Django REST framework
Celery 5.2+
Redis
Requests
BeautifulSoup4

1. Start Scraping Endpoint
Endpoint:

**http**
Copy code
**_POST /api/crypto/start_scraping/_
****Request Payload:
**
**json**
Copy code
_{
    "coins": ["DUKO", "NOT", "GORILLA"]
}_
Possible Responses:

Successful Request:

**json**
Copy code
_{
    "job_id": "<UUID>",
    "task_ids": "{\"DUKO\": \"<task_id>\", \"NOT\": \"<task_id>\", \"GORILLA\": \"<task_id>\"}"
}_
Explanation:

job_id: A unique identifier for the scraping job.
task_ids: A JSON string mapping each coin to its respective Celery task ID.
Error Response (No Coins Provided):

**json**
Copy code
_{
    "error": "No coins provided"
}_
HTTP Status Code: 400 Bad Request

![Screenshot 2024-06-08 212715](https://github.com/sayanghosh-28/django_Api/assets/119283018/9f9fbf79-cab6-491c-b3c6-58cffaeb095f)

. Check Scraping Status Endpoint
Endpoint:

**http**
Copy code
**_GET /api/crypto/scraping_status/<job_id>/?task_ids=<encoded_task_ids_json>_
_Possible Responses:

Successful Request (Tasks Completed):

**json**
Copy code
**_{
    "job_id": "<UUID>",
    "tasks": [
        {
            "coin": "DUKO",
            "output": {
                "price": 0.003913,
                "price_change": -5.44,
                "market_cap": 37814377,
                "market_cap_rank": 740,
                "volume": 4583151,
                "volume_rank": 627,
                "volume_change": 12.21,
                "circulating_supply": 9663955990,
                "total_supply": 9999609598,
                "diluted_market_cap": 39127766,
                "contracts": [
                    {
                        "name": "solana",
                        "address": "HLptm5e6rTgh4EKgDpYFrnRHbjpkMyVdEeREEa2G7rf9"
                    }
                ],
                "official_links": [
                    {
                        "name": "website",
                        "link": "https://dukocoin.com"
                    }
                ],
                "socials": [
                    {
                        "name": "twitter",
                        "url": "https://twitter.com/dukocoin"
                    },
                    {
                        "name": "telegram",
                        "url": "https://t.me/+jlScZmFrQ8g2MDg8"
                    }
                ]
            }
        },
        {
            "coin": "NOT",
            "output": "Task not completed yet"
        },
        {
            "coin": "GORILLA",
            "output": "Task not completed yet"
        }
    ]
}_
**Explanation**:

job_id: The unique identifier for the scraping job.
tasks: An array of objects containing each coin and its corresponding scraping result or status.
If the task is completed, the output will contain the scraped data.
If the task is not yet completed, the output will indicate "Task not completed yet".
Error Response (No task_ids Provided):

**json**
Copy code
**_{
    "error": "No task_ids provided"
}_
HTTP Status Code: 400 Bad Request

Error Response (Invalid task_ids Format):

**json**
Copy code
**_{
    "error": "Invalid task_ids format"
}_
HTTP Status Code: 400 Bad Request
**Response got**
![Screenshot 2024-06-08 212736](https://github.com/sayanghosh-28/django_Api/assets/119283018/c2263fa5-de65-403a-9f0e-be924d6bcf7c)

**explanation of Functionality**
**_1. Start Scraping (start_scraping View)_**
Request Handling:
Receives a list of coin acronyms in the request payload.
Validates that the list is not empty.
Creates a unique job ID for tracking the scraping tasks.
Initiates a Celery task for each coin to scrape the data.
Returns a response with the job ID and the mapping of coin names to Celery task IDs.
**_2. Check Scraping Status (scraping_status View)_**
Request Handling:
Receives a job ID and encoded task IDs from the query parameters.
Decodes the task IDs and retrieves the status of each Celery task.
Checks if each task is complete or still pending.
Returns a response with the job ID and the status/result of each task.
By following these detailed responses and explanations, you can better understand the API's functionality and handle different scenarios that might arise during the scraping process.

The tables from the admin panel are the following :
![Screenshot 2024-06-08 215945](https://github.com/sayanghosh-28/django_Api/assets/119283018/ff2f4087-8e47-44b0-831c-f48bd6f2f231)
