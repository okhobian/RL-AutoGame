import pywinauto

app_name = "C:\\Program Files\\BlueStacks\\Bluestacks.exe"

# app = pywinauto.application.Application()
# app.start(app_name)

app = pywinauto.Application().connect(path=app_name)
app.MainDialog.print_control_identifiers()
# dlg = app['BlueStacks']
# app.dlg.print_control_identifiers()
# app.MainDialog.click_input(coords=(953, 656))

# print(app.process_id())

# hwin = app.top_window()
# hwin.set_focus()
# img = hwin.capture_as_image()
# img.save('ss.png')