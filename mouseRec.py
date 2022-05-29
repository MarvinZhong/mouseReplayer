import win32api
import win32con
import time
import pyautogui


def writer(click):
    x, y = pyautogui.position()
    print('click recorded at: ' + str(x) + ', ' + str(y))
    time.sleep(0.1)
    with open(cordFile+'.txt', 'a') as f:
        f.write(str(click) + ' ' + str(x) + ' ' + str(y) + ' 1\n')
    time.sleep(0.1)


def recorder(action):
    print('program ready to record | press Shift to STOP')
    # action = act
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


# delete the file if it exists
def main():
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


if __name__ == '__main__':
    cordFile = 'mousePosition'
    main()
