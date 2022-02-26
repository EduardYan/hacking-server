"""
Route to use in the
server.
"""


from flask import (
    Blueprint,
    render_template,
    send_file,
)
from utils.fnt import get_script
from utils.config import SCRIPTS_INFO


# routes
myroutes = Blueprint('myroutes', __name__)

# the scripts to show in the page
SCRIPTS = SCRIPTS_INFO['SCRIPTS']


@myroutes.route('/')
def home():
    """
    Principal route to use
    in the server.
    """

    # pass the list with the scripts
    return render_template('index.html', scripts_list = SCRIPTS)


@myroutes.route('/get-script/<id>')
def get_script_route(id):
    """
    Send the script
    according to the id passed
    in the url.
    """

    # getting the correct script for send the file
    script = get_script(int(id))

    return send_file(script.path)


@myroutes.route('/about')
def about():
    """
    Route for render about the page.
    """

    return render_template('about.html')
