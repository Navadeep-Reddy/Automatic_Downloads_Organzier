import os
import glob
import shutil

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def move_file(src, dest_folder):
    dest = os.path.join(dest_folder, os.path.basename(src))
    if os.path.exists(dest):
        base, ext = os.path.splitext(dest)
        counter = 1
        while os.path.exists(dest):
            dest = f"{base}_{counter}{ext}"
            counter += 1
    shutil.move(src, dest)

def main():
    # store the path of downloads folder
    downloads_folder = "/home/navadeep/Downloads/"

    # create necessary folders
    folders = ["Photos", "Video", "Docs", "Audio", "Compressed", "Code", "Misc", "Folders"]
    for folder in folders:
        create_directory(os.path.join(downloads_folder, folder))

    # store the names of all the image files in a variable
    images_names = []
    image_types = ["*.jpg", "*.png", "*.svg", "*.gif", "*.webp"]
    for temp in image_types:
        images_names.extend(glob.glob(os.path.join(downloads_folder, temp))) 

    # move images to Photos folder
    for name in images_names:
        move_file(name, os.path.join(downloads_folder, "Photos"))

    # store the names of all videos in a variable
    video_names = []
    video_types = ["*.mp4", "*.mov", "*.webm", "*.avi", "*.mkv"]
    for temp in video_types:
        video_names.extend(glob.glob(os.path.join(downloads_folder, temp)))

    for name in video_names:
        move_file(name, os.path.join(downloads_folder, "Video"))

    # store all the names of documents
    doc_names = []
    doc_types = ["*.pptx", "*.docx", "*.pdf", "*.doc", "*.xlsx", "*.odt"] 
    for temp in doc_types:
        doc_names.extend(glob.glob(os.path.join(downloads_folder, temp)))

    for name in doc_names:
        move_file(name, os.path.join(downloads_folder, "Docs"))

    # store all the names of audio files
    au_names = []
    au_types = ["*.mp3", "*.m4a", "*.wav", "*.ogg", "*.opus"]
    for temp in au_types:
        au_names.extend(glob.glob(os.path.join(downloads_folder, temp)))

    for name in au_names:
        move_file(name, os.path.join(downloads_folder, "Audio"))

    # store compressed file names
    comp_names = []
    comp_types = ["*.zip", "*.rar", "*.tar", "*.z"]
    for temp in comp_types:
        comp_names.extend(glob.glob(os.path.join(downloads_folder, temp)))
    for name in comp_names:
        move_file(name, os.path.join(downloads_folder, "Compressed"))

    # store names of code files
    c_names = []
    c_types = ["*.py", "*.cpp", "*.html", "*.js", "*.css", "*.c"]
    for temp in c_types:
        c_names.extend(glob.glob(os.path.join(downloads_folder, temp)))
    for name in c_names:
        move_file(name, os.path.join(downloads_folder, "Code"))

    # move the remaining files to Misc
    misc_names = glob.glob(os.path.join(downloads_folder, "*.*"))
    for name in misc_names:
        move_file(name, os.path.join(downloads_folder, "Misc"))

    # get the names of all the folders
    fa_names = glob.glob(os.path.join(downloads_folder, "*"))
    f_names = []
    for temp in fa_names:
        if temp not in [os.path.join(downloads_folder, folder) for folder in folders]:
            f_names.append(temp)

    for name in f_names:
        move_file(name, os.path.join(downloads_folder, "Folders"))

main()
