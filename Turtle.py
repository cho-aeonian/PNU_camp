import turtle
import random
import time

# 화면 설정
window = turtle.Screen()
window.title("거북이는 이겨야지ㅋㅋ")
window.bgcolor("white")
window.setup(width=600, height=600)
window.tracer(0)

# 점수판 설정
score = 0
score_pen = turtle.Turtle()
score_pen.color("black")
score_pen.penup()
score_pen.hideturtle()
score_pen.goto(0, 260)
score_pen.write("Score: 0", align="center", font=("Courier", 24, "normal"))

# 거북이 설정
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.speed(0)
player.goto(0, -250)

# 거북이 이동 속도
player_speed = 15

# 장애물 설정
obstacles = []

# 장애물 생성 함수
def create_obstacle():
    obstacle = turtle.Turtle()
    obstacle.shape("square")
    obstacle.color("red")
    obstacle.penup()
    obstacle.speed(0)
    obstacle.goto(random.randint(-290, 290), 290)
    obstacles.append(obstacle)

# 플레이어 이동 함수
def move_left():
    x = player.xcor()
    x -= player_speed
    if x < -290:
        x = -290
    player.setx(x)

def move_right():
    x = player.xcor()
    x += player_speed
    if x > 290:
        x = 290
    player.setx(x)

def move_up():
    y = player.ycor()
    y += player_speed
    if y > 290:
        y = 290
    player.sety(y)

def move_down():
    y = player.ycor()
    y -= player_speed
    if y < -290:
        y = -290
    player.sety(y)

# 키보드 입력 처리
window.listen()
window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right")
window.onkeypress(move_up, "Up")
window.onkeypress(move_down, "Down")

# 게임 실행
next_obstacle = time.time() + 2.0  # 초기 장애물 생성 시간 (2초 뒤에 첫 장애물 생성)
while True:
    window.update()

    # 점수 표시
    score_pen.clear()
    score_pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

    # 장애물 생성 및 이동
    current_time = time.time()
    if current_time > next_obstacle:
        create_obstacle()
        next_obstacle = current_time + random.uniform(1.0, 3.0)  # 장애물 생성 주기를 1~3초 사이로 랜덤하게 설정

    for obstacle in obstacles:
        obstacle.sety(obstacle.ycor() - 20)
        if obstacle.ycor() < -290:
            obstacles.remove(obstacle)
            obstacle.hideturtle()
            if score % 5 == 0:  # 5점마다 장애물을 하나씩 추가
                create_obstacle()
            obstacle.hideturtle()
            if score % 10 == 0: # 10점마다 장애물을 하나씩 더 추가
                create_obstacle()
            score += 1  # 장애물이 사라지면 점수를 1 증가시킴

    # 충돌 검사
    for obstacle in obstacles:
        if player.distance(obstacle) < 15:
            player.color("red")
            player.goto(0, 0)
            window.update()
            time.sleep(1)
            player.color("green")
            score = 0
            for obstacle in obstacles:
                obstacle.hideturtle()
            obstacles.clear()

    # 점수에 따라 장애물 속도 조절
    if score % 10 == 0:
        for obstacle in obstacles:
            obstacle.sety(obstacle.ycor() - 3)  # 장애물 속도를 2만큼 빠르게 조정

    # 잠시 대기 (게임 속도 조절)
    time.sleep(0.02)

# 게임 종료
window.mainloop()