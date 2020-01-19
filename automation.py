import shutil
import os

source_folder = 'C:\\Users\\Vishal-PC\\Downloads'
zip_folder = 'D:\\zip'
img_folder = 'D:\\Pictures'
video_folder = 'D:\\Videos'
music_folder = 'D:\\Music'
exe_folder = 'D:\\Softwares'
miscellaneous_folder= 'D:\\miscellaneous'
pdf_folder = 'D:\\PDFs'

for filename in os.listdir(source_folder):
    if filename.endswith('zip'):
        shutil.move(source_folder + "\\" + filename, zip_folder)
    elif filename.endswith('exe'):
        shutil.move(source_folder + "\\" + filename, exe_folder)
    elif filename.endswith('jpg') or filename.endswith('png'):
        shutil.move(source_folder + "\\" + filename, img_folder)
    elif filename.endswith('mp4') or filename.endswith('.mkv') or filename.endswith('.m4a'):
        shutil.move(source_folder + "\\" + filename, video_folder)
    elif filename.endswith('mp3') or filename.endswith('.wav'):
        shutil.move(source_folder + "\\" + filename, music_folder)
    elif filename.endswith('pdf'):
        shutil.move(source_folder + "\\" + filename, pdf_folder)
