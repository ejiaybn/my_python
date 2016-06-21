import subprocess;

#Open the total commander application#
ps1 = subprocess.Popen(r'"e:\download\totalcmd\TOTALCMD64.EXE"')
ps1.wait

#Open the outlook application#
ps2 = subprocess.Popen(r'"c:\Program Files (x86)\Microsoft Office\root\Office16\ONENOTE.EXE"')
ps2.wait