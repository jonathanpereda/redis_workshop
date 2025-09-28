from kv_store import KeyValueStore
import time

def main():
    store = KeyValueStore()
    print("Creating with 5s")
    store.add("Hello", "World",5)
    print(store.get("Hello"))

    print("Waiting 4 seconds")
    time.sleep(4)

    print(store.get("Hello"))

    print("Adding 3s")
    store.add_time("Hello", 3)

    print("Waiting 1 seconds")
    time.sleep(1)


    print(store.get("Hello"))
    


if __name__ == "__main__":
    main()