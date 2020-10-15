# The session object preserve certain parameters across multiple requests.
# It will persist cookie data across all requests made using the same session.
# The Session object uses urllib3's connection pooling.
# This means that the underlying TCP connection will be reused for all the requests made to the same host.
# This can significantly boost the performance.
import requests

reqone = requests.get('https://tutsplus.com/')
reqone.cookies['_tuts_session']
# print(reqone)

reqtwo = requests.get('https://tutsplus.com/')
reqtwo.cookies['_tuts_session']
# print(reqtwo)

sesone = requests.Session()
sesone.get('https://tutsplus.com/')
sesone.cookies['_tuts_session']
 # print(sesone)

reqthree = sesone.get('https://code.tutsplus.com/tutorials')
reqthree.cookies['_tuts_session']
# print(reqthree) 

