import turtle
import time
import random
from tkinter import PhotoImage
from tkinter import messagebox
import tkinter as tk

#Hàm đặt các giá trị ban đầu
delay = 0.1
score = 0
high_score = 0  
obstacle_prob = 0.01

#Vẽ viền bản đồ
def draw_border():
    border_pen = turtle.Turtle()
    border_pen.speed(0)
    border_pen.color("white")
    border_pen.penup()
    border_pen.goto(-290, 290)
    border_pen.pendown()
    border_pen.pensize(3)
    for _ in range(4):
        border_pen.fd(580)
        border_pen.rt(90)
    border_pen.hideturtle()
   
# Tạo một đối tượng TurtleScreen (cửa sổ)
wn = turtle.Screen()

# 2 dòng này để gắn giá trị cho root là cửa sổ gốc
canvas = wn.getcanvas()

root = canvas.winfo_toplevel()

# Đường dẫn đến file ảnh biểu tượng
icon_path = "Icon.png"

# Tạo một đối tượng PhotoImage từ file ảnh
icon_image = PhotoImage(file=icon_path)

# Đặt biểu tượng cho cửa sổ
root.iconphoto(True, icon_image)

def setup_screen():
   wn.clear()
   wn.title("Snake Game")
   wn.bgcolor("dark green")
   wn.setup(width=600, height=600)
   wn.tracer(0) 
   draw_border() 
   return wn

# Khởi tạo đầu rắn
def create_snake_head(wn):
    head = turtle.Turtle()
    head.speed(0)
    head.shape("circle")
    head.color("white")
    head.penup()
    head.goto(0, 0)
    head.direction = "stop"
       
    return head

# Tạo thức ăn
def create_food(wn):
    food = turtle.Turtle()
    food.speed(0)
    food.shape("circle")
    food.color("red")
    food.penup()
    food.goto(0, 100)
    return food

# Hàm tạo chướng ngại vật
def create_obstacle():
    obstacle = turtle.Turtle()
    obstacle.speed(0)
    obstacle.shape("square")
    obstacle.color("grey")
    obstacle.penup()
    x = random.randint(-290, 290)
    y = random.randint(-290, 290)
    obstacle.goto(x, y)
    obstacles.append(obstacle)
    return obstacle

# Hàm tạo chướng ngại vật một cách ngẫu nhiên
def create_random_obstacles():
    if random.random() < obstacle_prob:
        obstacle = create_obstacle()
        obstacles.append(obstacle)
        
#Hàm tạo điểm
def create_point():
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))
    return pen

#Hàm tạo phần đuôi
def create_segment():
    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape("circle")
    new_segment.color("grey")
    new_segment.penup()
    segments.append(new_segment)
    update_segments_position()
    return new_segment

# Thiết lập bàn phím
def setup_keyboard_controls(wn):
    def go_up():
        if head.direction != "down":
            head.direction = "up"

    def go_down():
        if head.direction != "up":
            head.direction = "down"

    def go_left():
        if head.direction != "right":
            head.direction = "left"

    def go_right():
        if head.direction != "left":
            head.direction = "right"

    wn.listen()
    wn.onkeypress(go_up, "w")
    wn.onkeypress(go_down, "s")
    wn.onkeypress(go_left, "a")
    wn.onkeypress(go_right, "d")

# Hàm di chuyển
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

        
# Hàm chọn độ khó
def choose_difficulty():
    def set_difficulty():
        global delay, obstacle_prob
        if var.get() == 1:
            delay, obstacle_prob = 0.1, 0.01
        elif var.get() == 2:
            delay, obstacle_prob = 0.08, 0.015
        elif var.get() == 3:
            delay, obstacle_prob = 0.05, 0.2
        root.destroy()

    root = tk.Tk()
    root.title("Choose Difficulty")

    var = tk.IntVar()
    tk.Label(root, text="Select difficulty:").pack()
    tk.Radiobutton(root, text="Easy", variable=var, value=1).pack()
    tk.Radiobutton(root, text="Medium", variable=var, value=2).pack()
    tk.Radiobutton(root, text="Hard", variable=var, value=3).pack()
    tk.Button(root, text="OK", command=set_difficulty).pack()


    
# Hàm cập nhật vị trí của phần đuôi
def update_segments_position():
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)        
        
# Hàm di chuyển rắn
def move_snake():
    if head.direction != "stop":
        wn.update()
        update_segments_position()  # Cập nhật vị trí của phần đuôi
        move()
        time.sleep(delay)
        create_random_obstacles()
        check_collisions()
        
# Reset trò chơi
def reset_game():
    global score, high_score, head, food, obstacles,segments

    # Reset điểm số
    score = 0
 
    # Xóa rắn và thức ăn
    head.clear()
    food.clear()

    # Xóa các chướng ngại vật
    for obstacle in obstacles:
        obstacle.hideturtle()
        obstacle.clear()
    
    # Xóa phần đuôi
    for new_segment in segments:
        new_segment.hideturtle()
        new_segment.clear()

    # Cập nhật điểm số trên màn hình
    pen.clear()
    pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    start_game()
    

# Hiển thị thông báo khi thua
def game_over():
    global high_score, score

    # Xóa màn hình
    wn.clear()
    wn.bgcolor("black")

    # Hiển thị thông báo Game Over
    pen.goto(0, 0)
    pen.write("Game Over", align="center", font=("Courier", 36, "normal"))
    pen.goto(0, -50)
    pen.write(f"Your score: {score}", align="center", font=("Courier", 24, "normal"))

    # Cập nhật high score 
    if score > high_score:
        high_score = score

    pen.goto(0, -100)
    pen.write(f"High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

    # Hiển thị hộp thoại 
    choice = messagebox.askyesno("Game Over", "Try again ?") 

    if choice:
        reset_game()  # Bắt đầu lại trò chơi nếu người dùng chọn yes
    else:
        quit()  # Thoát trò chơi nếu người dùng chọn no
    
      
# Kiểm tra va chạm với đuôi của con rắn
def check_self_collision():
    if len(segments) < 2:
        return False  # Không có phần đuôi nào để kiểm tra
    for segment in segments[1:]:
        if head.distance(segment) < 20:
            return True
    return False

# Kiểm tra va chạm
def check_collisions():
    global score, high_score,delay
    # Kiểm tra va chạm với tường
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        game_over()

    # Kiểm tra va chạm với thức ăn
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        create_segment()
        

        score += 10
        if score > high_score:
            high_score = score

        pen.clear()
        pen.goto(0, 260)
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
  
    # Kiểm tra va chạm với chướng ngại vật
    for obstacle in obstacles:
        if head.distance(obstacle) < 20:
            game_over()
            
    # Kiểm tra va chạm với đuôi của con rắn
    if check_self_collision():
        game_over()

#Khởi tạo điểm
pen = create_point()

#Khởi tạo biến running
running = True

#Hàm thoát trò chơi
def quit():
    global running
    running = False
    
#Khi bấm 'X' thì chạy hàm quit
root.protocol("WM_DELETE_WINDOW", quit)
    
def on_close():

     #custom close options, here's one example:

     close = messagebox.askokcancel("Close", "Would you like to close the program?")
     if close:
          root.destroy()

#Hàm bắt đầu trò chơi
def start_game():
    global head,food,obstacles,segments
    # Khởi tạo màn hình
    setup_screen()

    # Khởi tạo đầu rắn
    head = create_snake_head(wn)

    # Khởi tạo thức ăn
    food = create_food(wn)
    
    # Danh sách chướng ngại vật
    obstacles = []
    
    # Danh sách các đoạn của con rắn
    segments = []

    # Thiết lập bàn phím điều khiển
    setup_keyboard_controls(wn)

    # Chọn độ khó và bắt đầu
    choose_difficulty()
    
#Gọi hàm bắt đầu trò chơi
start_game()

# Vòng lặp chính của trò chơi
while running:
    wn.update()

    move_snake()
   
#Kết thúc chương trình
turtle.bye()
