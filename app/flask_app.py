# -*- coding: utf-8 -*-

from flask import Blueprint, abort, render_template
from app.config import config

bp = Blueprint('simple_page', __name__, template_folder='templates')

PAGES = {
    '': ('home', ''),
    'behind-the-scenes': ('use_cases', 'Behind the scenes'),
    'my-work-experience': ('work', 'My work experience'),
    'about-me': ('about', 'About me'),
    'my-projects': ('projects', 'My Projects')
}


@bp.route('/', methods=['GET'], defaults={'ajax': False, 'page': ''})
@bp.route('/<page>/<ajax>/', methods=['GET'])
@bp.route('/<page>/', methods=['GET'], defaults={'ajax': False})
def pages(page, ajax):
    if not page in PAGES:
        return abort(404)

    (tmpl, title) = PAGES[page]
    keys = {
        'include': ajax is not False,
        'base_url': config.get('app').get('base_dir'),
        'page_title': '- ' + title if title else title
    }

    return render_template('pages/{}.html'.format(tmpl), **keys)
