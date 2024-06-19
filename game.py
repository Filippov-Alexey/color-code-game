import time
import tkinter as tk
from PIL import ImageTk, Image, ImageOps
import random
root = tk.Tk()
root.geometry("750x650")
root.title('Цветовой код')
root.resizable(False,False)
g='picture\\'
image_path=[]
image_paths=[]
color='#6ff55d'
for i in range(0,18,1):image_paths.append(g+"\\0\\"+str(i)+".png")
image_path.append(g+"\\0\\18.png")
dragging = False
drag_data = {"x": 0, "y": 0, "image": None}
width=50
height=50
widthh=8
heighth=8
border_width = 1
border_color = (255, 0, 0)
i=1
ygl=0
ygls=0
images = []
canvas = tk.Canvas(root, width=750, height=650, highlightthickness=0, background=color)
canvas.pack()
imxy=(365,510)
thwh=170,170
txy=353,600
st=font=('arial',24)
level=[]

def on_img_press(event):
    global dragging, drag_data, ygl
    drag_data["x"] = event.x
    drag_data["y"] = event.y
    drag_data["image"] = event.widget.find_withtag("current")  
    drag_data['ygl']=ygl
    dragging = True

def on_img_motion(event):
    global dragging, drag_data
    if dragging:
        delta_x = event.x - drag_data["x"]
        delta_y = event.y - drag_data["y"]
        drag_data["x"] = event.x
        drag_data["y"] = event.y
        overlapping_objects = canvas.find_overlapping(*canvas.bbox(drag_data["image"]))

        if line1 in overlapping_objects or line2 in overlapping_objects or line3 in overlapping_objects:
            event.widget.coords(drag_data["image"], 353, 277)
        else:
            event.widget.move(drag_data["image"], delta_x, delta_y)
    canvas.tag_raise(tk.CURRENT)
    
def on_img_release(event):
    global dragging, drag_data, ygl
    drag_data["x"] = event.x
    drag_data["y"] = event.y
    dragging = False
    
def on_button4_click():
    global drag_data, images, image_paths, image_path
    ygl=drag_data['ygl']//90
    ygl = ygl + 1
    if ygl == 4:
        ygl = 0
    if ygl == 2:
        ygl = 2
    if ygl == 1:
        ygl = 1
    ygls = ygl * 90
    drag_data["ygl"]=ygls
    img_id = drag_data["image"][0]
    image_path = image_paths[img_id-2]
    s = str(image_path)
    stn1 = s.replace('\\'+str(0)+'\\','\\'+str(ygls)+'\\')
    time.sleep(0.5)
    stn = stn1.replace('\\'+str(img_id)+'.png','\\'+str(img_id-2)+'.png')
    img = Image.open(stn) 
    img = ImageTk.PhotoImage(img, master=root)
    
    new_images = list(images)
    new_images[drag_data["image"][0]-5] = img
    images[0] = new_images
    
    canvas.itemconfig(img_id, image=img)
 
def on_button3_click():
    global drag_data, images, image_paths, image_path
    ygl=drag_data['ygl']//90
    ygl = ygl - 1
    if ygl == -1:
        ygl = 3
    if ygl == 2:
        ygl = 2
    if ygl == 1:
        ygl = 1
    ygls = ygl * 90
    drag_data["ygl"]=ygls
    img_id = drag_data["image"][0]
    image_path = image_paths[img_id-2]
    s = str(image_path)
    stn1 = s.replace('\\'+str(0)+'\\','\\'+str(ygls)+'\\')
    time.sleep(0.5)
    stn = stn1.replace('\\'+str(img_id)+'.png','\\'+str(img_id-2)+'.png')
    img = Image.open(stn) 
    img = ImageTk.PhotoImage(img, master=root)
    
    new_images = list(images)
    new_images[drag_data["image"][0]-5] = img
    images[0] = new_images
    
    canvas.itemconfig(img_id, image=img)

def on_button1_click():
    global i, image_list
    i += 1
    if i > len(result):
        i = 1
    index = 0
    canvas.delete("image1")
    image_list = []  
    for item in result[i]:
        folder = item[0]
        file = item[1]
        image_path = f"{g}/{folder}/{file}.png"
        original_image = Image.open(image_path)
        resized_image = original_image.resize((thwh))
        image = ImageTk.PhotoImage(resized_image)
        image_list.append(image)  
        canvas.create_image(imxy, image=image, tags="image1")
        canvas.scale("image1", imxy[0], imxy[1], 2, 2)
        it = tk.Label(root, text=str(i)+'            ', bg=color, font=st)
        it.place(x=txy[0], y=txy[1])
        index += 1

def on_button2_click():
    global i, image_list
    i -= 1
    if i < 1:
        i = len(result)
    index = 0
    canvas.delete("image1")
    image_list = []  
    for item in result[i]:
        folder = item[0]
        file = item[1]
        image_path = f"{g}/{folder}/{file}.png"
        original_image = Image.open(image_path)
        resized_image = original_image.resize((thwh))
        image = ImageTk.PhotoImage(resized_image)
        image_list.append(image)  
        canvas.create_image(imxy, image=image, tags="image1")
        canvas.scale("image1", imxy[0], imxy[1], 2, 2)
        it = tk.Label(root, text=str(i)+'            ', bg=color, font=st)
        it.place(x=txy[0], y=txy[1])
        index += 1

with open('level.txt','r')as f:
    level=f.read()
lines = level.strip().split("\n")
result = {}
for line in lines:
    if line != "":
        key, value = line.split(":")
        result[int(key)] = eval(value)

button1 = tk.Button(root, text='←', command=on_button1_click, bg=color, fg='black', font=('Arial', 40, 'bold'), bd=0)
button1.place(x=180, y=420)
button2 = tk.Button(root, text='→', command=on_button2_click, bg=color, fg='black', font=('Arial', 40, 'bold'), bd=0)
button2.place(x=450, y=420)
button3 = tk.Button(root, text='⟲', command=on_button4_click, bg=color, fg='black', font=('Arial', 40, 'bold'), bd=0)
button3.place(x=180, y=20)
button4 = tk.Button(root, text='⟳', command=on_button3_click, bg=color, fg='black', font=('Arial', 40, 'bold'), bd=0)
button4.place(x=450, y=20)
it=tk.Label(root,text=str(i),bg=color,font=st)
it.place(x=txy[0],y=txy[1])
for path in image_path:
    image = Image.open(path)
    image = image.convert("RGBA")
    images.append(ImageTk.PhotoImage(image, master=root))
    x,y=350,300
  
    img_id = canvas.create_image(x, y, image=images[-1], tags='image')
for path in image_paths:
    image = Image.open(path)
    images.append(ImageTk.PhotoImage(image, master=root))

    img_id = canvas.create_image(random.randint(1,2)*1600-2000, random.randint(1,3)*500-600, image=images[-1], tags='image')
    canvas.scale(img_id, x, y, width/images[-1].width(), height/images[-1].height())

    canvas.tag_bind(img_id, "<Button-1>", on_img_press)
    canvas.tag_bind(img_id, "<B1-Motion>", on_img_motion)
    canvas.tag_bind(img_id, "<ButtonRelease-1>", on_img_release)
canvas.create_rectangle(280,424,448,595, fill='white',outline='white')
i=1
image_list=[]
for item in result[i]:
    folder = item[0]
    file = item[1]
    image_path = f"{g}/{folder}/{file}.png"
    original_image = Image.open(image_path)
    resized_image = original_image.resize((thwh))
    image = ImageTk.PhotoImage(resized_image)
    image_list.append(image) 
    canvas.create_image(imxy, image=image, tags="image1")
    canvas.scale("image1", imxy[0], imxy[1], 2, 2)
    it = tk.Label(root, text=str(i)+'            ', bg=color, font=st)
    it.place(x=txy[0], y=txy[1])


line1 = canvas.create_line(275, 200, 275, 355, fill="white")
line2 = canvas.create_line(430, 200, 430, 355, fill="white")
line3 = canvas.create_line(275, 355, 430, 355, fill="white")
root.mainloop()
    