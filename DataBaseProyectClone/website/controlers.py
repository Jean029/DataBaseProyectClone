from .models import Products

def ProductsList():
    product = []
    for id in Products.id:
        index = Products.id.index(id)
        newProduct = [id, 
                    Products.name[index],
                    Products.brand[index],
                    Products.lens[index],
                    Products.mount[index],
                    Products.aperture[index],
                    Products.focalDis[index],
                    Products.price[index]]
        product.append(newProduct)
    return product