🛡️ Wi-Fi Sentinel - Network Security Auditor

    A professional command-line interface (CLI) tool for scanning, analyzing, and auditing local wireless networks for security vulnerabilities.

📖 Overview

    Wi-Fi Sentinel is a cybersecurity prototype designed to demonstrate network reconnaissance and security assessment techniques. It automates the process of discovering nearby Wi-Fi networks and evaluating their encryption protocols (WEP, WPA2, WPA3, Open) to identify potential security risks.
    
    Built with Python and the Rich library, it features a hacker-style terminal interface that provides real-time feedback and actionable security advice.

✨ Key Features

    📡 Automated Scanning: Instantly detects all available Wi-Fi access points in range using system interfaces.
    
    🔓 Vulnerability Detection: Identifies risky networks (Open/No Encryption) and obsolete protocols (WEP).
    
    📊 Security Grading: automatically classifies networks as SECURE, MODERATE, or CRITICAL.
    
    🖥️ Professional UI: Features a modern, color-coded terminal dashboard with loading bars and data tables.
    
    📝 Actionable Reporting: Provides specific recommendations for every network detected.

🛠️ Tech Stack & Modules

    The project is structured into modular Python scripts to simulate real-world software architecture:
    
    <img width="958" height="513" alt="Screenshot (32)" src="https://github.com/user-attachments/assets/a295956a-6ba3-4d8b-9e1a-1704e3578022" />


🚀 How to Run

    Prerequisites
    
        OS: Windows 10/11 (Uses netsh command).
        
        Python: Version 3.x installed.
    
    Installation Steps
    
        Clone the Repository
        
        git clone [https://github.com/ayush007-lio/WiFi-Sentinel.git](https://github.com/ayush007-lio/WiFi-Sentinel.git)
        cd WiFi-Sentinel
    
    
    Install Dependencies
        This tool requires the rich library for the interface.
        
        pip install -r requirements.txt
    
    
    Run the Auditor
        Execute the main script:
        
        python main.py


⚙️ How It Works (Under the Hood)

        Initialization: When you run main.py, the tool displays the author's digital signature and checks for system compatibility.
    
    Scanning Phase:
    
        The scan_wifi_networks() function in scanner.py executes a shell command (netsh wlan show network).
        
        It captures the raw text output and uses Regular Expressions (Regex) to extract clean data: SSID (Name), Signal Strength, and Authentication type.
        
    Analysis Phase:
    
        The raw data is passed to analyzer.py.
        
        The analyze_security() function checks the encryption strings.
        
        Logic Example: If Authentication == "Open", the status is set to CRITICAL. If WPA2, it is set to SECURE.
        
    Rendering:
    
        The results are sent back to main.py.
        
        The rich library compiles the data into a neat table with color-coded risk levels (Red for danger, Green for safe) and prints it to the user's console.

📸 Demo Output

<img width="587" height="124" alt="Screenshot (34)" src="https://github.com/user-attachments/assets/b233af42-0027-4db4-ad58-41e6a4c151ee" />



⚠️ Legal Disclaimer

    AUTHORIZED USE ONLY.
    
    This tool is created for educational purposes and for auditing networks you own or have explicit permission to test. Unauthorized scanning or accessing of networks is illegal. The developer assumes no liability for misuse of this software.

👨‍💻 Author

    Ayush S

Role: Cyber Security Researcher

GitHub: @ayush007-lio

