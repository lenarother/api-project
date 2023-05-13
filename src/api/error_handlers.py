from fastapi import Request
from fastapi.responses import JSONResponse
from .application import app


@app.exception_handler(IndexError)
def storage_error_handler(request: Request, exc: IndexError):
    print(f"log msg, {exc}")
    return JSONResponse(
        status_code=404,
        content={"message": f"error occured"}
    )