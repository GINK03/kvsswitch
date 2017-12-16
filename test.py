import RARSwitch

'''
rocksdb-test
'''
db = RARSwitch.as_open('rocksdb', 'test.db')
db.put('1', '2')
db.put('3', '4')
print(db.get('1'))
print(list(db.keys()))

'''
leveldb-test
'''
db = RARSwitch.as_open('leveldb', 'test-leveldb.db')
db.put('7', '9')
db.put('9', '11')
print(db.get('7'))
print(list(db.keys()))

'''
aerospike-test
'''
db = RARSwitch.as_open('aerospike', 'test.db')
db.put('3', '4')
db.put('5', '7')
print(db.get('3'))
print('aerospike keys', list(db.keys()) )

'''
redis-test
'''
db = RARSwitch.as_open('redis', 'test')
db.put('5', '6')
db.put('7', '9')
print(db.get('5'))
print('redis get keys',list(db.keys()))
