import math, time

t = 0
while True:
    output = []
    for y in range(-12, 13):
        row = []
        for x in range(-30, 31):
            d = math.sqrt(x*x + (y*2)**2)
            val = math.sin(d * 0.3 - t)
            i = int((val + 1) * 4.5)
            row.append(" .:-=+*#%@"[i])
        output.append("".join(row))
    print("\033[H" + "\n".join(output))  # Clears screen and prints new frame
    t += 0.2
    time.sleep(0.03)