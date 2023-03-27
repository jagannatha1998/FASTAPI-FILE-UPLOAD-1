from fastapi import UploadFile, File
from app.file_upload.service.GCStorage import GCStorage
from app.file_upload.schemas.profileschemas import ProfileResponseSchema

async def upload_file(file:UploadFile=File(...) ):
    file_path=GCStorage().upload_file(file)
    return "File Upload SucessFully"
    # return ResponseSchema(data=ProfileResponseSchema(URL=file_path))