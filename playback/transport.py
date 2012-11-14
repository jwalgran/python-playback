from appscript import *
from playback import Track
import time

def is_playing():
    itunes = app('itunes')
    if itunes.isrunning():
        if itunes.player_state() == k.playing:
            return True
        else:
            return False
    else:
        return False
    
def now_playing():   
    if is_playing():
        try:
            return Track(app('itunes').current_track())
        except:
            return None
    else:
        return None
    
def play():
    itunes = app('itunes')
    itunes.launch()
    itunes.play()
    
def pause():
    itunes = app('itunes')
    if itunes.isrunning():
        itunes.pause()
        
def stop():
    itunes = app('itunes')
    if itunes.isrunning():
        itunes.stop()
        
def skip(fade=False):
    return next(fade=fade)
        
def next(fade=False):
    itunes = app('itunes')
    if itunes.isrunning():
        if not is_playing():
            itunes.next_track()
            if fade:
                fade_in()
            else:
                play()
        else:
            if fade: fade_out()
            itunes.next_track()
            if fade: fade_in()
            
        timeout = 0
        next = now_playing()
        while timeout < 50 and next is None:
            time.sleep(0.2)
            next = now_playing()
            timeout += 1
        return next

def fade_out():
    itunes = app('itunes')
    if itunes.isrunning() and is_playing():
        vol = itunes.sound_volume()
        cur_vol = vol
        while cur_vol > 0:
            cur_vol -= 1
            itunes.sound_volume.set(cur_vol)
            if cur_vol > 0:
                time.sleep(0.02)
            else:
                stop()
                itunes.sound_volume.set(vol)
                
def fade_in():
    itunes = app('itunes')
    if not itunes.isrunning():
        itunes.launch()
    if not is_playing():
        vol = itunes.sound_volume()
        cur_vol = 0
        itunes.sound_volume.set(cur_vol)
        play()
        while cur_vol < vol:
            cur_vol += 1
            itunes.sound_volume.set(cur_vol)
            if cur_vol < vol:
                time.sleep(0.02)
    return now_playing()                