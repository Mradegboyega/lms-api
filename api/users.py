import fastapi
from fastapi import HTTPException, Path
from pydantic import BaseModel
from typing import Union, Optional, List

router = fastapi.APIRouter()

# In-memory storage for users (replace this with a database in a real-world scenario)
users = []

# Pydantic model for user data validation
class User(BaseModel):
    name: str
    is_active: bool
    bio: Optional[str]

# Define a route for creating a new user ("/users")
@router.post("/users")
async def create_user(user: User):
    try:
        # Append the new user to the in-memory storage
        users.append(user)
        # Return a JSON response
        return {"message": f"Congratulations, {user.name}! Your account is successfully created."}
    except Exception as e:
        # Handle other potential errors
        raise HTTPException(status_code=500, detail=str(e))

# Define a route for retrieving the list of users ("/users")
@router.get("/users")
async def get_users():
    try:
        # Return a JSON response
        return {"users": users}
    except Exception as e:
        # Handle other potential errors
        raise HTTPException(status_code=500, detail=str(e))

# Define a route to retrieve a user by index from the list of users ("/users/{id}")
@router.get("/users/{id}")
async def get_user(id: int = Path(..., description="The ID of user you intend to retrieve")):
    try:
        # Check if the index is within a valid range
        if 0 <= id < len(users):
            user = users[id]
            return {"user": user}
        else:
            # Return a 404 Not Found response for out-of-range index
            raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        # Handle other potential errors
        raise HTTPException(status_code=500, detail=str(e))