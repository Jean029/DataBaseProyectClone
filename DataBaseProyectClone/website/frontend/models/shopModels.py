from flask_login import UserMixin

class Products():
    id = [1, 2, 3, 4, 5, 6]
    name = ['Travel Scope', 
            'Astromaster', 
            'Advanced VX', 
            'Skyscanner 10012', 
            'Maksutov-Cassegrain Starmac', 
            'Astroview 9024']
    brand = ['Celestron', 'Celestron', 'Celestron', 'Orion', 'Orion', 'Orion']
    description = [' ', 
                   ' ', 
                   ' ', 
                   ' ', 
                   ' ', 
                   ' ']
    lens = ['Refractor', 'Reflector', 'Catadioptric', 'Reflector', 'Catadioptric', 'Refractor']
    mount = ['Altazimuth', 'Equatorial', 'Equatorial', 'Altazimuth', 'Altazimuth', 'Equatorial']
    aperture = [70, 130, 235, 100, 90, 90]
    focalDis = [400, 650, 2359, 400, 1250, 910]
    image = ['TravelScope.png', 'AstroMaster.png', 'AdvancedVX.jpg', 'Skyscanner.jpg', 'Starmax.jpg', 'AstroView.jpg']
    stock = [5, 3, 1, 2, 1, 4]
    state = ['Active', 'Active', 'Active', 'Active', 'Active', 'Active']
    price = [86, 300, 3699, 130, 180, 250]
            