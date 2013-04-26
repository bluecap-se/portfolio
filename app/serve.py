# -*- coding: utf-8 -*-

import time
from werkzeug.serving import BaseRequestHandler


class TimedRequestHandler(BaseRequestHandler):
    """Extend werkzeug request handler to suit our needs."""
    def handle(self):
        self.starttime = time.time()
        rv = super(TimedRequestHandler, self).handle()
        return rv

    def send_response(self, code, message=None):
        self.endtime = time.time()
        super(TimedRequestHandler, self).send_response(code, message=None)

    def log_request(self, code='-', size='-'):
        duration = int((self.endtime - self.starttime) * 1000)
        self.log('info', '"{0}" {1} {2} [{3}ms]'.format(self.requestline, code, size, duration))
