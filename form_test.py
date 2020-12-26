import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')

from System.Windows.Forms import Application, Button, Form
from System.Drawing import Point

x = 0
y = 0

form = Form()
form.Text = "Hello World"

button = Button(Text="Button Text")

form.Controls.Add(button)

def click(sender, event):
    global x, y
    button.Location = Point(x, y)
    x += 5
    y += 5

button.Click += click

Application.Run(form)
