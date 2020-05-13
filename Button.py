import wx
def Buton1Click(event):
    frame.SetStatusText('Click1')
def Buton2Click(event):
    frame.SetStatusText('Click2')
def ButonClick(event):
    if event.GetId() == 3333:
        frame.SetStatusText('Click3')
    elif event.GetId() == 4444:
        frame.SetStatusText('Click4')
app = wx.App()
frame = wx.Frame(None, wx.ID_ANY, 'テストフレーム', size=(300, 300))
frame.CreateStatusBar()
panel = wx.Panel(frame, wx.ID_ANY)
panel.SetBackgroundColour('gray') 

button1 =wx.Button(panel, wx.ID_ANY, 'ボタン1')
button2 =wx.Button(panel, wx.ID_ANY, 'ボタン2')
button3 =wx.Button(panel, 3333, 'ボタン3', size=(100,100))
button4 =wx.Button(panel, 4444, 'ボタン4')


# font = wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
# button3.SetFont(font)
# button3.SetBackgroundColour('red')
# button3.SetToolTip('python=izm.com')
# button3.Hide()

button1.Bind(wx.EVT_BUTTON, Buton1Click)
button2.Bind(wx.EVT_BUTTON, Buton2Click)
frame.Bind(wx.EVT_BUTTON, ButonClick, button3)
frame.Bind(wx.EVT_BUTTON, ButonClick, button4)

layout = wx.GridSizer(rows=2, cols=2, gap=(0,0))
# layout.Add(button1, 0, wx.GROW)
# layout.Add(button2, 0, wx.GROW)
# layout.Add(button3, 0, wx.GROW)
# layout.Add(button4, 0, wx.GROW)
layout.Add(button1)
layout.Add(button2)
layout.Add(button3)
layout.Add(button4)
panel.SetSizer(layout)
frame.Show()
app.MainLoop()