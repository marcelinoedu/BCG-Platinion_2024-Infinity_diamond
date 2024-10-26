from fastapi import FastAPI
import uvicorn
from adapters.input.router import InputRouter



app = FastAPI()
InputRouter(app)
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)



