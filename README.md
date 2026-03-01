# Smart File Organizer

A Python CLI tool to automatically organize files into folders based on their extensions.  
Supports dry-run mode to preview actions without moving files.

📌 **Features**
- Organize files by extension into separate folders
- Handles filename collisions automatically
- Dry-run mode to preview changes
- Configurable via `extension_map.json`

🧱 **Architecture**
- `smart_file_organizer.py`: Main CLI script  
- `extension_map.json`: Maps file extensions to folder names  
- Logging handled via `organizer.log` (excluded from git)  
- Default folder is `Downloads` if no path is provided  

🎮 **Example Usage**
Run from terminal:

Dry-run (preview changes):
```bash
py smart_file_organizer.py --dry-run "C:\Users\YourUser\Desktop\test_file_org"
```
Normal mode (move files):
```bash
py smart_file_organizer.py "C:\Users\YourUser\YourFile\"
```
Default folder (Downloads):
```bash
py smart_file_organizer.py
```
⚙️ Requirements
Python 3.10+
Standard library only (no external dependencies)
