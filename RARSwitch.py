
import rocksdb
class RocksDB(object):
  def __init__(self, name):
    db = rocksdb.DB(name, rocksdb.Options(create_if_missing=True))
    self.db = db
  def put(self, key:str, value:str):
    self.db.put(bytes(key,'utf8'), bytes(value, 'utf8')) 
  def get(self, key:str):
    return self.db.get(bytes(key,'utf8')).decode()
  def keys(self):
    it = self.db.iterkeys() 
    it.seek_to_first()
    for key in it:
      yield key.decode()
    
import plyvel
class LevelDB(object):
  def __init__(self, name):
    db = plyvel.DB(name, create_if_missing=True)  
    self.db = db 
  def put(self, key:str, value:str):
    self.db.put(bytes(key,'utf8'), bytes(value, 'utf8')) 
  def get(self, key:str):
    return self.db.get(bytes(key,'utf8')).decode()
  def keys(self):
    with self.db.iterator() as it:
      for key, value in it:
        yield key.decode()

import aerospike
class Aerospike(object):
  def __init__(self, name):
    config = { 'hosts': [ ('127.0.0.1', 3000) ] }
    client = aerospike.client(config).connect()
    self.name = name
    self.client = client
  def put(self, key:str, value:str):
    key = ('hdd', self.name, key)
    self.client.put(key, {'value':value})
  def get(self, key:str):
    key = ('hdd', self.name, key)
    (key, metadata, record) = self.client.get(key)
    return record.get('value')
  def keys(self):
    scan = self.client.scan('hdd', self.name)
    records = []
    def _result(arr):
      key, metadata, record = arr
      records.append(record.get('value'))
    scan.foreach(_result)
    for record in records:
      yield record

import redis
class Redis(object):
  def __init__(self, name):
    r = redis.StrictRedis(host='localhost', port=6379, db=0) 
    self.r = r
  def put(self, key:str, value:str):
    self.r.set(key, value)
  def get(self, key:str):
    return self.r.get(key).decode()
  def keys(self):
    for key in self.r.scan_iter('*'):
      yield key.decode()

def as_open(type_name:str, file_name:str):
  if type_name == 'rocksdb':
    return RocksDB(file_name)
  elif type_name == 'leveldb':
    return LevelDB(file_name)
  elif type_name == 'aerospike':
    return Aerospike(file_name)
  elif type_name == 'redis':
    return Redis(file_name)
    
