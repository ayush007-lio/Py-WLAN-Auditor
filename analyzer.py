def analyze_security(auth_type, encryption):
    """
    Analyzes the authentication type and returns a security score and status.
    """
    auth_type = auth_type.upper()
    
    if "OPEN" in auth_type:
        return "CRITICAL", "No Encryption (Data visible to anyone)"
    elif "WEP" in auth_type:
        return "HIGH RISK", "Obsolete Encryption (Easily cracked)"
    elif "WPA2" in auth_type or "WPA3" in auth_type:
        return "SECURE", "Modern Encryption Standard"
    elif "WPA" in auth_type:
        return "MODERATE", "Older Standard (Vulnerable to dictionary attacks)"
    else:
        return "UNKNOWN", "Manual Verification Required"

def suggest_improvements(status):
    if status == "CRITICAL":
        return "Action: AVOID. Use a VPN if you must connect."
    elif status == "HIGH RISK":
        return "Action: Upgrade router to WPA2/WPA3 immediately."
    elif status == "SECURE":
        return "Action: Safe to connect (Ensure strong password)."
    else:
        return "Action: Proceed with caution."