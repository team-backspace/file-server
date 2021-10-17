from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from fastapi.responses import FileResponse
from fastapi import File, UploadFile, HTTPException

import os

router = InferringRouter()

@cbv(router)
class Files:
    @router.get("/files/{file_name}")
    async def get_file(self, file_name: str):
        if not os.path.exists(f"files/{file_name}"):
            return HTTPException(status_code=404, detail="File not found")

        return FileResponse(f"files/{file_name}")

    @router.post("/upload")
    async def upload_file(self, file: UploadFile = File(...)):
        # return {"file_name" : file.filename}
        contents = await file.read()
        file_name = os.urandom(30).hex() + os.path.splitext(file.filename)[-1]

        with open(f"./files/{file_name}", "wb") as new_file:
            new_file.write(contents)

        return {"file_name" : file_name}