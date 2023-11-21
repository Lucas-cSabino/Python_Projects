import pymongo as pyM
from pprint import pprint
from datetime import datetime

client = pyM.MongoClient("mongodb+srv://lucascarvalhopa:Aa%407894561@cluster0.btxh1t0.mongodb.net/?retryWrites=true&w=majority")

db = client.bank
collection = db.bank
print(db.bank)

# definição de info para compor o doc
client = {
    "name" : "Lucas Carvalho",
    "cpf" : "01232145689",
    "endereco" : "12345678",
    "conta" : {"tipo" : "conta corrente",
               "agencia" : "belem",
               "num": "1234",
               "saldo": "500"},
    "data": datetime.utcnow()
}

# preparando para submeter as infos
clients = db.clients
post_id = clients.insert_one(client).inserted_id
print(post_id)

# print(db.posts.find_one())
pprint(db.posts.find_one())

#bulk inserts
new_clients = [{
    "name" : "George Braga",
    "cpf" : "98756712324",
    "endereco" : "89067123",
    "conta" : {"tipo" : "poupança",
               "agencia" : "minas",
               "num": "5612",
               "saldo": "2000"},
    "data": datetime.utcnow()
    },
    {
    "name" : "Laura",
    "cpf" : "23145678902",
    "endereco" : "789123234",
    "conta" : {"tipo" : "poupança",
               "agencia" : "pedreira",
               "num": "4512",
               "saldo": "200000"},
    "data": datetime.utcnow()
    }
]
result = clients.insert_many(new_clients)
print(result.inserted_ids)

print("\nRecuperação final")
pprint(db.posts.find_one({'author': "Mike"}))

print("\n documentos presentes na coleção posts")
for post in clients.find():
    pprint(post)