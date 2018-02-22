import os  
ini="""[global] 
index-url = http://pypi.doubanio.com/simple/ 
[install] 
trusted-host=pypi.doubanio.com 
disable-pip-version-check=true 
timeout=600 
"""  
  
pippath=os.environ["USERPROFILE"]+"\\pip\\"  
  
if not os.path.exists(pippath):  
    os.mkdir(pippath)  
  
with open(pippath+"pip.ini","w+") as f:  
    f.write(ini)