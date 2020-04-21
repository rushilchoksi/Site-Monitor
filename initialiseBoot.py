import winreg as reg  
import os              
  
def AddToRegistry(): 
    pth = os.path.dirname(os.path.realpath(__file__))
    s_name = "automationCheck.py"
    address = os.getcwd()+"\\"+s_name
    key = reg.HKEY_CURRENT_USER 
    key_value = "Software\Microsoft\Windows\CurrentVersion\Run"
    open = reg.OpenKey(key,key_value,0,reg.KEY_ALL_ACCESS) 
    reg.SetValueEx(open,"any_name",0,reg.REG_SZ,address) 
    reg.CloseKey(open)
    print("Done")
  
if __name__ == "__main__": 
    AddToRegistry() 
