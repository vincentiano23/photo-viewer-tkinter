from tkinter import *
from PIL import ImageTk, Image

# Initialize root window
root = Tk()
root.title("Image Viewer App")

# Define image resizing function
def resize_image(image_path, width, height):
    img = Image.open(image_path)
    return img.resize((width, height))

# Set a consistent size for the images
image_width, image_height = 500, 500

# Load and resize images
img_1 = ImageTk.PhotoImage(resize_image("img1.jpg", image_width, image_height))
img_2 = ImageTk.PhotoImage(resize_image("img2.jpg", image_width, image_height))
img_3 = ImageTk.PhotoImage(resize_image("img3.jpg", image_width, image_height))
img_4 = ImageTk.PhotoImage(resize_image("img4.jpg", image_width, image_height))

# List of images
image_list = [img_1, img_2, img_3, img_4]

# Label to hold images
my_label = Label(image=img_1)
my_label.grid(row=0, column=0, columnspan=3)

# Define the forward and back functionality
def forward(image_number):
    global my_label
    global button_forward
    global button_back

    # Remove the current image and update it with the next one
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    my_label.grid(row=0, column=0, columnspan=3)

    # Update the forward button
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    # Disable the forward button when the user reaches the last image
    if image_number == len(image_list):
        button_forward = Button(root, text=">>", state=DISABLED)

    button_back.grid(row=1, column=0)
    button_exit.grid(row=1, column=1)
    button_forward.grid(row=1, column=2)

def back(image_number):
    global my_label
    global button_forward
    global button_back

    # Remove the current image and update it with the previous one
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    my_label.grid(row=0, column=0, columnspan=3)

    # Update the back button
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    # Disable the back button when the user reaches the first image
    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    button_back.grid(row=1, column=0)
    button_exit.grid(row=1, column=1)
    button_forward.grid(row=1, column=2)

# Exit button functionality
button_exit = Button(root, text="EXIT PROGRAM", command=root.quit)

# Initialize the first image and buttons
button_back = Button(root, text="<<", command=back, state=DISABLED)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

# Start the main event loop
root.mainloop()
