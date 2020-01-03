# Register Blueprints/Views.
from application.extensions import jinja

# import all component here
# from .location.model import Country, City
# from application.components.port.model import *
from application.components.exceptions.model import *
# from .test.model import Test
from application.components.booking.model import *
from application.components.item.model import *
from application.components.contact.model import *
from application.components.user.model import *


def init_components(app):
    # import application.components.location.view
    # import application.components.port.view
    import application.components.exceptions.view
    # import application.components.test.view
    import application.components.booking.view
    import application.components.contact.view
    import application.components.item.view
    import application.components.user.view
    pass
    
    @app.route('/')
    def index(request):
        return jinja.render('index.html', request)