import os, shutil, argparse
import magic

def sort_files(dir):
    
    # Define MIME categories
    mime = magic.Magic(mime=True)

    files = os.listdir(dir)

    for file_name in files:
        file_path = os.path.join(dir, file_name)
        
        if os.path.isfile(file_path):
            type = mime.from_file(file_path)

            if "audio" in type:
                destination_folder = os.path.join(dir, "Audio")
            elif "image" in type:
                destination_folder = os.path.join(dir, "Images")
            elif "video" in type:
                destination_folder = os.path.join(dir, "Videos")
            elif type in ["application/pdf", "application/vnd.openxmlformats-officedocument.wordprocessingml.document"]:
                destination_folder = os.path.join(dir, "Documents")
            elif type in ["application/zip", "application/x-rar", "application/x-gzip", "application/gzip", "application/x-7z-compressed"]:
                destination_folder = os.path.join(dir, "Compressed Files")
            elif type in ["application/vnd.microsoft.portable-executable", "application/x-dosexec"]:
                destination_folder = os.path.join(dir, "Installers")
            elif type in ["text/plain", "application/octet-stream"]:
                destination_folder = os.path.join(dir, "Shortcuts")
            elif type in ["application/x-bittorrent"]:
                destination_folder = os.path.join(dir, "Torrent")
            else:
                destination_folder = os.path.join(dir, "Others")
            
            # Create folders if not exist
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)
            
            # Move files
            shutil.move(file_path, os.path.join(destination_folder, file_name))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', type=str)
    args = parser.parse_args()

    # If no args are passed, ask the user
    if args.dir:
        directory = args.dir
    else:
        directory = input("path of the directory to be sorted: ")

    if os.path.isdir(directory):
        sort_files(directory)
        print('done!')
    else: 
        print('directory not found')

if __name__ == '__main__':
    main()