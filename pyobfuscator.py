#!/usr/bin/env python3
"""
Python Script Obfuscator Tool
A command-line tool for encoding and obfuscating Python scripts using base64 encoding.
"""

import os
import sys
import base64
import argparse
import pathlib
from typing import List, Optional


class PyObfuscator:
    """Main class for Python script obfuscation using base64 encoding."""
    
    def __init__(self):
        self.supported_extensions = ['.py', '.pyw']
        self.obfuscated_suffix = '_obfuscated'
    
    def is_python_file(self, file_path: pathlib.Path) -> bool:
        """Check if the file is a Python script."""
        return file_path.suffix.lower() in self.supported_extensions
    
    def read_script(self, file_path: pathlib.Path) -> str:
        """Read Python script content from file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            return content
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")
        except PermissionError:
            raise PermissionError(f"Permission denied: {file_path}")
        except UnicodeDecodeError:
            raise UnicodeDecodeError(f"Cannot decode file (not UTF-8): {file_path}")
    
    def encode_script(self, script_content: str) -> str:
        """Encode Python script content using base64."""
        try:
            # Convert string to bytes
            script_bytes = script_content.encode('utf-8')
            # Encode using base64
            encoded_bytes = base64.b64encode(script_bytes)
            # Convert back to string
            encoded_string = encoded_bytes.decode('ascii')
            return encoded_string
        except Exception as e:
            raise Exception(f"Failed to encode script: {e}")
    
    def create_obfuscated_script(self, encoded_content: str) -> str:
        """Create the obfuscated Python script wrapper."""
        # Create the obfuscated script template similar to the image
        obfuscated_template = f'''#!/usr/bin/env python3
import base64
unknownkcc = """{encoded_content}"""
eval(compile(base64.b64decode(unknownkcc), "<string>", "exec"))
'''
        return obfuscated_template
    
    def generate_output_path(self, input_path: pathlib.Path, output_dir: Optional[str] = None) -> pathlib.Path:
        """Generate output file path for obfuscated script."""
        if output_dir:
            output_directory = pathlib.Path(output_dir)
            output_directory.mkdir(parents=True, exist_ok=True)
            filename = input_path.stem + self.obfuscated_suffix + input_path.suffix
            return output_directory / filename
        else:
            # Save in the same directory as input
            filename = input_path.stem + self.obfuscated_suffix + input_path.suffix
            return input_path.parent / filename
    
    def write_obfuscated_script(self, obfuscated_content: str, output_path: pathlib.Path) -> None:
        """Write obfuscated script to file."""
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(obfuscated_content)
            
            # Make the file executable on Unix-like systems
            if os.name == 'posix':
                os.chmod(output_path, 0o755)
                
        except PermissionError:
            raise PermissionError(f"Permission denied writing to: {output_path}")
        except Exception as e:
            raise Exception(f"Failed to write obfuscated script: {e}")
    
    def obfuscate_single_file(self, input_file: str, output_dir: Optional[str] = None) -> str:
        """Obfuscate a single Python file."""
        input_path = pathlib.Path(input_file)
        
        # Validate input file
        if not input_path.exists():
            raise FileNotFoundError(f"Input file does not exist: {input_file}")
        
        if not input_path.is_file():
            raise ValueError(f"Input path is not a file: {input_file}")
        
        if not self.is_python_file(input_path):
            raise ValueError(f"File is not a Python script: {input_file}")
        
        # Read and validate script content
        script_content = self.read_script(input_path)
        
        if not script_content.strip():
            raise ValueError(f"Script file is empty: {input_file}")
        
        # Try to compile the script to check for syntax errors
        try:
            compile(script_content, str(input_path), 'exec')
        except SyntaxError as e:
            raise SyntaxError(f"Syntax error in script {input_file}: {e}")
        
        # Encode the script
        encoded_content = self.encode_script(script_content)
        
        # Create obfuscated script
        obfuscated_script = self.create_obfuscated_script(encoded_content)
        
        # Generate output path
        output_path = self.generate_output_path(input_path, output_dir)
        
        # Write obfuscated script
        self.write_obfuscated_script(obfuscated_script, output_path)
        
        return str(output_path)
    
    def obfuscate_multiple_files(self, input_files: List[str], output_dir: Optional[str] = None) -> List[str]:
        """Obfuscate multiple Python files."""
        results = []
        errors = []
        
        for input_file in input_files:
            try:
                output_path = self.obfuscate_single_file(input_file, output_dir)
                results.append(output_path)
                print(f"✓ Successfully obfuscated: {input_file} -> {output_path}")
            except Exception as e:
                error_msg = f"✗ Failed to obfuscate {input_file}: {e}"
                errors.append(error_msg)
                print(error_msg, file=sys.stderr)
        
        if errors:
            print(f"\nCompleted with {len(errors)} error(s) out of {len(input_files)} file(s)")
        else:
            print(f"\nSuccessfully obfuscated all {len(input_files)} file(s)")
        
        return results
    
    def find_python_files(self, directory: str, recursive: bool = False) -> List[str]:
        """Find Python files in a directory."""
        directory_path = pathlib.Path(directory)
        
        if not directory_path.exists():
            raise FileNotFoundError(f"Directory does not exist: {directory}")
        
        if not directory_path.is_dir():
            raise ValueError(f"Path is not a directory: {directory}")
        
        python_files = []
        
        if recursive:
            for ext in self.supported_extensions:
                python_files.extend(directory_path.rglob(f'*{ext}'))
        else:
            for ext in self.supported_extensions:
                python_files.extend(directory_path.glob(f'*{ext}'))
        
        return [str(f) for f in python_files]


def main():
    """Main function to handle command line arguments and execute obfuscation."""
    parser = argparse.ArgumentParser(
        description='Python Script Obfuscator - Encode Python scripts using base64',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s script.py                    # Obfuscate single file
  %(prog)s *.py                         # Obfuscate multiple files
  %(prog)s -d /path/to/scripts          # Obfuscate all Python files in directory
  %(prog)s -d /path/to/scripts -r       # Obfuscate recursively
  %(prog)s script.py -o /output/dir     # Specify output directory
        """
    )
    
    # Input arguments
    parser.add_argument(
        'files',
        nargs='*',
        help='Python files to obfuscate'
    )
    
    parser.add_argument(
        '-d', '--directory',
        help='Directory containing Python files to obfuscate'
    )
    
    parser.add_argument(
        '-r', '--recursive',
        action='store_true',
        help='Recursively search for Python files in directory'
    )
    
    parser.add_argument(
        '-o', '--output',
        help='Output directory for obfuscated files'
    )
    
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enable verbose output'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version='%(prog)s 1.0.0'
    )
    
    args = parser.parse_args()
    
    # Validate arguments
    if not args.files and not args.directory:
        parser.error("Must specify either files or directory")
    
    if args.files and args.directory:
        parser.error("Cannot specify both files and directory")
    
    # Initialize obfuscator
    obfuscator = PyObfuscator()
    
    try:
        # Determine input files
        if args.directory:
            input_files = obfuscator.find_python_files(args.directory, args.recursive)
            if not input_files:
                print("No Python files found in the specified directory")
                return 1
        else:
            input_files = args.files
        
        if args.verbose:
            print(f"Found {len(input_files)} Python file(s) to obfuscate")
            for f in input_files:
                print(f"  - {f}")
            print()
        
        # Obfuscate files
        if len(input_files) == 1:
            try:
                output_path = obfuscator.obfuscate_single_file(input_files[0], args.output)
                print(f"✓ Successfully obfuscated: {input_files[0]} -> {output_path}")
                return 0
            except Exception as e:
                print(f"✗ Failed to obfuscate {input_files[0]}: {e}", file=sys.stderr)
                return 1
        else:
            results = obfuscator.obfuscate_multiple_files(input_files, args.output)
            return 0 if results else 1
    
    except KeyboardInterrupt:
        print("\nOperation cancelled by user", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
