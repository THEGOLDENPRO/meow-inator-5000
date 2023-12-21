from fastapi import APIRouter, Request

router = APIRouter(
    tags = ["misc"]
)

@router.get("/nya")
async def status(request: Request):
    return {
        "version": request.app.version
    }