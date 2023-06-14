
class Note:
    def __init__(self, x, y, hitrad, apprad, hitspeed, number, game):
        self.game = game
        self.miss = False
        self.great = False
        self.missframe = 0
        self.greatframe = 0
        self.x = x
        self.y = y
        self.hitrad = hitrad
        self.apprad = apprad
        self.hitspeed = hitspeed
        self.number = number

        self.a = 0
        self.app = loadImage("appcircle.png")

        self.img = loadImage("Note.png")
        
        self.x = int(self.x)
        self.y = int(self.y)
        self.hitrad = int(self.hitrad)
        self.apprad = int(self.apprad)
        self.hitspeed = int(self.hitspeed)
        self.number = int(self.number)
        
        
    def delete(self):
        self.game.objects.remove(self)
        
    def on_draw(self):
        noStroke()
        
        if self.miss:
            fill(255, 20, 50)
            textSize(50)
            text("x", self.x, self.y)
            self.game.hpdrain = 0.75
            
        elif self.great:
            fill(162, 252, 115)
            textSize(30)
            text("100", self.x, self.y)
            
        else:
            
        
            image(self.app, self.x, self.y, self.apprad, self.apprad)
        
        
            image(self.img, self.x, self.y, self.hitrad, self.hitrad)
        
        
            fill(255, 255, 255)
            textSize(50)
            text(self.number, self.x, self.y)
    
    def on_update(self):
        
        if self.a == 9:
            self.a = 0
        
        self.apprad -= self.hitspeed
        if self.apprad <= self.hitrad - 5 and not self.miss:
            if not self.great:
                #self.objects.remove(self)
                self.miss = True
                self.missframe = frameCount
                self.a += 1
                self.game.combo = 0
        if frameCount - self.missframe > 30 and self.miss:
            self.delete()
            
        if frameCount - self.greatframe > 30 and self.great:
            self.delete()
        
            
            
        
        
                
    def on_key_press(self, key):
    
        if self.game.kuso == False:
            if (key == 'z' or key == 'x') and self.y - 50 < mouseY < self.y + 50 and self.x - 50 < mouseX < self.x + 50 and self.hitrad - 5 < self.apprad < self.hitrad + 70:
                self.a += 1
                self.game.score += self.game.combo
                self.game.combo += 1
                self.delete()
                self.game.hpdrain = 0.5
                self.game.hp += 10
                self.game.kuso = True
            
        if self.game.kuso == False:
            if (key == 'z' or key == 'x') and self.y - 50 < mouseY < self.y + 50 and self.x - 50 < mouseX < self.x + 50 and self.hitrad - 5 < self.apprad < self.hitrad + 120:

                self.greatframe = frameCount
                self.great = True
                self.a += 1
                self.game.score += 0.75 * self.game.combo
                self.game.combo += 1
                self.game.hpdrain = 0.5
                self.game.hp += 10
                self.game.kuso = True
           

    
    def on_key_release(self, key):
        self.game.kuso = False
