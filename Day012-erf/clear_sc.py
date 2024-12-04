import os,time,subprocess
def clear_screen():
  if os.name == 'nt':
    subprocess.call('cls',shell=True)
  else: 
    subprocess.call('clear',shell=True)
