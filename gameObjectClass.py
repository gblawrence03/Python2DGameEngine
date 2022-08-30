def init(screenWidth, screenHeight, Handler):
    global screen_width
    screen_width = screenWidth
    global screen_height
    screen_height = screenHeight
    global handler
    handler = Handler

class GameObject():
    def __init__(self, x, y, ID):
        self.posX = x
        self.posY = y
        self.id = ID
        global handler
        self.handler = handler 

    # Algorithm to detect if two rectangular objects are colliding
    def collideTwo(self, obj1, obj2):
        return (obj1.posX < obj2.posX + obj2.width and
                obj1.posX + obj1.width > obj2.posX and
                obj1.posY < obj2.posY + obj2.height and
                obj1.posY + obj1.height > obj2.posY)

    def tick(self, *args):
        pass

    def render(self, graphics):
        pass




