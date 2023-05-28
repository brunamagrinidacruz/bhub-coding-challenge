from app import is_client_id_valid, is_client_complete, is_client_valid
import pytest

def test_valid_client_id():
    assert is_client_id_valid('64734e19e8fd9f53f9e8e572') == True

def test_invalid_client_id():
    assert is_client_id_valid(None) == False
    assert is_client_id_valid('') == False
    assert is_client_id_valid('client_id') == False
    assert is_client_id_valid('64734e19e8fd9f53f9e8e57') == False

@pytest.fixture(scope='function')
def client():
    return {
        'company_name': 'i2a Advogados',
        'telephone': '(11) 5102-5400',
        'address': 'Rua Cardeal Arcoverde, 2365 - Pinheiros, São Paulo - SP, 05407-003',
        'declared_billing': 100000000,
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
    }

def test_complete_client(client):
    is_complete, _ = is_client_complete(client)
    assert is_complete == True

def test_incomplete_client_missing_company_name(client):
    del client['company_name']
    is_complete, error = is_client_complete(client)
    assert is_complete == False
    assert error == "missing company_name"

def test_incomplete_client_missing_telephone(client):
    del client['telephone']
    is_complete, error = is_client_complete(client)
    assert is_complete == False
    assert error == "missing telephone"

def test_incomplete_client_missing_address(client):
    del client['address']
    is_complete, error = is_client_complete(client)
    assert is_complete == False
    assert error == "missing address"

def test_incomplete_client_missing_declared_billing(client):
    del client['declared_billing']
    is_complete, error = is_client_complete(client)
    assert is_complete == False
    assert error == "missing declared_billing"

def test_incomplete_client_missing_bank_accounts(client):
    del client['bank_accounts']
    is_complete, error = is_client_complete(client)
    assert is_complete == False
    assert error == "missing bank_accounts"

def test_incomplete_client_empty_bank_accounts(client):
    client['bank_accounts'] = []
    is_complete, error = is_client_complete(client)
    assert is_complete == False
    assert error == "empty bank_accounts"

def test_incomplete_client_missing_bank(client):
    del client['bank_accounts'][0]['bank']
    is_complete, error = is_client_complete(client)
    assert is_complete == False
    assert error == "missing bank"

def test_incomplete_client_missing_agency(client):
    del client['bank_accounts'][1]['agency']
    is_complete, error = is_client_complete(client)
    assert is_complete == False
    assert error == "missing agency"

def test_incomplete_client_missing_account_number(client):
    del client['bank_accounts'][2]['account_number']
    is_complete, error = is_client_complete(client)
    assert is_complete == False
    assert error == "missing account_number"

def test_valid_client(client):
    is_valid, _ = is_client_valid(client)
    assert is_valid == True

def test_invalid_client_telephone(client):
    client['telephone'] = ''
    is_valid, error = is_client_valid(client)
    assert is_valid == False
    assert error == "telephone not well formated"

    client['telephone'] = '(11 3141-4524'
    is_valid, error = is_client_valid(client)
    assert is_valid == False
    assert error == "telephone not well formated"

    client['telephone'] = '(11) 31414524'
    is_valid, error = is_client_valid(client)
    assert is_valid == False
    assert error == "telephone not well formated"

    client['telephone'] = '(1) 3141-4524'
    is_valid, error = is_client_valid(client)
    assert is_valid == False
    assert error == "telephone not well formated"

def test_invalid_client_declared_billing(client):
    client['declared_billing'] = ''
    is_valid, error = is_client_valid(client)
    assert is_valid == False
    assert error == "declared_billing wrong type"

    client['declared_billing'] = '100000'
    is_valid, error = is_client_valid(client)
    assert is_valid == False
    assert error == "declared_billing wrong type"

def test_invalid_client_bank(client):
    client['bank_accounts'][0]['bank'] = ''
    is_valid, error = is_client_valid(client)
    assert is_valid == False
    assert error == "bank not well formated"

    client['bank_accounts'][0]['bank'] = '12345'
    is_valid, error = is_client_valid(client)
    assert is_valid == False
    assert error == "bank not well formated"

def test_invalid_client_agency(client):
    client['bank_accounts'][0]['agency'] = ''
    is_valid, error = is_client_valid(client)
    assert is_valid == False
    assert error == "agency not well formated"

    client['bank_accounts'][0]['agency'] = 'agency'
    is_valid, error = is_client_valid(client)
    assert is_valid == False
    assert error == "agency not well formated"

    client['bank_accounts'][0]['agency'] = '123456'
    is_valid, error = is_client_valid(client)
    assert is_valid == False
    assert error == "agency not well formated"

def test_invalid_client_account_number(client):
    client['bank_accounts'][0]['account_number'] = ''
    is_valid, error = is_client_valid(client)
    assert is_valid == False
    assert error == "account_number not well formated"

    client['bank_accounts'][0]['account_number'] = 'account_number'
    is_valid, error = is_client_valid(client)
    assert is_valid == False
    assert error == "account_number not well formated"

    client['bank_accounts'][0]['account_number'] = '1234-#'
    is_valid, error = is_client_valid(client)
    assert is_valid == False
    assert error == "account_number not well formated"