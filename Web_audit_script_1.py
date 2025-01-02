import os
import subprocess
import sys

def run_command(command, output_file):
    """Runs a shell command and writes its output to the given file."""
    try:
        with open(output_file, "a") as f:
            f.write(f"\nRunning: {command}\n")
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()
            f.write(stdout.decode("utf-8"))
            f.write(stderr.decode("utf-8"))
    except Exception as e:
        print(f"Error running command {command}: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python web_audit.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    output_file = "website_audit_report.txt"

    # Clear or create the output file
    with open(output_file, "w") as f:
        f.write(f"Website Audit Report for {url}\n")
        f.write("=" * 50 + "\n\n")

    # Gobuster command
    gobuster_command = f"gobuster dir --url {url} --wordlist /home/kali/Downloads/directory-list-2.3-small.txt"
    run_command(gobuster_command, output_file)

    # SQLMap command (example cookie can be modified as per requirement)
    sqlmap_command = f"sqlmap -u '{url}' --cookie='PHPSESSID=dummy_cookie_value'"
    run_command(sqlmap_command, output_file)

    # SSTI Detection with tplmap
    tplmap_command = f"tplmap -u '{url}'"
    run_command(tplmap_command, output_file)

    print(f"Audit completed. Results written to {output_file}")

if __name__ == "__main__":
    main()



##### python web_audit.py http://example.com

### tplmap: Install via tplmap GitHub repo.