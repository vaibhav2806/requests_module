# everything learned from here : read://https_code.tutsplus.com/?url=https%3A%2F%2Fcode.tutsplus.com%2Ftutorials%2Fusing-the-requests-module-in-python--cms-28204%23%3A~%3Atext%3DUsing%2520the%2520Requests%2520Module%2520in%2520Python%25201%2520Making%2Cyou%2520using%2520req.cookies%2520and%2520req.headers.%2520More%2520items...%2520

import requests 
req = requests.get('http://www.tutsplus.com/') # All the information about our request is now stored in a Response object called req.

print(req.encoding)                 # req.encoding returns 'utf-8'. 
                                    # You can get the encoding of the webpage using the req.encoding property.

print(req.status_code)              # req.status_code returns 200. 
                                    # You can also get the status code of the request using the req.status_code property.

print(req.elapsed)                  # req.elapsed returns datetime.timedate(0 , 1 , 666890)
print(req.url)                      # to see final response URL we use req.url
print(req.history)                  # returns [<Response [301]>, <Response [301]>]

print(req.headers['content-type'])  # You can get the response headers using req.headers. 
                                    # The req.headers property returns a case insensitive dictionary of response headers. 
                                    # This means that req.headers['Content-Length'], req.headers['content-length'] and req.headers['CONTENT-LENGTH'] 
                                    # will all return the value of the 'Content-Length' response header.

# NOTE:
# Getting all this information about the webpage you are accessing is nice, 
# but you most probably want to access the actual content.
# If the content you are accessing is text, you can use the "req.text" property to access it.
# The content is then parsed as unicode. 
# You can pass the encoding with which to decode the text using the req.encoding property

# In the case of non-text responses, you can access them in binary form using req.content. 
# The module will automatically decode gzip and deflate transfer-encodings.

# You can also get the raw response from the server using req.raw. 
# Keep in mind that you will have to pass stream=True in the request to get the raw response.

