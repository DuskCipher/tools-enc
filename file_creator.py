
#!/usr/bin/env python3
"""
Advanced Python File Creator
A comprehensive tool for creating Python files with various templates and features.
"""

import os
import sys
import pathlib
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
    END = '\033[0m'


class AdvancedFileCreator:
    """Advanced file creator with multiple templates and features"""
    
    def __init__(self):
        self.templates = {
            '1': {
                'name': 'Basic Script',
                'desc': 'Simple Python script with main function',
                'content': '''#!/usr/bin/env python3
"""
{filename}.py - {description}
Created on {date}
"""

def main():
    """Main function"""
    print("Hello, World!")
    print("This is {filename}")
    
    # Your code here
    

if __name__ == "__main__":
    main()
'''
            },
            '2': {
                'name': 'Interactive Script',
                'desc': 'Script with user input and interaction',
                'content': '''#!/usr/bin/env python3
"""
{filename}.py - {description}
Created on {date}
"""

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
    print("{filename} - Interactive Python Script")
    print("=" * 60)
    
    name = get_user_input()
    print(f"\\nHello, {{name}}! Welcome to {filename}!")
    
    print(f"\\nCurrent time: {{datetime.now()}}")
    print("\\n✅ Script completed successfully!")

if __name__ == "__main__":
    main()
'''
            },
            '3': {
                'name': 'Web Server',
                'desc': 'Simple HTTP server',
                'content': '''#!/usr/bin/env python3
"""
{filename}.py - {description}
Created on {date}
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
        print("{filename} - Web Server")
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
    
    run_server(port)
'''
            },
            '4': {
                'name': 'API Client',
                'desc': 'Script for making API requests',
                'content': '''#!/usr/bin/env python3
"""
{filename}.py - {description}
Created on {date}
"""

import urllib.request
import urllib.parse
import json
import sys

class APIClient:
    """Simple API client"""
    
    def __init__(self, base_url):
        self.base_url = base_url.rstrip('/')
    
    def get(self, endpoint, params=None):
        """Make GET request"""
        url = f"{{self.base_url}}/{{endpoint.lstrip('/')}}"
        
        if params:
            query_string = urllib.parse.urlencode(params)
            url = f"{{url}}?{{query_string}}"
        
        try:
            with urllib.request.urlopen(url) as response:
                return json.loads(response.read().decode())
        except Exception as e:
            print(f"❌ Error making request: {{e}}")
            return None
    
    def post(self, endpoint, data):
        """Make POST request"""
        url = f"{{self.base_url}}/{{endpoint.lstrip('/')}}"
        
        json_data = json.dumps(data).encode('utf-8')
        
        req = urllib.request.Request(url, data=json_data)
        req.add_header('Content-Type', 'application/json')
        
        try:
            with urllib.request.urlopen(req) as response:
                return json.loads(response.read().decode())
        except Exception as e:
            print(f"❌ Error making request: {{e}}")
            return None

def main():
    """Main function"""
    # Example usage
    client = APIClient("https://jsonplaceholder.typicode.com")
    
    # Get posts
    posts = client.get("posts")
    if posts:
        print(f"📊 Found {{len(posts)}} posts")
        print(f"First post: {{posts[0]['title']}}")
    
    # Create new post
    new_post = {{
        "title": "Test Post",
        "body": "This is a test post",
        "userId": 1
    }}
    
    result = client.post("posts", new_post)
    if result:
        print(f"✅ Created post with ID: {{result.get('id')}}")

if __name__ == "__main__":
    main()
'''
            },
            '5': {
                'name': 'Class Template',
                'desc': 'Object-oriented class with methods',
                'content': '''#!/usr/bin/env python3
"""
{filename}.py - {description}
Created on {date}
"""

class {classname}:
    """A sample class for demonstration"""
    
    def __init__(self, name):
        """Initialize the object"""
        self.name = name
        self.data = []
        self.created_at = "{date}"
    
    def add_item(self, item):
        """Add an item to the collection"""
        self.data.append(item)
        print(f"✅ Added: {{item}}")
    
    def remove_item(self, item):
        """Remove an item from the collection"""
        if item in self.data:
            self.data.remove(item)
            print(f"🗑️  Removed: {{item}}")
        else:
            print(f"❌ Item not found: {{item}}")
    
    def get_items(self):
        """Get all items"""
        return self.data.copy()
    
    def get_count(self):
        """Get number of items"""
        return len(self.data)
    
    def clear_items(self):
        """Clear all items"""
        self.data.clear()
        print("🧹 All items cleared")
    
    def __str__(self):
        """String representation"""
        return f"{classname}(name='{{self.name}}', items={{len(self.data)}})"
    
    def __repr__(self):
        """Developer representation"""
        return f"{classname}(name='{{self.name}}', data={{self.data}})"

def main():
    """Main function for testing"""
    # Create instance
    obj = {classname}("Test Object")
    
    # Add some items
    obj.add_item("Item 1")
    obj.add_item("Item 2")
    obj.add_item("Item 3")
    
    # Display info
    print(f"Object: {{obj}}")
    print(f"Items: {{obj.get_items()}}")
    print(f"Count: {{obj.get_count()}}")
    
    # Remove an item
    obj.remove_item("Item 2")
    print(f"After removal: {{obj.get_items()}}")

if __name__ == "__main__":
    main()
'''
            },
            '6': {
                'name': 'Command Line Tool',
                'desc': 'Script with argument parsing',
                'content': '''#!/usr/bin/env python3
"""
{filename}.py - {description}
Created on {date}
"""

import argparse
import sys
import os

def process_file(file_path, options):
    """Process a single file"""
    if not os.path.exists(file_path):
        print(f"❌ File not found: {{file_path}}")
        return False
    
    print(f"📄 Processing: {{file_path}}")
    
    # Your file processing logic here
    if options.get('verbose'):
        print(f"📊 File size: {{os.path.getsize(file_path)}} bytes")
    
    return True

def main():
    """Main function"""
    parser = argparse.ArgumentParser(
        description='{description}',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        'files',
        nargs='*',
        help='Files to process'
    )
    
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enable verbose output'
    )
    
    parser.add_argument(
        '-o', '--output',
        help='Output directory'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version='%(prog)s 1.0.0'
    )
    
    args = parser.parse_args()
    
    if not args.files:
        parser.print_help()
        return 1
    
    options = {{
        'verbose': args.verbose,
        'output': args.output
    }}
    
    success_count = 0
    for file_path in args.files:
        if process_file(file_path, options):
            success_count += 1
    
    print(f"\\n✅ Processed {{success_count}}/{{len(args.files)}} files successfully")
    return 0 if success_count == len(args.files) else 1

if __name__ == "__main__":
    sys.exit(main())
'''
            }
        }
    
    def print_banner(self):
        """Display banner"""
        print(f"\n{Colors.MAGENTA}{'╔' + '═' * 68 + '╗'}{Colors.END}")
        print(f"{Colors.MAGENTA}║{Colors.CYAN}{Colors.BOLD}{'ADVANCED PYTHON FILE CREATOR':^68}{Colors.END}{Colors.MAGENTA}║{Colors.END}")
        print(f"{Colors.MAGENTA}║{Colors.YELLOW}{'Professional File Templates & Code Generation':^68}{Colors.END}{Colors.MAGENTA}║{Colors.END}")
        print(f"{Colors.MAGENTA}{'╚' + '═' * 68 + '╝'}{Colors.END}")
    
    def show_templates(self):
        """Display available templates"""
        print(f"\n{Colors.GREEN}📋 Available Templates:{Colors.END}")
        print(f"{Colors.MAGENTA}{'' + '' * 68 + ''}{Colors.END}")
        
        for key, template in self.templates.items():
            print(f"{Colors.MAGENTA}{Colors.END} {Colors.CYAN}[{key}]{Colors.END} {Colors.WHITE}{template['name']:<20}{Colors.GRAY} - {template['desc']:<37}{Colors.MAGENTA} {Colors.END}")
        
        print(f"{Colors.MAGENTA}{Colors.END} {Colors.YELLOW}[0]{Colors.END} {Colors.WHITE}{'Empty File':<20}{Colors.GRAY} - {'Create empty file with basic header':<37}{Colors.MAGENTA} {Colors.END}")
        print(f"{Colors.MAGENTA}{'' + '' * 68 + ''}{Colors.END}")
    
    def get_filename(self):
        """Get filename from user"""
        while True:
            filename = input(f"\n{Colors.YELLOW}📝 Enter filename (without .py): {Colors.END}").strip()
            
            if not filename:
                print(f"{Colors.RED}❌ Filename cannot be empty{Colors.END}")
                continue
            
            if not filename.endswith('.py'):
                filename += '.py'
            
            if os.path.exists(filename):
                overwrite = input(f"{Colors.YELLOW}⚠️  File {filename} exists. Overwrite? (y/n): {Colors.END}").strip().lower()
                if overwrite != 'y':
                    continue
            
            return filename
    
    def get_template_choice(self):
        """Get template choice from user"""
        while True:
            choice = input(f"\n{Colors.YELLOW}🎯 Select template [0-{len(self.templates)}]: {Colors.END}").strip()
            
            if choice == '0':
                return None
            elif choice in self.templates:
                return choice
            else:
                print(f"{Colors.RED}❌ Invalid choice. Please select 0-{len(self.templates)}{Colors.END}")
    
    def create_file_with_template(self, filename, template_key):
        """Create file with selected template"""
        template = self.templates[template_key]
        
        # Get additional info
        description = input(f"{Colors.YELLOW}📝 Enter description: {Colors.END}").strip()
        if not description:
            description = template['desc']
        
        # For class template, get class name
        classname = ""
        if template_key == '5':
            classname = input(f"{Colors.YELLOW}🏷️  Enter class name: {Colors.END}").strip()
            if not classname:
                classname = pathlib.Path(filename).stem.title().replace('_', '')
        
        # Format template
        content = template['content'].format(
            filename=pathlib.Path(filename).stem,
            description=description,
            date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            classname=classname
        )
        
        return content
    
    def create_empty_file(self, filename):
        """Create empty file with basic header"""
        description = input(f"{Colors.YELLOW}📝 Enter description: {Colors.END}").strip()
        if not description:
            description = "Python script"
        
        content = f'''#!/usr/bin/env python3
"""
{pathlib.Path(filename).stem}.py - {description}
Created on {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
"""

def main():
    """Main function"""
    pass

if __name__ == "__main__":
    main()
'''
        return content
    
    def save_file(self, filename, content):
        """Save file with content"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            
            # Make executable on Unix systems
            if os.name == 'posix':
                os.chmod(filename, 0o755)
            
            file_size = len(content.encode('utf-8'))
            line_count = len(content.splitlines())
            
            print(f"\n{Colors.GREEN}✅ File created successfully!{Colors.END}")
            print(f"{Colors.MAGENTA}{'┌' + '─' * 50 + '┐'}{Colors.END}")
            print(f"{Colors.MAGENTA}│{Colors.END} {Colors.GRAY}Filename : {Colors.CYAN}{filename:<35}{Colors.MAGENTA} │{Colors.END}")
            print(f"{Colors.MAGENTA}│{Colors.END} {Colors.GRAY}Size     : {Colors.YELLOW}{file_size} bytes{Colors.GRAY}{' ' * (35-len(str(file_size)+' bytes'))}{Colors.MAGENTA} │{Colors.END}")
            print(f"{Colors.MAGENTA}│{Colors.END} {Colors.GRAY}Lines    : {Colors.GREEN}{line_count}{Colors.GRAY}{' ' * (35-len(str(line_count)))}{Colors.MAGENTA} │{Colors.END}")
            print(f"{Colors.MAGENTA}{'└' + '─' * 50 + '┘'}{Colors.END}")
            
            return True
            
        except Exception as e:
            print(f"{Colors.RED}❌ Failed to create file: {e}{Colors.END}")
            return False
    
    def run(self):
        """Run the file creator"""
        os.system('clear' if os.name == 'posix' else 'cls')
        self.print_banner()
        
        while True:
            self.show_templates()
            
            filename = self.get_filename()
            template_choice = self.get_template_choice()
            
            if template_choice is None:
                content = self.create_empty_file(filename)
            else:
                content = self.create_file_with_template(filename, template_choice)
            
            if self.save_file(filename, content):
                # Ask if user wants to create another file
                another = input(f"\n{Colors.YELLOW}🔄 Create another file? (y/n): {Colors.END}").strip().lower()
                if another != 'y':
                    break
            else:
                retry = input(f"\n{Colors.YELLOW}🔄 Try again? (y/n): {Colors.END}").strip().lower()
                if retry != 'y':
                    break
        
        print(f"\n{Colors.GREEN}👋 Thank you for using Advanced File Creator!{Colors.END}")


def main():
    """Main function"""
    try:
        creator = AdvancedFileCreator()
        creator.run()
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}⏹️  Operation cancelled by user{Colors.END}")
    except Exception as e:
        print(f"\n{Colors.RED}❌ Error: {e}{Colors.END}")


if __name__ == "__main__":
    main()
