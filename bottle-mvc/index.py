# -*- coding: utf-8 -*-

import sys
sys.path.append('libs')

from app import app


# ==========================================
#   add static path
# ==========================================
@route('/stat/<filepath:path>')
def server_static(filepath):
	return static_file(filepath, root='./app/static')

# ==========================================
# run only in bottle
# ==========================================
from bottle.bottle import debug, run

debug(True)
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    run(app, reloader=True, host='0.0.0.0', port=port)

# ==========================================
# run in gunicorn
# ==========================================
#app = default_app()