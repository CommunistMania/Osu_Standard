class ArcSlider:
    def __init__(self, x, y, r, t, e, hitrad, apprad, hitspeed, vel, velocity, number, game):
        self.game = game
        self.miss = False
        self.missframe = 0
        self.vel = vel
        self.x = x
        self.y = y
        self.r = r
        self.t = t
        self.t1 = t
        self.e1 = e
        self.e = e
        self.velocity = velocity
        self.hitrad = hitrad
        self.apprad = apprad
        self.hitspeed = hitspeed
        self.number = number
        
        self.x = int(self.x)
        self.y = int(self.y)
        self.r = int(self.r)
        self.t = int(self.t)
        self.e = int(self.e)
        self.hitrad = int(self.hitrad)
        self.apprad = int(self.apprad)
        self.hitspeed = int(self.hitspeed)
        self.vel = int(self.vel)
        self.velocity = int(self.velocity)
        self.number = int(self.number)
        

        self.a = 0
    
        self.y1 = self.y + self.r
        self.xv = self.x
        self.yv = self.y1
        
        self.app = loadImage("appcircle.png")

        self.img = loadImage("Note.png")

        
       
        
    def delete(self):
        self.game.objects.remove(self)
        
    def on_draw(self):
        stroke(30, 30, 30)
        
        
        if self.miss:
            fill(255, 20, 50)
            textSize(50)
            text("x", self.r * cos(radians(self.t)) + self.x, self.r * sin(radians(self.t)) + self.y)
            self.game.hpdrain = 0.75
    
        else:
            noFill()
            stroke(100, 100, 100)
            strokeWeight(115)
            arc(self.x, self.y, 2*self.r, 2*self.r, radians(self.e), radians(self.t))
            noStroke()
            
            noFill()
            stroke(30, 30, 30)
            strokeWeight(102.5)
            arc(self.x, self.y, 2*self.r, 2*self.r, radians(self.e), radians(self.t))
            noStroke()
            
            
            image(self.app, self.xv, self.yv, self.apprad, self.apprad)
        
            
            image(self.img, self.xv, self.yv, self.hitrad, self.hitrad)
            
            self.t -= self.vel
            self.xv = self.r * cos(radians(self.t)) + self.x
            self.yv = self.r * sin(radians(self.t)) + self.y
        
            fill(255, 255, 255)
            textSize(50)
            text(self.number, self.r * cos(radians(self.t)) + self.x, self.r * sin(radians(self.t)) + self.y )
        
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
        
            
        
        if self.t <= self.e:
            self.delete()
            self.game.hpdrain = 0.25
        
        
                
    def on_key_press(self, key):

        if self.game.kuso == False:
            if (key == 'z' or key == 'x') and self.yv - 50 < mouseY < self.yv + 50 and self.xv - 50 < mouseX < self.xv + 50 and self.hitrad - 5 < self.apprad < self.hitrad + 90:
                self.hitspeed = 0
                self.apprad = 250
                self.vel = self.velocity
                
                self.a += 1
                self.game.score += self.game.combo
                self.game.combo += 1
                self.game.hpdrain = 0
                self.game.hp += 10
                self.game.kuso = True
           
           
    def on_key_release(self, key):
        self.game.kuso = False
           

    
    
          
        
