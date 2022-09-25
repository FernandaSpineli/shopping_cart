from src.models.order import (
    create_order,
    delete_order,
    get_order
)
from src.models.user import UserSchema
from src.server.database import connect_db, db, disconnect_db


async def orders_crud():
    option = input("Entre com a opção de CRUD: ")
    
    await connect_db()
    order_collection = db.order_collection
    users_collection = db.users_collection

    user = {
        "email" : "lu_domagalu@gmail.com"
    }
    order = {}

    if option == '1':
        order = await create_order(
            user['email'],
            users_collection,
            order_collection)
        print(order)
        
    elif option == '2':
        order = await get_order(order_collection, order['_id'])
        print(order)
    
    elif option == '3':
        order = await delete_order(order['_id'], order_collection)
        print(order)
        
    await disconnect_db()