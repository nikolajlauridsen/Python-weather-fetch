import functions as vf
from tkinter import *

print('Henter vejr side...')
file_path = vf.get_image()        # Downloads image and returns path to image
print('Færdig! Viser oversigt...')

root = Tk()
root.title('Vejroversigt')

# Display image
image = PhotoImage(file=file_path)
image_label = Label(image=image)
image_label.pack()

# Keybind esc and return to exit
vf.bindings(root)

root.mainloop()
