from random import randint
class RandomBall:
     def __init__(self,canvas):
         self.canvas=canvas
         self.screen_width=canvas.winfo_screenwidth()
         self.screen_height=canvas.winfo_screenheight()
         self.create_ball()

     def create_ball(self):
         self.generate_random_attribute()
         self.create_oval()

     def generate_random_attribute(self):
         self.radius=r=randint(40,70)
         self.x_cordinate=randint(r,self.screen_width-r)
         self.y_cordinate=randint(r,self.screen_height-r)
         self.x_velocity=randint(6,12)
         self.y_velocity=randint(6,12)
         self.color=self.generate_random_color()
     
     def generate_random_color(self):
         r = lambda:randint(0, 0xffff)
         return '#{:04x}{:04x}{:04x}'.format(r(), r(), r())    

     def create_oval(self):
        x1=self.x_cordinate-self.radius
        y1=self.y_cordinate-self.radius
        x2=self.x_cordinate+self.radius
        y2=self.y_cordinate+self.radius
        self.ball=self.canvas.create_oval(x1,y1,x2,y2,fill=self.color,outline=self.color)   

     def move_ball(self):
         self.check_screen_bound()
         self.x_cordinate+=self.x_velocity
         self.y_cordinate+=self.y_velocity
         self.canvas.move(self.ball,self.x_velocity,self.y_velocity)

     def check_screen_bound(self):
         r=self.radius
         if not r<self.x_cordinate<self.screen_width-r:
             self.x_velocity=-self.x_velocity
         if not r<self.y_cordinate<self.screen_height-r:
             self.y_velocity=-self.y_velocity
