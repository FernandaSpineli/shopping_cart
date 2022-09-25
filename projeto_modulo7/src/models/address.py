from src.schemas.address import Address, AddressSchema
from src.models.user import get_user_by_email


async def create_address(user_email, users_collection, address_collection, newAddress: Address, limit):
  try:
    user = await get_user_by_email(users_collection, user_email)
    if user == None:
      return 'Usuário não cadastrado!'

    address_cursor = address_collection.find({'user._id': user['_id']})
    addresses = await address_cursor.to_list(limit)

    if addresses:
      result = await update_address(address_collection, addresses[0], newAddress)
      if result.modified_count > 0:
        return newAddress
      else:
        return 'Endereço já existe!'
    else:
      result = await address_collection.insert_one({
        'user': user,
        'address': [newAddress]
      })

      if result.inserted_id:
        newAddress = await get_address(address_collection, result.inserted_id)
        return newAddress
    
  except Exception as e:
    print(f'create_address.error: {e}')


async def get_address(address_collection, address_id):
  try:
    address = await address_collection.find_one({'_id': address_id})
    if address:
      return address
  except Exception as e:
    print(f'get_address.error: {e}')


async def update_address(address_collection, address, newAddress):
  try:
    result = await address_collection.update_one(
      { "_id": address["_id"] },
      {
        "$addToSet": {
          "address": newAddress
        }
      }
    )
    return result
  except Exception as e:
    print(f'update_address.error')

async def delete_address(address_collection, address_id):
  try:
        address = await address_collection.delete_one(
            {'_id': address_id}
        )
        if address.deleted_count:
            return {'status': 'Address deleted'}
  except Exception as e:
        print(f'delete_address.error: {e}')

  