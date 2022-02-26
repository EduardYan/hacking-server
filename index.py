"""
Principal file for execute
the hacking server.

"""


from server import server
from utils.config import CONFIG


if __name__ == '__main__':
    # running the server
    server.run(
        host = '0.0.0.0',
        port = CONFIG['PORT'],
        debug = True
    )
