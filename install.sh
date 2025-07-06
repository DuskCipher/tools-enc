
#!/bin/bash

# DUSK CIPHER Universal Installation Script
# Compatible with Linux, Termux, and Replit

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
MAGENTA='\033[0;35m'
NC='\033[0m'

# Global variables
PYTHON_CMD=""
ENV_TYPE=""
PACKAGE_MANAGER=""

print_status() {
    echo -e "${GREEN}✓${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

print_error() {
    echo -e "${RED}✗${NC} $1"
}

print_info() {
    echo -e "${BLUE}ℹ${NC} $1"
}

print_header() {
    clear
    echo -e "${CYAN}╔══════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${CYAN}║${YELLOW}                    DUSK CIPHER INSTALLER                    ${CYAN} ║${NC}"
    echo -e "${CYAN}║${BLUE}              Professional Encryption Toolkit              ${CYAN}   ║${NC}"
    echo -e "${CYAN}║${MAGENTA}             Universal Installer (Linux/Termux)            ${CYAN}   ║${NC}"
    echo -e "${CYAN}╚══════════════════════════════════════════════════════════════╝${NC}"
    echo ""
}

detect_environment() {
    print_info "Detecting environment..."

    # Check for Replit
    if [[ -n "$REPL_ID" ]] || [[ -n "$REPLIT_CLI" ]] || [[ -d "/nix" ]]; then
        ENV_TYPE="replit"
        PACKAGE_MANAGER="nix"
        print_status "Environment: Replit"
        return 0
    fi

    # Check for Termux
    if [[ -n "$TERMUX_VERSION" ]] || [[ -d "/data/data/com.termux" ]] || [[ "$PREFIX" == *"termux"* ]]; then
        ENV_TYPE="termux"
        PACKAGE_MANAGER="pkg"
        print_status "Environment: Termux"
        return 0
    fi

    # Check for standard Linux distributions
    if [[ -f "/etc/os-release" ]]; then
        source /etc/os-release
        ENV_TYPE="linux"
        
        # Detect package manager
        if command -v apt >/dev/null 2>&1; then
            PACKAGE_MANAGER="apt"
        elif command -v yum >/dev/null 2>&1; then
            PACKAGE_MANAGER="yum"
        elif command -v dnf >/dev/null 2>&1; then
            PACKAGE_MANAGER="dnf"
        elif command -v pacman >/dev/null 2>&1; then
            PACKAGE_MANAGER="pacman"
        elif command -v zypper >/dev/null 2>&1; then
            PACKAGE_MANAGER="zypper"
        else
            PACKAGE_MANAGER="unknown"
        fi
        
        print_status "Environment: Linux ($ID)"
        print_status "Package Manager: $PACKAGE_MANAGER"
        return 0
    fi

    # Fallback - assume generic Linux
    ENV_TYPE="linux"
    PACKAGE_MANAGER="unknown"
    print_warning "Environment: Generic Linux (package manager unknown)"
}

check_python() {
    print_info "Checking Python installation..."

    # Check for Python 3
    if command -v python3 >/dev/null 2>&1; then
        PYTHON_VERSION=$(python3 --version 2>&1 | grep -oP '\d+\.\d+')
        print_status "Python $PYTHON_VERSION detected ✓"
        PYTHON_CMD="python3"
        return 0
    elif command -v python >/dev/null 2>&1; then
        PYTHON_VERSION=$(python --version 2>&1 | grep -oP '\d+\.\d+')
        # Check if it's Python 3
        if python -c "import sys; exit(0 if sys.version_info[0] >= 3 else 1)" 2>/dev/null; then
            print_status "Python $PYTHON_VERSION detected ✓"
            PYTHON_CMD="python"
            return 0
        else
            print_error "Python 2 detected, but Python 3 is required"
            return 1
        fi
    else
        print_error "Python not found"
        return 1
    fi
}

install_python() {
    print_info "Installing Python..."

    case "$ENV_TYPE" in
        "termux")
            print_info "Installing Python via Termux..."
            if ! pkg update && pkg install -y python; then
                print_error "Failed to install Python via pkg"
                return 1
            fi
            ;;
        "linux")
            case "$PACKAGE_MANAGER" in
                "apt")
                    print_info "Installing Python via apt..."
                    if ! sudo apt update && sudo apt install -y python3 python3-pip; then
                        print_error "Failed to install Python via apt"
                        return 1
                    fi
                    ;;
                "yum"|"dnf")
                    print_info "Installing Python via $PACKAGE_MANAGER..."
                    if ! sudo $PACKAGE_MANAGER install -y python3 python3-pip; then
                        print_error "Failed to install Python via $PACKAGE_MANAGER"
                        return 1
                    fi
                    ;;
                "pacman")
                    print_info "Installing Python via pacman..."
                    if ! sudo pacman -S --noconfirm python python-pip; then
                        print_error "Failed to install Python via pacman"
                        return 1
                    fi
                    ;;
                "zypper")
                    print_info "Installing Python via zypper..."
                    if ! sudo zypper install -y python3 python3-pip; then
                        print_error "Failed to install Python via zypper"
                        return 1
                    fi
                    ;;
                *)
                    print_error "Unknown package manager. Please install Python manually."
                    return 1
                    ;;
            esac
            ;;
        "replit")
            print_warning "Python should be pre-installed in Replit"
            return 1
            ;;
        *)
            print_error "Unknown environment type"
            return 1
            ;;
    esac

    print_status "Python installation completed ✓"
}

install_dependencies() {
    print_info "Installing additional dependencies..."

    case "$ENV_TYPE" in
        "termux")
            print_info "Installing Termux dependencies..."
            pkg install -y git curl wget || true
            ;;
        "linux")
            case "$PACKAGE_MANAGER" in
                "apt")
                    sudo apt install -y git curl wget || true
                    ;;
                "yum"|"dnf")
                    sudo $PACKAGE_MANAGER install -y git curl wget || true
                    ;;
                "pacman")
                    sudo pacman -S --noconfirm git curl wget || true
                    ;;
                "zypper")
                    sudo zypper install -y git curl wget || true
                    ;;
            esac
            ;;
        "replit")
            print_info "Dependencies should be available in Replit"
            ;;
    esac

    print_status "Dependencies installation completed ✓"
}

set_permissions() {
    print_info "Setting file permissions..."

    # Make Python scripts executable
    chmod +x *.py 2>/dev/null || true
    chmod +x *.sh 2>/dev/null || true

    # Special permissions for Termux
    if [[ "$ENV_TYPE" == "termux" ]]; then
        # Termux might need special handling
        termux-fix-shebang *.py 2>/dev/null || true
        termux-fix-shebang *.sh 2>/dev/null || true
    fi

    print_status "File permissions set ✓"
}

create_directories() {
    print_info "Creating project directories..."

    # Create directories if they don't exist
    mkdir -p logs 2>/dev/null || true
    mkdir -p output 2>/dev/null || true
    mkdir -p temp 2>/dev/null || true
    mkdir -p backups 2>/dev/null || true

    # Set appropriate permissions
    chmod 755 logs output temp backups 2>/dev/null || true

    print_status "Project directories created ✓"
}

verify_installation() {
    print_info "Verifying installation..."

    # Check if main scripts exist
    MAIN_SCRIPTS=("dusk_cipher.py" "pyobfuscator.py" "pydecoder.py" "web_obfuscator.py" "file_creator.py")

    for script in "${MAIN_SCRIPTS[@]}"; do
        if [ ! -f "$script" ]; then
            print_error "$script not found"
            return 1
        fi
    done

    # Test Python basic modules
    if $PYTHON_CMD -c "import base64, json, os, sys, pathlib, re, time, argparse" >/dev/null 2>&1; then
        print_status "Core modules ready ✓"
    else
        print_error "Some Python modules are missing"
        return 1
    fi

    # Test script execution
    if $PYTHON_CMD -c "print('Python test successful')" >/dev/null 2>&1; then
        print_status "Python execution test passed ✓"
    else
        print_error "Python execution test failed"
        return 1
    fi

    print_status "All components verified ✓"
}

show_environment_info() {
    echo ""
    echo -e "${CYAN}╔══════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${CYAN}║${YELLOW}                    ENVIRONMENT INFO                         ${CYAN} ║${NC}"
    echo -e "${CYAN}╚══════════════════════════════════════════════════════════════╝${NC}"
    echo ""
    echo -e "${GREEN}Environment Details:${NC}"
    echo -e "  ${CYAN}•${NC} Type: $ENV_TYPE"
    echo -e "  ${CYAN}•${NC} Package Manager: $PACKAGE_MANAGER"
    echo -e "  ${CYAN}•${NC} Python Command: $PYTHON_CMD"
    echo -e "  ${CYAN}•${NC} Python Version: $($PYTHON_CMD --version 2>/dev/null || echo 'Not detected')"
    echo -e "  ${CYAN}•${NC} Installation Directory: $(pwd)"
    
    if [[ "$ENV_TYPE" == "termux" ]]; then
        echo -e "  ${CYAN}•${NC} Termux Version: ${TERMUX_VERSION:-Unknown}"
        echo -e "  ${CYAN}•${NC} Architecture: $(uname -m)"
    elif [[ "$ENV_TYPE" == "linux" ]] && [[ -f "/etc/os-release" ]]; then
        source /etc/os-release
        echo -e "  ${CYAN}•${NC} OS: $PRETTY_NAME"
        echo -e "  ${CYAN}•${NC} Kernel: $(uname -r)"
    fi
}

show_usage() {
    echo ""
    echo -e "${CYAN}╔══════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${CYAN}║${YELLOW}                        USAGE GUIDE                          ${CYAN} ║${NC}"
    echo -e "${CYAN}╚══════════════════════════════════════════════════════════════╝${NC}"
    echo ""

    echo -e "${GREEN}Available Tools:${NC}"
    echo -e "  ${YELLOW}$PYTHON_CMD dusk_cipher.py${NC}      - Main encryption toolkit (interactive)"
    echo -e "  ${YELLOW}$PYTHON_CMD pyobfuscator.py${NC}     - Command-line obfuscator"
    echo -e "  ${YELLOW}$PYTHON_CMD pydecoder.py${NC}        - Command-line decoder"
    echo -e "  ${YELLOW}$PYTHON_CMD web_obfuscator.py${NC}   - Web interface"
    echo -e "  ${YELLOW}$PYTHON_CMD file_creator.py${NC}     - Advanced file creator"
    echo ""
    echo -e "${GREEN}Quick Start:${NC}"
    echo -e "  ${CYAN}1.${NC} Run: ${YELLOW}$PYTHON_CMD dusk_cipher.py${NC}"
    echo -e "  ${CYAN}2.${NC} Choose option 1 to encrypt a Python file"
    echo -e "  ${CYAN}3.${NC} Choose option 2 to decrypt an encrypted file"
    echo -e "  ${CYAN}4.${NC} Choose option 9 for web interface"
    echo ""
    
    if [[ "$ENV_TYPE" != "termux" ]]; then
        echo -e "${GREEN}Web Interface:${NC}"
        echo -e "  ${CYAN}•${NC} Run: ${YELLOW}$PYTHON_CMD web_obfuscator.py${NC}"
        echo -e "  ${CYAN}•${NC} Open browser to: ${YELLOW}http://0.0.0.0:5000${NC}"
        echo ""
    fi

    # Environment-specific tips
    case "$ENV_TYPE" in
        "termux")
            echo -e "${GREEN}Termux Tips:${NC}"
            echo -e "  ${CYAN}•${NC} Use ${YELLOW}pkg update${NC} to keep packages updated"
            echo -e "  ${CYAN}•${NC} Grant storage permission: ${YELLOW}termux-setup-storage${NC}"
            echo -e "  ${CYAN}•${NC} For better performance, use ${YELLOW}pkg install clang${NC}"
            ;;
        "linux")
            echo -e "${GREEN}Linux Tips:${NC}"
            echo -e "  ${CYAN}•${NC} Use sudo for system-wide installations"
            echo -e "  ${CYAN}•${NC} Keep your system updated with ${YELLOW}$PACKAGE_MANAGER update${NC}"
            ;;
        "replit")
            echo -e "${GREEN}Replit Tips:${NC}"
            echo -e "  ${CYAN}•${NC} Use the Run button to start the application"
            echo -e "  ${CYAN}•${NC} Web interface will be automatically exposed"
            ;;
    esac
}

main() {
    print_header
    
    # Detect environment first
    detect_environment
    
    print_status "Starting DUSK CIPHER installation for $ENV_TYPE..."
    echo ""

    # Check Python installation
    if ! check_python; then
        print_warning "Python not found, attempting to install..."
        if ! install_python; then
            print_error "Python installation failed"
            exit 1
        fi
        # Recheck after installation
        if ! check_python; then
            print_error "Python installation verification failed"
            exit 1
        fi
    fi

    # Install additional dependencies
    install_dependencies

    # Setup environment
    set_permissions
    create_directories

    # Verify installation
    if ! verify_installation; then
        print_error "Installation verification failed"
        exit 1
    fi

    echo ""
    print_status "Installation completed successfully! 🎉"

    # Show environment info
    show_environment_info

    # Show usage information
    show_usage

    echo ""
    echo -e "${GREEN}Installation Summary:${NC}"
    echo -e "  ${CYAN}•${NC} Environment: $ENV_TYPE"
    echo -e "  ${CYAN}•${NC} Package Manager: $PACKAGE_MANAGER"
    echo -e "  ${CYAN}•${NC} Python version: $($PYTHON_CMD --version 2>/dev/null || echo 'Not detected')"
    echo -e "  ${CYAN}•${NC} All main scripts are ready to use"
    echo ""
    echo -e "${CYAN}Happy encrypting with DUSK CIPHER! 🔐${NC}"

    # Ask user if they want to launch the tool immediately
    echo ""
    echo -ne "${YELLOW}Launch DUSK CIPHER now? (Y/n): ${NC}"
    read -r launch_choice

    if [[ "$launch_choice" =~ ^[Nn]$ ]]; then
        echo -e "${CYAN}You can start DUSK CIPHER anytime with: ${YELLOW}$PYTHON_CMD dusk_cipher.py${NC}"
    else
        echo -e "${GREEN}🚀 Launching DUSK CIPHER...${NC}"
        echo ""
        $PYTHON_CMD dusk_cipher.py
    fi
}

# Function to show help
show_help() {
    print_header
    echo -e "${GREEN}DUSK CIPHER Universal Installer Help${NC}"
    echo ""
    echo -e "${YELLOW}Usage:${NC}"
    echo -e "  ${CYAN}bash install.sh${NC}          - Install DUSK CIPHER"
    echo -e "  ${CYAN}bash install.sh --help${NC}   - Show this help"
    echo -e "  ${CYAN}bash install.sh --version${NC} - Show version info"
    echo ""
    echo -e "${YELLOW}Supported Environments:${NC}"
    echo -e "  ${CYAN}•${NC} Linux (Ubuntu, Debian, CentOS, Fedora, Arch, openSUSE)"
    echo -e "  ${CYAN}•${NC} Termux (Android)"
    echo -e "  ${CYAN}•${NC} Replit (Online IDE)"
    echo ""
    echo -e "${YELLOW}This installer:${NC}"
    echo -e "  ${CYAN}•${NC} Auto-detects your environment"
    echo -e "  ${CYAN}•${NC} Installs Python if needed"
    echo -e "  ${CYAN}•${NC} Sets up file permissions"
    echo -e "  ${CYAN}•${NC} Creates necessary directories"
    echo -e "  ${CYAN}•${NC} Verifies all components"
    echo ""
    echo -e "${YELLOW}Package Managers Supported:${NC}"
    echo -e "  ${CYAN}•${NC} apt (Ubuntu/Debian)"
    echo -e "  ${CYAN}•${NC} yum/dnf (CentOS/Fedora)"
    echo -e "  ${CYAN}•${NC} pacman (Arch Linux)"
    echo -e "  ${CYAN}•${NC} zypper (openSUSE)"
    echo -e "  ${CYAN}•${NC} pkg (Termux)"
    echo ""
}

# Trap Ctrl+C
trap 'echo -e "\n${YELLOW}Installation cancelled by user${NC}"; exit 1' INT

# Check for command line arguments
case "${1:-}" in
    "--help"|"-h")
        show_help
        exit 0
        ;;
    "--version"|"-v")
        print_header
        echo -e "${GREEN}DUSK CIPHER Universal Installer${NC}"
        echo -e "${CYAN}Version: 2.0${NC}"
        echo -e "${CYAN}Compatible with: Linux, Termux, Replit${NC}"
        echo ""
        exit 0
        ;;
    "")
        # No arguments, proceed with installation
        ;;
    *)
        echo -e "${RED}Unknown option: $1${NC}"
        echo -e "Use ${YELLOW}--help${NC} for usage information"
        exit 1
        ;;
esac

# Run main function
main "$@"
