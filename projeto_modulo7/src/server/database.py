from os import environ

from motor.motor_asyncio import AsyncIOMotorClient


class DataBase:
    client: AsyncIOMotorClient = None
    database_uri = "mongodb+srv://fernandaSpineli:paraface1400@cluster0.zyt1nd8.mongodb.net/?retryWrites=true&w=majority"
    users_collection = None
    address_collection = None
    product_collection = None
    order_collection = None

db = DataBase()

async def connect_db():
    # conexao mongo, com no máximo 10 conexões async
    db.client = AsyncIOMotorClient(
        db.database_uri,
        maxPoolSize=10,
        minPoolSize=10,
        tls=True,
        tlsAllowInvalidCertificates=True
    )
    db.users_collection = db.client.shopping_cart.users
    db.address_collection = db.client.shopping_cart.address
    db.product_collection = db.client.shopping_cart.products
    db.order_collection = db.client.shopping_cart.orders

async def disconnect_db():
    db.client.close()
