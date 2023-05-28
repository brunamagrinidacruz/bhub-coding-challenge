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

| Operation with Clients |   Link   |  Method | Request | Response |
|------------|----------------------|---------|---------|--------------|
| Create     | /clients             |   POST  | http://127.0.0.1:5000/clients + Body | 201 + Client Created  |
| Read All   | /clients             |   GET   | http://127.0.0.1:5000/clients | 200 + List of Clients |
| Read One   | /clients/<client_id> |   GET   | http://127.0.0.1:5000/clients/647352c00a8355f49c039cb3  | 404 If Client Not Found or 200 + Client Read | |
| Update     | /clients/<client_id> |   PUT   | http://127.0.0.1:5000/clients/647352c00a8355f49c039cb3 + Body | 404 If Client Not Found or 200 + Client Updated |
| Delete     | /clients/<client_id> |  DELETE | http://127.0.0.1:5000/clients/647352c00a8355f49c039cb3 | 404 If Client Not Found or 201 |

- Create Body:

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
- Update Body:
```
{
    "company_name": "BHub",
    "telephone": "(11) 3888-2187",
    "address": "Rua Brigadeiro Faria Lima, 500 - Itaim Bibi, São Paulo - SP, 09720-010",
    "declared_billing": 1000000000,
    "bank_accounts": [
        {
            "bank": "001",
            "agency": "6484",
            "account_number": "98236-X"
        }
    ]
}
```

## Development

### Configuration

The configuration below only need to be performed once, before running the application for the first time.

Create the [Python Virtual Environments](https://realpython.com/python-virtual-environments-a-primer/) to mantain the API:
```
python3 -m venv venv
```
Then, create a MongoDB using Docker to accomodate the database:
```
docker create --name BHubMongoDB -p 27017:27017 mongo
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
docker start BHubMongoDB
```
Finally, the API can be runned with the command:
```
flask run
```

### Additional Commands

To connect mongo with the BHubMongoDB instance and visualize the data:
```
mongo
> use bhub
> db.clients.find()
```

To delete the BHubMongoDB container:
```
docker rm -f BHubMongoDB
```

## References

[Best Practices for Designing a Pragmatic RESTful API](https://www.vinaysahni.com/best-practices-for-a-pragmatic-restful-api#useful-post-responses)

[Handling Application Errors](https://flask.palletsprojects.com/en/2.3.x/errorhandling/)

[How to create Restful CRUD API with Python Flask, MongoDB, and Docker](https://ishmeet1995.medium.com/how-to-create-restful-crud-api-with-python-flask-mongodb-and-docker-8f6ccb73c5bc)