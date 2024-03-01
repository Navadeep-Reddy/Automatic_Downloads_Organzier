import os
import sys
import glob
import shutil


def main():

    #store the path of downloads folder
    downloads_folder = "/home/navadeep/Downloads/"

    #store the names of all the image files in a variable
    images_names = []
    image_types = ["*.jpg", "*.png", "*.svg", "*.gif", "*.webp"]
    for temp in image_types:
        images_names.extend(glob.glob(os.path.join(downloads_folder, temp))) 

    #move images to Pictures folder
    for name in images_names:
        shutil.move(name, "/home/navadeep/Downloads/Photos")


    #store the names of all videos in a variable
    video_names = []
    video_types = ["*.mp4", "*.mov", "*.webm", "*.avi"]
    for temp in video_types:
        video_names.extend(glob.glob(os.path.join(downloads_folder, temp)))

    for name in video_names:
        shutil.move(name, "/home/navadeep/Downloads/Video")


    #store all the names of documents
    doc_names = []
    doc_types = ["*.pptx", "*.docx", "*.pdf", "*.doc"] 
    for temp in doc_types:
        doc_names.extend(glob.glob(os.path.join(downloads_folder, temp)))

    for name in doc_names:
        shutil.move(name, "/home/navadeep/Downloads/Docs")

    #store all the names of audio files
    au_names = []
    au_types = ["*.mp3", "*.m4a", "*.wav", "*.ogg", "*.opus"]
    for temp in au_types:
        au_names.extend(glob.glob(os.path.join(downloads_folder, temp)))

    for name in au_names:
        shutil.move(name, "/home/navadeep/Downloads/Audio")

    #store compressed file name
    comp_name = []
    comp_types = ["*.zip", "*.rar", "*.tar", "*.z"]
    for temp in comp_types:
        comp_name.extend(glob.glob(os.path.join(downloads_folder, temp)))
    for name in comp_name:
        shutil.move(name, "/home/navadeep/Downloads/Compressed")

    #store names of code
    c_name = []
    c_types = ["*.py", "*.cpp", "*.html", "*.js", "*.css", "*.c"]
    for temp in c_types:
        c_name.extend(glob.glob(os.path.join(downloads_folder, temp)))
    for name in c_name:
        shutil.move(name, "/home/navadeep/Downloads/Code")

    #move the remaining to misc
    misc_names = glob.glob(os.path.join(downloads_folder, "*.*"))
    for name in misc_names:
        shutil.move(name, "/home/navadeep/Downloads/Misc")

main()
