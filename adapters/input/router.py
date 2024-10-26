from email.headerregistry import Address
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from model.location import Location




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