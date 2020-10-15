# Some files that you download from the internet using the Requests module may have a huge size. 
# In such cases, it will not be wise to load the whole response or file in the memory at once. 
# You can download a file in pieces or chunks using the iter_content(chunk_size = 1, decode_unicode=False) method.  

# This method iterates over the response data in chunk_size number of bytes at once. 
# When stream=True has been set on the request, this method will avoid reading the whole file into memory at once for large responses. 
# The chunk_size parameter can be either an integer or None. 
# When set to an integer value, chunk_size determines the number of bytes that should be read into the memory.

# When chunk_size is set to None and stream is set to True,the data will be read as it arrives in whatever size of chunks are received.
# When chunk_size is set to None and stream is set to False, all the data will be returned as a single chunk.
 
# Let's download image of a forest on Pixabay using the Requests module.


import requests
req = requests.get('https://media.geeksforgeeks.org/wp-content/cdn-uploads/gfg_200x200-min.png', stream = True)
req.raise_for_status()
with open('gfg_200x200-min.png', 'wb') as f:                         # wb = file is opened for writing in binary mode
    for chunk in req.iter_content(chunk_size=50000):
        print("Chunk has been recieved.")
        f.write(chunk)

 
 