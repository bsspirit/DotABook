# -*- coding: utf-8 -*-
from flask import Flask
from view import heroes, items, rest, nav, maps
from sina import oauth

SERVER_PATH='http://dotabook.info/'
STATIC_PATH='http://dotabook.info/static/'


app = Flask(__name__)
app.debug = True
app.config.from_object(__name__)
#app.config.from_envvar('/home/conan/dotabook.cfg',silent=True)
app.secret_key = 'sdfaA0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

app.register_module(nav.view, url_prefix='')
app.register_module(oauth.view, url_prefix='/oauth')
app.register_module(heroes.view, url_prefix='/heroes')
app.register_module(items.view, url_prefix='/items')
app.register_module(rest.view, url_prefix='/rest')
app.register_module(maps.view, url_prefix='/maps')


if __name__ == '__main__':
	app.run()
