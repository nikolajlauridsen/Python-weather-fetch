import functions as vf
from tkinter import *

print('Fetching weather site...')
file_path_1 = vf.get_image('#dk_days_two_forecast', " 2_day")        # Downloads image and returns path to image
file_path_2 = vf.get_image('#dk_days_three_forecast', " 1 day")
print('Done! Displaying forecast...')

root = Tk()
root.title('Weather forecast.')

# Display image
image_1 = PhotoImage(file=file_path_1)
image_2 = PhotoImage(file=file_path_2)

image_labe_1 = Label(image=image_1)
image_label_2 = Label(image=image_2)

image_labe_1.pack()
image_label_2.pack()

# Keybind esc and return to exit
vf.bindings(root)

root.mainloop()
