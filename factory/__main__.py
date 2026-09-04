from .api import FactoryAPI, APIRequest

def main() -> None:
    api = FactoryAPI()
    api.register("health", lambda _: {"status": "ok"})
    print("The Factory kernel ready")
    print(api.handle(APIRequest("health", {})).payload)

if __name__ == "__main__":
    main()
