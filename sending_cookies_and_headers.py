# You can access the cookies and headers that the server sends back to you using req.cookies and req.headers.
# Requests also allows you to send your own custom cookies and headers with a request.
# This can be helpful when you want to, let's say, set a custom user agent for your request.

# To add HTTP headers to a request, you can simply pass them in a DICT to the HEADER parameter. Similarly, 
# you can also send your own cookies to a server using a DICT passed to the COOKIES parameter.

import requests

url = 'http://some-domain.com/set/cookies/headers'

headers = {'user-agent' : 'your-own-user-agent/0.0.1'} 
cookies = {'visit-month' : 'Octuber'}

req = requests.get(url , headers = headers , cookies = cookies)

# 'http://www.tutsplus.com/set/cookies/headers'
# 'http://some-domain.com/set/cookies/headers'