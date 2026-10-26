class Player:
    def __init__(self, joystick):
        self.x = 0
        self.y = 0
        self.joystick = joystick

    def update(self):  # called every game frame
        self.x += sidewinder.get_x_axis(1)
        self.y += sidewinder.get_y_axis(1)

        if self.joystick.button(4) == 1:
            self.fire_lasers()

        self.update_graphics()

    # ...

sidewinder = SidewinderJoystick()
xboxgamepad = XboxGamepad()
p = Player(sidewinder)

# ... Game code continues ...

class SidewinderJoystick:
    BUTTON_UP = 2
    BUTTON_DOWN = 3

    def get_x_axis(self, stick_id) # returns -1.0 to 1.0
    def get_y_axis(self, stick_id) # returns -1.0 to 1.0
    def button(self, button_id)    # Returns BUTTON_UP or BUTTON_DOWN

class XboxGamepad:
    def get_x_axis(stick_id) # returns -128 to 127
    def get_y_axis(stick_id) # returns -128 to 127
    def button_status(button_id)  # float from 0.0 (up) to 1.0 (down)

class Joystick:
    def get_x_axis(self):
        pass
    def get_y_axis(self):
        pass
    def button_status(self):
        pass

class WrappedXboxGamepad(Joystick):
    def __init__(self):
        self.xboxgamepad = XboxGamepad()

    def get_x_axis(self, stick_id) # adjust to return -1.0 to 1.0
        x_axis = self.xboxgamepad.get_x_axis(stick_id)
        return (2 * x_axis) / 255
    
    def get_y_axis(self, stick_id):
        x_axis = self.xboxgamepad.get_x_axis(stick_id)
        return (2 * x_axis) / 255
    
    def button_status(self, button_id) # adjust to return BUTTON_UP or BUTTON_DOWN
        return self.xboxgamepad.button_status(button_id)

class WrappedSideWinderJoystick(SidewinderJoystick, Joystick):
    def __init__(self):
        self.sidewinder = SidewinderJoystick()

    def get_x_axis(self, stick_id) # adjust to return -1.0 to 1.0
        x_axis = self.sidewinder.get_x_axis(stick_id)
        return (2 * x_axis) / 255
    
    def get_y_axis(self, stick_id):
        x_axis = self.sidewinder.get_x_axis(stick_id)
        return (2 * x_axis) / 255
    
    def button_status(self, button_id) # adjust to return BUTTON_UP or BUTTON_DOWN
        button_down = self.sidewinder.BUTTON_DOWN
        button = self.sidewinder.button_status(button_id)
        return 1 if button == button_down else 0



# One or two sentences (or code if you prefer) describing how you might also add the keyboard as a method of input in addition to the two joysticks.

# I would probably further abstract the input controls and create an input abstract class that is a 
# parent for the joysticks and keyboard and the keyboard would be a child of that class

# Answer: how was the author of the original code being short-sighted?

# The author was being shortsighted because they only implemented the sidewinder joystick without 
# considering abstraction for when more joysticks or controls will be added. While the code works, 
# it requires a lot of changes to add a controller
