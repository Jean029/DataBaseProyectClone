
class User():
    id = [1, 2, 3, 4, 5, 6]
    first_name = ['Jean','Ursula','Nebula']
    last_name = ['Rios', 'Lopez', 'Acevedo']
    email = ['jean@upr.edu', 'user@gmail.com', 'nebula@gmail.com']
    password = ['pass1234', 'pass1234', 'pass1234']
    phone_number = ['7879514586', '9392487598', '7874561452']
    status = ['active', 'active', 'active']
    address_1 = ['Sector Barrios', 'Victor Azul', 'Vista Azulin' ]
    address_2 = ['Calle 8 H20', 'Calle 9 A10', 'Calle L11 L13']
    city = ['Hatillo', 'Arecibo', 'Fajardo']
    state = ['Puerto Rico', 'Puerto Rico', 'Puerto Rico']
    zipcode = ['00612','00610', '00651']
    card_name = ['Jean Rios', 'Ursula Lopez', 'Nebula Acevedo']
    card_type = ['Visa', 'Discover', 'Mastercard']
    card_num = ['1234123412341234','4567456745674567', '7896789678967896']
    exp_date = ['05-04-24', '01-01-23', '01-01-25']
    
class Products():
    id = [1, 2, 3, 4, 5, 6]
    name = ['Travel Scope', 'Astromaster', 'Advanced VX', 'Skyscanner 10012', 'Maksutov-Cassegrain Starmac', 'Astroview 9024']
    brand = ['Celestron', 'Celestron', 'Celestron', 'Orion', 'Orion', 'Orion']
    description = [' ', ' ', ' ', ' ', ' ', ' ']
    lens = ['Refractor', 'Reflector', 'Catadioptric', 'Reflector', 'Catadioptric', 'Refractor']
    mount = ['Altazimuth', 'Equatorial', 'Equatorial', 'Altazimuth', 'Altazimuth', 'Equatorial']
    aperture = [70, 130, 235, 100, 90, 90]
    focalDis = [400, 650, 2359, 400, 1250, 910]
    image = ['TravelScope.png', 'AstroMaster.png', 'AdvancedVX.jpg', 'Skyscanner.jpg', 'Starmax.jpg', 'AstroView.jpg']
    stock = [5, 3, 1, 2, 1, 4]
    state = ['Active', 'Active', 'Active', 'Active', 'Active', 'Active']
    price = [86, 300, 3699, 130, 180, 250]

#Usando de ejemplo los modelos previos has un modelo de ordenes, en el modelo asigna la orden a un usuario
#Has al menos 2 o 3 ordenes por usuario, en el modelo tambien pon una parte que guarde el id de los productos
#que contiene la orden, esto lo puedes guardar como una lista.

order1 = {"tracking_num": "71287249",
    "order_date": "01/17/23",
    "arrival_date": "01/20/23",
    "address_line_1": "Vista Azulin Calle 11 L13",
    "address_line_2": "Arecibor Puerto Ricor, 00614",
    "total": 1197.00,
    "amount": 3,
    "payment_method": "Mastercard",
    "status": 'shipped'}

order2 = {"tracking_num": "92391290",
    "order_date": "01/20/23",
    "arrival_date": "01/23/23",
    "address_line_1": "Vista Azulin Calle 11 L13",
    "address_line_2": "Arecibor Puerto Ricor, 00614",
    "total": 629.00,
    "amount": 3,
    "payment_method": "Mastercard",
    "status": 'delivered'}

