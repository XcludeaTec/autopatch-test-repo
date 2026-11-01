import subprocess

def execute_user_ping(user_input: str) -> str:
    # Vulnerable Command Injection
    command = f"ping -c 1 {user_input}"
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"
