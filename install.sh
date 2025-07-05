
#!/bin/bash

# DUSK CIPHER Project Installation Script
# This script installs all necessary dependencies and sets up the project

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
MAGENTA='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}✓${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

print_error() {
    echo -e "${RED}✗${NC} $1"
}

print_header() {
    clear
    echo -e "${MAGENTA}╔══════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${MAGENTA}║${CYAN}                    DUSK CIPHER INSTALLER                    ${MAGENTA} ║${NC}"
    echo -e "${MAGENTA}║${YELLOW}              Professional Encryption Toolkit              ${MAGENTA}   ║${NC}"
    echo -e "${MAGENTA}╚══════════════════════════════════════════════════════════════╝${NC}"
    echo ""
}

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function to check Python version
check_python() {
    print_status "Checking Python installation..."
    
    if command_exists python3; then
        PYTHON_VERSION=$(python3 --version 2>&1 | grep -oP '\d+\.\d+')
        MAJOR_VERSION=$(echo $PYTHON_VERSION | cut -d. -f1)
        MINOR_VERSION=$(echo $PYTHON_VERSION | cut -d. -f2)
        
        if [ "$MAJOR_VERSION" -eq 3 ] && [ "$MINOR_VERSION" -ge 6 ]; then
            print_status "Python $PYTHON_VERSION detected ✓"
            return 0
        else
            print_error "Python 3.6+ required, found $PYTHON_VERSION"
            return 1
        fi
    else
        print_error "Python 3 not found. Please install Python 3.6 or higher."
        return 1
    fi
}

# Function to install system packages
install_system_packages() {
    print_status "Installing system dependencies..."
    
    # Check if we're on a Debian/Ubuntu system
    if command_exists apt-get; then
        
        # Update package list quietly
        sudo apt-get update -qq >/dev/null 2>&1
        
        # Install required packages quietly
        sudo apt-get install -y \
            python3 \
            python3-pip \
            python3-dev \
            python3-venv \
            nano \
            curl \
            wget \
            git \
            build-essential >/dev/null 2>&1
            
        print_status "System dependencies ready"
        
    # Check if we're on a Red Hat/CentOS/Fedora system
    elif command_exists yum || command_exists dnf; then
        print_status "Detected Red Hat/CentOS/Fedora system"
        
        if command_exists dnf; then
            PACKAGE_MANAGER="dnf"
        else
            PACKAGE_MANAGER="yum"
        fi
        
        # Install required packages
        sudo $PACKAGE_MANAGER install -y \
            python3 \
            python3-pip \
            python3-devel \
            nano \
            curl \
            wget \
            git \
            gcc \
            gcc-c++ \
            make
            
        print_status "System packages installed ✓"
        
    # Check if we're on an Arch system
    elif command_exists pacman; then
        print_status "Detected Arch Linux system"
        
        # Install required packages
        sudo pacman -S --noconfirm \
            python \
            python-pip \
            nano \
            curl \
            wget \
            git \
            base-devel
            
        print_status "System packages installed ✓"
        
    else
        print_warning "Unknown package manager. Please install the following manually:"
        echo "- Python 3.6+"
        echo "- pip3"
        echo "- nano (text editor)"
        echo "- curl"
        echo "- wget"
        echo "- git"
    fi
}

# Function to upgrade pip
upgrade_pip() {
    print_status "Setting up pip..."
    
    if command_exists pip3; then
        pip3 install --upgrade pip >/dev/null 2>&1
        print_status "pip ready"
    else
        if command_exists python3; then
            python3 -m ensurepip --upgrade >/dev/null 2>&1
            python3 -m pip install --upgrade pip >/dev/null 2>&1
            print_status "pip configured"
        else
            print_error "Cannot install pip - Python 3 not found"
            return 1
        fi
    fi
}

# Function to install Python packages
install_python_packages() {
    print_status "Installing required packages..."
    
    # Common packages that might be useful
    PACKAGES=(
        "requests"
        "urllib3"
        "certifi"
        "charset-normalizer"
        "idna"
    )
    
    for package in "${PACKAGES[@]}"; do
        pip3 install --upgrade "$package" >/dev/null 2>&1 || true
    done
    
    print_status "Python packages ready"
}

# Function to set file permissions
set_permissions() {
    print_status "Setting file permissions..."
    
    # Make Python scripts executable
    chmod +x *.py 2>/dev/null || true
    chmod +x install.sh 2>/dev/null || true
    
    # Set proper permissions for directories
    chmod 755 examples/ 2>/dev/null || true
    
    print_status "File permissions set ✓"
}

# Function to create necessary directories
create_directories() {
    print_status "Creating project directories..."
    
    # Create directories if they don't exist
    mkdir -p logs 2>/dev/null || true
    mkdir -p output 2>/dev/null || true
    mkdir -p temp 2>/dev/null || true
    mkdir -p backups 2>/dev/null || true
    
    print_status "Project directories created ✓"
}

# Function to verify installation
verify_installation() {
    print_status "Verifying installation..."
    
    # Check if main scripts can be imported
    if python3 -c "import base64, json, os, sys, pathlib, re, time, argparse, urllib.request, urllib.parse" >/dev/null 2>&1; then
        print_status "Core modules ready"
    else
        print_error "Some Python modules are missing"
        return 1
    fi
    
    # Check if main scripts exist
    MAIN_SCRIPTS=("dusk_cipher.py" "pyobfuscator.py" "pydecoder.py" "web_obfuscator.py" "file_creator.py")
    
    for script in "${MAIN_SCRIPTS[@]}"; do
        if [ ! -f "$script" ]; then
            print_error "$script not found"
            return 1
        fi
    done
    
    print_status "All components verified"
}

# Function to display usage information
show_usage() {
    echo ""
    echo -e "${CYAN}╔══════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${CYAN}║${YELLOW}                        USAGE GUIDE                          ${CYAN} ║${NC}"
    echo -e "${CYAN}╚══════════════════════════════════════════════════════════════╝${NC}"
    echo ""
    echo -e "${GREEN}Available Tools:${NC}"
    echo -e "  ${YELLOW}python3 dusk_cipher.py${NC}      - Main encryption toolkit (interactive)"
    echo -e "  ${YELLOW}python3 pyobfuscator.py${NC}     - Command-line obfuscator"
    echo -e "  ${YELLOW}python3 pydecoder.py${NC}        - Command-line decoder"
    echo -e "  ${YELLOW}python3 web_obfuscator.py${NC}   - Web interface"
    echo -e "  ${YELLOW}python3 file_creator.py${NC}     - Advanced file creator"
    echo ""
    echo -e "${GREEN}Quick Start:${NC}"
    echo -e "  ${CYAN}1.${NC} Run: ${YELLOW}python3 dusk_cipher.py${NC}"
    echo -e "  ${CYAN}2.${NC} Choose option 1 to encrypt a Python file"
    echo -e "  ${CYAN}3.${NC} Choose option 2 to decrypt an encrypted file"
    echo -e "  ${CYAN}4.${NC} Choose option 9 for web interface"
    echo ""
    echo -e "${GREEN}Web Interface:${NC}"
    echo -e "  ${CYAN}•${NC} Run: ${YELLOW}python3 web_obfuscator.py${NC}"
    echo -e "  ${CYAN}•${NC} Open browser to: ${YELLOW}http://localhost:5000${NC}"
    echo ""
}

# Main installation function
main() {
    print_header
    
    print_status "Starting DUSK CIPHER installation..."
    echo ""
    
    # Check Python installation
    if ! check_python; then
        print_error "Python check failed. Please install Python 3.6+ first."
        exit 1
    fi
    
    # Install system packages (requires sudo)
    echo -ne "${YELLOW}Install system dependencies? (Y/n): ${NC}"
    read -r response
    if [[ ! "$response" =~ ^[Nn]$ ]]; then
        install_system_packages >/dev/null 2>&1 || print_warning "Some system packages may need manual installation"
    fi
    
    # Setup environment
    upgrade_pip
    install_python_packages
    set_permissions
    create_directories
    
    # Quick verification
    if ! verify_installation; then
        print_error "Installation verification failed"
        exit 1
    fi
    
    echo ""
    print_status "Installation completed successfully! 🎉"
    
    # Show usage information
    show_usage
    
    echo -e "${GREEN}Installation Summary:${NC}"
    echo -e "  ${CYAN}•${NC} Python version: $(python3 --version)"
    echo -e "  ${CYAN}•${NC} Installation directory: $(pwd)"
    echo -e "  ${CYAN}•${NC} All main scripts are ready to use"
    echo ""
    echo -e "${MAGENTA}Happy encrypting with DUSK CIPHER! 🔐${NC}"
    
    # Ask user if they want to launch the tool immediately
    echo ""
    echo -ne "${YELLOW}Launch DUSK CIPHER now? (Y/n): ${NC}"
    read -r launch_choice
    
    if [[ "$launch_choice" =~ ^[Nn]$ ]]; then
        echo -e "${CYAN}You can start DUSK CIPHER anytime with: ${YELLOW}python3 dusk_cipher.py${NC}"
    else
        echo -e "${GREEN}🚀 Launching DUSK CIPHER...${NC}"
        echo ""
        python3 dusk_cipher.py
    fi
}

# Function to show quick launch menu
show_launch_menu() {
    echo ""
    echo -e "${CYAN}╔══════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${CYAN}║${YELLOW}                      QUICK LAUNCH MENU                      ${CYAN} ║${NC}"
    echo -e "${CYAN}╚══════════════════════════════════════════════════════════════╝${NC}"
    echo ""
    echo -e "${GREEN}Available Commands:${NC}"
    echo -e "  ${YELLOW}1.${NC} ${CYAN}python3 dusk_cipher.py${NC}      - Main interactive toolkit"
    echo -e "  ${YELLOW}2.${NC} ${CYAN}python3 web_obfuscator.py${NC}   - Web interface"
    echo -e "  ${YELLOW}3.${NC} ${CYAN}python3 file_creator.py${NC}     - Advanced file creator"
    echo -e "  ${YELLOW}4.${NC} ${CYAN}python3 pyobfuscator.py${NC}     - Command-line obfuscator"
    echo -e "  ${YELLOW}5.${NC} ${CYAN}python3 pydecoder.py${NC}        - Command-line decoder"
    echo ""
}

# Trap Ctrl+C
trap 'echo -e "\n${YELLOW}Installation cancelled by user${NC}"; exit 1' INT

# Run main function
main "$@"
