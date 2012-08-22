## ping couchapp
This couchapp creates a document in CouchDB and can list up documents
which have the field "answer" with the value "pong"

## pong.py
This script listens to the changesfeed of the ping database and if it founds a
new document with the field "name" with the value "ping", it writes the field "answer" : "pong" to the document. 



