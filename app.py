import os
import pathlib
import shutil
import glob

files = []


src_folder = r"D:\Stažené soubory"
stl_folder = r"D:\Stažené soubory\\STLs\\"
exe_folder = r"D:\Stažené soubory\\EXEs\\"
img_folder = r"D:\Stažené soubory\\IMGs\\"
audio_folder = r"D:\Stažené soubory\\MP3s\\"
video_folder = r"D:\Stažené soubory\\VIDEOs\\"
zip_folder = r"D:\Stažené soubory\\ZIPs\\"


docs = ("\*.pdf", "\*.docx", "\*.doc")
stl_pattern = ("\*.stl", "\*.3mf", "\*.obj", "\*.step", "\*.gcode", "\*.scad", "\*.dxf")
exe_pattern = ("\*.exe", "\*.msi")
img_pattern = ("\*.jpeg", "\*.jpg", "\*.svg", "\*.gif", "\*.png")
audio_pattern = ("\*.mp3", "\*.wav")
video_pattern = ("\*.srt", "\*.avi", "\*.mp4")
zip_pattern = ("\*.zip", "\*.rar")

print(stl_pattern)

def organize(pattern, folder):
    global files

    try:
        dst_folder = os.mkdir(folder)
    except OSError:
        print ("Creation of the directory %s failed" % folder)
    else:
        print ("Successfully created the directory %s " % folder)

    for item in pattern:
        files.append(glob.glob(src_folder + item))                  #adds pattern to a list files[]
        print(item)
    new_files = [a for sublist in files for a in sublist]           #flattens the files[] list
    for file in new_files:
        file_name = os.path.basename(file)
        shutil.move(file, folder + file_name)
        print('Moved:', file)
    files = []

if __name__ == "__main__":
    organize(stl_pattern, stl_folder)
    organize(exe_pattern, exe_folder)
    organize(img_pattern, img_folder)
    organize(audio_pattern, audio_folder)
    organize(video_pattern, video_folder)
    organize(zip_pattern, zip_folder)





