from google.appengine.ext import ndb

class user_schedule():
    name = nbd.StringProperty(required=true)
    monday = ndb.ListProperty(required=false)
    tuesday = nbd.ListProperty(required=false)
    wednesday = nbd.ListProperty(required=false)
    thursday = nbd.ListProperty(required=false)
    friday = nbd.ListProperty(required=false)
    saturday = nbd.ListProperty(required=false)
    sunday = nbd.ListProperty(required=false)
