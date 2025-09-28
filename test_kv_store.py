from kv_store import KeyValueStore


def main():
    store = KeyValueStore()
    store.add("I cant", "Die")
    store.add("Hello", "World",60)
    print(store.get("Hello"))
    print(store.get("I cant"))


if __name__ == "__main__":
    main()