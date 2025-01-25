## About
A Python sorting script that separetes files according to MIME definitions in:
- **Audio** (``` .wav ```, ``` .mp3 ```, ``` .flac ...```)
- **Compressed Files** (``` .rar ```, ``` .zip ```, ``` .7z ```, ...)
- **Images** (``` .png ```, ``` .jpg ```, ``` .jpeg ```, ``` .gif ```, ...)
- **Installers** (``` .exe ```, ``` .msi ```, ...)
- **Shortcuts** (``` .lnk ```, ``` .url ```, ``` .webloc ```, ...)
- **Torrent** (``` .torrent ```)
- **Videos** (``` .mp4 ```, ``` .mov ```, ``` .avi ```, ``` .mkv ```, ...)
- **Documents** (``` .pdf ```, ``` .docx ```, ``` .xlsx ```, ``` .pptx ```, ...)
- **Others** (Other uncategorized file types)

## Installation

### 1. Clone the repository
 ```sh
   git clone https://github.com/mat-cf/sort-files.git
   cd sort-files
```

### 2. Install the requirements
```sh
pip install -r requirements.txt
```

## Usage
You can pass the directory path as a argument 
```sh
$ python sort_folder.py --dir "C:\Users\user\Downloads"
```
Or input as the program asks 
```sh
path of the directory to be sorted: C:\Users\user\Downloads
```

