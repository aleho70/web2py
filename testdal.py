from gluon.dal import *
db = DAL('google:ndb')
#db = DAL('google:datastore')
t = db.define_table('funtest', 
                Field('name', length=128)) 
print t.insert(name='Ales')
print db(t.id>0).select()