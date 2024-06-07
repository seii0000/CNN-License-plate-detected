import tkinter as tk
from PIL import ImageTk, Image

# Recognized license plate
license_plate = "ABC1234"  # replace with your recognized license plate

# Create the main window
root = tk.Tk()

# Create a label for the license plate
label = tk.Label(root, text=f"License Plate: {license_plate}")
label.pack()

# Load and display the image
img = Image.open("path_to_your_image.jpg")  # replace with the path to your image
img = img.resize((500, 300), Image.ANTIALIAS)  # resize the image
img = ImageTk.PhotoImage(img)
panel = tk.Label(root, image=img)
panel.pack()

# Run the GUI
root.mainloop()