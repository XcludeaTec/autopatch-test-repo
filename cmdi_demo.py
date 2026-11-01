import subprocess
import shlex

def execute_user_ping(user_input: str) -> str:
    # Command Injection Defense: Use shlex.quote() if string command construction is unavoidable.
    # Prefer high-level Python standard libraries (e.g., os.path, shutil, ipaddress) over shell commands.
    try:
        command = shlex.quote(f"ping -c 1 {user_input}")
        result = subprocess.run(command, shell=False, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error executing command: {e.stderr}"