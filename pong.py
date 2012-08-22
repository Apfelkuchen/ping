import couchdb

couch = couchdb.Server('http://localhost:5984')  # set the server
db = couch ['ping']								 # set the database
newest = db.changes()['last_seq']			 # gets newest element in the changesfeed to get only the changes since the program is running 
changesfeed = db.changes(feed='continuous', heartbeat='1000', include_docs=True,filter='Ping/ping', since=newest)

# defines the changesfeed; heartbeat ensures that there is a connection to the database; 
# the filter is specified in the design doc and filters deleted documents and the design doc
# this is a generator object, that means it runs continously

for line in changesfeed:		
	doc = line['doc']
	# process doc here
	try:
		if(doc['name']=='ping'):
			try:
				if(doc['answer'] != 'pong'):
					doc['answer'] ='pong'
					db.save(doc)
				else:					
					pass	# this ensures, that a doc changed by this script is not seen as a new ping
	
			except KeyError:
				doc['answer'] = 'pong'
				db.save(doc)
	except KeyError:
		print 'New doc found, but there is no ping in it!'

