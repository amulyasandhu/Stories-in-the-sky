from graphics import Canvas
import random

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400

# List of constellations: name and list of (x, y, connections) for stars
CONSTELLATIONS = [
    {
        'name': 'Ursa Major',
        'stars': [
            (100, 100, [1, 2]),
            (150, 80, [0, 3]),
            (200, 100, [0, 3, 4]),
            (180, 150, [1, 2, 4]),
            (220, 180, [2, 3, 5]),
            (260, 200, [4, 6]),
            (300, 220, [5])
        ]
    },
    {
        'name': 'Orion',
        'stars': [
            (120, 120, [1, 3]),
            (140, 100, [0, 2]),
            (160, 120, [1, 3, 4]),
            (140, 160, [0, 2]),
            (180, 140, [2, 5]),
            (200, 180, [4, 6]),
            (220, 200, [5])
        ]
    },
    {
        'name': 'Cassiopeia',
        'stars': [
            (100, 150, [1]),
            (130, 120, [0, 2]),
            (160, 140, [1, 3]),
            (190, 120, [2, 4]),
            (220, 150, [3])
        ]
    },
    {
        'name': 'Scorpio',
        'stars': [
            (100, 200, [1]),
            (130, 180, [0, 2]),
            (150, 160, [1, 3]),
            (170, 180, [2, 4]),
            (200, 200, [3, 5]),
            (220, 220, [4, 6]),
            (240, 240, [5])
        ]
    },
    {
        'name': 'Leo',
        'stars': [
            (120, 140, [1, 2]),
            (150, 120, [0, 3]),
            (170, 140, [0, 3, 4]),
            (160, 180, [1, 2, 4]),
            (190, 200, [2, 3])
        ]
    },
    {
        'name': 'Gemini',
        'stars': [
            (140, 100, [1]),
            (160, 120, [0, 2]),
            (140, 160, [1, 3]),
            (160, 180, [2, 4]),
            (180, 160, [3, 5]),
            (200, 140, [4])
        ]
    }
]

def draw_background(canvas):
    # Dark blue background
    canvas.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, color='#523A28')
    # Draw random stars (small white ovals)
    for _ in range(100):
        x = random.randint(0, CANVAS_WIDTH)
        y = random.randint(0, CANVAS_HEIGHT)
        
       

def draw_constellation(canvas, constellation):
    # Clear previous constellation
    canvas.clear()
    draw_background(canvas)
    
    # Draw stars (white filled ovals, no outline)
    star_objects = []
    for x, y, _ in constellation['stars']:
        star = canvas.create_oval(x-5, y-5, x+5, y+5, color='#E4D4C8')
        star_objects.append((star, x, y))
    
    # Draw lines ( thicker) to connect stars
    for i, (_, _, connections) in enumerate(constellation['stars']):
        for j in connections:
            x1, y1 = star_objects[i][1], star_objects[i][2]
            x2, y2 = star_objects[j][1], star_objects[j][2]
            canvas.create_line(x1, y1, x2, y2, color='#D0B49F')
    
    # Draw constellation name (cyan) and prompt (white)
    canvas.create_text(
        CANVAS_WIDTH // 2, 30,
        text=constellation['name'], font='Anurati', font_size=20, color='#A47551'
    )
    canvas.create_text(
        CANVAS_WIDTH // 2, CANVAS_HEIGHT - 30,
        text='Click to change constellation', font='ultra', font_size=12, color='#D0B49F'
    )

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    current_constellation = [0]  # Store index for cycling
    
    # Draw initial constellation
    draw_background(canvas)
    draw_constellation(canvas, CONSTELLATIONS[0])
    
    # Loop to cycle constellations on mouse click
    while True:
        canvas.wait_for_click()  # Wait for user click
        current_constellation[0] = (current_constellation[0] + 1) % len(CONSTELLATIONS)
        draw_constellation(canvas, CONSTELLATIONS[current_constellation[0]])

if __name__ == '__main__':
    main()