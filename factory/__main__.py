from .api import FactoryAPI, APIRequest

def main() -> None:
    api = FactoryAPI()
    print("The Factory kernel ready")
    print(api.handle(APIRequest("health", {})).ok)

if __name__ == "__main__":
    main()
