
import rocksdb

class RocksDB(object):
  def __init__(self, name):
    db = rocksdb.DB(name, rocksdb.Options(create_if_missing=True))
    self.db = db
  def put(self, key:str, value:str):
    self.db.put(bytes(key,'utf8'), bytes(value, 'utf8')) 
  def get(self, key:str):
    return self.db.get(bytes(key,'utf8')).decode('utf8')
    
import aerospike
class Aerospike(object):
  def __init__(self, name):
    config = { 'hosts': [ ('127.0.0.1', 3000) ] }
    client = aerospike.client(config).connect()
    self.name = name
    self.client = client
  def put(self, key:str, value:str):
    key = ('rar-aerospike', self.name, key)
    self.client.put(key, { 'data': value })
  def get(self, key:str):
    key = ('rar-aerospike', self.name, key)
    (key, metadata, record) = client.get(key)
    return record
    
def as_open(type_name:str, file_name:str):
  if type_name == 'rocksdb':
    return RocksDB(file_name)
  elif type_name == 'aerospike':
    return Aerospike(file_name)
    
