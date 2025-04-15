import os
from subprocess import PIPE
from subprocess import Popen


def run_encrypt(data):
    env = os.environ.copy()
    env["password"] = "zf7ShyBhZOraQDdE/FiZpm/m/8f9X+M1"
    proc = Popen(
        ["openssl", "enc", "-pbkdf2", "-pass", "env:password"],
        env=env,
        stdin=PIPE,
        stdout=PIPE,
    )
    proc.stdin.write(data)
    proc.stdin.flush()  # Ensure that the child gets input
    return proc


procs = []
for _ in range(3):
    data = os.urandom(10)
    proc = run_encrypt(data)
    procs.append(proc)

for proc in procs:
    out, _ = proc.communicate()
    print(out[-10:])
