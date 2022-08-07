'''We use mixer module along with the music module'''
#mixer module is used to control the playback of the streamed music
#mixer.music.load 
'''loads music file object and prepares it for playback if music is
already playing it will stop. This doesn't start playing music'''

#.unload
'''unload currently loaded music file and free up resources'''

#.play
'''start the playback can have 0 to 3 arguments, loops how many times the music
would be repeated, start position float arg., fade_ms the time for which the music 
will fade away to volume 0'''

#.rewind
'''plays the audio file from beginning. If music is paused it remains paused'''

#.stop
'''stops music if playing note stop and unload are not same'''

#.pause
'''temporarily stops playing the music stream. '''
#. unpause
'''to resume paused music after it has been paused'''
#.fadeout
'''takes time argument for which music has to fade out'''
#.set_volume
'''to set volume of audio'''
#.get_volume
'''to know the current volume of the audio'''

#.get_busy
'''Returns true when music is playing'''

#.set_pos
'''to set the point from which playback should start playing'''

#.get_pos
'''to get the time for how long the music is been playing'''

#.queue()
'''to enqueue a song to the current one'''


from pygame import mixer
mixer.init()

mixer.music.load('song.mp3')
mixer.music.play()
mixer.music.set_pos(170)
mixer.music.queue('nextsong.mp3')



#mixer.music.set_pos(120)#time from which the audio should start in seconds here 2.00
#print(mixer.music.get_busy())#is the player is busy or not

# print(mixer.music.get_volume())
# mixer.music.set_volume(0.81)
# print(mixer.music.get_volume())
#print(mixer.music.get_pos())#for how long the audio is playing in ms
#mixer.music.fadeout(10000)#this is 10 seconds after 10 seconds music stops playing
#print(mixer.music.get_busy())
# print(mixer.music.get_volume())
#print(mixer.music.get_pos())
'''Press "P" to pause
Press "U" to unpause
Press "R" to rewind
Press "S" to exit'''
while True:
    inp = input(' ')
    if inp== 'P':
        mixer.music.pause()
        print(mixer.music.get_busy())
    elif inp == 'U':
        mixer.music.unpause()
        print(mixer.music.get_busy())
    elif inp=='S':
        mixer.music.stop()
        print(mixer.music.get_busy())
        break
    elif inp == 'R':
        mixer.music.rewind()
        print(mixer.music.get_busy())
    
    
    
