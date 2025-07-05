#!/usr/bin/env python3
"""
Python Script Decoder Tool
A command-line tool for decoding obfuscated Python scripts that were encoded using base64.
"""

import os
import sys
import base64
import argparse
import pathlib
import re
from typing import List, Optional


class PyDecoder:
    """Main class for Python script deobfuscation."""
    
    def __init__(self):
        self.supported_extensions = ['.py', '.pyw']
        self.decoded_suffix = '_decoded'
    
    def is_python_file(self, file_path: pathlib.Path) -> bool:
        """Check if the file is a Python script."""
        return file_path.suffix.lower() in self.supported_extensions
    
    def read_script(self, file_path: pathlib.Path) -> str:
        """Read obfuscated script content from file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            return content
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")
        except PermissionError:
            raise PermissionError(f"Permission denied: {file_path}")
        except UnicodeDecodeError:
            raise ValueError(f"Cannot decode file (not UTF-8): {file_path}")
    
    def decode_obfuscated_script(self, obfuscated_code: str) -> str:
        """Decode an obfuscated Python script back to original."""
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
            raise ValueError("Cannot find valid base64 content in the script. Make sure this is an obfuscated Python script.")
        
        try:
            # Decode the base64 content
            decoded_bytes = base64.b64decode(base64_content)
            original_script = decoded_bytes.decode('utf-8')
            return original_script
        except Exception as e:
            raise ValueError(f"Failed to decode base64 content: {str(e)}")
    
    def is_base64(self, s: str) -> bool:
        """Check if string is valid base64."""
        try:
            # Remove whitespace and newlines
            s = re.sub(r'\s+', '', s)
            # Check if it's valid base64
            if len(s) % 4 != 0:
                return False
            base64.b64decode(s)
            return True
        except:
            return False
    
    def generate_output_path(self, input_path: pathlib.Path, output_dir: Optional[str] = None) -> pathlib.Path:
        """Generate output file path for decoded script."""
        if output_dir:
            output_directory = pathlib.Path(output_dir)
            output_directory.mkdir(parents=True, exist_ok=True)
            filename = input_path.stem + self.decoded_suffix + input_path.suffix
            return output_directory / filename
        else:
            # Save in the same directory as input
            filename = input_path.stem + self.decoded_suffix + input_path.suffix
            return input_path.parent / filename
    
    def write_decoded_script(self, decoded_content: str, output_path: pathlib.Path) -> None:
        """Write decoded script to file."""
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(decoded_content)
            
            # Make the file executable on Unix-like systems
            if os.name == 'posix':
                os.chmod(output_path, 0o755)
                
        except PermissionError:
            raise PermissionError(f"Permission denied writing to: {output_path}")
        except Exception as e:
            raise Exception(f"Failed to write decoded script: {e}")
    
    def decode_single_file(self, input_file: str, output_dir: Optional[str] = None) -> str:
        """Decode a single obfuscated Python file."""
        input_path = pathlib.Path(input_file)
        
        # Validate input file
        if not input_path.exists():
            raise FileNotFoundError(f"Input file does not exist: {input_file}")
        
        if not input_path.is_file():
            raise ValueError(f"Input path is not a file: {input_file}")
        
        if not self.is_python_file(input_path):
            raise ValueError(f"File is not a Python script: {input_file}")
        
        # Read obfuscated script content
        obfuscated_content = self.read_script(input_path)
        
        if not obfuscated_content.strip():
            raise ValueError(f"Script file is empty: {input_file}")
        
        # Decode the script
        decoded_content = self.decode_obfuscated_script(obfuscated_content)
        
        # Generate output path
        output_path = self.generate_output_path(input_path, output_dir)
        
        # Write decoded script
        self.write_decoded_script(decoded_content, output_path)
        
        return str(output_path)
    
    def decode_multiple_files(self, input_files: List[str], output_dir: Optional[str] = None) -> List[str]:
        """Decode multiple obfuscated Python files."""
        results = []
        errors = []
        
        for input_file in input_files:
            try:
                output_path = self.decode_single_file(input_file, output_dir)
                results.append(output_path)
                print(f"✓ Successfully decoded: {input_file} -> {output_path}")
            except Exception as e:
                error_msg = f"✗ Failed to decode {input_file}: {e}"
                errors.append(error_msg)
                print(error_msg, file=sys.stderr)
        
        if errors:
            print(f"\nCompleted with {len(errors)} error(s) out of {len(input_files)} file(s)")
        else:
            print(f"\nSuccessfully decoded all {len(input_files)} file(s)")
        
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
    """Main function to handle command line arguments and execute decoding."""
    parser = argparse.ArgumentParser(
        description='Python Script Decoder - Decode obfuscated Python scripts',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s obfuscated_script.py           # Decode single file
  %(prog)s *_obfuscated.py                # Decode multiple files
  %(prog)s -d /path/to/scripts            # Decode all Python files in directory
  %(prog)s -d /path/to/scripts -r         # Decode recursively
  %(prog)s script.py -o /output/dir       # Specify output directory
        """
    )
    
    # Input arguments
    parser.add_argument(
        'files',
        nargs='*',
        help='Obfuscated Python files to decode'
    )
    
    parser.add_argument(
        '-d', '--directory',
        help='Directory containing obfuscated Python files to decode'
    )
    
    parser.add_argument(
        '-r', '--recursive',
        action='store_true',
        help='Recursively search for Python files in directory'
    )
    
    parser.add_argument(
        '-o', '--output',
        help='Output directory for decoded files'
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
    
    # Initialize decoder
    decoder = PyDecoder()
    
    try:
        # Determine input files
        if args.directory:
            input_files = decoder.find_python_files(args.directory, args.recursive)
            if not input_files:
                print("No Python files found in the specified directory")
                return 1
        else:
            input_files = args.files
        
        if args.verbose:
            print(f"Found {len(input_files)} Python file(s) to decode")
            for f in input_files:
                print(f"  - {f}")
            print()
        
        # Decode files
        if len(input_files) == 1:
            try:
                output_path = decoder.decode_single_file(input_files[0], args.output)
                print(f"✓ Successfully decoded: {input_files[0]} -> {output_path}")
                return 0
            except Exception as e:
                print(f"✗ Failed to decode {input_files[0]}: {e}", file=sys.stderr)
                return 1
        else:
            results = decoder.decode_multiple_files(input_files, args.output)
            return 0 if results else 1
    
    except KeyboardInterrupt:
        print("\nOperation cancelled by user", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())