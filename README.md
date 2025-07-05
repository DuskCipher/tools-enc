
# 🔐 DUSK CIPHER - Professional Encryption Toolkit

![Version](https://img.shields.io/badge/version-3.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.6+-green.svg)
![License](https://img.shields.io/badge/license-MIT-yellow.svg)

**DUSK CIPHER** adalah toolkit enkripsi profesional untuk melindungi dan mengobfuscate script Python menggunakan encoding base64. Tool ini menyediakan interface command-line dan web interface yang user-friendly.

## ✨ Fitur Utama

- 🔒 **Enkripsi Script Python** - Obfuscate kode Python dengan base64 encoding
- 🔓 **Dekripsi Script** - Restore file yang sudah dienkripsi kembali ke bentuk asli
- 🌐 **Web Interface** - Interface web yang mudah digunakan
- 📝 **File Creator** - Tool untuk membuat file Python dengan template
- 🔄 **Batch Operations** - Proses multiple file sekaligus
- 📊 **File Analyzer** - Analisis detail file Python
- 📈 **Usage Statistics** - Tracking penggunaan tool

## 🚀 Instalasi

### Instalasi Otomatis

```bash
# Clone atau download project ini
# Jalankan installer
chmod +x install.sh
./install.sh
```

### Instalasi Manual

```bash
# Pastikan Python 3.6+ terinstall
python3 --version

# Install dependensi sistem (Ubuntu/Debian)
sudo apt-get update
sudo apt-get install python3 python3-pip nano curl wget git

# Install dependensi Python
pip3 install --upgrade pip requests urllib3
```

## 📖 Cara Penggunaan

### 1. Mode Interaktif (Recommended)

```bash
python3 dusk_cipher.py
```

Interface interaktif akan menampilkan menu dengan berbagai pilihan:
- [1] 🔒 ENCRYPT SCRIPT - Enkripsi file Python
- [2] 🔓 DECRYPT SCRIPT - Dekripsi file yang sudah dienkripsi
- [3] 📝 CREATE NEW FILE - Buat file Python baru
- [4] 📁 FILE ANALYZER - Analisis file
- [5] 🔄 BATCH OPERATIONS - Proses multiple file
- [9] 🌐 WEB INTERFACE - Buka interface web

### 2. Command Line Tools

#### Enkripsi File
```bash
# Enkripsi single file
python3 pyobfuscator.py script.py

# Enkripsi multiple file
python3 pyobfuscator.py *.py

# Enkripsi dengan output directory
python3 pyobfuscator.py script.py -o /path/to/output
```

#### Dekripsi File
```bash
# Dekripsi single file
python3 pydecoder.py encrypted_script.py

# Dekripsi multiple file
python3 pydecoder.py *_encrypted.py

# Dekripsi dengan output directory
python3 pydecoder.py encrypted_script.py -o /path/to/output
```

### 3. Web Interface

```bash
# Start web server
python3 web_obfuscator.py

# Buka browser ke http://localhost:5000
```

Interface web menyediakan:
- ✅ Enkripsi script secara online
- ✅ Dekripsi script secara online  
- ✅ Copy to clipboard
- ✅ Download hasil sebagai file

### 4. File Creator

```bash
python3 file_creator.py
```

Template yang tersedia:
- 📄 Basic Script - Script Python sederhana
- 🔄 Interactive Script - Script dengan input user
- 🌐 Web Server - HTTP server sederhana
- 🔌 API Client - Client untuk API calls
- 🏗️ Class Template - Template class OOP
- ⚙️ Command Line Tool - CLI dengan argparse

## 📁 Struktur Project

```
dusk_cipher/
├── dusk_cipher.py          # Main interactive tool
├── pyobfuscator.py         # Command-line obfuscator
├── pydecoder.py           # Command-line decoder
├── web_obfuscator.py      # Web interface
├── file_creator.py        # Advanced file creator
├── install.sh             # Installation script
├── examples/
│   └── sample.py          # Sample Python file
├── README.md              # Documentation
└── .gitignore            # Git ignore rules
```

## 🔧 Contoh Penggunaan

### Enkripsi Script

**File Asli (hello.py):**
```python
#!/usr/bin/env python3
print("Hello, World!")
name = input("Enter your name: ")
print(f"Hello, {name}!")
```

**Hasil Enkripsi (hello_encrypted.py):**
```python
#!/usr/bin/env python3
import base64
unknownkcc = """IyEvdXNyL2Jpbi9lbnYgcHl0aG9uMwpwcmludCgiSGVsbG8sIFdvcmxkISIpCm5hbWUgPSBpbnB1dCgiRW50ZXIgeW91ciBuYW1lOiAiKQpwcmludChmIkhlbGxvLCB7bmFtZX0hIik="""
eval(compile(base64.b64decode(unknownkcc), "<string>", "exec"))
```

### Batch Operations

```bash
# Enkripsi semua file .py di directory
python3 dusk_cipher.py
# Pilih option 5 (Batch Operations)
# Pilih "encrypt"
# Masukkan pattern "*.py"
```

## 🛡️ Keamanan

⚠️ **Penting:** Tool ini menggunakan base64 encoding untuk obfuscation, **BUKAN** enkripsi kriptografis yang sesungguhnya. Base64 dapat dengan mudah di-decode oleh siapa saja yang memahami encoding ini.

**Gunakan untuk:**
- ✅ Obfuscate kode untuk menghindari casual reading
- ✅ Menyembunyikan logic bisnis dari user umum
- ✅ Proteksi sederhana terhadap reverse engineering

**JANGAN gunakan untuk:**
- ❌ Menyimpan password atau data sensitif
- ❌ Keamanan tingkat production yang kritis
- ❌ Proteksi terhadap security expert

## 🔍 Troubleshooting

### Error: "Module not found"
```bash
# Install ulang Python packages
pip3 install --upgrade pip
pip3 install requests urllib3
```

### Error: "Permission denied"
```bash
# Set permissions
chmod +x *.py
chmod +x install.sh
```

### Error: "Cannot bind to port 5000"
```bash
# Gunakan port lain untuk web interface
python3 web_obfuscator.py -p 8080
```

### Error: "Python version too old"
```bash
# Check Python version
python3 --version
# Upgrade ke Python 3.6 atau lebih baru
```

## 📊 Statistik Penggunaan

Tool ini menyimpan statistik penggunaan di file `.dusk_stats.json`:
```json
{
  "total_runs": 42,
  "last_run": "2024-01-15T10:30:00"
}
```

Lihat statistik dengan menu option 7 di mode interaktif.

## 🤝 Contributing

1. Fork project ini
2. Buat feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push ke branch (`git push origin feature/amazing-feature`)
5. Buat Pull Request

## 📝 Changelog

### Version 3.0
- ✅ Interactive mode dengan menu lengkap
- ✅ Web interface yang responsive
- ✅ Advanced file creator dengan templates
- ✅ Batch operations untuk multiple files
- ✅ File analyzer dan statistics
- ✅ Improved error handling
- ✅ Cross-platform compatibility

### Version 2.0
- ✅ Command-line tools
- ✅ Basic web interface
- ✅ Dekripsi functionality

### Version 1.0
- ✅ Basic enkripsi dengan base64
- ✅ Simple CLI interface

## 📜 License

Distributed under the MIT License. See `LICENSE` file for more information.

## 👨‍💻 Author

**DuskCipher Community**
- 🌐 Platform: Linux x86_64
- 📧 Support: [Create an issue](https://github.com/yourusername/dusk_cipher/issues)

## ⭐ Support

Jika tool ini berguna untuk Anda, berikan ⭐ star di repository ini!

---

**Made with ❤️ by DuskCipher Community**

*Happy coding and stay secure! 🔐*
