#!/usr/bin/python
## -*- coding: utf-8 -*-

from flask import Flask, abort, render_template
from flask.ext.assets import Environment


application = app = Flask(__name__)
assets = Environment(app)
assets.init_app(app)


BASE_URL = '/'
PAGES = {
    '': ('home', ''),
    'behind-the-scenes': ('use_cases', 'Behind the scenes'),
    'my-work-experience': ('work', 'My work experience'),
    'about-me': ('about', 'About me'),
    'my-projects': ('projects', 'My Projects')
}


@app.route('/', methods=['GET'], defaults={'ajax': False, 'page': ''})
@app.route('/<page>/<ajax>/', methods=['GET'])
@app.route('/<page>/', methods=['GET'], defaults={'ajax': False})
def pages(page, ajax):
    if not page in PAGES:
        return abort(404)

    (tmpl, title) = PAGES[page]
    keys = {
        'include': ajax is not False,
        'base_url': BASE_URL,
        'page_title': '- ' + title if title else title
    }

    return render_template('pages/{}.html'.format(tmpl), **keys)


if __name__ == '__main__':
    app.run(debug=False)
