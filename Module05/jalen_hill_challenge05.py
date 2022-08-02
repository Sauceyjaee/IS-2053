GRAVITY = 9.8
def main():
    print('Welcome to my Falling Distance Calculator')
    time_of_fall = int(input('Please enter the amount of time the object is falling and I will give you the distance it fell at each second: \n'))
    fallingDistance(time_of_fall)
def fallingDistance(time):
    for currTime in range(1, time + 1):
     distance_travelled_per_second = 0.0
     distance_travelled_per_second = .5 * GRAVITY * currTime**2
     print(f'{distance_travelled_per_second}')
main()
