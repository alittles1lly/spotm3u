import os
import spotdl


playlists = []

with open('playlistlinks.txt', 'r') as f:
        
    for item in f.readlines():
        if item.startswith('#') == False:
            item = item.strip("\n").split(' | ')
            if item[0] != '':
                playlists.append(item)
    
for item in playlists:
#    os.mkdir(playlists[playlists.index(item)][1])
#    os.mkdir(f"{playlists[playlists.index(item)][1]}/audio")
    os.chdir(f"{playlists[playlists.index(item)][1]}/audio")
#    os.system(f'python -m spotdl {playlists[playlists.index(item)][0]}')
    os.chdir('..')
    
    with open('playlist.m3u', 'w') as f:
        for item in os.listdir('audio'):
            f.write(f'audio/{item}\n')
    
    
print(playlists)