# GUI app

import wx
import os
import verify_db
import db_check
import datetime, time


global check_dir
global check_loc
global check_last
global save_dir
global save_loc
global save_last
global file_list
global move_box_title
global move_list
global action_date
global move_date

class window(wx.Frame):        
    def __init__(self, title):

        global check_dir
        global check_loc
        global check_last
        global save_dir
        global save_loc
        global save_last
        global file_list
        global move_box_title
        global move_list
        global action_date
        global move_date

        check_dir = os.getcwd()
        save_dir = os.getcwd()

        file_list = []
        action_date = []
        move_date = []
        verify_db.db_initialize()
        
        db_check.viewLastCheck(action_date)
        db_check.viewLastMove(move_date)

        action_date = ''.join(action_date)
        action_date = time.ctime((float(action_date)))
        print action_date
        
        move_date = ''.join(move_date)
        move_date = time.ctime((float(move_date)))
        print move_date
              
          
        wx.Frame.__init__(self, None, wx.ID_ANY, title=title, size=(640, 480))

        self.panel = wx.Panel(self, wx.ID_ANY)
               
        menuBar = wx.MenuBar()

        fileMenu = wx.Menu()
        menuBar.Append(fileMenu, "&File")


        move_box_title = wx.StaticBox(self.panel, label='Select folders to check:', pos=(250, 10), size = (300, 220))
        move_list = wx.StaticText(self.panel, label='', pos=(260, 30))
                
        wx.StaticBox(self.panel, label='Location to be checked:', pos=(10, 280), size=(605, 50))
        check_loc = wx.StaticText(self.panel, label=check_dir, pos=(50, 300))        

        chkDirButton = wx.Button(self.panel, label="...", pos=(20, 300), size=(20, 20))
        chkDirButton.Bind (wx.EVT_BUTTON, self.chkDir)

        
        wx.StaticBox(self.panel, label='Location to be save copies:', pos=(10,340), size=(605,50))
        save_loc = wx.StaticText(self.panel, label=save_dir, pos=(50, 360))

        savDirButton = wx.Button(self.panel, label="...", pos=(20, 360), size=(20, 20))
        savDirButton.Bind (wx.EVT_BUTTON, self.savDir)

        
        button = wx.Button(self.panel, label="Check now", pos=(40,40), size=(100,40))
        button.Bind (wx.EVT_BUTTON, self.file_check)
        check_last = wx.StaticText(self.panel, label='Last Checked: '+ action_date , pos=(20, 100))
        
        
        button = wx.Button(self.panel, label="Move now", pos=(40,140), size=(100,40))
        button.Bind (wx.EVT_BUTTON, self.file_move)
        save_last = wx.StaticText(self.panel, label='Last Moved: '+ move_date, pos=(20, 200))
        

                
        button = wx.Button(self.panel, label="Exit", size=(40,40), pos=(575,10))
        button.Bind (wx.EVT_BUTTON, self.exit)
        
        exitItem = fileMenu.Append(wx.NewId(), "E&xit", "Exit the program")

        
        self.Bind(wx.EVT_MENU, self.exit, exitItem)


        self.SetMenuBar(menuBar)
        self.CreateStatusBar()
    
    def chkDir(self, event):
        global check_dir
        global check_loc
        
        path= os.getcwd()
        dlg = wx.DirDialog(self, "Directory to check", 
            style=wx.DD_DEFAULT_STYLE|wx.DD_DIR_MUST_EXIST|wx.DD_CHANGE_DIR)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
        dlg.Destroy()
        check_dir = path

        check_loc.SetLabel(check_dir)

        print check_dir
        return check_dir
        
    def savDir(self, event):
        global save_dir
        global save_loc
        
        path= os.getcwd()
        dlg = wx.DirDialog(self, "Directory to save", 
            style=wx.DD_DEFAULT_STYLE|wx.DD_DIR_MUST_EXIST|wx.DD_CHANGE_DIR)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
        dlg.Destroy()
        save_dir = path

        save_loc.SetLabel(save_dir)
        
        print save_dir
        return save_dir


    def file_check(self, event):
        global check_dir
        global save_dir
        global file_list
        global move_list

        file_list = []
        
        verify_db.file_check(check_dir, save_dir, file_list)
        
        print file_list

        fl = str(file_list)
        fl1 = fl.replace("[", "\n")
        fl2 = fl1.replace("u'", '')
        fl3 = fl2.replace(', ', '\n')
        fl4 = fl3.replace("]", '\n')
        fl5 = fl4.replace("'", '')

        print fl5
        
        move_list.SetLabel(fl5)
        move_box_title.SetLabel('These files will be moved:')

        action_date = []
        db_check.viewLastCheck(action_date)

        action_date = ''.join(action_date)
        action_date = time.ctime((float(action_date)))
        print action_date
        
        check_last.SetLabel('Last Checked: '+ action_date)


    def file_move(self, event):
        global check_dir
        global save_dir
        global file_list
        global move_list

        file_list = []

        move_list = wx.StaticText(self.panel, label='', pos=(260, 30))
               
        verify_db.file_move(check_dir, save_dir, file_list)
        
        print file_list

        fl = str(file_list)
        fl1 = fl.replace("[", "\n")
        fl2 = fl1.replace("u'", '')
        fl3 = fl2.replace(', ', '\n')
        fl4 = fl3.replace("]", '\n')
        fl5 = fl4.replace("'", '')

        print fl5
        
        move_list.SetLabel(fl5)
        move_box_title.SetLabel('These files were moved:')

        move_date = []
        db_check.viewLastMove(move_date)
        print move_date

        move_date = ''.join(move_date)
        move_date = time.ctime((float(move_date)))
        print move_date
        
        save_last.SetLabel('Last Moved: '+ move_date)


    def exit(self, event):
        self.Destroy()


app = wx.App()
frame = window("File Check")
frame.Show()
app.MainLoop()
