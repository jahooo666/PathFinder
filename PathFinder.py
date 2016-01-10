# -*- coding: <utf-8> -*-
import random
from flask import Flask, request, redirect, render_template, session
from werkzeug.debug import DebuggedApplication

#app_url = '/okraskaj/PathFinder'
app_url = ''
app = Flask(__name__)
app.secret_key = '$a82sd7DS35gfs*@#DSc'

app.debug = True
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)
#
# links = {}
# users = {'admin': 'admin'}
# users_links={}
# users_links['admin'] = {}

@app.route(app_url + '/', methods=['POST','GET'])
def index():



if __name__ == '__main__':
    app.run()