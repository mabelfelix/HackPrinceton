#!/usr/bin/env python
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
import webapp2
import urllib2
import jinja2
import os

jinja_environment = jinja2.Environment(
   loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        mainPageTemplate = jinja_env.get_template('home.html')

        # if request.user.is_authenticated():
        #     self.redirect("/")
        # else:
        self.response.out.write(mainPageTemplate.render())

# class UserHandler(webapp2.RequestHandler):
#     def get(self):
        # insidePageTemplate = jinja_env.get_template('inside.html')

        # monday_sevenam = self.request.get('monday_sevenam')
        # monday_eightam = self.request.get('monday_eightam')
        # monday_nineam = self.request.get('monday_nineam')
        # monday_tenam = self.request.get('monday_tenam')
        # monday_elevenam = self.request.get('monday_elevenam')
        # monday_twelvepm = self.request.get('monday_twelvepm')
        # monday_onepm = self.request.get('monday_onepm')
        # monday_twopm = self.request.get('monday_twopm')
        # monday_threepm = self.request.get('monday_threepm')
        # monday_fourpm = self.request.get('monday_fourpm')
        # monday_fivepm = self.request.get('monday_fivepm')
        # monday_sixpm = self.request.get('monday_sixpm')
        # monday_sevenpm = self.request.get('monday_sevenpm')
        # monday_eightpm = self.request.get('monday_eightpm')
        # monday_ninepm = self.request.get('monday_ninepm')
        # monday_tenpm = self.request.get('monday_tenpm')
        # monday_elevenpm = self.request.get('monday_elevenpm')
        # monday_twelveam = self.request.get('monday_twelveam')
        # monday_oneam = self.request.get('monday_oneam')
        # monday_twoam = self.request.get('monday_twoam')
        # monday_threeam = self.request.get('monday_threeam')
        # monday_fouram = self.request.get('monday_fouram')
        # monday_fiveam = self.request.get('monday_fiveam')
        # monday_sixam = self.request.get('monday_sixam')

        # monday = [self.request.get('monday_sevenam'), self.request.get('monday_eightam'), self.request.get('monday_nineam'), self.request.get('monday_tenam'), self.request.get('monday_elevenam'), self.request.get('monday_twelvepm'), self.request.get('monday_onepm'), self.request.get('monday_twopm')]
        # monday.extend(self.request.get('monday_threepm'), self.request.get('monday_fourpm'), self.request.get('monday_fivepm'), self.request.get('monday_sixpm'), self.request.get('monday_sevenpm'), self.request.get('monday_eightpm'), self.request.get('monday_ninepm'), self.request.get('monday_tenpm'))
        # monday.extend(self.request.get)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
    # ('/', UserHandler)
], debug=True)
