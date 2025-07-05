#!/usr/bin/env python3
"""
DUSK CIPHER - Professional Encryption Toolkit v3.0
Advanced Script Protection & Obfuscation System
"""

import os
import sys
import base64
import argparse
import pathlib
import re
import time
import json
from typing import List, Optional
from datetime import datetime


class Colors:
    """Terminal color codes for styling"""
    CYAN = '\033[96m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    WHITE = '\033[97m'
    GRAY = '\033[90m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

    # Background colors
    BG_DARK = '\033[100m'
    BG_CYAN = '\033[106m'
    BG_YELLOW = '\033[103m'


class DuskCipher:
    """Main class for the DUSK CIPHER encryption toolkit"""

    def __init__(self):
        self.version = "3.0"
        self.author = "DuskCipher"
        self.community = "DuskCipher"
        self.platform = "Linux x86_64"
        self.total_runs = self.get_total_runs()
        self.status = "Active & Secure"
        self.supported_extensions = ['.py', '.pyw']
        self.obfuscated_suffix = '_encrypted'
        self.decoded_suffix = '_decrypted'

    def get_total_runs(self):
        """Get total runs from stats file"""
        stats_file = ".dusk_stats.json"
        try:
            if os.path.exists(stats_file):
                with open(stats_file, 'r') as f:
                    data = json.load(f)
                    return data.get('total_runs', 0)
        except:
            pass
        return 0

    def update_stats(self):
        """Update statistics"""
        stats_file = ".dusk_stats.json"
        try:
            data = {
                'total_runs': self.total_runs + 1,
                'last_run': datetime.now().isoformat()
            }
            with open(stats_file, 'w') as f:
                json.dump(data, f)
        except:
            pass

    def print_banner(self):
        """Display the professional banner"""
        print(f"\n{Colors.CYAN}{'╔' + '═' * 68 + '╗'}{Colors.END}")
        print(
            f"{Colors.CYAN}║{Colors.END}{Colors.MAGENTA}{Colors.BOLD}{'DUSK CIPHER':^68}{Colors.END}{Colors.CYAN}║{Colors.END}"
        )
        print(
            f"{Colors.CYAN}║{Colors.YELLOW}{'Professional Encryption Toolkit v' + self.version:^68}{Colors.END}{Colors.CYAN}║{Colors.END}"
        )
        print(
            f"{Colors.CYAN}║{Colors.GRAY}{'Advanced Script Protection System':^68}{Colors.END}{Colors.CYAN}║{Colors.END}"
        )
        print(f"{Colors.CYAN}{'╠' + '═' * 68 + '╣'}{Colors.END}")

        # Simplified info display
        print(
            f"{Colors.CYAN}║{Colors.END} {Colors.GRAY}Version: {Colors.GREEN}v{self.version}{Colors.GRAY} │Runs: {Colors.GREEN}{self.total_runs}{Colors.GRAY} │             Status: {Colors.GREEN}{self.status[:15]:<15}{Colors.CYAN}      ║{Colors.END}"
        )
        print(
            f"{Colors.CYAN}║{Colors.END} {Colors.GRAY}Platform: {Colors.YELLOW}{self.platform[:30]:<30}{Colors.GRAY} │ Author: {Colors.YELLOW}{self.author}{Colors.GRAY}{' ' * (10-len(self.author))}{Colors.CYAN}       ║{Colors.END}"
        )

        print(f"{Colors.CYAN}{'╚' + '═' * 68 + '╝'}{Colors.END}")

        # Welcome message
        print(
            f"\n{Colors.GREEN}🚀 Welcome to DUSK CIPHER Encryption Toolkit!{Colors.END}"
        )
        print(
            f"{Colors.GRAY}   Select an operation from the menu below to get started{Colors.END}"
        )

    def print_operations_menu(self):
        """Display the operations menu"""
        print(f"\n{Colors.CYAN}{'╔' + '═' * 68 + '╗'}{Colors.END}")
        print(
            f"{Colors.CYAN}║{Colors.YELLOW}{Colors.BOLD}{'🔐 OPERATIONS MENU 🔐':^66}{Colors.END}{Colors.CYAN}║{Colors.END}"
        )
        print(f"{Colors.CYAN}{'╠' + '═' * 68 + '╣'}{Colors.END}")

        operations = [("[1] 🔒 Encrypt Script", "Protect Python files"),
                      ("[2] 🔓 Decrypt Script", "Restore encrypted files"),
                      ("[3] 📝 Create New File", "Build Python scripts"),
                      ("[4] 📁 File Analyzer", "Analyze file details"),
                      ("[5] 🔄 Batch Operations", "Process multiple files"),
                      ("[6] 🛡️  Security Scanner", " Security analysis"),
                      ("[7] 📊 Usage Statistics", "View usage logs"),
                      ("[8] ⚙️  System Tools v01", "  Advanced utilities"),
                      ("[9] 🌐 Web Interface", "Launch web UI"),
                      ("[0] 🚪 Exit", "Close application")]

        for op, desc in operations:
            print(
                f"{Colors.CYAN}║{Colors.END} {Colors.WHITE}{op:<22}{Colors.GRAY} {desc:<40}{Colors.CYAN}   ║{Colors.END}"
            )

        print(f"{Colors.CYAN}{'╠' + '═' * 68 + '╣'}{Colors.END}")
        print(
            f"{Colors.CYAN}║{Colors.END} {Colors.GRAY}Files: {Colors.GREEN}{self.count_python_files()}{Colors.GRAY} | Status: {Colors.GREEN}Online{Colors.GRAY} | Ready for operations{Colors.GRAY}{' ' * 18}{Colors.CYAN} ║{Colors.END}"
        )
        print(f"{Colors.CYAN}{'╚' + '═' * 68 + '╝'}{Colors.END}")

    def count_python_files(self):
        """Count Python files in current directory"""
        try:
            count = len(
                [f for f in os.listdir('.') if f.endswith(('.py', '.pyw'))])
            return count
        except:
            return 0

    def get_user_choice(self):
        """Get user menu choice"""
        try:
            choice = input(
                f"\n{Colors.YELLOW}▶ Choose option [{Colors.CYAN}0-9{Colors.YELLOW}]: {Colors.END}"
            ).strip()
            return choice
        except KeyboardInterrupt:
            print(f"\n{Colors.RED}✗ Operation cancelled{Colors.END}")
            return "0"

    def encrypt_script(self, script_content: str) -> str:
        """Encrypt Python script content using base64"""
        try:
            script_bytes = script_content.encode('utf-8')
            encoded_bytes = base64.b64encode(script_bytes)
            return encoded_bytes.decode('ascii')
        except Exception as e:
            raise Exception(f"Encryption failed: {e}")

    def create_encrypted_script(self, encoded_content: str) -> str:
        """Create the encrypted Python script wrapper"""
        return f'''#!/usr/bin/env python3
import base64
unknownkcc = """{encoded_content}"""
eval(compile(base64.b64decode(unknownkcc), "<string>", "exec"))
'''

    def decrypt_script(self, encrypted_code: str) -> str:
        """Decrypt an encrypted Python script back to original"""
        base64_content = None

        # Pattern matching for various variable names
        pattern = r'(\w+)\s*=\s*"""([^"]+)"""'
        match = re.search(pattern, encrypted_code, re.DOTALL)

        if match:
            var_name = match.group(1)
            content = match.group(2).strip()
            if var_name in encrypted_code and 'base64.b64decode' in encrypted_code:
                base64_content = content

        if not base64_content:
            pattern = r"(\w+)\s*=\s*'([^']+)'"
            match = re.search(pattern, encrypted_code, re.DOTALL)
            if match:
                var_name = match.group(1)
                content = match.group(2).strip()
                if var_name in encrypted_code and 'base64.b64decode' in encrypted_code:
                    base64_content = content

        if not base64_content:
            pattern = r'base64\.b64decode\(["\']([^"\']+)["\']\)'
            match = re.search(pattern, encrypted_code)
            if match:
                base64_content = match.group(1).strip()

        if not base64_content:
            raise ValueError("Cannot find valid base64 content in the script")

        try:
            decoded_bytes = base64.b64decode(base64_content)
            original_script = decoded_bytes.decode('utf-8')
            return original_script
        except Exception as e:
            raise ValueError(f"Decryption failed: {str(e)}")

    def handle_encrypt_operation(self):
        """Handle encryption operation"""
        print(f"\n{Colors.CYAN}🔒 ENCRYPT SCRIPT OPERATION{Colors.END}")
        print(f"{Colors.MAGENTA}{'╔' + '═' * 48 + '╗'}{Colors.END}")
        print(
            f"{Colors.MAGENTA}║{Colors.YELLOW}{'  SCRIPT ENCRYPTION MODULE  ':^48}{Colors.MAGENTA}║{Colors.END}"
        )
        print(f"{Colors.MAGENTA}{'╚' + '═' * 48 + '╝'}{Colors.END}")

        # Show available files
        python_files = [
            f for f in os.listdir('.') if f.endswith(('.py', '.pyw'))
        ]
        if python_files:
            print(f"\n{Colors.GREEN}📁 File Python yang tersedia:{Colors.END}")
            for i, file in enumerate(python_files[:5], 1):
                print(f"{Colors.GRAY}  {i}. {file}{Colors.END}")
            if len(python_files) > 5:
                print(
                    f"{Colors.GRAY}  ... dan {len(python_files)-5} file lainnya{Colors.END}"
                )

        filename = input(
            f"\n{Colors.YELLOW}📝 Masukkan nama file Python: {Colors.END}"
        ).strip()

        if not filename:
            print(f"{Colors.RED}❌ Nama file tidak boleh kosong{Colors.END}")
            return

        try:
            if not os.path.exists(filename):
                print(
                    f"{Colors.RED}❌ File tidak ditemukan: {filename}{Colors.END}"
                )
                return

            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()

            print(
                f"\n{Colors.YELLOW}⏳ Sedang mengenkripsi script...{Colors.END}"
            )

            encoded_content = self.encrypt_script(content)
            encrypted_script = self.create_encrypted_script(encoded_content)

            print(f"{Colors.GRAY}   {'█' * 40} 100%{Colors.END}")

            base_name = pathlib.Path(filename).stem
            output_file = f"{base_name}{self.obfuscated_suffix}.py"

            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(encrypted_script)

            if os.name == 'posix':
                os.chmod(output_file, 0o755)

            print(f"\n{Colors.GREEN}✅ Enkripsi berhasil!{Colors.END}")
            print(f"{Colors.MAGENTA}┌{'─' * 50}┐{Colors.END}")
            print(
                f"{Colors.MAGENTA}│{Colors.END} {Colors.GRAY}Input File  : {Colors.CYAN}{filename:<34}{Colors.MAGENTA} │{Colors.END}"
            )
            print(
                f"{Colors.MAGENTA}│{Colors.END} {Colors.GRAY}Output File : {Colors.GREEN}{output_file:<34}{Colors.MAGENTA} │{Colors.END}"
            )
            print(
                f"{Colors.MAGENTA}│{Colors.END} {Colors.GRAY}Size        : {Colors.YELLOW}{len(encrypted_script)} bytes{Colors.GRAY}{' ' * (34-len(str(len(encrypted_script))+' bytes'))}{Colors.MAGENTA} │{Colors.END}"
            )
            print(f"{Colors.MAGENTA}└{'─' * 50}┘{Colors.END}")

        except Exception as e:
            print(f"{Colors.RED}❌ Enkripsi gagal: {e}{Colors.END}")

    def handle_decrypt_operation(self):
        """Handle decryption operation"""
        print(f"\n{Colors.CYAN}🔓 DECRYPT SCRIPT OPERATION{Colors.END}")
        print(f"{Colors.MAGENTA}{'╔' + '═' * 48 + '╗'}{Colors.END}")
        print(
            f"{Colors.MAGENTA}║{Colors.YELLOW}{'  SCRIPT DECRYPTION MODULE  ':^48}{Colors.MAGENTA}║{Colors.END}"
        )
        print(f"{Colors.MAGENTA}{'╚' + '═' * 48 + '╝'}{Colors.END}")

        # Show encrypted files
        encrypted_files = [
            f for f in os.listdir('.')
            if '_encrypted' in f and f.endswith('.py')
        ]
        if encrypted_files:
            print(
                f"\n{Colors.GREEN}🔐 File terenkripsi yang tersedia:{Colors.END}"
            )
            for i, file in enumerate(encrypted_files[:5], 1):
                print(f"{Colors.GRAY}  {i}. {file}{Colors.END}")
            if len(encrypted_files) > 5:
                print(
                    f"{Colors.GRAY}  ... dan {len(encrypted_files)-5} file lainnya{Colors.END}"
                )

        filename = input(
            f"\n{Colors.YELLOW}📝 Masukkan nama file terenkripsi: {Colors.END}"
        ).strip()

        if not filename:
            print(f"{Colors.RED}❌ Nama file tidak boleh kosong{Colors.END}")
            return

        try:
            if not os.path.exists(filename):
                print(
                    f"{Colors.RED}❌ File tidak ditemukan: {filename}{Colors.END}"
                )
                return

            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()

            print(
                f"\n{Colors.YELLOW}⏳ Sedang mendekripsi script...{Colors.END}")

            decrypted_content = self.decrypt_script(content)

            print(f"{Colors.GRAY}   {'█' * 40} 100%{Colors.END}")

            base_name = pathlib.Path(filename).stem
            if base_name.endswith('_encrypted'):
                base_name = base_name[:-10]  # Remove '_encrypted'
            output_file = f"{base_name}{self.decoded_suffix}.py"

            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(decrypted_content)

            if os.name == 'posix':
                os.chmod(output_file, 0o755)

            print(f"\n{Colors.GREEN}✅ Dekripsi berhasil!{Colors.END}")
            print(f"{Colors.MAGENTA}┌{'─' * 50}┐{Colors.END}")
            print(
                f"{Colors.MAGENTA}│{Colors.END} {Colors.GRAY}Input File  : {Colors.CYAN}{filename:<34}{Colors.MAGENTA} │{Colors.END}"
            )
            print(
                f"{Colors.MAGENTA}│{Colors.END} {Colors.GRAY}Output File : {Colors.GREEN}{output_file:<34}{Colors.MAGENTA} │{Colors.END}"
            )
            print(
                f"{Colors.MAGENTA}│{Colors.END} {Colors.GRAY}Size        : {Colors.YELLOW}{len(decrypted_content)} bytes{Colors.GRAY}{' ' * (34-len(str(len(decrypted_content))+' bytes'))}{Colors.MAGENTA} │{Colors.END}"
            )
            print(f"{Colors.MAGENTA}└{'─' * 50}┘{Colors.END}")

        except Exception as e:
            print(f"{Colors.RED}❌ Dekripsi gagal: {e}{Colors.END}")

    def handle_batch_operations(self):
        """Handle batch operations"""
        print(f"\n{Colors.CYAN}🔄 BATCH OPERATIONS{Colors.END}")
        print(f"{Colors.GRAY}{'─' * 40}{Colors.END}")

        operation = input(
            f"{Colors.YELLOW}Choose operation (encrypt/decrypt): {Colors.END}"
        ).strip().lower()

        if operation not in ['encrypt', 'decrypt']:
            print(f"{Colors.RED}❌ Invalid operation{Colors.END}")
            return

        pattern = input(
            f"{Colors.YELLOW}Enter file pattern (e.g., *.py): {Colors.END}"
        ).strip()

        if not pattern:
            pattern = "*.py"

        try:
            import glob
            files = glob.glob(pattern)

            if not files:
                print(
                    f"{Colors.RED}❌ No files found matching pattern: {pattern}{Colors.END}"
                )
                return

            print(
                f"{Colors.GREEN}Found {len(files)} files to process{Colors.END}"
            )

            success_count = 0
            for file in files:
                try:
                    if operation == 'encrypt':
                        with open(file, 'r', encoding='utf-8') as f:
                            content = f.read()
                        encoded_content = self.encrypt_script(content)
                        encrypted_script = self.create_encrypted_script(
                            encoded_content)
                        base_name = pathlib.Path(file).stem
                        output_file = f"{base_name}{self.obfuscated_suffix}.py"
                        with open(output_file, 'w', encoding='utf-8') as f:
                            f.write(encrypted_script)
                    else:  # decrypt
                        with open(file, 'r', encoding='utf-8') as f:
                            content = f.read()
                        decrypted_content = self.decrypt_script(content)
                        base_name = pathlib.Path(file).stem
                        if base_name.endswith('_encrypted'):
                            base_name = base_name[:-10]
                        output_file = f"{base_name}{self.decoded_suffix}.py"
                        with open(output_file, 'w', encoding='utf-8') as f:
                            f.write(decrypted_content)

                    print(f"{Colors.GREEN}✅ Processed: {file}{Colors.END}")
                    success_count += 1

                except Exception as e:
                    print(f"{Colors.RED}❌ Failed: {file} - {e}{Colors.END}")

            print(
                f"\n{Colors.CYAN}Batch operation completed: {success_count}/{len(files)} files processed{Colors.END}"
            )

        except Exception as e:
            print(f"{Colors.RED}❌ Batch operation failed: {e}{Colors.END}")

    def handle_web_interface(self):
        """Launch web interface"""
        print(f"\n{Colors.CYAN}🌐 LAUNCHING WEB INTERFACE{Colors.END}")
        print(f"{Colors.GRAY}{'─' * 40}{Colors.END}")

        try:
            import subprocess
            print(f"{Colors.YELLOW}⏳ Starting web server...{Colors.END}")
            print(
                f"{Colors.GREEN}🌐 Web interface will be available at: http://localhost:5000{Colors.END}"
            )
            print(
                f"{Colors.YELLOW}Press Ctrl+C to return to main menu{Colors.END}"
            )

            # Run the web interface
            subprocess.run([sys.executable, "web_obfuscator.py"], check=True)

        except KeyboardInterrupt:
            print(f"\n{Colors.YELLOW}Web interface stopped{Colors.END}")
        except Exception as e:
            print(
                f"{Colors.RED}❌ Failed to start web interface: {e}{Colors.END}"
            )

    def handle_file_analyzer(self):
        """File analyzer operation"""
        print(f"\n{Colors.CYAN}📁 FILE ANALYZER{Colors.END}")
        print(f"{Colors.GRAY}{'─' * 40}{Colors.END}")

        filename = input(
            f"{Colors.YELLOW}Enter file name to analyze: {Colors.END}").strip(
            )

        if not filename or not os.path.exists(filename):
            print(f"{Colors.RED}❌ File not found{Colors.END}")
            return

        try:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()

            file_size = os.path.getsize(filename)
            line_count = len(content.splitlines())
            char_count = len(content)

            # Check if encrypted
            is_encrypted = 'base64.b64decode' in content and (
                'unknownkcc' in content or 'unknownkece' in content)

            print(f"{Colors.GREEN}📊 File Analysis Results:{Colors.END}")
            print(
                f"{Colors.GRAY}• File Size    : {Colors.CYAN}{file_size} bytes{Colors.END}"
            )
            print(
                f"{Colors.GRAY}• Lines        : {Colors.CYAN}{line_count}{Colors.END}"
            )
            print(
                f"{Colors.GRAY}• Characters   : {Colors.CYAN}{char_count}{Colors.END}"
            )
            print(
                f"{Colors.GRAY}• Status       : {Colors.YELLOW}{'Encrypted' if is_encrypted else 'Plain Text'}{Colors.END}"
            )
            print(
                f"{Colors.GRAY}• Type         : {Colors.CYAN}Python Script{Colors.END}"
            )

        except Exception as e:
            print(f"{Colors.RED}❌ Analysis failed: {e}{Colors.END}")

    def handle_create_file(self):
        """Handle file creation with advanced options"""
        print(f"\n{Colors.CYAN}📝 CREATE NEW PYTHON FILE{Colors.END}")
        print(f"{Colors.MAGENTA}{'╔' + '═' * 58 + '╗'}{Colors.END}")
        print(
            f"{Colors.MAGENTA}║{Colors.YELLOW}{'  ADVANCED PYTHON FILE CREATOR  ':^58}{Colors.MAGENTA}║{Colors.END}"
        )
        print(f"{Colors.MAGENTA}{'╚' + '═' * 58 + '╝'}{Colors.END}")

        choice = input(
            f"\n{Colors.YELLOW}Choose editor mode:{Colors.END}\n"
            f"{Colors.CYAN}[1]{Colors.END} Simple Editor (dalam DUSK CIPHER)\n"
            f"{Colors.CYAN}[2]{Colors.END} Nano Editor (external)\n"
            f"{Colors.CYAN}[3]{Colors.END} Advanced Creator (script terpisah)\n"
            f"{Colors.YELLOW}Pilihan [1-3]: {Colors.END}").strip()

        if choice == '2':
            self.handle_nano_editor()
            return
        elif choice == '3':
            try:
                import subprocess
                print(
                    f"\n{Colors.GREEN}🚀 Membuka Advanced File Creator...{Colors.END}"
                )
                subprocess.run([sys.executable, "file_creator.py"])
                return
            except Exception as e:
                print(
                    f"{Colors.RED}❌ Gagal membuka Advanced Creator: {e}{Colors.END}"
                )
                print(
                    f"{Colors.YELLOW}💡 Menggunakan Simple Editor sebagai fallback{Colors.END}"
                )

        # Simple Editor (option 1 or fallback)
        # Get filename
        filename = input(
            f"\n{Colors.YELLOW}📝 Masukkan nama file (tanpa .py): {Colors.END}"
        ).strip()

        if not filename:
            print(f"{Colors.RED}❌ Nama file tidak boleh kosong{Colors.END}")
            return

        if not filename.endswith('.py'):
            filename += '.py'

        if os.path.exists(filename):
            overwrite = input(
                f"{Colors.YELLOW}⚠️  File {filename} sudah ada. Timpa? (y/n): {Colors.END}"
            ).strip().lower()
            if overwrite != 'y':
                print(f"{Colors.YELLOW}⏹️  Operasi dibatalkan{Colors.END}")
                return

        print(f"\n{Colors.GREEN}📝 Simple Python Editor{Colors.END}")
        print(f"{Colors.MAGENTA}{'┌' + '─' * 58 + '┐'}{Colors.END}")
        print(
            f"{Colors.MAGENTA}│{Colors.END} {Colors.YELLOW}💡 Commands:{Colors.GRAY}{' ' * 45}{Colors.MAGENTA}│{Colors.END}"
        )
        print(
            f"{Colors.MAGENTA}│{Colors.END} {Colors.GRAY}• SAVE     - Simpan dan keluar{Colors.GRAY}{' ' * 27}{Colors.MAGENTA}│{Colors.END}"
        )
        print(
            f"{Colors.MAGENTA}│{Colors.END} {Colors.GRAY}• CANCEL   - Batalkan editor{Colors.GRAY}{' ' * 29}{Colors.MAGENTA}│{Colors.END}"
        )
        print(
            f"{Colors.MAGENTA}│{Colors.END} {Colors.GRAY}• TEMPLATE - Gunakan template{Colors.GRAY}{' ' * 28}{Colors.MAGENTA}│{Colors.END}"
        )
        print(
            f"{Colors.MAGENTA}│{Colors.END} {Colors.GRAY}• SHOW     - Tampilkan kode saat ini{Colors.GRAY}{' ' * 21}{Colors.MAGENTA}│{Colors.END}"
        )
        print(f"{Colors.MAGENTA}{'└' + '─' * 58 + '┘'}{Colors.END}")

        lines = []
        line_number = 1

        while True:
            try:
                user_input = input(
                    f"{Colors.CYAN}{line_number:3d}:{Colors.END} ")

                if user_input.upper() == 'SAVE':
                    break
                elif user_input.upper() == 'CANCEL':
                    print(f"{Colors.YELLOW}⏹️  Editor dibatalkan{Colors.END}")
                    return
                elif user_input.upper() == 'SHOW':
                    print(f"\n{Colors.GREEN}📄 Current content:{Colors.END}")
                    for i, line in enumerate(lines, 1):
                        print(f"{Colors.GRAY}{i:3d}: {line}{Colors.END}")
                    print()
                    continue
                elif user_input.upper() == 'TEMPLATE':
                    template_choice = input(
                        f"\n{Colors.YELLOW}Template options:{Colors.END}\n"
                        f"{Colors.CYAN}[1]{Colors.END} Basic Script\n"
                        f"{Colors.CYAN}[2]{Colors.END} Interactive Script\n"
                        f"{Colors.CYAN}[3]{Colors.END} Web Server\n"
                        f"{Colors.YELLOW}Pilih [1-3]: {Colors.END}").strip()
                    template = self.get_template(template_choice, filename)
                    lines.extend(template.split('\n'))
                    line_number += len(template.split('\n'))
                    baris_template = len(template.split('\n'))
                    print(
                        f"{Colors.GREEN}✅ Template ditambahkan ({baris_template} baris){Colors.END}"
                    )
                    continue
                else:
                    lines.append(user_input)
                    line_number += 1

            except KeyboardInterrupt:
                print(
                    f"\n{Colors.YELLOW}⏹️  Editor dibatalkan dengan Ctrl+C{Colors.END}"
                )
                return

        # Save file
        try:
            content = '\n'.join(lines)
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)

            # Make executable on Unix systems
            if os.name == 'posix':
                os.chmod(filename, 0o755)

            file_size = len(content.encode('utf-8'))

            print(f"\n{Colors.GREEN}✅ File berhasil dibuat!{Colors.END}")
            print(f"{Colors.MAGENTA}{'┌' + '─' * 40 + '┐'}{Colors.END}")
            print(
                f"{Colors.MAGENTA}│{Colors.END} {Colors.GRAY}Filename : {Colors.CYAN}{filename:<27}{Colors.MAGENTA} │{Colors.END}"
            )
            print(
                f"{Colors.MAGENTA}│{Colors.END} {Colors.GRAY}Lines    : {Colors.YELLOW}{len(lines)}{Colors.GRAY}{' ' * (27-len(str(len(lines))))}{Colors.MAGENTA} │{Colors.END}"
            )
            print(
                f"{Colors.MAGENTA}│{Colors.END} {Colors.GRAY}Size     : {Colors.GREEN}{file_size} bytes{Colors.GRAY}{' ' * (27-len(str(file_size)+' bytes'))}{Colors.MAGENTA} │{Colors.END}"
            )
            print(f"{Colors.MAGENTA}{'└' + '─' * 40 + '┘'}{Colors.END}")

            # Ask if user wants to run the file
            run_choice = input(
                f"\n{Colors.YELLOW}🚀 Jalankan file sekarang? (y/n): {Colors.END}"
            ).strip().lower()
            if run_choice == 'y':
                print(f"\n{Colors.CYAN}{'='*50}{Colors.END}")
                print(f"{Colors.YELLOW}🚀 Menjalankan {filename}:{Colors.END}")
                print(f"{Colors.CYAN}{'='*50}{Colors.END}")
                try:
                    import subprocess
                    result = subprocess.run([sys.executable, filename],
                                            timeout=30)
                except subprocess.TimeoutExpired:
                    print(
                        f"{Colors.YELLOW}⏰ Eksekusi dihentikan (timeout 30 detik){Colors.END}"
                    )
                except Exception as e:
                    print(
                        f"{Colors.RED}❌ Error menjalankan file: {e}{Colors.END}"
                    )
                print(f"{Colors.CYAN}{'='*50}{Colors.END}")

        except Exception as e:
            print(f"{Colors.RED}❌ Gagal menyimpan file: {e}{Colors.END}")

    def get_template(self, choice, filename="script"):
        """Get code template based on user choice"""
        script_name = pathlib.Path(filename).stem if filename else "script"
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        templates = {
            '1':
            f'''#!/usr/bin/env python3
"""
{script_name}.py - Basic Python Script
Created with DUSK CIPHER at {current_time}
"""

def main():
    """Main function"""
    print("Hello, World!")
    print("This is a basic Python script created with DUSK CIPHER.")
    print(f"Script name: {script_name}")
    
    # Your code here
    

if __name__ == "__main__":
    main()''',
            '2':
            f'''#!/usr/bin/env python3
"""
{script_name}.py - Interactive Python Script
Created with DUSK CIPHER at {current_time}
"""

import os
import sys
from datetime import datetime

def get_user_input():
    """Get user input with validation"""
    try:
        name = input("Enter your name: ").strip()
        if not name:
            print("Name cannot be empty!")
            return get_user_input()
        return name
    except KeyboardInterrupt:
        print("\\nOperation cancelled.")
        sys.exit(1)

def main():
    """Main function"""
    print("=" * 60)
    print(f"{{script_name.upper()}} - Interactive Python Script")
    print("Created with DUSK CIPHER")
    print("=" * 60)
    
    name = get_user_input()
    print(f"\\nHello, {{name}}! Welcome to {script_name}!")
    
    print(f"\\nSystem Information:")
    print(f"• Current time: {{datetime.now()}}")
    print(f"• Python version: {{sys.version_info.major}}.{{sys.version_info.minor}}")
    print(f"• Platform: {{os.name}}")
    
    print("\\n✅ Script completed successfully!")

if __name__ == "__main__":
    main()''',
            '3':
            f'''#!/usr/bin/env python3
"""
{script_name}.py - Simple Web Server
Created with DUSK CIPHER at {current_time}
"""

from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
import sys

class CustomHandler(SimpleHTTPRequestHandler):
    """Custom HTTP request handler"""
    
    def log_message(self, format, *args):
        """Override default logging"""
        print(f"[{{self.log_date_time_string()}}] {{format % args}}")

def run_server(port=8000):
    """Run the HTTP server"""
    try:
        server_address = ('0.0.0.0', port)
        httpd = HTTPServer(server_address, CustomHandler)
        
        print("=" * 50)
        print(f"{{script_name.upper()}} - Web Server")
        print("Created with DUSK CIPHER")
        print("=" * 50)
        print(f"🌐 Server running at http://localhost:{{port}}")
        print(f"📁 Serving directory: {{os.getcwd()}}")
        print("⏹️  Press Ctrl+C to stop server")
        print("-" * 50)
        
        httpd.serve_forever()
        
    except KeyboardInterrupt:
        print("\\n⏹️  Server stopped by user")
        httpd.shutdown()
    except Exception as e:
        print(f"❌ Error: {{e}}")

if __name__ == "__main__":
    port = 8000
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print("❌ Invalid port number")
            sys.exit(1)
    
    run_server(port)'''
        }

        return templates.get(choice, templates['1'])

    def handle_nano_editor(self):
        """Handle file creation using nano editor"""
        print(f"\n{Colors.CYAN}📝 NANO EDITOR MODE{Colors.END}")
        print(f"{Colors.MAGENTA}{'╔' + '═' * 48 + '╗'}{Colors.END}")
        print(
            f"{Colors.MAGENTA}║{Colors.YELLOW}{'  NANO EDITOR INTEGRATION  ':^48}{Colors.MAGENTA}║{Colors.END}"
        )
        print(f"{Colors.MAGENTA}{'╚' + '═' * 48 + '╝'}{Colors.END}")

        # Get filename
        filename = input(
            f"\n{Colors.YELLOW}📝 Masukkan nama file (tanpa .py): {Colors.END}"
        ).strip()

        if not filename:
            print(f"{Colors.RED}❌ Nama file tidak boleh kosong{Colors.END}")
            return

        if not filename.endswith('.py'):
            filename += '.py'

        if os.path.exists(filename):
            overwrite = input(
                f"{Colors.YELLOW}⚠️  File {filename} sudah ada. Timpa? (y/n): {Colors.END}"
            ).strip().lower()
            if overwrite != 'y':
                print(f"{Colors.YELLOW}⏹️  Operasi dibatalkan{Colors.END}")
                return

        # Ask for template
        template_choice = input(
            f"\n{Colors.YELLOW}Template options:{Colors.END}\n"
            f"{Colors.CYAN}[1]{Colors.END} Basic Script\n"
            f"{Colors.CYAN}[2]{Colors.END} Interactive Script\n"
            f"{Colors.CYAN}[3]{Colors.END} Web Server\n"
            f"{Colors.CYAN}[0]{Colors.END} Empty File\n"
            f"{Colors.YELLOW}Pilih [0-3]: {Colors.END}").strip()

        # Create initial content
        if template_choice != '0':
            template = self.get_template(template_choice, filename)
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(template)
                print(
                    f"{Colors.GREEN}✅ Template ditambahkan ke {filename}{Colors.END}"
                )
            except Exception as e:
                print(f"{Colors.RED}❌ Gagal membuat template: {e}{Colors.END}")
                return
        else:
            # Create empty file
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write('')
                print(
                    f"{Colors.GREEN}✅ File kosong {filename} dibuat{Colors.END}"
                )
            except Exception as e:
                print(f"{Colors.RED}❌ Gagal membuat file: {e}{Colors.END}")
                return

        # Launch nano editor
        print(
            f"\n{Colors.GREEN}🚀 Membuka nano editor untuk {filename}...{Colors.END}"
        )
        print(
            f"{Colors.GRAY}💡 Gunakan Ctrl+X untuk save dan keluar dari nano{Colors.END}"
        )
        print(
            f"{Colors.GRAY}💡 Setelah save, Anda akan kembali ke DUSK CIPHER{Colors.END}"
        )

        input(
            f"\n{Colors.YELLOW}Tekan Enter untuk membuka nano...{Colors.END}")

        try:
            import subprocess
            # Launch nano editor
            result = subprocess.run(['nano', filename], check=True)

            # Check if file was saved and has content
            if os.path.exists(filename):
                file_size = os.path.getsize(filename)
                with open(filename, 'r', encoding='utf-8') as f:
                    content = f.read()
                line_count = len(content.splitlines())

                print(f"\n{Colors.GREEN}✅ File berhasil disimpan!{Colors.END}")
                print(f"{Colors.MAGENTA}{'┌' + '─' * 38 + '┐'}{Colors.END}")
                print(
                    f"{Colors.MAGENTA}│{Colors.END} {Colors.GRAY}Filename : {Colors.CYAN}{filename:<25}{Colors.MAGENTA} │{Colors.END}"
                )
                print(
                    f"{Colors.MAGENTA}│{Colors.END} {Colors.GRAY}Size     : {Colors.YELLOW}{file_size} bytes{Colors.GRAY}{' ' * (25-len(str(file_size)+' bytes'))}{Colors.MAGENTA} │{Colors.END}"
                )
                print(
                    f"{Colors.MAGENTA}│{Colors.END} {Colors.GRAY}Lines    : {Colors.GREEN}{line_count}{Colors.GRAY}{' ' * (25-len(str(line_count)))}{Colors.MAGENTA} │{Colors.END}"
                )
                print(f"{Colors.MAGENTA}{'└' + '─' * 38 + '┘'}{Colors.END}")

                # Make executable on Unix systems
                if os.name == 'posix':
                    os.chmod(filename, 0o755)

                # Ask if user wants to run the file
                run_choice = input(
                    f"\n{Colors.YELLOW}🚀 Jalankan file sekarang? (y/n): {Colors.END}"
                ).strip().lower()
                if run_choice == 'y':
                    print(f"\n{Colors.CYAN}{'='*50}{Colors.END}")
                    print(
                        f"{Colors.YELLOW}🚀 Menjalankan {filename}:{Colors.END}"
                    )
                    print(f"{Colors.CYAN}{'='*50}{Colors.END}")
                    try:
                        result = subprocess.run([sys.executable, filename],
                                                timeout=30)
                    except subprocess.TimeoutExpired:
                        print(
                            f"{Colors.YELLOW}⏰ Eksekusi dihentikan (timeout 30 detik){Colors.END}"
                        )
                    except Exception as e:
                        print(
                            f"{Colors.RED}❌ Error menjalankan file: {e}{Colors.END}"
                        )
                    print(f"{Colors.CYAN}{'='*50}{Colors.END}")
            else:
                print(
                    f"{Colors.YELLOW}⚠️  File tidak ditemukan setelah nano editor{Colors.END}"
                )

        except subprocess.CalledProcessError:
            print(f"{Colors.YELLOW}⏹️  Nano editor dibatalkan{Colors.END}")
        except FileNotFoundError:
            print(
                f"{Colors.RED}❌ Nano tidak tersedia di sistem ini{Colors.END}")
            print(
                f"{Colors.YELLOW}💡 Menggunakan Simple Editor sebagai fallback...{Colors.END}"
            )
            # Fallback to simple editor
            self.handle_simple_editor(filename)
        except Exception as e:
            print(f"{Colors.RED}❌ Error dengan nano editor: {e}{Colors.END}")

    def handle_simple_editor(self, filename=None):
        """Handle simple editor as fallback"""
        if not filename:
            filename = input(
                f"\n{Colors.YELLOW}📝 Masukkan nama file (tanpa .py): {Colors.END}"
            ).strip()
            if not filename:
                print(
                    f"{Colors.RED}❌ Nama file tidak boleh kosong{Colors.END}")
                return
            if not filename.endswith('.py'):
                filename += '.py'

        print(f"\n{Colors.GREEN}📝 Simple Python Editor{Colors.END}")
        print(f"{Colors.MAGENTA}{'┌' + '─' * 59 + '┐'}{Colors.END}")
        print(
            f"{Colors.MAGENTA}│{Colors.END} {Colors.YELLOW}💡 Commands:{Colors.GRAY}{' ' * 31}{Colors.MAGENTA}│{Colors.END}"
        )
        print(
            f"{Colors.MAGENTA}│{Colors.END} {Colors.GRAY}• SAVE     - Simpan dan keluar{Colors.GRAY}{' ' * 27}{Colors.MAGENTA}│{Colors.END}"
        )
        print(
            f"{Colors.MAGENTA}│{Colors.END} {Colors.GRAY}• CANCEL   - Batalkan editor{Colors.GRAY}{' ' * 28}{Colors.MAGENTA}│{Colors.END}"
        )
        print(
            f"{Colors.MAGENTA}│{Colors.END} {Colors.GRAY}• TEMPLATE - Gunakan template{Colors.GRAY}{' ' * 26}{Colors.MAGENTA}│{Colors.END}"
        )
        print(
            f"{Colors.MAGENTA}│{Colors.END} {Colors.GRAY}• SHOW     - Tampilkan kode saat ini{Colors.GRAY}{' ' * 21}{Colors.MAGENTA}│{Colors.END}"
        )
        print(f"{Colors.MAGENTA}{'└' + '─' * 56 + '┘'}{Colors.END}")

        lines = []
        line_number = 1

        while True:
            try:
                user_input = input(
                    f"{Colors.CYAN}{line_number:3d}:{Colors.END} ")

                if user_input.upper() == 'SAVE':
                    break
                elif user_input.upper() == 'CANCEL':
                    print(f"{Colors.YELLOW}⏹️  Editor dibatalkan{Colors.END}")
                    return
                elif user_input.upper() == 'SHOW':
                    print(f"\n{Colors.GREEN}📄 Current content:{Colors.END}")
                    for i, line in enumerate(lines, 1):
                        print(f"{Colors.GRAY}{i:3d}: {line}{Colors.END}")
                    print()
                    continue
                elif user_input.upper() == 'TEMPLATE':
                    template_choice = input(
                        f"\n{Colors.YELLOW}Template options:{Colors.END}\n"
                        f"{Colors.CYAN}[1]{Colors.END} Basic Script\n"
                        f"{Colors.CYAN}[2]{Colors.END} Interactive Script\n"
                        f"{Colors.CYAN}[3]{Colors.END} Web Server\n"
                        f"{Colors.YELLOW}Pilih [1-3]: {Colors.END}").strip()
                    template = self.get_template(template_choice, filename)
                    lines.extend(template.split('\n'))
                    line_number += len(template.split('\n'))
                    baris_template = len(template.split('\n'))
                    print(
                        f"{Colors.GREEN}✅ Template ditambahkan ({baris_template} baris){Colors.END}"
                    )
                    continue
                else:
                    lines.append(user_input)
                    line_number += 1

            except KeyboardInterrupt:
                print(
                    f"\n{Colors.YELLOW}⏹️  Editor dibatalkan dengan Ctrl+C{Colors.END}"
                )
                return

        # Save file
        try:
            content = '\n'.join(lines)
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)

            # Make executable on Unix systems
            if os.name == 'posix':
                os.chmod(filename, 0o755)

            file_size = len(content.encode('utf-8'))

            print(f"\n{Colors.GREEN}✅ File berhasil dibuat!{Colors.END}")
            print(f"{Colors.MAGENTA}{'┌' + '─' * 40 + '┐'}{Colors.END}")
            print(
                f"{Colors.MAGENTA}│{Colors.END} {Colors.GRAY}Filename : {Colors.CYAN}{filename:<25}{Colors.MAGENTA} │{Colors.END}"
            )
            print(
                f"{Colors.MAGENTA}│{Colors.END} {Colors.GRAY}Lines    : {Colors.YELLOW}{len(lines)}{Colors.GRAY}{' ' * (25-len(str(len(lines))))}{Colors.MAGENTA} │{Colors.END}"
            )
            print(
                f"{Colors.MAGENTA}│{Colors.END} {Colors.GRAY}Size     : {Colors.GREEN}{file_size} bytes{Colors.GRAY}{' ' * (25-len(str(file_size)+' bytes'))}{Colors.MAGENTA} │{Colors.END}"
            )
            print(f"{Colors.MAGENTA}{'└' + '─' * 40 + '┘'}{Colors.END}")

        except Exception as e:
            print(f"{Colors.RED}❌ Gagal menyimpan file: {e}{Colors.END}")

    def handle_usage_logs(self):
        """Display usage statistics"""
        print(f"\n{Colors.CYAN}📊 USAGE STATISTICS{Colors.END}")
        print(f"{Colors.MAGENTA}{'╔' + '═' * 48 + '╗'}{Colors.END}")
        print(
            f"{Colors.MAGENTA}║{Colors.YELLOW}{'  STATISTIK PENGGUNAAN  ':^48}{Colors.MAGENTA}║{Colors.END}"
        )
        print(f"{Colors.MAGENTA}{'╚' + '═' * 48 + '╝'}{Colors.END}")

        try:
            stats_file = ".dusk_stats.json"
            if os.path.exists(stats_file):
                with open(stats_file, 'r') as f:
                    data = json.load(f)

                print(f"\n{Colors.GREEN}📈 Laporan Statistik:{Colors.END}")
                print(f"{Colors.MAGENTA}┌{'─' * 40}┐{Colors.END}")
                print(
                    f"{Colors.MAGENTA}│{Colors.END} {Colors.GRAY}Total Runs   : {Colors.CYAN}{str(data.get('total_runs', 0)):>23}{Colors.MAGENTA} │{Colors.END}"
                )
                print(
                    f"{Colors.MAGENTA}│{Colors.END} {Colors.GRAY}Last Run     : {Colors.CYAN}{str(data.get('last_run', 'Never'))[:20]:>23}{Colors.MAGENTA} │{Colors.END}"
                )
                print(
                    f"{Colors.MAGENTA}│{Colors.END} {Colors.GRAY}Version      : {Colors.CYAN}{('v' + self.version):>23}{Colors.MAGENTA} │{Colors.END}"
                )
                print(
                    f"{Colors.MAGENTA}│{Colors.END} {Colors.GRAY}Platform     : {Colors.CYAN}{self.platform[:20]:>23}{Colors.MAGENTA} │{Colors.END}"
                )
                print(f"{Colors.MAGENTA}└{'─' * 40}┘{Colors.END}")
            else:
                print(
                    f"\n{Colors.YELLOW}💭 Belum ada statistik yang tersimpan{Colors.END}"
                )

        except Exception as e:
            print(f"\n{Colors.RED}❌ Gagal memuat statistik: {e}{Colors.END}")

    def run_interactive_mode(self):
        """Run the interactive mode"""
        os.system('clear' if os.name == 'posix' else 'cls')
        self.print_banner()
        self.update_stats()

        while True:
            self.print_operations_menu()
            choice = self.get_user_choice()

            if choice == "0":
                print(
                    f"\n{Colors.YELLOW}Thank you for using DUSK CIPHER!{Colors.END}"
                )
                print(f"{Colors.CYAN}Stay secure! 🔒{Colors.END}\n")
                break
            elif choice == "1":
                self.handle_encrypt_operation()
            elif choice == "2":
                self.handle_decrypt_operation()
            elif choice == "3":
                self.handle_create_file()
            elif choice == "4":
                self.handle_file_analyzer()
            elif choice == "5":
                self.handle_batch_operations()
            elif choice == "6":
                print(
                    f"\n{Colors.YELLOW}🛡️ Security scanner - Feature coming soon!{Colors.END}"
                )
            elif choice == "7":
                self.handle_usage_logs()
            elif choice == "8":
                print(
                    f"\n{Colors.YELLOW}⚙️ System tools - Feature coming soon!{Colors.END}"
                )
            elif choice == "9":
                self.handle_web_interface()
            else:
                print(
                    f"\n{Colors.RED}❌ Invalid choice. Please select 0-9{Colors.END}"
                )

            input(f"\n{Colors.GRAY}Press Enter to continue...{Colors.END}")
            # Clear screen after user presses enter
            os.system('clear' if os.name == 'posix' else 'cls')


def main():
    """Main function"""
    parser = argparse.ArgumentParser(
        description='DUSK CIPHER - Professional Encryption Toolkit',
        formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('--encrypt', '-e', help='Encrypt a Python file')

    parser.add_argument('--decrypt',
                        '-d',
                        help='Decrypt an encrypted Python file')

    parser.add_argument('--batch',
                        help='Batch process files (encrypt/decrypt)')

    parser.add_argument('--web',
                        action='store_true',
                        help='Launch web interface')

    parser.add_argument('--version',
                        action='version',
                        version='DUSK CIPHER v3.0')

    args = parser.parse_args()

    cipher = DuskCipher()

    # Handle command line arguments
    if args.encrypt:
        try:
            with open(args.encrypt, 'r', encoding='utf-8') as f:
                content = f.read()
            encoded_content = cipher.encrypt_script(content)
            encrypted_script = cipher.create_encrypted_script(encoded_content)
            base_name = pathlib.Path(args.encrypt).stem
            output_file = f"{base_name}{cipher.obfuscated_suffix}.py"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(encrypted_script)
            print(f"✅ Encrypted: {args.encrypt} -> {output_file}")
        except Exception as e:
            print(f"❌ Encryption failed: {e}")
        return

    if args.decrypt:
        try:
            with open(args.decrypt, 'r', encoding='utf-8') as f:
                content = f.read()
            decrypted_content = cipher.decrypt_script(content)
            base_name = pathlib.Path(args.decrypt).stem
            if base_name.endswith('_encrypted'):
                base_name = base_name[:-10]
            output_file = f"{base_name}{cipher.decoded_suffix}.py"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(decrypted_content)
            print(f"✅ Decrypted: {args.decrypt} -> {output_file}")
        except Exception as e:
            print(f"❌ Decryption failed: {e}")
        return

    if args.web:
        try:
            import subprocess
            subprocess.run([sys.executable, "web_obfuscator.py"])
        except Exception as e:
            print(f"❌ Failed to start web interface: {e}")
        return

    # Run interactive mode if no arguments
    if len(sys.argv) == 1:
        cipher.run_interactive_mode()
    else:
        parser.print_help()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}Operation cancelled by user{Colors.END}")
        sys.exit(1)
    except Exception as e:
        print(f"\n{Colors.RED}Error: {e}{Colors.END}")
        sys.exit(1)
