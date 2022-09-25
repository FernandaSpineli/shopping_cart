from src.models.product import(
    create_product,
    get_product_by_code,
    update_product,
    delete_product
)

from src.server.database import connect_db, db, disconnect_db


async def products_crud():
    option = input("Entre com a opção de CRUD: ")
    
    await connect_db()
    product_collection = db.product_collection

    product =  {
        "name": "Sorvete",
        "description": "Doce gelado",
        "price": 9.99,
        "image": "sorvete de casquinha",
        "code": 4355
    }

    if option == '1':
        product = await create_product(
            product_collection,
            product
        )
        print(product)
        
    elif option == '2':
        product = await get_product_by_code(
            product_collection,
            product["code"]
        )
        print(product)
        
    elif option == '3':
        product = await get_product_by_code(
            product_collection,
            product["code"]
        )
        product_data = {
            "price": 12.54
        }
        is_updated, numbers_updated = await update_product(
            product_collection,
            product["_id"],
            product_data
        )
        if is_updated:
            print(f"Atualização realizada com sucesso, número de documentos alterados {numbers_updated}")
        else:
            print("Atualização falhou!")
            
    elif option == '4':
        user = await get_product_by_code(
            product_collection,
            product["code"]
        )
        result = await delete_product(
            product_collection,
            product["_id"]
        )
        print(result)
        
        
    await disconnect_db()
