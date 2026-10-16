
from pathlib import Path

CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Music": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
}


def organize_files(folder_path):
    folder = Path(folder_path).expanduser()

    if not folder.is_dir():
        print("Error: The folder does not exist.")
        return

    moved_count = 0

    for file in folder.iterdir():
        if not file.is_file():
            continue

        for category, extensions in CATEGORIES.items():
            if file.suffix.lower() not in extensions:
                continue

            destination = folder / category
            target = destination / file.name

            # Avoid moving a file onto itself or overwriting files.
            if target.exists():
                print(f"Skipped duplicate: {file.name}")
                break

            try:
                destination.mkdir(exist_ok=True)
                file.rename(target)
                print(f"Moved {file.name} -> {category}/")
                moved_count += 1
            except OSError as error:
                print(f"Could not move {file.name}: {error}")

            break

    print(f"\nDone! Organized {moved_count} file(s).")


if __name__ == "__main__":
    folder = input("Enter the folder path to organize: ").strip()
    organize_files(folder)
