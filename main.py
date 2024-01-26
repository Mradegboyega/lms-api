from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

users = []

# Define a route for retrieving the list of users ("/users")
@app.get("/users")
async def get_users():
    # Return a JSON response
    return {"users": users}

# Define a route for creating a new user ("/users")
@app.post("/users")
async def create_user(user: str):
    users.append(user)
    # Return a JSON response
    return {"message": f"Congratulations, {user}! Your account is successfully created."}
