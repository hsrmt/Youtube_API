#ccmixter_search_url="http://dig.ccmixter.org/search?searchp=instrumental"

from tkinter import Y
import urllib.request
import random

song_list=[]

webUrl=urllib.request.urlopen("http://dig.ccmixter.org/search?searchp=pop")
print("result code:"+str(webUrl.getcode()))

data=webUrl.read()
#Sprint(type(data))
x=str(data).split('1 - 40 of ')[1].split('</div><label')
print(x[0])
new_url="http://dig.ccmixter.org/search?limit="+x[0].replace(',','')+"&searchp=pop"
#new_url="http://dig.ccmixter.org/search?limit=10&searchp=pop"
print(new_url)

new_webUrl=urllib.request.urlopen(new_url)
new_data=new_webUrl.read()
y=str(new_data).split('<a class="upload-link song-title"')

for i in range(1,len(y)):
    song_list.append(y[i].split('</a> <a class="people-link artist-name light-color" ')[0].split('>')[1])
# for song in song_list:
#     print(song)
   # print("aaa "+y[i].split('</a> <a class="people-link artist-name light-color" ')[0].split('>')[1])
#[1].split('<a class="people-link artist-name light-color" ')
random_song=random.sample(song_list,1)
print(random_song)