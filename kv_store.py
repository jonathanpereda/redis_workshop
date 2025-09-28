import time

class KeyValueStore:

    def __init__(self):
        self.record = {}
        self.ttl = {}

    def add(self, key, value, lifespan=-1):
        self.record[key] = value
        if lifespan>=0:
            self.ttl[key] = time.time() + lifespan
        elif key in self.ttl:
            del self.ttl[key]


    def get(self, key):
        if key in self.ttl and self.ttl[key] < time.time():
            self.delete(key)
        elif key in self.record:
            return self.record[key]
        return None
    
    def delete(self, key):
        if key in self.record:
            del self.record[key]
        if key in self.ttl:
            del self.ttl[key]


    def get_expiration(self,key):
        _key = self.get(key)
        if _key and key in self.ttl:
            return self.ttl[key]
        return None

    def refresh_time(self,key,lifespan=10):
        _key = self.get(key)
        if _key and key in self.ttl:
            self.ttl[key] = time.time() + lifespan
            return True
        return False

    def add_time(self,key,increase=10):
        _key = self.get(key)
        if _key and key in self.ttl:
            self.ttl[key] += increase
            return True
        return False

    def decrease_time(self,key,decrease=10):
        _key = self.get(key)
        if _key and key in self.ttl:
            self.ttl[key] -= decrease
            return True
        return False





    