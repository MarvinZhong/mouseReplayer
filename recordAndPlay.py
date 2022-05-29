import win32api
import win32con
import time
import pyautogui
import random


def writer(click):
    x, y = pyautogui.position()
    print('click recorded at: ' + str(x) + ', ' + str(y))
    time.sleep(0.1)
    with open(cordFile+'.txt', 'a') as f:
        f.write(str(click) + ' ' + str(x) + ' ' + str(y) + ' 1\n')
    time.sleep(0.1)


def recorder(action):
    print('program ready to record | press Shift to STOP')
    # get state from virtual-key-codes
    while action:
        if (win32api.GetKeyState(0x01)) < 0:
            writer(1)
        elif (win32api.GetKeyState(0x02)) < 0:
            writer(2)
        elif (win32api.GetKeyState(0x10)) < 0:
            print('program stopped')
            action = False


def realTimer(action):
    print('program ready to record | press Shift to STOP')
    # get state from virtual-key-codes
    rTime = time.time()
    print(rTime)
    while action:
        if (win32api.GetKeyState(0x01)) < 0:
            x, y = pyautogui.position()
            pTime = int(time.time() - rTime)
            print('click recorded at: ' + str(x) + ', ' + str(y))
            time.sleep(0.1)
            with open(cordFile+'.txt', 'a') as f:
                f.write('1 ' + str(x) + ' ' + str(y) +
                        ' ' + str(pTime) + ' 1\n')
            time.sleep(0.1)
        elif (win32api.GetKeyState(0x02)) < 0:
            x, y = pyautogui.position()
            pTime = int(time.time() - rTime)
            print('click recorded at: ' + str(x) + ', ' + str(y))
            time.sleep(0.1)
            with open(cordFile+'.txt', 'a') as f:
                f.write('2 ' + str(x) + ' ' + str(y) +
                        ' ' + str(pTime) + ' 1\n')
            time.sleep(0.1)
        elif (win32api.GetKeyState(0x10)) < 0:
            print('program stopped')
            break


def Rec():
    # delete the file if it exists
    try:
        open(cordFile+'.txt', 'w').close()
    except:
        pass
    print(pyautogui.size())  # print screen size
    print('mode : [1] speed, [2] time-range, [3] real-time')
    mode = input('select mode : ')
    if mode == '1':
        print('speed mode selected')
        with open(cordFile+'.txt', 'a') as f:
            f.write('1 0 0\n')
        recorder(True)
    elif mode == '2':
        print('time range mode selected')
        sTime = input('start range (s) :')
        eTime = input('end range (s) :')
        timeRange = sTime + ' ' + eTime
        print('time range : ' + timeRange)
        with open(cordFile+'.txt', 'a') as f:
            f.write('2 ' + timeRange + '\n')
        recorder(True)
    elif mode == '3':
        print('real time mode selected')
        with open(cordFile+'.txt', 'a') as f:
            f.write('3 0 0\n')
        realTimer(True)
    else:
        print('error')
        exit()


def rightCord(xCord=None, yCord=None, pressTimes=1):
    pyautogui.rightClick(xCord, yCord, pressTimes)


def clickCord(xCord=None, yCord=None, pressTimes=1):
    pyautogui.click(xCord, yCord, pressTimes)


def moveCord(xCord=None, yCord=None, delay=0.1):
    pyautogui.moveTo(xCord, yCord, delay)


# read cordFile and loop through each line
def Play():
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


def main():
    # by marvin zhong at github
    print('Welcome to the Mouse Replayer by Marvin Zhong at github')
    while True:
        print(
            'mode to select\t: [1] to record mouse event, [2] to  replay your recorded mouse event')
        mode = input('select mode\t: ')
        if mode == '1':
            Rec()
        elif mode == '2':
            timeSecs = int(input('program will run after (s) : '))
            startTime = time.time()
            # for timeSecs make countdown
            while time.time() - startTime < timeSecs:
                print(timeSecs - int(time.time() - startTime))
                time.sleep(1)
            Play()
            endTime = int(time.time() - startTime)
            print('program runtime : ', endTime, 's')
        else:
            print('error')
            exit()
        print('do you want to close the program? [y/n]')
        close = input('close? : ')
        if close == 'y':
            break


if __name__ == '__main__':
    cordFile = 'mousePosition'
    main()
