from app import app
import json
import pytest

def test_index():
      with app.test_client() as test_client:
            response = test_client.get('/')
            assert response.status_code == 200
            assert b"https://www.linkedin.com/in/brunamagrinidacruz/" in response.data

def test_read_clients():
      with app.test_client() as test_client:
            response = test_client.get('/clients')
            assert response.status_code == 200
            
            clients = json.loads(response.data)
            for client in clients:
                  assert 'company_name' in client
                  assert 'telephone' in client
                  assert 'address' in client
                  assert 'declared_billing' in client
                  assert 'bank_accounts' in client
                  assert len(client['bank_accounts']) > 0
                  for bank_account in client['bank_accounts']:
                        assert 'bank' in bank_account
                        assert 'agency' in bank_account
                        assert 'account_number' in bank_account

def test_read_one_client(client):
      with app.test_client() as test_client:
            response = test_client.post('/clients', data=json.dumps(client), headers={'Content-Type': 'application/json', 'Accept': 'application/json'})
            assert response.status_code == 201
            client_read = json.loads(response.data)
            
            response = test_client.get('/clients/' + client_read['_id'])
            del client_read['_id']
            del client_read['registration_date']
            
            assert client == client_read

def test_read_one_client_invalid_id():
      with app.test_client() as test_client:
            response = test_client.get('/clients/1')
            assert response.status_code == 400

@pytest.fixture(scope='function')
def client():
    return {
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

def test_create_client(client):
      with app.test_client() as test_client:
            response = test_client.post('/clients', data=json.dumps(client), headers={'Content-Type': 'application/json', 'Accept': 'application/json'})
            assert response.status_code == 201
            client_created = json.loads(response.data)
            del client_created['_id']
            del client_created['registration_date']
            assert client_created == client

def test_update_client(client):
      with app.test_client() as test_client:
            response = test_client.post('/clients', data=json.dumps(client), headers={'Content-Type': 'application/json', 'Accept': 'application/json'})
            assert response.status_code == 201
            client_id = json.loads(response.data)['_id']
            
            client['company_name'] = 'BHub - Todo seu financeiro por um preço justo.'
            response = test_client.put('/clients/' + client_id, data=json.dumps(client), headers={'Content-Type': 'application/json', 'Accept': 'application/json'})
            assert response.status_code == 200
            client_updated = json.loads(response.data)
            del client_updated['_id']
            del client_updated['registration_date']

            assert client_updated == client

def test_update_nonexisting_client(client):
      with app.test_client() as test_client:
            response = test_client.put('/clients/64737d2347c8f9d2daade792', data=json.dumps(client), headers={'Content-Type': 'application/json', 'Accept': 'application/json'})
            assert response.status_code == 404

def test_delete_client(client):
      with app.test_client() as test_client:
            response = test_client.post('/clients', data=json.dumps(client), headers={'Content-Type': 'application/json', 'Accept': 'application/json'})
            assert response.status_code == 201
            client_id = json.loads(response.data)['_id']
            
            response = test_client.delete('/clients/' + client_id)
            assert response.status_code == 204

def test_delete_nonexisting_client():
      with app.test_client() as test_client:
            response = test_client.delete('/clients/64737d2347c8f9d2daade792')
            assert response.status_code == 404