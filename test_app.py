import wx
# import os
from pathlib import Path

class HelloFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="Hello World")
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(wx.StaticText(panel, label="Hello from test app", pos=(25, 25)), 0, wx.ALL, 5)
        
        # Any of the following will cause notarization to fail
        # file_path = os.path.abspath(__file__)
        file_path = str(Path(__file__).parent.absolute())
        # file_path = str(Path("~/Desktop/").expanduser())
        
        sizer.Add(wx.StaticText(panel, label="Running from " + file_path), 0, wx.ALL, 5)
        panel.SetSizer(sizer)
        self.Bind(wx.EVT_CLOSE, self.on_close)
        self.Show()
    
    def on_close(self, _):
        # needed to prevent segfault on close
        self.Destroy()

if __name__ == '__main__':
    app = wx.App()
    frame = HelloFrame()
    app.MainLoop()