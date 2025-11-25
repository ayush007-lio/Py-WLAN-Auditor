import subprocess
import re

def scan_wifi_networks():
    """
    Executes a system command to list available Wi-Fi networks 
    and parses the output into a structured list.
    """
    networks = []
    
    try:
        # Run the Windows command to show networks
        # We use 'chcp 65001' to ensure UTF-8 encoding helps with special characters
        command_output = subprocess.check_output(
            ["netsh", "wlan", "show", "network", "mode=bssid"], 
            shell=True, 
            text=True
        )
        
        # Regex to extract SSID (Name), Authentication, and Signal Strength
        # This parses the raw text block returned by Windows
        network_blocks = command_output.split("SSID")
        
        for block in network_blocks[1:]: # Skip the first empty split
            ssid_match = re.search(r":\s*(.*)", block)
            auth_match = re.search(r"Authentication\s*:\s*(.*)", block)
            encryption_match = re.search(r"Encryption\s*:\s*(.*)", block)
            signal_match = re.search(r"Signal\s*:\s*(\d+)%", block)
            
            if ssid_match:
                ssid = ssid_match.group(1).strip()
                # Skip empty SSIDs (Hidden networks)
                if not ssid: 
                    continue
                    
                auth = auth_match.group(1).strip() if auth_match else "Unknown"
                enc = encryption_match.group(1).strip() if encryption_match else "Unknown"
                signal = signal_match.group(1).strip() if signal_match else "0"
                
                networks.append({
                    "SSID": ssid,
                    "Authentication": auth,
                    "Encryption": enc,
                    "Signal": int(signal)
                })
                
        return networks

    except subprocess.CalledProcessError:
        return []
    except Exception as e:
        print(f"Error during scan: {e}")
        return []