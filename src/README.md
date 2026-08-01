# Engineering File Manager

Engineering File Manager is a desktop application developed in Python to help Mechanical Engineers compare SolidWorks BOMs with project folders.
It automatically detects missing files, revision mismatches, duplicate drawings, and generates a clear comparison report.

---

## Features

- Compare BOM ↔ Folder
- Revision Comparison
- Compare Folder ↔ Folder
- Duplicate Detection
- Progress Bar & Logging
- Configurable Column Mapping
- Multiple Themes (ttkbootstrap)

---

## Screenshots

(Add screenshots here)

---

## Installation

Download the latest release.

or

```bash
git clone ...
pip install -r requirements.txt
python main.py
```

---

## Project Structure

```
src/
│
├── controllers/
├── exceptions/
├── models/
├── rules/
├── services/
├── views/
├── workflows/
├── app.py
└── main.py
```

---

## Architecture

MVC + Service Layer

```
UI
↓

Controller
↓

Services

↓

Models
```

---

## Future Roadmap

- Read SolidWorks Revision
- PDF Metadata
- Export Excel Report
- Plugin System

---

## License

MIT

## Build Script

MIT