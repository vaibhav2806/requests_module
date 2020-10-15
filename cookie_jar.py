# Cookies can also be passed in a Cookie Jar. 
# They provide a more complete interface to allow you to use those cookies over multiple paths.

import requests

jar = requests.cookies.RequestsCookieJar()
jar.set('first_cookie' , 'first' , domain = 'httpbin.org' , path = '/cookies')
jar.set('second_cookie' , 'second' , domain = 'httpbin.org' , path = '/extra')
jar.set('third_cookie' , 'third' , domain = 'httpbin.org' , path = '/cookies')

url = 'http://httpbin.org/cookies'
req = requests.get(url , cookies = jar)
print(req.text)