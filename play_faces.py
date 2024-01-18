from furhat_remote_api import FurhatRemoteAPI
from time import sleep

frame_count_dict = {
    "Mask": 31,
    "Landscape": 29,
    "Flowers": 32,
    "Tears": 24,
    "Sweating": 43,
    "Battery": 12,
    "Eyes": 23,
    "Clock": 25
}

CHAR_NAME = "Clock"
CHAR_FRAME_COUNT = frame_count_dict[CHAR_NAME]

def check_clock(index):
    if index % 3 == 0:
        # 3, 6, 9, 12, 15, 18, 21, 24
        furhat.gesture(name="BrowFrown")
    else:
        if index % 4 == 0:
            # 4, 8, 16, 20
            furhat.gesture(name="ExpressFear")
        else:
            if index % 5 == 0:
                # 5, 10, 15, 25
                furhat.gesture(name="ExpressSad")

# Create an instance of the FurhatRemoteAPI class, providing the address of the robot or the SDK running the virtual robot
# furhat = FurhatRemoteAPI("localhost")
furhat = FurhatRemoteAPI("10.100.238.89")

# Get the voices on the robot
voices = furhat.get_voices()

# Set the voice of the robot
furhat.set_voice(name='Matthew')

# load 
# furhat.set_face(mask="adult",character="James")

# Say "Hi there!"
furhat.say(text="Top of the morning to ya!")

# Perform a named gesture
# furhat.gesture(name="BrowRaise")


# Loop through faces to create animation
start_index = 1
end_index = CHAR_FRAME_COUNT+1
step = 1
if CHAR_NAME == "Battery":
    start_index = CHAR_FRAME_COUNT
    end_index = 0
    step = -1
    
for i in range(start_index, end_index, step):
    # furhat.set_face(mask="adult",character="Amauri/Amauri"+str(i))
    curr_face = CHAR_NAME+"/"+CHAR_NAME+str(i)
    print("Setting face to %s" % curr_face)
    furhat.set_face(mask="adult",character=curr_face)
    
    # check if need to perform gestures
    if CHAR_NAME == "Mask":
        if i >= 26:
            furhat.gesture(name="CloseEyes")
    if CHAR_NAME == "Sweating":
        if i >= 28:
            furhat.gesture(name="BigSmile")
    if CHAR_NAME == "Clock":
        check_clock(i)
            
    # delay
    sleep(2)

# furhat.set_face(mask="adult", character="Amauri/Victor")
# furhat.set_face(mask="adult", character="StandardExtras/Luna")

# Set the voice of the robot
furhat.set_voice(name='Brian')

# Say "Hi there!"
furhat.say(text="See ya later aligator!")