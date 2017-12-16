import RARSwitch

'''
rocksdb-test
'''
db = RARSwitch.as_open('rocksdb', 'test.db')
db.put('1', '2')
print(db.get('1'))

'''
leveldb-test
'''
db = RARSwitch.as_open('leveldb', 'test-leveldb.db')
db.put('7', '9')
print(db.get('7'))

'''
aerospike-test
'''
db = RARSwitch.as_open('aerospike', 'test.db')
db.put('3', '4')
print(db.get('3'))

'''
redis-test
'''
db = RARSwitch.as_open('redis', 'test')
db.put('5', '6')
print(db.get('5'))
