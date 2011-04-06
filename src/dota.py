# -*- coding: utf-8 -*-
from flask import Flask
from view import heroes, items, rest, nav, maps, admin
from sina import oauth

#SERVER_PATH='http://dotabook.info/'
#STATIC_PATH='http://1.dotabook.sinaapp.com/static/'
#LOCAL_PATH='/home/deploy/DotABook/'

SERVER_PATH='http://localhost:5000/'
STATIC_PATH='http://localhost/static/'
LOCAL_PATH='/home/conan/workspace/app/DotABook/'

app = Flask(__name__)
app.debug = True
app.config.from_object(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

app.register_module(nav.view, url_prefix='')
app.register_module(oauth.view, url_prefix='/oauth')
app.register_module(heroes.view, url_prefix='/heroes')
app.register_module(items.view, url_prefix='/items')
app.register_module(rest.view, url_prefix='/rest')
app.register_module(maps.view, url_prefix='/maps')
app.register_module(admin.view, url_prefix='/admin')


if __name__ == '__main__':
	app.run()
