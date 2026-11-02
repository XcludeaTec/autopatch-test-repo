import subprocess
import shlex

def execute_user_ping(user_input: str) -> str:
    # Fix the vulnerability by using shlex.quote() and passing command and arguments as a sequence list
    command = shlex.quote(f"ping -c 1 {user_input}")
    try:
        result = subprocess.run(shlex.split(command), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error executing ping: {e.stderr}"