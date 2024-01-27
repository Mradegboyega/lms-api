from fastapi import FastAPI

from api import users, courses, sections

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

app.include_router(users.router)
app.include_router(sections.router)
app.include_router(courses.router)
