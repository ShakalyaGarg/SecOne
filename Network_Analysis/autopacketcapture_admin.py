import os 
import subprocess
os.chdir("C:\Program Files\Wireshark")
#system("cmd /k cd C:\Program Files\Wireshark")
"""p = subprocess.Popen(
        "start /wait cmd /k",
        shell=1,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )"""
command = ['cmd.exe', '/c', 'runas', '/user:administrator', 'regedit']
p = subprocess.Popen(command, stdin=subprocess.PIPE)
pw="10052004"
pw_bytes=pw.encode("ascii")
print(pw_bytes)
p.stdin.write(pw_bytes)
p.communicate()
os.system("cmd /k tshark -i Wi-Fi -a duration:10 -w test_capture.pcapng")
print("end")
