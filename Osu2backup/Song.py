class Song:
    def __init__(self, y, name, creator, file, difficulty, r, g, b, game):
        self.game = game
        self.y = y
        self.name = name
        self.creator = creator
        self.file = str(file)+".txt"
        self.difficulty = difficulty
        self.r = r
        self.g = g
        self.b = b
        self.map1x = 600
        
    def on_draw(self):
        noStroke()
        fill(49, 206, 15)
        rect(1000, self.y, 1400, self.y - 150)
        fill(255, 255, 255)
        textSize(30)
        text("Click to\nPlay", 1200, self.y - 75)
        fill(self.r, self.g, self.b)
        rect(self.map1x, self.y, 700 + self.map1x, self.y - 150)
        fill(255, 255, 255)
        textSize(50)
        text(self.name, 300 + self.map1x, self.y - 100)
        textSize(30)
        text(self.creator, 100 + self.map1x, self.y - 50)
        text("Difficulty: "+self.difficulty, 500 + self.map1x, self.y - 50)
        
    def on_update(self):
        if 600 < mouseX < 1400 and self.y - 150 < mouseY < self.y:
            self.map1x = 400
        else:
            self.map1x = 600
            
    def on_mouse_clicked(self, mouseX, mouseY):
        if 600 < mouseX < 1400 and self.y - 150 < mouseY < self.y and self.game.select:
            with open(str(self.file)) as file:
                for row in file:
                    row = row.strip()
                    self.game.j = row.split(",")
                    for c in range(len(self.game.j)):
                        self.game.j[c] = float(self.game.j[c])
                    self.game.i.append(self.game.j)
            self.game.play = True
            self.game.count = 0
            self.game.select = False
