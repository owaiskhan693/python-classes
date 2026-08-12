# Parse any URL

from urllib.parse import urlparse

url = "https://www.google.com/search?abc=ahmed&x=123#marks"   

parsed = urlparse(url)   # urlparse ko bola "isko tor do" aur result parsed me rakh do

print(parsed)         # pore parsed ke types ko aik sath print karna
print(parsed.scheme)  # siraf netloc print karna
print(parsed.netloc)  # siraf scheme ko print karna
print(parsed.path)    # siraf path ko print karna
print(parsed.query)   # siraf query ko print karna
print(parsed.fragment) # siraf fragment ko print karna

# url with fragment 
url = "https://www.google.com/search?a=owais&x=123"

# fragment add kar diya
url_with_fragment = url + "#result" 

print(url_with_fragment)


from urllib.parse import urlparse, parse_qs

url = "https://www.youtube.com/watch?id=156&class=9#data"

parsed = urlparse(url)
params = parse_qs(parsed.query)  # ye wala dictionary hi  params hain

print(params)   # output: {'id': ['101'], 'class': ['9']}

print(params['id'][0])  








