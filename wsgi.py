# Main entry point (multiple applications on same Python process)
from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware

from mamigot.me import main
from mamigot.me.api import api


application = DispatcherMiddleware(main, {
    '/api': api
})


if __name__ == "__main__":
    run_simple( '0.0.0.0', 5000, application,
                use_reloader=True, use_debugger=True)
