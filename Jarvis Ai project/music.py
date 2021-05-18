import os
print("playing music")
music_list='C:\\Users\\Akash koirala\\Music\\iTunes\\iTunes Media\\Music\\Unknown Artist\\Unknown Album'
songs=os.listdir(music_list)
print(f"{songs}\n")
os.startfile(os.path.join(music_list,songs[0]))
