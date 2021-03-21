import gpiozero
import time
import detector

# initialize LED on gpio pin 17
led = gpiozero.LED(17)

# saved detector results in the past hour; 1 hour == 600 segments of 6 seconds
timeline = [0 for _ in range(600)]

# for debugging
# statusLight = gpiozero.LED(4)
# statusLightSwitch = 1

while True:
    # indicate if the program is still running
#     statusLightSwitch *= -1
#     if statusLightSwitch > 0:
#         statusLight.on()
#     else:
#         statusLight.off()
    
    # default for the program is to detect every 6 seconds
    time.sleep(6) # call detector every 6 seconds
    s = detector.detect_face() # detection results: true for face detected
    timeline.pop(0)
    if s:
        timeline.append(1)
    else:
        timeline.append(0)
    
    # more calculation, but simplifies the design logic
    sit = sum(timeline)
    if sit >= 500:
        led.on()
    else:
        led.off()
    
    # if leave for 5 minutes, reset timeline
    if sum(timeline[-50:]) == 0: # -50
        timeline = [0 for _ in range(600)]
    
    print("detector results: ", s)
    print("sit for ", sit/10, " minutes")
