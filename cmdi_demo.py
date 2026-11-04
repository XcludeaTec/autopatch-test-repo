import subprocess
import shlex

def execute_user_ping(user_input: str) -> str:
    # Command Injection Defense: Use shlex.quote() to safely construct the command
    command = shlex.quote("ping -c 1 " + user_input)
    try:
        result = subprocess.run(command, shell=False, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error executing command: {e.stderr}"