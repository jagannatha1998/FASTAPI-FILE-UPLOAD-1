from fastapi import FastAPI
import uvicorn
from fastapi import APIRouter
from app.file_upload.api import profile_upload_controller

def init_app():
    app=FastAPI(title="File Upload")

    profile_router = APIRouter(prefix=f"/app/v1/profile", tags=["Profile"])
    profile_router.add_api_route(path="/", methods=["POST"],
                               endpoint=profile_upload_controller.upload_file,
                               response_model=str)
    app.include_router(router=profile_router)
    return app

app=init_app()

def start():
    uvicorn.run("app.main:app", host="0.0.0.0",port=8080,reload=True)