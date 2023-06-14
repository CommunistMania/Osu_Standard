class Slider:
    def __init__(self, x, y, r, t, hitrad, apprad, hitspeed, vel, number, game):
        self.game = game
        self.miss = False
        self.missframe = 0
        self.greatframe = 0
        self.x = x
        self.y = y
        self.r = r
        self.t = t
        self.vel = vel
        self.hitrad = hitrad
        self.apprad = apprad
        self.hitspeed = hitspeed
        self.number = number
        
        self.x = int(self.x)
        self.y = int(self.y)
        self.r = int(self.r)
        self.t = int(self.t)
        self.hitrad = int(self.hitrad)
        self.apprad = int(self.apprad)
        self.hitspeed = int(self.hitspeed)
        self.vel = int(self.vel)
        self.number = int(self.number)
        
        self.x1 = self.r * cos(radians(self.t)) + self.x
        self.y1 = self.r * sin(radians(self.t)) + self.y
        self.x2 = self.r * cos(radians(self.t))
        self.y2 = self.r * sin(radians(self.t))
        self.xv = 0
        self.yv = 0

        self.a = 0
        self.xx = self.x + self.r
        self.yy = self.y + self.r
        
        self.app = loadImage("appcircle.png")

        self.img = loadImage("Note.png")
        
        
        
    def delete(self):
        self.game.objects.remove(self)
        
    def on_draw(self):
        noStroke()
        
        if self.miss:
            fill(255, 20, 50)
            textSize(50)
            text("x", self.x, self.y)
            self.game.hpdrain = 0.75
            
        
            
        else:
            
            
            
        
            fill(100, 100, 100)
            circle(self.x1, self.y1, 115)
            
            
            
        
            stroke(100, 100, 100)
            strokeWeight(115)
            line(self.x, self.y, self.x1, self.y1)
            noStroke()
            
            stroke(30, 30, 30)
            strokeWeight(102.5)
            line(self.x, self.y, self.x1, self.y1)
            noStroke()
            
        
        
       
            
            fill(30, 30, 30)
            circle(self.x1, self.y1, 101)
            
            
            image(self.app, self.x, self.y, self.apprad, self.apprad)
            
        
            
            image(self.img, self.x, self.y, self.hitrad, self.hitrad)
            
            
            self.x += 0.1 * self.xv * (self.vel/2)
            self.y += 0.1 * self.yv * (self.vel/2)
        
            fill(255, 255, 255)
            textSize(50)
            text(self.number, self.x, self.y)
            
        
    def on_update(self):
        
        if self.a == 9:
            self.a = 0
        
        self.apprad -= self.hitspeed
        if self.apprad < self.hitrad and not self.miss:
                #self.objects.remove(self)
                self.miss = True
                self.missframe = frameCount
                self.a += 1
                self.game.combo = 0
        if frameCount - self.missframe > 30 and self.miss:
            self.delete()
            
        
            
            
        if self.x1 - 6 < self.x < self.x1 + 6:
                self.delete()
                self.game.hpdrain = 0.25
                
                
    def on_key_press(self, key):
        if self.game.kuso == False:
            if (key == 'z' or key == 'x') and self.y - 50 < mouseY < self.y + 50 and self.x - 50 < mouseX < self.x + 50 and self.hitrad - 5 < self.apprad < self.hitrad + 90:
                self.hitspeed = 0
                self.apprad = 250
                self.xv = self.x2
                self.yv = self.y2
                self.a += 1
                self.game.score += self.game.combo
                self.game.combo += 1
                self.game.hpdrain = 0
                self.game.hp += 10
                self.game.kuso = True
                
    
        
    
    def on_key_release(self, key):
        self.game.kuso = False
           
        
