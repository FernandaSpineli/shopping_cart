import asyncio
#from src.controllers.orders import orders_crud

from src.controllers.users import users_crud
from src.controllers.addresses import addresses_crud
from src.controllers.products import products_crud
from src.controllers.orders import orders_crud


loop = asyncio.get_event_loop()
#loop.run_until_complete(users_crud())
#loop.run_until_complete(products_crud())
#loop.run_until_complete(addresses_crud())
loop.run_until_complete(orders_crud())

