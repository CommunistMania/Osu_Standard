from __future__ import division, print_function
import arcade
import Note
import Slider
import SliderBF
import ArcSlider
import ArcSlider2
import Song
import random


WIDTH = 1920
HEIGHT = 1080 # height of screen in pixels

BACKGROUND_COLOR = color(30)  # (0black), 255(white)


class Window:    
    def __init__(self):
        self.Cursor = loadImage("Cursor2.png")
        self.Background = loadImage("Menu2.png")
        self.Background2 = loadImage("Menu.png")
        self.Sora = loadImage("Sora.png")
        self.Select = loadImage("Select.jpg")
        self.SongCard1 = loadImage("SongCard1.png")
        self.objects = []
        self.sorasize = 600
        self.map1x = 600
        self.count = 0
        self.clicktoplay = False
        #Note Layout: (self, x, y, hitrad, apprad, hitspeed, number, game)
        #if (frameCount / 60) % 0.5 == 0:
        #Slider Layout: (self, x, y, x1/y1, hitrad, apprad, hitspeed, vel, velocity, number, game)
        #follow beats 1 to 4 for each "measure"
        self.play = False
        self.select = False
        self.menu = True
        self.endscreen = False
        self.kuso = False
        self.reset = False
        self.hp = 800
        self.hpdrain = 0.25
        self.score = 0
        self.combo = 0
        self.maxcombo = 0
        self.i = []
        self.j = []
        self.acc = 100
        self.fail = False
        """
        with open("Levels2.txt") as file:
            for row in file:
                row = row.strip()
                self.j = row.split(",")
                for c in range(len(self.j)):
                    self.j[c] = float(self.j[c])
                self.i.append(self.j)
                #print(self.j)
        #print(self.i)
        """
        
        self.Song1 = Song.Song(200, "Harumachi Clover", "Will Stetson", "Levels2", "Hard", 211, 2, 227, self)
        self.Song2 = Song.Song(350, "Amongus Drip", "sus remix", "Levels3", "Normal", 113, 21, 206, self)
        self.Song3 = Song.Song(500, "Let Him COOK", "rizzler", "Levels2", "Insane", 49, 194, 232, self)
        self.Songs = [self.Song1, self.Song2, self.Song3]
    def on_draw(self):
        
        cursor(self.Cursor, 26, 26)

        """
        with open("Levels2.txt") as file:
            for row in file:
                row = row.strip()
                self.j = row.split(",")
        """
        
            
        if self.play:
            self.j = []
            for n in self.i:
                self.j = n
                for x in self.j:
                    if self.j[0] == 1.0:
                        if 60 * float(self.j[1]) - 0.001 < self.count < 60 * float(self.j[1]) + 0.001:
                            self.objects.append(Note.Note(self.j[2], self.j[3], self.j[4], self.j[5], self.j[6], self.j[7], self))
                            break
                    if self.j[0] == 2.0:
                        if 60 * float(self.j[1]) - 0.001 < self.count < 60 * float(self.j[1]) + 0.001:
                            self.objects.append(Slider.Slider(self.j[2], self.j[3], self.j[4], self.j[5], self.j[6], self.j[7], self.j[8], self.j[9], self.j[10], self))
                            break
                    if self.j[0] == 3.0:
                        if 60 * float(self.j[1]) - 0.001 < self.count < 60 * float(self.j[1]) + 0.001:
                            self.objects.append(SliderBF.SliderBF(self.j[2], self.j[3], self.j[4], self.j[5], self.j[6], self.j[7], self.j[8], self.j[9], self.j[10], self))
                            break
                    if self.j[0] == 4.0:
                        if 60 * float(self.j[1]) - 0.001 < self.count < 60 * float(self.j[1]) + 0.001:
                            self.objects.append(ArcSlider.ArcSlider(self.j[2], self.j[3], self.j[4], self.j[5], self.j[6], self.j[7], self.j[8], self.j[9], self.j[10], self.j[11], self.j[12], self))
                            break
                    if self.j[0] == 5.0:
                        if 60 * float(self.j[1]) - 0.001 < self.count < 60 * float(self.j[1]) + 0.001:
                            self.objects.append(ArcSlider2.ArcSlider2(self.j[2], self.j[3], self.j[4], self.j[5], self.j[6], self.j[7], self.j[8], self.j[9], self.j[10], self.j[11], self.j[12], self))
                            break
                    if self.j[0] == 6.0:
                        if 60 * float(self.j[1]) - 0.001 < self.count < 60 * float(self.j[1]) + 0.001:
                            self.endscreen = True
                            self.select = False
                            self.menu = False
                            self.play = False
                            self.count = 0
                            break
                        
                    
            fill(250, 200, 255)
            textSize(50)
            text(int(self.score), 1200, 100)
            
            fill(255, 200, 250)
            textSize(50)
            text(str(self.combo)+"x", 100, 100)
            
            fill(200, 255, 170)
            textSize(50)
            text(frameRate, 1000, 100)
            
            fill(255, 228, 193)
            textSize(50)
            text("HP", 400, 100)
            
            fill(255, 228, 193)
            rect(500, 75, self.hp, 100, 10)
            self.hp -= self.hpdrain
            """
            fill(255, 228, 193)
            textSize(50)
            text(self.hpdrain, 400, 200)
            
            fill(255, 228, 193)
            textSize(50)
            text(self.hp, 400, 300)
            """
            if self.hp < 510:
                self.fail = True
                self.count = 0
                self.hp = 800
                self.play = False
                #self.hp = 510
                
            if self.hp > 800:
                self.hp = 800
                
        if self.select:
            for song in self.Songs:
                song.on_draw()
            textSize(30)
            fill(98, 218, 250)
            rect(25, 50, 150, 50+75, 30)
            fill(39, 77, 88)
            rect(30, 55, 145, 45+75, 25)
            fill(255, 255, 255)
            text("Menu", 85, 50+35)
            """
            image(self.Select, 650, 540)
            noStroke()
            fill(29, 160, 58)
            rect(1000, 350, 1400, 200)
            fill(255, 255, 255)
            textSize(30)
            text("Click to\nPlay", 1200, 275)
            image(self.SongCard1, 400 + self.map1x, 275, 600, 150)
            fill(255, 255, 255)
            #textSize(30)
            #text("Harumachi Clover", 150 + self.map1x, 300)
            #textSize(20)
            #text("Will Stetson", 80 + self.map1x, 330)
            textSize(50)
            """
                
        if self.menu:
            image(self.Background, 960, 540)
            image(self.Sora, 650, 540, self.sorasize, self.sorasize)
            textSize(60)
            text("Click the Circle!", 650, 100)
            textSize(50)
            if self.sorasize < 580:
                self.sorasize = 600
                
        if self.endscreen:
            textSize(60)
            text("Score: "+str(self.score), 300, 300)
            text("Max Combo: "+str(self.maxcombo), 300, 500)
            textSize(30)
            fill(98, 218, 250)
            rect(25, 50, 150, 50+75, 30)
            fill(39, 77, 88)
            rect(30, 55, 145, 45+75, 25)
            fill(255, 255, 255)
            text("Back", 85, 50+35)

        if self.fail:
            textSize(60)
            text("You Failed!", 300, 300)
            textSize(30)
            fill(98, 218, 250)
            rect(25, 50, 150, 50+75, 30)
            fill(39, 77, 88)
            rect(30, 55, 145, 45+75, 25)
            fill(255, 255, 255)
            text("Back", 85, 50+35)
    
    
        #self.j = [type, time, x, y, radius, outer radius, approach speed, number, self]
        
   
        #self.objects.append(Note.Note(objects[1], objects[2], objects[3], objects[4], objects[5], objects[6], objects[7], self))
            
        

        
                # self, x, y, r, t, hitrad, apprad, hitspeed, vel, velocity, number, game
                        
       
        
       
        
        
            
        for object in reversed(self.objects):
            object.on_update()
            object.on_draw()
            object.frameCount = frameCount
            
    
        

            
        
    
    
        
       
        
    def on_update(self):
        if self.select:
            for song in self.Songs:
                song.on_update()
        self.count += 1
        self.sorasize -= 2
        if self.combo > self.maxcombo:
            self.maxcombo = self.combo
        
        if 600 < mouseX < 1400 and 200 < mouseY < 350:
            self.map1x = 400
        else:
            self.map1x = 600
        
       
       
        
    def on_key_press(self, key):
        

        for object in self.objects:
            object.on_key_press(key)
            
            
      
        pass
    def on_key_release(self, key):
        
        for object in self.objects:
            object.on_key_release(key)
    
        pass 
        
    def on_mouse_clicked(self, mouseX, mouseY):
        for song in self.Songs:
                song.on_mouse_clicked(mouseX, mouseY)
        if 300 < mouseX < 900 and 240 < mouseY < 840 and self.menu:
            self.menu = False
            self.select = True
            #frameCount = 0
            self.i = []
            self.j = []
            self.objects = []
            self.hp = 800
            self.maxcombo = 0

            
        if 25 < mouseX < 150 and 50 < mouseY < 50+75 and self.endscreen:
            self.select = True
            self.menu = False
            self.endscreen = False
            self.count = 0
            self.i = []
            self.j = []
            self.objects = []
            self.hp = 800
            self.maxcombo = 0
            
        if 25 < mouseX < 150 and 50 < mouseY < 50+75 and self.fail:
            self.select = True
            self.fail = False
            self.HP = 800
            self.menu = False
            self.count = 0
            self.i = []
            self.j = []
            self.objects = []
            self.hp = 800
            self.maxcombo = 0
            
        if 25 < mouseX < 150 and 50 < mouseY < 50+75 and self.select:
            self.select = False
            self.fail = False
            self.HP = 800
            self.menu = True
            self.count = 0
            self.i = []
            self.j = []
            self.objects = []
            self.hp = 800
            self.maxcombo = 0
    
