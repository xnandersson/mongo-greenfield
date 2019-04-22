from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017')
db = client['sudoers']
sudoroles= db.sudoroles

def insert_one():
    sudorole = {
        'sudo_user': 'nandersson',
        'sudo_host': 'host0001',
        'sudo_command': 'ALL'
    }

    result = sudoroles.insert_one(sudorole)
    print(type(result))
    if result.acknowledged:
        print(type(result.inserted_id))
        print("Sudorole added. SudoRole id is {}".format(result.inserted_id))

def insert_many():
    arr_sudoroles = [
    {
        'sudo_user': 'nandersson1',
        'sudo_host': 'host0001',
        'sudo_command': 'ALL'
    },
    {
        'sudo_user': 'nandersson2',
        'sudo_host': 'host0002',
        'sudo_command': 'ALL'
    },
    {
        'sudo_user': 'nandersson3',
        'sudo_host': 'host0003',
        'sudo_command': 'ALL'
    },
    {
        'sudo_user': 'nandersson4',
        'sudo_host': 'host0004',
        'sudo_command': 'ALL'
    }
    ]   
    result = sudoroles.insert_many(arr_sudoroles)
    if result.acknowledged:
        for id in result.inserted_ids:
            print("{} inserted".format(id))

if __name__ == '__main__':
    insert_one()
    insert_many()
