import cv2
import pygame
import random

from hand_detection import HandController


# =========================================================
# SETTINGS
# =========================================================

WIDTH = 970
HEIGHT = 640
FPS = 60

ROAD_LEFT = 220
ROAD_RIGHT = 750

CAR_WIDTH = 85
CAR_HEIGHT = 145

OBSTACLE_WIDTH = 120
OBSTACLE_HEIGHT = 85

MIN_SPEED = 3
MAX_SPEED = 12


# =========================================================
# PYGAME
# =========================================================

pygame.init()

screen = pygame.display.set_mode(
    (WIDTH, HEIGHT)
)

pygame.display.set_caption(
    "Hand Controlled Car Racing Game"
)

clock = pygame.time.Clock()


# =========================================================
# FONTS
# =========================================================

font = pygame.font.Font(
    None,
    34
)

small_font = pygame.font.Font(
    None,
    23
)

big_font = pygame.font.Font(
    None,
    70
)


# =========================================================
# LOAD ASSETS
# =========================================================

road = pygame.image.load(
    "assets/road.png"
).convert()

car = pygame.image.load(
    "assets/car.png"
).convert_alpha()

obstacle = pygame.image.load(
    "assets/obstacal.png"
).convert_alpha()


# =========================================================
# RESIZE
# =========================================================

road = pygame.transform.scale(
    road,
    (WIDTH, HEIGHT)
)

car = pygame.transform.scale(
    car,
    (CAR_WIDTH, CAR_HEIGHT)
)

obstacle = pygame.transform.scale(
    obstacle,
    (OBSTACLE_WIDTH, OBSTACLE_HEIGHT)
)


# =========================================================
# HAND CONTROLLER
# =========================================================

controller = HandController()


# =========================================================
# GAME VARIABLES
# =========================================================

car_x = WIDTH // 2 - CAR_WIDTH // 2
car_y = HEIGHT - CAR_HEIGHT - 25

speed = 5.0
score = 0.0

road_y = 0

obstacles = []

spawn_timer = 0

paused = False
game_over = False

gesture_cooldown = 0


# =========================================================
# RESET
# =========================================================

def reset_game():

    global car_x
    global speed
    global score
    global road_y
    global obstacles
    global spawn_timer
    global paused
    global game_over

    car_x = (
        WIDTH // 2 -
        CAR_WIDTH // 2
    )

    speed = 5.0
    score = 0.0

    road_y = 0

    obstacles = []

    spawn_timer = 0

    paused = False
    game_over = False


# =========================================================
# CREATE OBSTACLE
# =========================================================

def create_obstacle():

    lanes = [
        ROAD_LEFT + 25,
        ROAD_LEFT + 190,
        ROAD_LEFT + 355
    ]

    x = random.choice(lanes)

    obstacles.append({
        "x": x,
        "y": -100
    })


# =========================================================
# TEXT
# =========================================================

def text(value, x, y, size=30):

    f = pygame.font.Font(
        None,
        size
    )

    image = f.render(
        str(value),
        True,
        (255, 255, 255)
    )

    screen.blit(
        image,
        (x, y)
    )


# =========================================================
# PANEL
# =========================================================

def panel(x, y, width, height):

    surface = pygame.Surface(
        (width, height),
        pygame.SRCALPHA
    )

    surface.fill(
        (0, 0, 0, 175)
    )

    screen.blit(
        surface,
        (x, y)
    )


# =========================================================
# CAMERA PREVIEW
# =========================================================

def draw_camera(frame):

    if frame is None:
        return

    # OpenCV BGR → RGB
    rgb = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )

    # Resize
    rgb = cv2.resize(
        rgb,
        (210, 155)
    )

    # NumPy RGB → Pygame surface
    preview = pygame.surfarray.make_surface(
        rgb.swapaxes(0, 1)
    )

    screen.blit(
        preview,
        (15, HEIGHT - 175)
    )

    pygame.draw.rect(
        screen,
        (90, 90, 230),
        (
            10,
            HEIGHT - 180,
            220,
            165
        ),
        3
    )

    text(
        "Hand Tracking",
        20,
        HEIGHT - 207,
        22
    )


# =========================================================
# MAIN LOOP
# =========================================================

running = True

while running:

    clock.tick(FPS)

    # =====================================================
    # EVENTS
    # =====================================================

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                running = False

            if event.key == pygame.K_r:
                reset_game()


    # =====================================================
    # HAND DETECTION
    # =====================================================

    (
        hand_x,
        hand_y,
        detected,
        fingers,
        camera_frame
    ) = controller.get_control()


    # =====================================================
    # GESTURE COOLDOWN
    # =====================================================

    if gesture_cooldown > 0:
        gesture_cooldown -= 1


    # =====================================================
    # GESTURES
    # =====================================================

    if detected and gesture_cooldown == 0:

        # FIST = PAUSE
        if fingers <= 1:

            if not paused and not game_over:

                paused = True
                gesture_cooldown = 30


        # OPEN HAND = RESUME
        elif fingers >= 4:

            if paused:

                paused = False
                gesture_cooldown = 30


    # =====================================================
    # GAME UPDATE
    # =====================================================

    if not paused and not game_over:

        # =================================================
        # STEERING
        # =================================================

        if detected:

            target_x = (
                ROAD_LEFT +
                hand_x *
                (ROAD_RIGHT - ROAD_LEFT)
            )

            target_x -= CAR_WIDTH / 2

            target_x = max(
                ROAD_LEFT + 5,
                target_x
            )

            target_x = min(
                ROAD_RIGHT -
                CAR_WIDTH -
                5,
                target_x
            )

            car_x += (
                target_x - car_x
            ) * 0.16


        # =================================================
        # SPEED
        # =================================================

        if detected:

            # HAND UP
            if hand_y < 0.38:

                speed += 0.10


            # HAND DOWN
            elif hand_y > 0.68:

                speed -= 0.15


            # NORMAL
            else:

                speed += (
                    5.0 - speed
                ) * 0.01


        speed = max(
            MIN_SPEED,
            min(
                speed,
                MAX_SPEED
            )
        )


        # =================================================
        # ROAD
        # =================================================

        road_y += speed

        if road_y >= HEIGHT:
            road_y = 0


        # =================================================
        # SPAWN
        # =================================================

        spawn_timer += 1

        spawn_limit = max(
            30,
            75 - int(speed * 3)
        )

        if spawn_timer >= spawn_limit:

            create_obstacle()

            spawn_timer = 0


        # =================================================
        # MOVE OBSTACLES
        # =================================================

        for item in obstacles:

            item["y"] += speed


        # =================================================
        # REMOVE OBSTACLES
        # =================================================

        obstacles = [

            item

            for item in obstacles

            if item["y"] < HEIGHT + 100

        ]


        # =================================================
        # SCORE
        # =================================================

        score += speed * 0.02


        # =================================================
        # COLLISION
        # =================================================

        car_rect = pygame.Rect(
            int(car_x + 15),
            int(car_y + 15),
            CAR_WIDTH - 30,
            CAR_HEIGHT - 30
        )


        for item in obstacles:

            obstacle_rect = pygame.Rect(
                int(item["x"] + 10),
                int(item["y"] + 10),
                OBSTACLE_WIDTH - 20,
                OBSTACLE_HEIGHT - 20
            )

            if car_rect.colliderect(
                obstacle_rect
            ):

                game_over = True

                speed = 0

                break


    # =====================================================
    # DRAW BACKGROUND
    # =====================================================

    screen.fill(
        (20, 20, 20)
    )


    # =====================================================
    # DRAW ROAD
    # =====================================================

    screen.blit(
        road,
        (0, int(road_y))
    )

    screen.blit(
        road,
        (0, int(road_y - HEIGHT))
    )


    # =====================================================
    # DRAW OBSTACLES
    # =====================================================

    for item in obstacles:

        screen.blit(
            obstacle,
            (
                int(item["x"]),
                int(item["y"])
            )
        )


    # =====================================================
    # DRAW CAR
    # =====================================================

    screen.blit(
        car,
        (
            int(car_x),
            car_y
        )
    )


    # =====================================================
    # SCORE PANEL
    # =====================================================

    panel(
        15,
        15,
        160,
        95
    )

    text(
        f"Score: {int(score)}",
        28,
        25,
        32
    )

    text(
        f"Speed: {int(speed)}",
        28,
        65,
        32
    )


    # =====================================================
    # QUIT
    # =====================================================

    panel(
        WIDTH - 175,
        15,
        160,
        55
    )

    text(
        "ESC = Quit",
        WIDTH - 160,
        29,
        25
    )


    # =====================================================
    # CAMERA
    # =====================================================

    draw_camera(
        camera_frame
    )


    # =====================================================
    # CONTROL PANEL
    # =====================================================

    px = WIDTH - 235
    py = HEIGHT - 205

    panel(
        px,
        py,
        220,
        190
    )

    text(
        "Hand Controls",
        px + 15,
        py + 10,
        27
    )

    text(
        "Left  → Car Left",
        px + 15,
        py + 45,
        21
    )

    text(
        "Right → Car Right",
        px + 15,
        py + 70,
        21
    )

    text(
        "Up → Accelerate",
        px + 15,
        py + 95,
        21
    )

    text(
        "Down → Brake",
        px + 15,
        py + 120,
        21
    )

    text(
        "Fist → Pause",
        px + 15,
        py + 145,
        21
    )


    # =====================================================
    # PAUSE
    # =====================================================

    if paused:

        overlay = pygame.Surface(
            (WIDTH, HEIGHT),
            pygame.SRCALPHA
        )

        overlay.fill(
            (0, 0, 0, 150)
        )

        screen.blit(
            overlay,
            (0, 0)
        )

        title = big_font.render(
            "PAUSED",
            True,
            (255, 255, 255)
        )

        screen.blit(
            title,
            (
                WIDTH // 2 -
                title.get_width() // 2,
                HEIGHT // 2 - 50
            )
        )

        text(
            "Open hand to resume",
            WIDTH // 2 - 120,
            HEIGHT // 2 + 35,
            28
        )


    # =====================================================
    # GAME OVER
    # =====================================================

    if game_over:

        overlay = pygame.Surface(
            (WIDTH, HEIGHT),
            pygame.SRCALPHA
        )

        overlay.fill(
            (0, 0, 0, 170)
        )

        screen.blit(
            overlay,
            (0, 0)
        )

        title = big_font.render(
            "GAME OVER",
            True,
            (255, 255, 255)
        )

        screen.blit(
            title,
            (
                WIDTH // 2 -
                title.get_width() // 2,
                HEIGHT // 2 - 70
            )
        )

        text(
            f"Score: {int(score)}",
            WIDTH // 2 - 60,
            HEIGHT // 2 + 10,
            35
        )

        text(
            "Press R to restart",
            WIDTH // 2 - 90,
            HEIGHT // 2 + 55,
            27
        )


    # =====================================================
    # DISPLAY
    # =====================================================

    pygame.display.flip()


# =========================================================
# CLEANUP
# =========================================================

controller.release()

pygame.quit()