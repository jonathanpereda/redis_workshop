from kv_store import KeyValueStore
import time

def main():
    store = KeyValueStore()
    store.add("I cant", "Die")
    store.add("Hello", "World",5)
    print(store.get("Hello"))
    print(store.get("I cant"))
    print("Waiting 4 seconds")
    time.sleep(4)
    print(store.get("Hello"))
    print(store.get("I cant"))

if __name__ == "__main__":
    main()