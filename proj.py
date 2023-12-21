# Modules Imported
from tkinter import *
from tkinter import colorchooser
from tkinter import filedialog
from PIL import ImageTk, ImageFilter, ImageOps,Image

# main window
main = Tk()
main.title('Image Editor')
main.geometry('1000x700')
main.config(background='#FFFFFF')
main.iconbitmap("icon.ico")

#default variables
pensize = 10
pencolour = "green"
file_path = ""
draw = None
original_image = None

# importing the image locally
def Import():
    global file_path, original_image
    file_path = filedialog.askopenfilename(initialdir="",
                                        filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
    if file_path:
        original_image = Image.open(file_path)
        display_image()

# displaying the image path on canvas 
def display_image():
    global file_path, original_image, photo_image
    canvas.delete("all")  # Clear the canvas
    canvas_width = canvas.winfo_reqwidth()
    canvas_height = canvas.winfo_reqheight()
    
    image = original_image.resize((canvas_width, canvas_height), Image.LANCZOS)
    
    photo_image = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor="nw", image=photo_image)

# Bringing back to original image    
def reset_image():
    global original_image
    if original_image:
        display_image()


# Functions related to Draw category
def enable_draw():
    canvas.bind("<B1-Motion>",draw_canvas)

def draw_canvas(event):
    x1, y1 = (event.x - pensize), (event.y - pensize)
    x2, y2 = (event.x + pensize), (event.y + pensize)
    canvas.create_oval(x1, y1, x2, y2, fill=pencolour, outline='')
    main.config(cursor='circle')

def color_chooser():
  global pencolour
  pencolour = colorchooser.askcolor(title="Choose Color")[1]

def pen_size(size):
    global pensize
    pensize=size

# Adding filter to images
def BW():
    global file_path
    if not file_path:
        return
    image = Image.open(file_path)
    canvas_width = canvas.winfo_reqwidth()
    canvas_height = canvas.winfo_reqheight() 
    image = image.resize((canvas_width, canvas_height), Image.LANCZOS)

    # Apply grayscale filter
    image = ImageOps.grayscale(image)

    # Update the canvas with the filtered image
    global photo_image
    photo_image = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor="nw", image=photo_image)

def blur():
    global file_path
    if not file_path:
        return
    image = Image.open(file_path)
    canvas_width = canvas.winfo_reqwidth()
    canvas_height = canvas.winfo_reqheight() 
    image = image.resize((canvas_width, canvas_height), Image.LANCZOS)

    # Blurring the image
    image = image.filter(ImageFilter.BLUR)

    # Update the canvas with the filtered image
    global photo_image
    photo_image = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor="nw", image=photo_image)

def Sharpen():
    global file_path
    if not file_path:
        return
    image = Image.open(file_path)
    canvas_width = canvas.winfo_reqwidth()
    canvas_height = canvas.winfo_reqheight() 
    image = image.resize((canvas_width, canvas_height), Image.LANCZOS)

    # Sharpen the image
    image = image.filter(ImageFilter.SHARPEN)

    # Update the canvas with the filtered image
    global photo_image
    photo_image = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor="nw", image=photo_image)

def Smooth():
    global file_path
    if not file_path:
        return
    image = Image.open(file_path)
    canvas_width = canvas.winfo_reqwidth()
    canvas_height = canvas.winfo_reqheight() 
    image = image.resize((canvas_width, canvas_height), Image.LANCZOS)

    # Blurring the image
    image = image.filter(ImageFilter.SMOOTH)

    # Update the canvas with the filtered image
    global photo_image
    photo_image = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor="nw", image=photo_image)

def Emboss():
    global file_path
    if not file_path:
        return
    image = Image.open(file_path)
    canvas_width = canvas.winfo_reqwidth()
    canvas_height = canvas.winfo_reqheight() 
    image = image.resize((canvas_width, canvas_height), Image.LANCZOS)

    # Emboss
    image = image.filter(ImageFilter.EMBOSS)

    # Update the canvas with the filtered image
    global photo_image
    photo_image = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor="nw", image=photo_image)

# flipping horizontally and vertically
def flip_x():
    global file_path
    if not file_path:
        return
    
    image = Image.open(file_path)
    canvas_width = canvas.winfo_reqwidth()
    canvas_height = canvas.winfo_reqheight() 
    image = image.resize((canvas_width, canvas_height), Image.LANCZOS)
    
    # Flip the image horizontally
    image = image.transpose(Image.FLIP_LEFT_RIGHT)
    
    # Update the canvas with the flipped image
    global photo_image
    photo_image = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor="nw", image=photo_image)

def flip_y():
    global file_path
    if not file_path:
        return
    
    image = Image.open(file_path)
    canvas_width = canvas.winfo_reqwidth()
    canvas_height = canvas.winfo_reqheight() 
    image = image.resize((canvas_width, canvas_height), Image.LANCZOS)
    
    # Flip the image vertically
    image = image.transpose(Image.FLIP_TOP_BOTTOM)
    
    # Update the canvas with the flipped image
    global photo_image
    photo_image = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor="nw", image=photo_image)

def rotate_90_clockwise():
    global file_path
    if not file_path:
        return
    
    image = Image.open(file_path)
    canvas_width = canvas.winfo_reqwidth()
    canvas_height = canvas.winfo_reqheight() 
    image = image.resize((canvas_width, canvas_height), Image.LANCZOS)
    
    # Rotate the image by 90 degrees clockwise
    image = image.rotate(-90)
    
    # Update the canvas with the rotated image
    global photo_image
    photo_image = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor="nw", image=photo_image)

def rotate_90_anticlockwise():
    global file_path
    if not file_path:
        return
    
    image = Image.open(file_path)
    canvas_width = canvas.winfo_reqwidth()
    canvas_height = canvas.winfo_reqheight() 
    image = image.resize((canvas_width, canvas_height), Image.LANCZOS)
    
    # Rotate the image by 90 degrees anticlockwise
    image = image.rotate(90)
    
    # Update the canvas with the rotated image
    global photo_image
    photo_image = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor="nw", image=photo_image)

# menu widget
menu_bar = Menu(main,border=2)

# file menu
file_menu = Menu(menu_bar,tearoff=0)
file_menu.add_command(label='Import',command=Import)
file_menu.add_command(label='Reset',command=reset_image)
file_menu.add_separator()
file_menu.add_command(label='Exit',command=main.quit)

# Draw menu
draw_menu = Menu(menu_bar,tearoff=0)
draw_menu.add_command(label='Pen',command=enable_draw)
draw_menu.add_command(label='Color picker',command=color_chooser)
draw_menu.add_command(label='Clear',command=reset_image)

pen_size_menu = Menu(draw_menu, tearoff=0)
pen_size_menu.add_command(label='Small', command=lambda:pen_size(2))
pen_size_menu.add_command(label='Medium', command=lambda:pen_size(5))
pen_size_menu.add_command(label='Large', command=lambda:pen_size(7))
draw_menu.add_cascade(label='Pen Size', menu=pen_size_menu)

# Filter menu
filter_menu = Menu(menu_bar,tearoff=0)
filter_menu.add_command(label="None",command=reset_image)
filter_menu.add_command(label="Black & white",command=BW)
filter_menu.add_command(label="Blur",command=blur)
filter_menu.add_command(label="Sharpen",command=Sharpen)
filter_menu.add_command(label="Smooth",command=Smooth)
filter_menu.add_command(label="Emboss",command=Emboss)

# position menu
position_menu = Menu(menu_bar,tearoff=0)
position_menu.add_command(label="Original",command=reset_image)
flip_menu = Menu(position_menu,tearoff=0)
flip_menu.add_command(label="Horizontal",command=flip_x)
flip_menu.add_command(label="Vertical",command=flip_y)
position_menu.add_cascade(label="Flip",menu=flip_menu)

rot_menu = Menu(position_menu,tearoff=0)
rot_menu.add_command(label="90 clockwise",command=rotate_90_clockwise)
rot_menu.add_command(label="90 anticlockwise",command=rotate_90_anticlockwise)
position_menu.add_cascade(label="Rotation",menu=rot_menu)


# menu bar
menu_bar.add_cascade(label='File',menu=file_menu)
menu_bar.add_cascade(label='Draw',menu=draw_menu)
menu_bar.add_cascade(label='Filters',menu=filter_menu)
menu_bar.add_cascade(label='Position',menu=position_menu)

#canvas
canvas = Canvas(main,width=950,height=650)
canvas.pack(side=TOP,expand=True)


main.config(menu=menu_bar)
main.mainloop()