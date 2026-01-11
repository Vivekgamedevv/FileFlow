📁 FileFlow – Python File Organizer

FileFlow is a Python-based file organizer that automatically sorts files in any selected folder into well-structured categories using a simple and clean GUI.

The application works on any folder chosen by the user and organizes files into an Organized_Folders directory inside the selected path.

🚀 How It Works

Run the application

Select any folder using the GUI

Click Organize Files

Files are scanned and categorized based on their extensions

Organized folders are created automatically

The program safely handles:

Multi-dot filenames

Uppercase file extensions

Files without extensions

📂 Output Structure
Selected_Folder/
└── Organized_Folders/
    ├── Videos/
    ├── Images/
    ├── Documents/
    ├── Music/
    ├── Code/
    ├── Archive/
    └── Junk/

🗂️ Categories Used
File Extension	Category
mp4, mkv, mov	Videos
mp3	Music
jpg, png, jpeg, gif	Images
pdf, txt, docx, xlsx	Documents
py, c, java, html	Code
zip, rar, 7z	Archive
No / unknown extension	Junk
▶️ How to Run
python gui.py

🛠️ Built With

Python 3

Tkinter

os & shutil
