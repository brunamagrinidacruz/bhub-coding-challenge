from pymongo import MongoClient
import datetime

clients = [
    {
        'company_name': 'i2a Advogados',
        'telephone': '(11) 5102-5400',
        'address': 'Rua Cardeal Arcoverde, 2365 - Pinheiros, São Paulo - SP, 05407-003',
        'declared_billing': 100000000,
        'registration_date': datetime.datetime.now(),
        'bank_accounts': [{
            'bank': '208',
            'agency': '0692',
            'account_number': '67272-8',
        },
        {
            'bank': '260',
            'agency': '5404',
            'account_number': '205556-2',
        },
        {
            'bank': '237',
            'agency': '5979',
            'account_number': '0885265-0',
        }]
    },
    {
        'company_name': 'Latitud',
        'telephone': '(11) 3141-4524',
        'address': 'Rua Cardeal Arcoverde, 2365 - Pinheiros, São Paulo - SP, 05407-003',
        'declared_billing': 20000000,
        'registration_date': datetime.datetime.now(),
        'bank_accounts': [{
            'bank': '033',
            'agency': '2311',
            'account_number': '0241820-7',
        }]
    },
    {
        'company_name': 'Noh',
        'telephone': '(11) 3674-4423',
        'address': 'Rua Cardeal Arcoverde, no 2365, 3o Andar, Conjunto 33 - Pinheiros, São Paulo - SP, CEP 05407-003',
        'declared_billing': 150000,
        'registration_date': datetime.datetime.now(),
        'bank_accounts': [{
            'bank': '422',
            'agency': '1834',
            'account_number': '0673360-3',
        },
        {
            'bank': '336',
            'agency': '4541',
            'account_number': '1124040-7',
        }]
    },
    {
        'company_name': 'Jeeves',
        'telephone': '(11) 2737-7472',
        'address': 'Avenida das Nações Unidas n° 12901, Torre Norte, sala 24-146, Brooklin Paulista, CEP 04.578.910',
        'declared_billing': 180000000,
        'registration_date': datetime.datetime.now(),
        'bank_accounts': [{
            'bank': '290',
            'agency': '0251',
            'account_number': '54035-7',
        }]
    },
    {
        'company_name': 'Dolado',
        'telephone': '(11) 3424-3059',
        'address': 'Rua Cardeal Arcoverde, 2365 - Pinheiros, São Paulo - SP, 05407-003',
        'declared_billing': 300000,
        'registration_date': datetime.datetime.now(),
        'bank_accounts': [{
            'bank': '336',
            'agency': '9336',
            'account_number': '64547-9',
        }]
    },
    {
        'company_name': 'Arado',
        'telephone': '(11) 2742-4591',
        'address': 'Rua Cardeal Arcoverde, 2365 - Pinheiros, São Paulo - SP, 05407-003',
        'declared_billing': 7800000000,
        'registration_date': datetime.datetime.now(),
        'bank_accounts': [{
            'bank': '001',
            'agency': '9336',
            'account_number': '64547-9',
        },
        {
            'bank': '341',
            'agency': '4159',
            'account_number': '134465-X',
        }]
    },
]   
    
class MongoAPI:
    def __init__(self):
        self.mongo_client = MongoClient("mongodb://localhost:27017/")  

        dbnames = self.mongo_client.list_database_names()
        if 'bhub' not in dbnames:
            cursor = self.mongo_client['bhub']
            self.collection = cursor['clients']
            for client in clients:
                self.create(client)
        else:
           cursor = self.mongo_client['bhub']
           self.collection = cursor['clients'] 

    def read(self):
        documents = self.collection.find()

        clients = []
        for document in documents:
            client = {}
            for item in document:
                if item != '_id':
                    client[item] = document[item]
                else:
                    client['_id'] = str(document['_id'])
            clients.append(client)
                    

        output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        return clients

    def create(self, client):
        client['registration_date'] = datetime.datetime.now()
        response = self.collection.insert_one(client)
        return self.collection.find_one({"_id": response.inserted_id})
    
    def delete(self, filter):
        response = self.collection.delete_one(filter)
        return response.deleted_count > 0