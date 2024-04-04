import time

i = 0
# mientras i sea mayor que 4 imprimir el valor de i
while i > 4:
    print(i)

j = 0
# mientras i sea mayor que 4 imprimir el valor de i
while j < 4:
    time.sleep(1)
    print(f"J vale: {j}")
    j += 1
    if j == 4:
        j = 0