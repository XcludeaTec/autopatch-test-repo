import subprocess
import shlex

def execute_user_ping(user_input: str) -> str:
    try:
        # Use shlex.quote to safely quote user input
        command = shlex.quote(f"ping -c 1 {user_input}")
        result = subprocess.run(command, shell=False, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"