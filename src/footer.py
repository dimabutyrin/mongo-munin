
if __name__ == "__main__":          
	
    from os import environ
    if 'HOST' in environ:
        host = environ['HOST']
    if 'PORT' in environ:
        port = environ['PORT']
    if 'USER' in environ:
        user = environ['USER']
    if 'PASSWORD' in environ:
        password = environ['PASSWORD']
    
m = re.search("mongo(_.*)_(.*)$", sys.argv[0])
if (m):
    instance = m.group(1)

if len(sys.argv) > 1 and sys.argv[1] == "config":
    doConfig()
else:
    doData()
