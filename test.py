import RARSwitch

'''
rocksdb-test
'''
db = RARSwitch.as_open('rocksdb', 'test.db')
db.put('1', '2')
print(db.get('1'))

'''
aerospike-test
'''
db = RARSwitch.as_open('aerospike', 'test.db')
db.put('3', '4')
print(db.get('3'))
