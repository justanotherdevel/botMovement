import curses, time

def input_char(message):
    try:
        win = curses.initscr()
        win.addstr(0, 0, message)
        while True: 
            ch = win.getch()
            if ch in range(32, 127): break
            time.sleep(0.05)
    except: raise
    finally:
        curses.endwin()
    return chr(ch)

if __name__ == "__main__":
    ch = 'a'
    while (ch != 'q'):
        ch = input_char("")
        if ch == 'A':
            print ("forward")
        elif ch == 'D':
            print ("left")
        elif ch == 'B':
            print ("down")
        elif ch == 'C':
            print ("right")
