from tkinter import *
from randomball import *
class Screensaver:
    balls=[]
    def __init__(self,no_of_balls):
        self.no_of_balls=no_of_balls
        self.root=Tk()
        self.create_screensaver()
        self.root.attributes('-fullscreen',True)
        self.quit_on_interaction()
        self.root.mainloop()
        
    def create_screensaver(self):
        self.create_canvas()
        self.add_ball()
        self.animate_ball()
   
    def create_canvas(self):
        self.canvas = Canvas(self.root)
        self.canvas.pack(expand=1, fill=BOTH)

    def add_ball(self):
        for i in range(self.no_of_balls):
            self.balls.append(RandomBall(self.canvas))

    def animate_ball(self):
        for ball in self.balls:
            ball.move_ball()
        self.root.after(30, self.animate_ball) 

    def quit_on_interaction(self):
        for seq in ('<Any-KeyPress>','<Any-Button>','<Motion>'):
            self.root.bind(seq,self.quit_screensaver)

    def quit_screensaver(self,event):
        self.root.destroy()


if __name__=='__main__':
   Screensaver(18)
