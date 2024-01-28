from fastapi import FastAPI
from api import users, courses, sections
from db.db_setup import engine, Base, get_db
from db.models import user, course

# Create database tables for the User and Course models
user.Base.metadata.create_all(bind=engine)
course.Base.metadata.create_all(bind=engine)

# Create an instance of the FastAPI class
app = FastAPI(
    title="fastapi lms portal",
    description="learning management portal api for imaginary school",
    version="1.0.0",
    contact={
        "name": "School is for learning",
        "url": "http://adegboyega.com.ng/",
        "email": "contact@adegboyega.com.ng",
    },
    license_info={
        "name": "My School",
    },
)

# Include routers for different components of the API
app.include_router(users.router)
app.include_router(sections.router)
app.include_router(courses.router)
