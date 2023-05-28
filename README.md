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

## Endpoints

| Operation  | Link | Example |
|------------|------|---------|
| Create     |      |         |
| Read All   | /v1/clients | http://127.0.0.1:5000/v1/clients |
| Read One   |      |         |
| Update     |      |         |
| Delete One |      |         |
| Delete All |      |         |

