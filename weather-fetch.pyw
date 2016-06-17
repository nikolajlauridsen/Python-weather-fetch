import functions as vf
from tkinter import *

print('Fetching weather site...')
# Download image and return path to image
file_path_1 = vf.get_image('#dk_days_two_forecast', " 2_day")
file_path_2 = vf.get_image('#dk_days_three_forecast', " 3_day")
# Return weather warnings as a string
warning = vf.get_warning()
print('Done! Displaying forecast...')

root = Tk()
root.title('Weather forecast.')

# Create image objects
image_1 = PhotoImage(file=file_path_1)
image_2 = PhotoImage(file=file_path_2)

# Create image labes
image_labe_1 = Label(image=image_1)
image_label_2 = Label(image=image_2)
# Create text labels
two_day_label = Label(text="Two day forecast")
three_day_label = Label(text='Three to seven day forecast')
warning_label = Label(text=warning)

# Pack it all in there
warning_label.pack()
two_day_label.pack()
image_labe_1.pack()
three_day_label.pack()
image_label_2.pack()

# Keybind esc and return to exit
vf.bindings(root)

root.mainloop()
