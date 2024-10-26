from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware


class Location:
    def __init__(self, id, latitude, longitude, timestamp, local):
        self.id = id
        self.latitude = latitude
        self.longitude = longitude
        self.timestamp = timestamp
        self.local = local

class Address:
    def __init__(self, id ):
        self.id = id
        self.cep
        self.type
        self.name
        self.country
        self.state
        self.city
        self.number
    
class InputRouter:
    
    def __init__(self, app: FastAPI):
        self.app = app
        self.setup_cors()
        self.setup_routes()


    def setup_cors(self):
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
          
    def setup_routes(self):
        self.app.add_api_route("/share_location", self.share_location, methods=["POST"])
        self.app.add_api_route("/address", self.share_location, methods=["POST"])

    def share_location(self, location: Location):
        pass
    
    def address(self, address: Address):
        pass