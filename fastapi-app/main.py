from fastapi import FastAPI,HTTPException,Request
from fastapi.responses import JSONResponse
# from starlette.responses import JSONResponse

app = FastAPI()

class UvicornExcpetion(Exception):
    def __init__(self,name):
        self.name = name

@app.exception_handler(UvicornExcpetion)
def unicorn_exception_handler(request: Request, exc:UvicornExcpetion):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
    )

@app.get("/{id}")
def health(id:int):
    if id<2:
        raise UvicornExcpetion("YOLO")
    if id<5:
        raise HTTPException(status_code=404,detail="Neehhh chill")
    return {"status": "ok"}