import time

error = True
while error:
    try:
        print(("Insert the time of the timer in this format hh:mm:ss"))
        time_in = input()
        hours, minutes, seconds = time_in.split(":")
        hours, minutes, seconds = int(hours), int(minutes), int(seconds)
        error = False
    except ValueError:
        (print("the format insert is incorrect try again"))

tot = seconds + (minutes * 60) + (hours * 60 * 60)

input("Press enter to start the count down")
for num in reversed(range(0, tot)):
    while seconds < 0:
        while minutes <= 0:
            hours -= 1
            minutes += 60
        minutes -= 1
        seconds += 60

    print(f"{hours}:{minutes}:{seconds}")
    seconds -= 1
    time.sleep(1)
print("times is up!")
