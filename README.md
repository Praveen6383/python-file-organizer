
# Python File Organizer 📁

A simple Python project that organizes files into folders based on their file types.

## 📌 About

The Python File Organizer helps keep folders clean and organized by automatically moving supported files into categories such as Images, Documents, Videos, Music, and Archives.

This project is designed for beginners who want to learn Python and contribute to open-source software.

## ✨ Features

- Organizes files by file extension
- Supports images, documents, videos, music, and archives
- Creates category folders automatically
- Skips duplicate filenames to avoid overwriting files
- Displays messages showing which files were moved
- Uses Python's built-in libraries

## 🛠️ Technologies Used

- Python 3
- pathlib (standard library)

## 📋 Requirements

- Python 3.9 or newer

No external packages are required.

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Praveen6383/python-file-organizer.git
```

### 2. Open the project folder

```bash
cd python-file-organizer
```

### 3. Run the program

```bash
python organizer.py
```

Enter the path of the folder you want to organize when prompted.

## 💡 Example

Before:

```text
MyFiles/
├── photo.jpg
├── notes.txt
└── video.mp4
```

After:

```text
MyFiles/
├── Images/
│   └── photo.jpg
├── Documents/
│   └── notes.txt
└── Videos/
    └── video.mp4
```

## ⚠️ Safety

- Test the program on a folder containing sample files first.
- The program moves files into category folders.
- Back up important files before running it.
- Files with unsupported extensions are left unchanged.

## 🗺️ Future Improvements

- Add a dry-run mode
- Add automated tests
- Support more file formats
- Improve error handling
- Add a graphical user interface

## 🤝 Contributing

Contributions, suggestions, and bug reports are welcome.

Please test your changes before submitting a pull request.

## 📄 License

This project is intended to be released under the MIT License once a LICENSE file is added.

## 👨‍💻 Author

Praveen (GitHub: [@Praveen6383](https://github.com/Praveen6383))
