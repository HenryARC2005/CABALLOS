import pygame as py

class caja():

    def __init__(self, x, y, w, h, color_active, color_inactive, font, active):
        self.x_pos=x
        self.y_pos=y
        self.color_active=color_active
        self.color_inactive=color_inactive
        self.color=color_inactive
        self.font=font
        self.w=w
        self.h=h
        self.active=active
        self.rect=py.Rect(x, y, w, h)

    def activar(self, event):
        if self.rect.collidepoint(event.pos):
            self.active=True
        else: self.active=False

    def cambia_color(self):
        if self.active:
            self.color=self.color_active
        else: self.color=self.color_inactive

    def dibujar(self, screen, user_text):
        py.draw.rect(screen, self.color, self.rect)
        text_surface = self.font.render(user_text, True, (255, 255, 255))
        screen.blit(text_surface, (self.rect.x+5, self.rect.y+5))
    


    

    

	
          
        
        
    
    
    



