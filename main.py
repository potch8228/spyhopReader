#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from os import environ
import logging
import webapp2
from spyframework import router


def handle_401(request, response, exception):
    logging.exception(exception)
    response.write('Not authorized!')
    response.set_status(exception.code)


def handle_404(request, response, exception):
    logging.exception(exception)
    response.write('Oops! I could swear this page was here!')
    response.set_status(exception.code)


def handle_500(request, response, exception):
    logging.exception(exception)
    response.write('A server error occurred!')
    response.set_status(500)

debug = environ.get('SERVER_SOFTWARE', '').startswith('Dev')

app = webapp2.WSGIApplication([
    ('/.*', 'modules.{module}.controllers.{controller}.{action}Handler'),
    webapp2.Route('/toppage/default/store', name='store-feed' ),
    webapp2.Route('/toppage/default/blogs', name='list-blogs' ),
], debug=debug)
app.router.set_dispatcher(router.custom_dispatcher)

app.error_handlers[401] = handle_401
app.error_handlers[404] = handle_404
app.error_handlers[500] = handle_500
