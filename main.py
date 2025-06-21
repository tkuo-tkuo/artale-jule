import random
import time
import pyautogui


def key(key: str, long_press: bool, iterations: int):
    for _ in range(iterations):
        keypress(key, long_press)


def keypress(key: str, long_press: bool):
    """
    模擬按下指定的鍵。
    :param key: 要按下的鍵
    """
    pyautogui.keyDown(key)
    if long_press:
        time.sleep(random.uniform(0.3, 0.5))
    else:
        time.sleep(random.uniform(0.05, 0.1))
    pyautogui.keyUp(key)


def check_minutes(minutes_interval: int):
    current_time = time.localtime()
    if current_time.tm_min % minutes_interval == 0:
        return True

    return False

# TODO: TK - test eat item 1/2
# TODO: TK - return to city every 30 minutes


def grind_stone_giant_one():
    eat_item_one = False
    count = 0
    start_time = time.time()

    try:
        time.sleep(3)  # 等待1秒鐘以便準備
        while True:
            minutes_passed = int((time.time() - start_time) // 60)
            seconds_passed = int((time.time() - start_time) % 60)
            print(f"已經過了 {minutes_passed} 分鐘 {seconds_passed} 秒")

            # Face left
            key('left', long_press=False, iterations=1)

            # Attack
            key('a', long_press=False, iterations=25)
            key('s', long_press=False, iterations=3)

            # Move left and attack
            key('left', long_press=True, iterations=4)
            key('a', long_press=False, iterations=25)
            key('s', long_press=False, iterations=3)

            # Collect and return
            key('left', long_press=True, iterations=4)
            key('s', long_press=False, iterations=3)
            key('right', long_press=True, iterations=10)

            if count >= 7:
                print("已經使用物品1 7次。")

                time.sleep(1)
                key('2', long_press=False, iterations=1)
                print("已使用物品2，程式結束。")

                break

            # Eat item 1 and 2
            if check_minutes(5):
                if not eat_item_one:
                    key('1', long_press=False, iterations=1)
                    count += 1
                    print("已使用物品1", "次數:", count)
                    eat_item_one = True
            else:
                eat_item_one = False

    except KeyboardInterrupt:
        print("程式已停止。")


if __name__ == "__main__":
    print("程式開始執行。按 Ctrl+C 可以停止程式。")
    grind_stone_giant_one()
