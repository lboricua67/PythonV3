# For loops


for i in range(30):
    print(i)

a={}
for i in range(30):
    a[i] = i

print(a)


#from urllib import request as urlrequest
from urllib import request

proxy_host={'http': 'http://proxy.fisdev.local:8080'}
url='http://sixty-north.com/c/t.txt'
vproxy = {'http': 'http://proxy.fisdev.local:8080', 'https': 'http://proxy.fisdev.local:8080'}
#url = 'http://portal.azure.com/'

url='https://fisglobal.sharepoint.com/sites/fisandme'
url='http://www.google.com/'
proxy = request.ProxyHandler(vproxy)
auth = request.HTTPBasicAuthHandler()
opener = request.build_opener(proxy, auth, request.HTTPHandler)
request.install_opener(opener)

story = request.urlopen(url)

print(story)
story_words = []
for line in story:
    line_words = line.split()
    for word in line_words:
        story_words.append(word)
story.close()
print(story_words)