import time

class KeyValueStore:

    def __init__(self):
        self.record = {}
        self.ttl = {}

    def add(self, key, value, lifespan=-1):
        self.record[key] = value
        if lifespan>=0:
            self.ttl[key] = time.time() + lifespan

    def get(self, key):
        if key in self.ttl and self.ttl[key] > time.time():
            self.delete(key)
        elif key in self.record:
            return self.record[key]
        return None
    
    def delete(self, key):
        if key in self.record:
            del self.record[key]


    