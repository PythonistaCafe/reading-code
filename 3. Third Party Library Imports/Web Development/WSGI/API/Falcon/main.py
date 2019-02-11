"""
This application is a simple example of how the falcon package works
"""

from falcon import API  # main falcon method
from app.views import EndpointOne, EndpointTwo

app = API()  # define the application name that will be called via a WSGI server

# Here we are defining the routes and assigning them to the app
app.add_route("/one", EndpointOne)
app.add_route("/two", EndpointTwo)

"""
This is all that we need to do to get a falcon API up and running. We simply need to load the app with a WSGI server
such as gunicorn to make it run. This is not like flask in that there is no "development" server that can be run.
"""
