# -*- coding: utf-8 -*-
from flask import Flask
from view import heroes, rest, nav
from sina import oauth

app = Flask(__name__)
app.debug = True
app.secret_key = 'sdfaA0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

app.register_module(nav.view, url_prefix='')
app.register_module(oauth.view, url_prefix='/oauth')
app.register_module(heroes.view, url_prefix='/heroes')
app.register_module(rest.view, url_prefix='/rest')


if __name__ == '__main__':
	app.run()
