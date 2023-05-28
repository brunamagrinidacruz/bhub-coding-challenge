# BHub Coding Challenge

## Description

This project consists in an API with CRUD operations for managing BHub clients.

It was implemented using Python Flask as the back-end framework and MongoDB as the database.

### Specifications

Each client is represented with the following informations:
- Company name;
- Telephone;
- Address;
- Declared billing (R$);
- Registration date;
- Bank account (one or more): bank, agency and account number.

## Endpoints

| Operation with Clients |   Link   |  Method |
|------------|----------------------|---------|
| Create     | /clients             |   POST  ||
| Read All   | /clients             |   GET   | http://127.0.0.1:5000/clients |
| Read One   | /clients/<client_id> |   GET   | http://127.0.0.1:5000/clients/647352c00a8355f49c039cb3  | 
| Update     | /clients/<client_id> |   PUT   | http://127.0.0.1:5000/clients/647352c00a8355f49c039cb3 + Body | 
| Delete     | /clients/<client_id> |  DELETE | http://127.0.0.1:5000/clients/647352c00a8355f49c039cb3 | 

### Create 

**Request**  
Path: /clients  
Method: POST  
Parameters: No  
Body: Client. Example:
```
{
    "company_name": "BHub",
    "telephone": "(11) 98876-7612",
    "address": "Rua Cardeal Arcoverde, 2365 - Andares 2 e 3 - Pinheiros, São Paulo - SP, 05407-003",
    "declared_billing": 180000000,
    "bank_accounts": [
        {
            "bank": "290",
            "agency": "0251",
            "account_number": "54035-7"
        }
    ]
}
```

**Response**  
Code: 200
```
{
    "_id": "64738c35bb7a45936e42a257",
    "address": "Rua Cardeal Arcoverde, 2365 - Andares 2 e 3 - Pinheiros, São Paulo - SP, 05407-003",
    "bank_accounts": [
        {
            "account_number": "54035-7",
            "agency": "0251",
            "bank": "290"
        }
    ],
    "company_name": "BHub",
    "declared_billing": 180000000,
    "registration_date": "Sun, 28 May 2023 17:15:33 GMT",
    "telephone": "(11) 98876-7612"
}
```

### Read All

**Request**  
Path: /clients  
Method: GET  
Parameters: No  
Body: No

**Response**  
Code: 200
```
[
    {
        "_id": "647388aa5969a00d3771c0e7",
        "address": "Rua Cardeal Arcoverde, 2365 - Pinheiros, São Paulo - SP, 05407-003",
        "bank_accounts": [
            {
                "account_number": "67272-8",
                "agency": "0692",
                "bank": "208"
            },
            {
                "account_number": "205556-2",
                "agency": "5404",
                "bank": "260"
            },
            {
                "account_number": "0885265-0",
                "agency": "5979",
                "bank": "237"
            }
        ],
        "company_name": "i2a Advogados",
        "declared_billing": 100000000,
        "registration_date": "Sun, 28 May 2023 17:00:26 GMT",
        "telephone": "(11) 5102-5400"
    },
...]
```

### Read One

**Request**  
Path: /clients  
Method: GET  
Parameters: client_id. Example: ```64738c35bb7a45936e42a257```  
Body: No

**Response**  
Code: 200
```
{
    "_id": "64738c35bb7a45936e42a257",
    "address": "Rua Cardeal Arcoverde, 2365 - Andares 2 e 3 - Pinheiros, São Paulo - SP, 05407-003",
    "bank_accounts": [
        {
            "account_number": "54035-7",
            "agency": "0251",
            "bank": "290"
        }
    ],
    "company_name": "BHub",
    "declared_billing": 180000000,
    "registration_date": "Sun, 28 May 2023 17:15:33 GMT",
    "telephone": "(11) 98876-7612"
}
```

### Update

**Request**  
Path: /clients  
Method: PUT  
Parameters: client_id. Example: ```64738c35bb7a45936e42a257```  
Body: Updated fields. Example:
```
{
    "company_name": "BHub - Todo seu financeiro por um preço justo.",
}
```

**Response**  
Code: 200
```
{
    "_id": "64738c35bb7a45936e42a257",
    "address": "Rua Cardeal Arcoverde, 2365 - Andares 2 e 3 - Pinheiros, São Paulo - SP, 05407-003",
    "bank_accounts": [
        {
            "account_number": "54035-7",
            "agency": "0251",
            "bank": "290"
        }
    ],
    "company_name": "BHub - Todo seu financeiro por um preço justo.",
    "declared_billing": 180000000,
    "registration_date": "Sun, 28 May 2023 17:15:33 GMT",
    "telephone": "(11) 98876-7612"
}
```

### Delete

**Request**  
Path: /clients  
Method: DELETE  
Parameters: client_id. Example: ```64738c35bb7a45936e42a257```  
Body: No

**Response**  
Code: 204

## Development

### Configuration

The configuration below only need to be performed once, before running the application for the first time.

Create the [Python Virtual Environments](https://realpython.com/python-virtual-environments-a-primer/) to mantain the API:
```
python3 -m venv venv
```
Then, create a MongoDB using Docker to accomodate the database:
```
docker create --name mongodb -p 27017:27017 mongo
```

### Running

With all the enviorment configured, the Python Virtual Envirorment can be activated with the command:
```
source venv/bin/activate
```
And to execute the API, the libraries must be installed:
```
pip3 install -r requirements.txt
```
The MongoDB database can be started with the command:
```
docker start mongodb
```
Finally, the API can be runned with the command:
```
flask run
```

## Test

Unit tests (for client validation) and e2e tests (for routes) are implemented using PyTest. To run the tests, execute the command:
```
python3 -m pytest
```

## Deployment on Docker

The application can be run directly with Docker, that it will be responsible for both running Python Flask and MongoDB:
```
docker-compose up
```

## References

[Best Practices for Designing a Pragmatic RESTful API](https://www.vinaysahni.com/best-practices-for-a-pragmatic-restful-api#useful-post-responses)

[Handling Application Errors](https://flask.palletsprojects.com/en/2.3.x/errorhandling/)

[How to create Restful CRUD API with Python Flask, MongoDB, and Docker](https://ishmeet1995.medium.com/how-to-create-restful-crud-api-with-python-flask-mongodb-and-docker-8f6ccb73c5bc)

[Testing Flask Applications with Pytest](https://testdriven.io/blog/flask-pytest/)