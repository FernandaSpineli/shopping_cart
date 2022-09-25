from src.models.address import (
  create_address,
  delete_address,
  get_address,
  update_address
)
from src.server.database import connect_db, db, disconnect_db

async def addresses_crud():
  option = input('Entre com a opção de CRUD: ')

  await connect_db()
  address_collection = db.address_collection
  users_collection = db.users_collection

  user =  {
    "email": "lu_domagalu@gmail.com"
  }

  address = {
    "street": "rua Cinza",
    "cep": "14.000-000",
    "district": "Jardim das Cores",
    "city": "Franca",
    "state": "SP",
    "is_delivery": False
  }

  addressLimit = 20

  if option == '1':
    address = await create_address(
      user['email'],
      users_collection,
      address_collection,
      address, 
      addressLimit
      )
    print(address)

  elif option == '2':
    address = await get_address(address_collection, address['_id'])
    print(address)
    
  elif option == '3':
    new_address = {
        "street": "rua Cinza",
        "cep": "14.000-000",
        "district": "Jardim das Cores",
        "city": "Franca",
        "state": "SP",
        "is_delivery": True
    }
    address = await update_address(address_collection,address['_id'],new_address)
    return(address)
  
  elif option == '4':
    address = await delete_address(address_collection, address('_id'))
    return(address)