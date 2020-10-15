# Making a POST request is just as easy as making GET requests. You just use the post() function instead of get(). 
# This can be useful when you are automatically submitting forms. 
# For example, the following code will download the whole Wikipedia page on Nanotechnology and save it on your PC.

import requests
req = requests.post('https://en.wikipedia.org/w/index.php', data = {'search' : 'Nanotechnology'})
req.raise_for_status()
with open('Nanotechnology.html' , 'wb') as f:
    for chunk in req.iter_content(chunk_size=50000):
        f.write(chunk)