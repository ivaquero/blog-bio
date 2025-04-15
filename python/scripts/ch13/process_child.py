from subprocess import PIPE
from subprocess import Popen

print("$nslookup")
p = Popen(["nslookup"], stdin=PIPE, stdout=PIPE, stderr=PIPE)
output, err = p.communicate(b"set q=mx\npython.org!=xit\n")
print(output.decode("utf-8"))
print("Exit code:", p.returncode)
