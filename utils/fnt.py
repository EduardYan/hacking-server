"""
This module have
some functions to use
for work with the scripts.
"""


from utils.config import CONFIG
from models.script import Script


# path for the scripts
SCRIPTS_PATH = CONFIG['SCRIPTS_PATH']


class ScriptIdInvalid(TypeError):
    """
    Model in case the id passed
    for parameter not is valid.
    """

    pass


def validate_id_script(id:int) -> bool:
    """
    Return the path of the script
    according to the id passed
    in the url.

    Execption is lauched if the id not
    is valid, or the datatype not is integer.

    """

    # validating the datatype
    if type(id) not in [int]:
        raise ScriptIdInvalid('The id of the script must be a integer.')

    for indx, script in enumerate(SCRIPTS_PATH):
        # lessing -1 for not problem with index
        if indx == id - 1:
            return script # in case is found return the script


def get_script(id:int) -> Script:
    """
    Return the script object
    with a path and a name.
    """


    path_script = validate_id_script(id)

    script = Script(
        path = path_script
    )

    return script
