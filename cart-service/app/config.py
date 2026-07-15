import os


class Config:

    MONGO_URI = os.getenv(
        "MONGO_URI",
        "mongodb://admin:password123@mongodb:27017/?authSource=admin"
    )


    DATABASE_NAME = os.getenv(
        "DATABASE_NAME",
        "cloudcart"
    )