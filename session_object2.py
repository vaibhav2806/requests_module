# Sessions are also helpful when you want to send the same data across all requests. 
# For example, if you decide to send a cookie or a user-agent header with all the requests to a 
# given domain, you can use Session objects.

import requests

ssn = requests.Session()
ssn.cookies.update({'visit-month' : 'Octuber'})

reqOne = ssn.get('http://httpbin.org/cookies')
print(reqOne)

reqTwo = ssn.get('http://httpbin.org/cookies' , cookies = {'visit-year' : '2020'})
print(reqTwo)

reqThree = ssn.get('http://httpbin.org/cookies')
print(reqThree)

# As you can see, the "visit-month" session cookie is sent with all three requests.
# However, the "visit-year" cookie is sent only during the second request. 
# There is no mention of the "vist-year" cookie in the third request too. 
# This confirms the fact that cookies or other data set on individual requests 
# won't be sent with other session requests.