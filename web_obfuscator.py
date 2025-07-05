#!/usr/bin/env python3
"""
Web Interface for Python Script Obfuscator
A simple web interface for encoding Python scripts using base64.
"""

import base64
import html
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
import json
import os
import sys

class ObfuscatorWebHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Handle GET requests - serve the web interface"""
        if self.path == '/' or self.path == '/index.html':
            self.serve_homepage()
        elif self.path == '/style.css':
            self.serve_css()
        else:
            self.send_error(404)
    
    def do_POST(self):
        """Handle POST requests - process obfuscation"""
        if self.path == '/obfuscate':
            self.handle_obfuscation()
        elif self.path == '/deobfuscate':
            self.handle_deobfuscation()
        else:
            self.send_error(404)
    
    def serve_homepage(self):
        """Serve the main HTML page"""
        html_content = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Script Obfuscator</title>
    <link rel="stylesheet" href="/style.css">
</head>
<body>
    <div class="container">
        <h1>🐍 Python Script Obfuscator</h1>
        <p>Paste kode Python Anda di bawah ini dan klik tombol untuk encode:</p>
        
        <div class="tab-section">
            <div class="tab-buttons">
                <button onclick="showTab('encode')" id="encodeTab" class="tab-button active">🔒 Encode</button>
                <button onclick="showTab('decode')" id="decodeTab" class="tab-button">🔓 Decode</button>
            </div>
        </div>
        
        <div id="encodeSection" class="form-section tab-content active">
            <h2>📝 Masukkan Kode Python:</h2>
            <textarea id="inputCode" placeholder="Paste kode Python Anda di sini...

Contoh:
#!/usr/bin/env python3
print('Hello World!')
name = input('Masukkan nama: ')
print(f'Halo {name}!')"></textarea>
            
            <div class="button-section">
                <button onclick="obfuscateCode()" id="obfuscateBtn">🔒 Encode Script</button>
                <button onclick="clearEncode()" id="clearEncodeBtn">🗑️ Clear</button>
            </div>
            
            <h2>🔐 Hasil Encode:</h2>
            <textarea id="outputCode" readonly placeholder="Hasil encode akan muncul di sini..."></textarea>
            
            <div class="button-section">
                <button onclick="copyToClipboard('outputCode')" id="copyBtn" disabled>📋 Copy ke Clipboard</button>
                <button onclick="downloadFile('outputCode', 'obfuscated_script.py')" id="downloadBtn" disabled>💾 Download File</button>
            </div>
        </div>
        
        <div id="decodeSection" class="form-section tab-content">
            <h2>🔓 Masukkan Kode yang Sudah Di-encode:</h2>
            <textarea id="inputDecodeCode" placeholder="Paste kode yang sudah di-encode di sini...

Contoh:
#!/usr/bin/env python3
import base64
unknownkcc = \"\"\"cHJpbnQoJ0hlbGxvIFdvcmxkIScpCm5hbWUgPSBpbnB1dCgnTWFzdWtrYW4gbmFtYTogJykKcHJpbnQoZidIYWxvIHtuYW1lfSEnKQ==\"\"\"
eval(compile(base64.b64decode(unknownkcc), \"<string>\", \"exec\"))"></textarea>
            
            <div class="button-section">
                <button onclick="deobfuscateCode()" id="deobfuscateBtn">🔓 Decode Script</button>
                <button onclick="clearDecode()" id="clearDecodeBtn">🗑️ Clear</button>
            </div>
            
            <h2>📜 Hasil Decode:</h2>
            <textarea id="outputDecodeCode" readonly placeholder="Hasil decode akan muncul di sini..."></textarea>
            
            <div class="button-section">
                <button onclick="copyToClipboard('outputDecodeCode')" id="copyDecodeBtn" disabled>📋 Copy ke Clipboard</button>
                <button onclick="downloadFile('outputDecodeCode', 'decoded_script.py')" id="downloadDecodeBtn" disabled>💾 Download File</button>
            </div>
        </div>
        
        <div class="info-section">
            <h3>ℹ️ Cara Menggunakan:</h3>
            <div class="info-tabs">
                <div class="info-tab active" id="encodeInfo">
                    <h4>🔒 Encode (Obfuscate):</h4>
                    <ol>
                        <li>Pilih tab "Encode"</li>
                        <li>Paste kode Python Anda di kotak atas</li>
                        <li>Klik tombol "Encode Script"</li>
                        <li>Copy hasil encode atau download sebagai file</li>
                        <li>File hasil encode bisa dijalankan normal seperti script asli</li>
                    </ol>
                </div>
                <div class="info-tab" id="decodeInfo">
                    <h4>🔓 Decode (Deobfuscate):</h4>
                    <ol>
                        <li>Pilih tab "Decode"</li>
                        <li>Paste kode yang sudah di-encode di kotak atas</li>
                        <li>Klik tombol "Decode Script"</li>
                        <li>Copy hasil decode atau download sebagai file</li>
                        <li>Hasil decode akan menampilkan kode Python asli</li>
                    </ol>
                </div>
            </div>
        </div>
    </div>

    <script>
        // Tab functionality
        function showTab(tabName) {
            // Hide all tab contents
            const tabContents = document.querySelectorAll('.tab-content');
            tabContents.forEach(content => content.classList.remove('active'));
            
            // Hide all tab buttons
            const tabButtons = document.querySelectorAll('.tab-button');
            tabButtons.forEach(button => button.classList.remove('active'));
            
            // Show selected tab
            document.getElementById(tabName + 'Section').classList.add('active');
            document.getElementById(tabName + 'Tab').classList.add('active');
            
            // Update info section
            const infoTabs = document.querySelectorAll('.info-tab');
            infoTabs.forEach(tab => tab.classList.remove('active'));
            document.getElementById(tabName + 'Info').classList.add('active');
        }
        
        async function obfuscateCode() {
            const inputCode = document.getElementById('inputCode').value.trim();
            const outputCode = document.getElementById('outputCode');
            const obfuscateBtn = document.getElementById('obfuscateBtn');
            const copyBtn = document.getElementById('copyBtn');
            const downloadBtn = document.getElementById('downloadBtn');
            
            if (!inputCode) {
                alert('Silakan masukkan kode Python terlebih dahulu!');
                return;
            }
            
            obfuscateBtn.disabled = true;
            obfuscateBtn.textContent = '⏳ Encoding...';
            
            try {
                const response = await fetch('/obfuscate', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ code: inputCode })
                });
                
                const result = await response.json();
                
                if (result.success) {
                    outputCode.value = result.obfuscated_code;
                    copyBtn.disabled = false;
                    downloadBtn.disabled = false;
                    alert('✅ Kode berhasil di-encode!');
                } else {
                    alert('❌ Error: ' + result.error);
                }
            } catch (error) {
                alert('❌ Terjadi kesalahan: ' + error.message);
            } finally {
                obfuscateBtn.disabled = false;
                obfuscateBtn.textContent = '🔒 Encode Script';
            }
        }
        
        async function deobfuscateCode() {
            const inputCode = document.getElementById('inputDecodeCode').value.trim();
            const outputCode = document.getElementById('outputDecodeCode');
            const deobfuscateBtn = document.getElementById('deobfuscateBtn');
            const copyBtn = document.getElementById('copyDecodeBtn');
            const downloadBtn = document.getElementById('downloadDecodeBtn');
            
            if (!inputCode) {
                alert('Silakan masukkan kode yang sudah di-encode terlebih dahulu!');
                return;
            }
            
            deobfuscateBtn.disabled = true;
            deobfuscateBtn.textContent = '⏳ Decoding...';
            
            try {
                const response = await fetch('/deobfuscate', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ code: inputCode })
                });
                
                const result = await response.json();
                
                if (result.success) {
                    outputCode.value = result.deobfuscated_code;
                    copyBtn.disabled = false;
                    downloadBtn.disabled = false;
                    alert('✅ Kode berhasil di-decode!');
                } else {
                    alert('❌ Error: ' + result.error);
                }
            } catch (error) {
                alert('❌ Terjadi kesalahan: ' + error.message);
            } finally {
                deobfuscateBtn.disabled = false;
                deobfuscateBtn.textContent = '🔓 Decode Script';
            }
        }
        
        function clearEncode() {
            document.getElementById('inputCode').value = '';
            document.getElementById('outputCode').value = '';
            document.getElementById('copyBtn').disabled = true;
            document.getElementById('downloadBtn').disabled = true;
        }
        
        function clearDecode() {
            document.getElementById('inputDecodeCode').value = '';
            document.getElementById('outputDecodeCode').value = '';
            document.getElementById('copyDecodeBtn').disabled = true;
            document.getElementById('downloadDecodeBtn').disabled = true;
        }
        
        async function copyToClipboard(elementId) {
            const outputCode = document.getElementById(elementId).value;
            try {
                await navigator.clipboard.writeText(outputCode);
                alert('📋 Kode berhasil di-copy ke clipboard!');
            } catch (err) {
                alert('❌ Gagal copy ke clipboard');
            }
        }
        
        function downloadFile(elementId, filename) {
            const outputCode = document.getElementById(elementId).value;
            const blob = new Blob([outputCode], { type: 'text/plain' });
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = filename;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            window.URL.revokeObjectURL(url);
        }
    </script>
</body>
</html>
        """
        
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(html_content.encode('utf-8'))
    
    def serve_css(self):
        """Serve CSS styles"""
        css_content = """
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            overflow: hidden;
        }
        
        h1 {
            background: linear-gradient(45deg, #4CAF50, #2196F3);
            color: white;
            text-align: center;
            padding: 30px;
            font-size: 2.5em;
            margin-bottom: 0;
        }
        
        .container > p {
            text-align: center;
            padding: 20px;
            font-size: 1.1em;
            color: #666;
            background: #f8f9fa;
        }
        
        .form-section {
            margin: 30px;
            padding: 20px;
            border: 2px solid #e9ecef;
            border-radius: 10px;
            background: #f8f9fa;
        }
        
        h2 {
            color: #333;
            margin-bottom: 15px;
            font-size: 1.3em;
        }
        
        textarea {
            width: 100%;
            height: 300px;
            padding: 15px;
            border: 2px solid #ddd;
            border-radius: 8px;
            font-family: 'Consolas', 'Monaco', monospace;
            font-size: 14px;
            resize: vertical;
            transition: border-color 0.3s;
        }
        
        textarea:focus {
            outline: none;
            border-color: #4CAF50;
        }
        
        textarea[readonly] {
            background-color: #f8f9fa;
        }
        
        .button-section {
            margin-top: 15px;
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }
        
        button {
            padding: 12px 24px;
            border: none;
            border-radius: 6px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s;
            min-width: 150px;
        }
        
        .tab-section {
            margin: 20px 30px 0;
            border-bottom: 2px solid #e9ecef;
        }
        
        .tab-buttons {
            display: flex;
            gap: 0;
        }
        
        .tab-button {
            background: #f8f9fa;
            border: 2px solid #e9ecef;
            border-bottom: none;
            border-radius: 10px 10px 0 0;
            padding: 15px 30px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s;
            min-width: 150px;
        }
        
        .tab-button:hover {
            background: #e9ecef;
        }
        
        .tab-button.active {
            background: white;
            color: #4CAF50;
            border-color: #4CAF50;
            position: relative;
            z-index: 1;
        }
        
        .tab-content {
            display: none;
        }
        
        .tab-content.active {
            display: block;
        }
        
        .info-tab {
            display: none;
        }
        
        .info-tab.active {
            display: block;
        }
        
        #obfuscateBtn {
            background: linear-gradient(45deg, #4CAF50, #45a049);
            color: white;
        }
        
        #obfuscateBtn:hover:not(:disabled) {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(76, 175, 80, 0.4);
        }
        
        #clearBtn {
            background: linear-gradient(45deg, #f44336, #da190b);
            color: white;
        }
        
        #clearBtn:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(244, 67, 54, 0.4);
        }
        
        #copyBtn {
            background: linear-gradient(45deg, #2196F3, #1976D2);
            color: white;
        }
        
        #copyBtn:hover:not(:disabled) {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(33, 150, 243, 0.4);
        }
        
        #downloadBtn {
            background: linear-gradient(45deg, #FF9800, #F57C00);
            color: white;
        }
        
        #downloadBtn:hover:not(:disabled) {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(255, 152, 0, 0.4);
        }
        
        button:disabled {
            opacity: 0.6;
            cursor: not-allowed;
            transform: none !important;
        }
        
        .info-section {
            margin: 30px;
            padding: 20px;
            background: #e8f5e8;
            border-radius: 10px;
            border-left: 5px solid #4CAF50;
        }
        
        .info-section h3 {
            color: #2e7d32;
            margin-bottom: 15px;
        }
        
        .info-section ol {
            margin-left: 20px;
            color: #1b5e20;
        }
        
        .info-section li {
            margin-bottom: 8px;
            line-height: 1.5;
        }
        
        @media (max-width: 768px) {
            .container {
                margin: 10px;
                border-radius: 10px;
            }
            
            h1 {
                font-size: 2em;
                padding: 20px;
            }
            
            .form-section {
                margin: 20px;
                padding: 15px;
            }
            
            textarea {
                height: 250px;
            }
            
            .button-section {
                flex-direction: column;
            }
            
            button {
                width: 100%;
                min-width: unset;
            }
        }
        """
        
        self.send_response(200)
        self.send_header('Content-type', 'text/css')
        self.end_headers()
        self.wfile.write(css_content.encode('utf-8'))
    
    def handle_obfuscation(self):
        """Handle the obfuscation request"""
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            
            python_code = data.get('code', '').strip()
            
            if not python_code:
                self.send_json_response({'success': False, 'error': 'Kode Python tidak boleh kosong'})
                return
            
            # Validate Python syntax
            try:
                compile(python_code, '<string>', 'exec')
            except SyntaxError as e:
                self.send_json_response({'success': False, 'error': f'Syntax error: {str(e)}'})
                return
            
            # Encode the Python code
            encoded_code = self.encode_python_script(python_code)
            obfuscated_script = self.create_obfuscated_script(encoded_code)
            
            self.send_json_response({
                'success': True,
                'obfuscated_code': obfuscated_script
            })
            
        except Exception as e:
            self.send_json_response({'success': False, 'error': str(e)})
    
    def handle_deobfuscation(self):
        """Handle the deobfuscation request"""
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            
            obfuscated_code = data.get('code', '').strip()
            
            if not obfuscated_code:
                self.send_json_response({'success': False, 'error': 'Kode yang sudah di-encode tidak boleh kosong'})
                return
            
            # Try to extract the base64 encoded content
            try:
                decoded_script = self.decode_obfuscated_script(obfuscated_code)
                self.send_json_response({
                    'success': True,
                    'deobfuscated_code': decoded_script
                })
            except Exception as e:
                self.send_json_response({'success': False, 'error': f'Gagal decode: {str(e)}'})
                
        except Exception as e:
            self.send_json_response({'success': False, 'error': str(e)})
    
    def encode_python_script(self, script_content):
        """Encode Python script content using base64"""
        script_bytes = script_content.encode('utf-8')
        encoded_bytes = base64.b64encode(script_bytes)
        return encoded_bytes.decode('ascii')
    
    def create_obfuscated_script(self, encoded_content):
        """Create the obfuscated Python script wrapper"""
        return f'''#!/usr/bin/env python3
import base64
unknownkcc = """{encoded_content}"""
eval(compile(base64.b64decode(unknownkcc), "<string>", "exec"))
'''
    
    def decode_obfuscated_script(self, obfuscated_code):
        """Decode an obfuscated Python script back to original"""
        import re
        
        base64_content = None
        
        # Try to extract the base64 content from the obfuscated script
        # Look for any variable name followed by base64 content in triple quotes
        pattern = r'(\w+)\s*=\s*"""([^"]+)"""'
        match = re.search(pattern, obfuscated_code, re.DOTALL)
        
        if match:
            var_name = match.group(1)
            content = match.group(2).strip()
            # Check if this variable is used in base64.b64decode
            if var_name in obfuscated_code and 'base64.b64decode' in obfuscated_code:
                base64_content = content
        
        if not base64_content:
            # Try alternative pattern with single quotes
            pattern = r"(\w+)\s*=\s*'([^']+)'"
            match = re.search(pattern, obfuscated_code, re.DOTALL)
            
            if match:
                var_name = match.group(1)
                content = match.group(2).strip()
                if var_name in obfuscated_code and 'base64.b64decode' in obfuscated_code:
                    base64_content = content
        
        if not base64_content:
            # Try pattern without variable name - look for base64.b64decode calls
            pattern = r'base64\.b64decode\(["\']([^"\']+)["\']\)'
            match = re.search(pattern, obfuscated_code)
            
            if match:
                base64_content = match.group(1).strip()
        
        if not base64_content:
            # Try looking for any base64-like content in triple quotes
            pattern = r'"""([A-Za-z0-9+/=\s]+)"""'
            match = re.search(pattern, obfuscated_code, re.DOTALL)
            if match:
                # Validate if it's actually base64
                content = match.group(1).strip()
                if self.is_base64(content):
                    base64_content = content
        
        if not base64_content:
            raise ValueError("Tidak dapat menemukan kode base64 yang valid dalam script")
        
        try:
            # Decode the base64 content
            decoded_bytes = base64.b64decode(base64_content)
            original_script = decoded_bytes.decode('utf-8')
            return original_script
        except Exception as e:
            raise ValueError(f"Gagal decode base64: {str(e)}")
    
    def is_base64(self, s):
        """Check if string is valid base64."""
        try:
            # Remove whitespace and newlines
            import re
            s = re.sub(r'\s+', '', s)
            # Check if it's valid base64
            if len(s) % 4 != 0:
                return False
            base64.b64decode(s)
            return True
        except:
            return False
    
    def send_json_response(self, data):
        """Send JSON response"""
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))
    
    def log_message(self, format, *args):
        """Override to reduce log noise"""
        pass

def run_web_server(port=5000):
    """Run the web server"""
    server_address = ('0.0.0.0', port)
    httpd = HTTPServer(server_address, ObfuscatorWebHandler)
    
    print(f"🌐 Python Script Obfuscator Web Interface")
    print(f"📡 Server berjalan di: http://localhost:{port}")
    print(f"🔗 Akses dari browser: http://localhost:{port}")
    print(f"⏹️  Tekan Ctrl+C untuk stop server")
    print("=" * 50)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n⏹️  Server dihentikan")
        httpd.shutdown()

if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='Python Script Obfuscator Web Interface')
    parser.add_argument('-p', '--port', type=int, default=5000, help='Port untuk web server (default: 5000)')
    
    args = parser.parse_args()
    run_web_server(args.port)