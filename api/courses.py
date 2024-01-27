import fastapi

router = fastapi.APIRouter()

@router.get("/courses")
async def read_courses():
    return {"courses": []}

@router.post("/courses")
async def create_course():
    return {"courses": []}

@router.get("/courses/{id}")
async def read_course(id: int):
    return {"courses": []}

@router.patch("/courses/{id}")
async def update_course(id: int):
    return {"courses": []}

@router.delete("/courses/{id}")
async def delete_course(id: int):
    return {"courses": []}
