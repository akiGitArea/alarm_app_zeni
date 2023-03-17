import time
import pygame

def set_alarm(alarm_time):
    current_time = time.strftime("%H:%M")
    while current_time != alarm_time:
        print("現在時刻: ", current_time)
        current_time = time.strftime("%H:%M")
        time.sleep(1)
    play_alarm()

def play_alarm():
    pygame.mixer.init()
    pygame.mixer.music.load("sample.mp3")
    pygame.mixer.music.play()
    print("目覚まし時刻です！")
    input("アラームを止めるにはEnterキーを押してください")
    pygame.mixer.music.stop()
    print("アラームが停止しました。")

def main():
    alarm_time = input("目覚まし時刻を入力してください（HH:MMの形式）: ")
    set_alarm(alarm_time)

if __name__ == "__main__":
    main()