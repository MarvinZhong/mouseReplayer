import time
import pyautogui
import random


def rightCord(xCord=None, yCord=None, pressTimes=1):
    pyautogui.rightClick(xCord, yCord, pressTimes)


def clickCord(xCord=None, yCord=None, pressTimes=1):
    pyautogui.click(xCord, yCord, pressTimes)


def moveCord(xCord=None, yCord=None, delay=0.1):
    pyautogui.moveTo(xCord, yCord, delay)


# read cordFile and loop through each line
def main():
    with open(cordFile+'.txt') as f:
        mode, sRange, eRange = map(int, f.readline().split(' '))
        if mode == 1:
            for line in f.readlines()[1:]:
                # print('hi')
                which, xCord, yCord, pressTimes = map(int, line.split())
                if which == 1:
                    clickCord(xCord, yCord, pressTimes)
                elif which == 2:
                    rightCord(xCord, yCord, pressTimes)
        elif mode == 2:
            print(sRange, eRange)
            # interval random float from sRange to eRange
            for line in f.readlines()[1:]:
                interval = random.uniform(sRange, eRange)
                print(interval)
                which, xCord, yCord, pressTimes = map(int, line.split())
                moveCord(xCord, yCord, interval)
                if which == 1:
                    clickCord(xCord, yCord, pressTimes)
                elif which == 2:
                    rightCord(xCord, yCord, pressTimes)
        elif mode == 3:
            reminder = 0
            for line in f.readlines()[1:]:
                which, xCord, yCord, interval, pressTimes = map(
                    int, line.split())
                # 0.6 seconds is the default prefix time
                moveCord(xCord, yCord, interval - reminder - 0.6)
                if which == 1:
                    clickCord(xCord, yCord, pressTimes)
                elif which == 2:
                    rightCord(xCord, yCord, pressTimes)
                reminder = interval
        else:
            print('mode not found')


if __name__ == '__main__':
    cordFile = 'mousePosition'
    timeSecs = int(input('program will run after (s) : '))
    startTime = time.time()
    # for timeSecs make countdown
    while time.time() - startTime < timeSecs:
        print(timeSecs - int(time.time() - startTime))
        time.sleep(1)
    main()
    endTime = int(time.time() - startTime)
    print('program runtime : ', endTime, 's')
