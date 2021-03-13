import gpiozero
import time
import detector
led = gpiozero.LED(17)

sit, leave = 0, 0
sitThreshold = 4
leaveThreshold = 2
restTime = 20 # 5 minutes

# if sit detected: sit counter ++
# if sit > 50 min: led on
# if led on and leave > sensitivity threshold:
#     5 mins count down, then clear sit counter and leave counter

while True:
    time.sleep(3)
    s = detector.detect_face()
    if s:
        sit += 1
    
    if sit > sitThreshold:
        led.on()
        if not s:
            leave += 1
    else:
        led.off()
    
    if leave > leaveThreshold:
        print("rest period triggered")
        time.sleep(restTime)
        sit = 0
        leave = 0
        
    print("sit:", sit, "leave:", leave)