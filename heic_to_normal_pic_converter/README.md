# HEIC to Normal Converter

A minimal Python script to convert `.heic` image files to standard formats like `.png`, `.jpeg`, `.webp`, etc., using only pure Python libraries.

## ✅ Features

- Converts a single `.heic` file to any Pillow-supported format
- Simple and lightweight
- No admin rights required
- Uses `pillow-heif` to read `.heic` images natively


## 🛣️ Roadmap / Plan

This project can evolve into a more advanced utility with a GUI and additional features:

### 🔧 Phase 1: Minimal CLI
- [x] Convert `.heic` to `.png` using `pillow-heif`
- [x] No admin rights or compilation (e.g. needed Build Tools for Visual Studio)

### 🖼 Phase 2: GUI
- [ ] Build a user interface with Tkinter
- [ ] File picker for selecting `.heic`
- [ ] Dropdown menu to choose output format
- [ ] Save-as dialog for output location
- [ ] Use `pillow-heif` or `ImageMagick` (portable fallback)

### 🧱 Phase 3: Modular Architecture
- [ ] Split logic into `converter.py`, `ui.py`, `main.py`
- [ ] Add error handling and format validation
- [ ] Make it extensible for batch conversion

### 🧪 Phase 4: Bonus Features
- [ ] Batch processing (multiple files at once)
- [ ] Progress bar or console feedback
- [ ] Theme or styling with ttkbootstrap
- [ ] Drag-and-drop support
