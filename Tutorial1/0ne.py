def stoh(sec):
    hours=sec//3600
    minutes=(sec%3600)//60
    sec=sec%60
    return f"{hours:02}:{minutes:02}:{sec:02}"

seconds=int(input("Enter the time in seconds: "))
actual_time=stoh(seconds)
print("Time in HH:MM:SS format",actual_time)