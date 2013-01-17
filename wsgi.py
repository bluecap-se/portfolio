#!/usr/bin/env python


import os
from flask import Flask, abort, render_template


application = app = Flask('wsgi')

BASE_URL = '/'
PAGES = {
    '': ('home', ''),
    'behind-the-scenes': ('use_cases', 'Behind the scenes'),
    'my-work-experience': ('work', 'My work experience'),
    'about-me': ('about', 'About me'),
    'my-projects': ('projects', 'My Projects')
}


@app.route('/', methods=['GET'], defaults={'ajax': False, 'page': ''})
@app.route('/<page>/<ajax>', methods=['GET'])
@app.route('/<page>/', methods=['GET'], defaults={'ajax': False})
def pages(page, ajax):
    if not page in PAGES:
        return abort(404)

    (tmpl, title) = PAGES[page]
    print tmpl, title
    keys = {
        'include': ajax is not False,
        'base_url': BASE_URL,
        'page_title': '- ' + title if title else title
    }

    return render_template('pages/{}.html'.format(tmpl), **keys)


@app.route('/env-status')
def env():
    return os.environ.get('VCAP_SERVICES', '{}')


if __name__ == '__main__':
    app.run(debug=False)
