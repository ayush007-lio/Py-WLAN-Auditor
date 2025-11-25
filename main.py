from scanner import scan_wifi_networks
from analyzer import analyze_security, suggest_improvements
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from rich.progress import track
import time
import os

console = Console()

# --- CONFIGURATION: PUT YOUR DETAILS HERE ---
AUTHOR_NAME = "Ayush S"  # e.g., "Eng. Rahul"
ROLE_TITLE = "Cyber Security Researcher"
PROJECT_NAME = "Wi-Fi Sentinel v1.0"
GITHUB_ID = "https://github.com/ayush007-lio"
# ---------------------------------------------

def display_signature():
    """
    Displays a professional 'Hacker-Style' banner with author details.
    """
    # clear terminal for a clean start
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Create the content for the panel
    signature_text = Text()
    signature_text.append(f"\n{PROJECT_NAME}\n", style="bold cyan")
    signature_text.append("="*30 + "\n", style="dim white")
    signature_text.append(f"DEVELOPED BY : {AUTHOR_NAME}\n", style="bold green")
    signature_text.append(f"ROLE         : {ROLE_TITLE}\n", style="yellow")
    signature_text.append(f"GITHUB       : {GITHUB_ID}\n", style="blue")
    signature_text.append("="*30 + "\n", style="dim white")
    signature_text.append("AUTHORIZED USE ONLY", style="bold red blink")

    # Create a panel box around the text
    banner_panel = Panel(
        Align.center(signature_text),
        border_style="cyan",
        title="[ SYSTEM INITIALIZED ]",
        subtitle=f"[ {AUTHOR_NAME} ]"
    )
    
    console.print(banner_panel)
    console.print("\n")

def main():
    # 1. Show the Author Signature
    display_signature()
    
    console.print("[yellow][*] Loading modules...[/yellow]")
    
    # Simulate a loading bar for effect
    for _ in track(range(15), description="[green][*] Calibrating Wireless Interface...[/green]"):
        time.sleep(0.1)
        
    networks = scan_wifi_networks()
    
    if not networks:
        console.print("[bold red][!] No networks found or Wi-Fi interface not active.[/bold red]")
        return

    # Create a table for results
    table = Table(title="SCAN RESULTS", show_header=True, header_style="bold magenta")
    table.add_column("SSID", style="white")
    table.add_column("Signal", justify="right")
    table.add_column("Protocol", style="cyan")
    table.add_column("Status", justify="center")
    table.add_column("Advisory", style="italic")

    secure_count = 0
    risk_count = 0

    for net in networks:
        risk_level, reason = analyze_security(net['Authentication'], net['Encryption'])
        recommendation = suggest_improvements(risk_level)
        
        # Color coding the output
        if "CRITICAL" in risk_level or "HIGH RISK" in risk_level:
            security_display = f"[bold red]{risk_level}[/bold red]"
            risk_count += 1
        elif "SECURE" in risk_level:
            security_display = f"[bold green]{risk_level}[/bold green]"
            secure_count += 1
        else:
            security_display = f"[yellow]{risk_level}[/yellow]"

        table.add_row(
            net['SSID'], 
            f"{net['Signal']}%", 
            net['Authentication'], 
            security_display,
            recommendation
        )

    console.print(table)
    
    # Summary Panel
    console.print("\n")
    summary_text = f"""
    [bold]Total Networks:[/bold] {len(networks)}
    [green]Secure:[/green] {secure_count} | [red]Vulnerable:[/red] {risk_count}
    """
    console.print(Panel(summary_text, title="Assessment Summary", border_style="white"))

    # 2. Final Footer Signature
    console.print(f"\n[dim]Audit Complete. Tool built by {AUTHOR_NAME}.[/dim]")

if __name__ == "__main__":
    main()