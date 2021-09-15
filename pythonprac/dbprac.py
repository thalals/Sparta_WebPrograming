from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# insert
doc = {'name' : 'hm', 'age' : 25}
db.users.insert_one(doc)

#find (모든 데이터)
same_ages = list(db.users.find({'age':21},{'_id':False}))

#find_one (한 개의 데이터)
user = db.users.find_one({'name':'bobby'})

#update - bobby 의 나이를 변경  ($set)
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

#update_many    해당되는 모든 데이터의 값을 변경
db.users.update_many({'name':'bobby'},{'$set':{'age':19}})

#delete
db.users.delete_one({'name':'bobby'})