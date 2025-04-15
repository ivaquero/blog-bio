import os

print(f"Process ({os.getpid()}) start...")
# Only works on Unix/Linux/Mac:
pid = os.fork()
if pid == 0:
    print(f"I am child process ({os.getpid()}) and my parent is {os.getppid}.")
else:
    print(f"I ({os.getpid()}) just created a child process ({pid}).")
