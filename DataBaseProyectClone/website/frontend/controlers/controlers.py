from ..models.shopModels import Products

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
                    Products.price[index],
                    Products.image[index],
                    Products.stock[index],
                    Products.state[index]]
        product.append(newProduct)
    return product