import os
import spotdl
from mutagen.easyid3 import EasyID3
from mutagen.flac import FLAC
playlists = []


#reads playlistlinks.txt, moves it to playlists list
with open('playlistlinks.txt', 'r') as f:
        
    for item in f.readlines():
        if item.startswith('#') == False:
            item = item.strip("\n").split(' | ')
            if item[0] != '':
                playlists.append(item)
    
for item in playlists:
    options = []
    
    flagS = 'False'
    flagF = 'mp3'
    
    #creates file structure
    os.mkdir(playlists[playlists.index(item)][1])
    os.mkdir(f"{playlists[playlists.index(item)][1]}/audio")
    os.chdir(f"{playlists[playlists.index(item)][1]}/audio")
    
    #check for options
    if playlists[playlists.index(item)][2] != '':
        options = playlists[playlists.index(item)][2].split(' ')
        

        print(options)
    #download audio files

    for item2 in options:
        
        if item2.startswith('-f='):
            flagF = item2.removeprefix('-f=')
        
        if item2.startswith('-s='):
            flagS = item2.removeprefix('-s=')
        
    os.system(f'python -m spotdl {playlists[playlists.index(item)][0]} --format {flagF}')
    

    
    #make m3u files
    os.chdir('..')
    with open('playlist.m3u', 'w') as f:
        for item in os.listdir('audio'):
            f.write(f'audio/{item}\n')
    
    #strip files
    print(flagS)
    if flagS == 'True':
        if flagF == 'mp3':
            for item2 in os.listdir('audio'):
                audio = EasyID3(f'audio/{item}')
                audio.delete()
                audio.save()
                
        elif flagF == 'flac':
            audio = FLAC(f'audio/{item}')
            audio.delete()
            audio.clear_pictures()
            audio.save
            
        else:
            print('non-mp3/flac files dont have id3 data to strip')
    
    #go back to rundir
    os.chdir('..')
    
    
print(playlists)