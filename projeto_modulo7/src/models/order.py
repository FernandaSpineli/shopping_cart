from src.schemas.order import OrderSchema
from src.models.user import get_user_by_email


async def create_order(user_email, users_collection, order_collection):
    try:
        user = await get_user_by_email(users_collection, user_email)
        if user == None:
            return 'Usuário não cadastrado!'
        
        order = await order_collection.insert_one(
            {
                "user" : user,
                "address" : {
                    "street": "rua Cinza",
                    "cep": "14.000-000",
                    "district": "Jardim das Cores",
                    "city": "Franca",
                    "state": "SP",
                    "is_delivery": False
                },
                "products": [],
                "price": 0,
                "paid": False
            }
        )
        
        if order.inserted_id:
            order = await get_order(order_collection, order.inserted_id)
            return order

    except Exception as e:
        print(f'create_order.error: {e}')
    
async def get_order(order_collection, order_id):
    try:
        data = await order_collection.find_one({'_id': order_id})
        if data:
            return data
    except Exception as e:
        print(f'get_order.error: {e}')
    
async def delete_order(order_id, order_collection):
    try:
        order = await order_collection.delete_one(
            {'_id': order_id}
        )
        if order.deleted_count:
            return {'status': 'Order deleted'}
    except Exception as e:
        print(f'delete_order.error: {e}')
