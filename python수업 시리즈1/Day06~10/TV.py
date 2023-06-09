"""
파일명: tv.py
프로그램 설명: TV를 객체로 만들어서 사용한다.
작성자: 파이썬마스터
"""

import os

# 클래스 정의
class MyTV:
    """MyTV 클래스"""
   
    def __init__(self):
        """생성자"""

        # 인스턴스 변수를 생성한다.
        self.modelName  = "MyTV"      # 모델명
        self.modelColor = "Green"     # 색상
        self.channel    = 1           # 채널 1 ~ 100
        self.volume     = 1           # 볼륨 1 ~ 30
        self.onOff      = False       # On/Off 상태 True : On, False : Off
        self.tvOffMessage = 'TV의 전원이 꺼졌습니다.'
        self.tvOnMessage = 'TV의 전원이 켜졌습니다.'

    # TV 전원 On/Off 메소드
    def tvOnOff(self):
        """
        TV On/Off 한다.
        매개 변수 : X
        리턴값 : X
        """
        # print('tvOnOff() 메소드 실행')
        self.onOff = not self.onOff  # 전원 상태를 변경한다.
        if self.onOff:  # 전원 On
            print(self.tvOnMessage)
        else:  # 전원 Off
            print(self.tvOffMessage)
    
    # 채널 UP 메소드
    def channelUp(self):
        """
        채널을 UP 시킨다.
        매개 변수 : X
        리턴값 : X
        """
        #print('channelUp() 메소드 실행')

        # TV의 전원이 켜졌는지 체크하는 부분
        if self.onOff:                 # TV의 전원이 켜졌는가 ?
            if self.channel == 100 :   # 채널이 100이면
                self.channel = 1       # 채널을 1로 설정한다.
                print(f'채널을 1로 설정합니다. ({self.channel})')
            else:
                self.channel += 1      # 채널을 증가한다. 
                print(f'채널을 1증가했습니다. ({self.channel})')
        else:
            print(self.tvOffMessage)

    # 채널 DOWN 메소드
    def channelDown(self):
        """
        채널을 DOWN 시킨다.
        매개 변수 : X
        리턴값 : X
        """
        # print('channelDown() 메소드 실행')

        # TV의 전원이 켜졌는지 체크하는 부분
        if self.onOff:                 # TV의 전원이 켜졌는가 ?
            if self.channel == 1 :     # 채널이 1이면
                self.channel = 100     # 채널을 100으로 설정한다.
                print(f'채널을 100로 설정합니다. ({self.channel})')
            else:
                self.channel -= 1      # 채널을 감소한다. 
                print(f'채널을 1감소했습니다. ({self.channel})')
        else:
            print(self.tvOffMessage)

    # 채널 직접 변경 메소드
    def channelChange(self, channel):
        """
        채널을 직접 변경한다.
        매개 변수 : O
        - channel : 변경할 채널 번호
        리턴값 : X
        """
        # print('channelChange() 메소드 실행')
        if self.onOff:                 # TV의 전원이 켜졌는가 ?        
            if channel >= 1 and channel <= 100:  # 채널범위 1 ~ 100
                self.channel = channel    
                print(f'채널을 직접 설정했습니다. ({self.channel})')
            else:
                print('채널은 1 ~ 100까지 입력해야 합니다.')
        else:
                print(self.tvOffMessage)

    # 볼륨 UP 메소드
    def volumeUp(self):
        """
        볼륨을 UP 시킨다.
        매개 변수 : X
        리턴값 : X
        볼륨의 범위 : 1 ~ 30   
        30까지 갔는데 volumeUp() 메소드를 호출하면 더이상 올라가지 않고 
        현재 최대 볼륨입니다. 라는 메세지를 출력한다.
        """        
        # print('volumeUp() 메소드 실행')

        if self.onOff:                 # TV의 전원이 켜졌는가 ?        
            if self.volume == 30:      # 볼륨이 30이면
                print(f'현재 최대 볼륨입니다. ({self.volume})')
            else:                      # 볼륨이 30보다 작으면
                self.volume += 1
                print(f'볼륨을 1증가했습니다. ({self.volume})')
        else:
            print(self.tvOffMessage)

    # 볼륨 DOWN 메소드
    def volumeDown(self):     
        """
        볼륨을 DOWN 시킨다.
        매개 변수 : X
        리턴값 : X
        볼륨의 범위 : 1 ~ 30   
        1까지 갔는데 volumeDown() 메소드를 호출하면 더이상 내려가지 않고 
        현재 최소 볼륨입니다. 라는 메세지를 출력한다.
        """
        # TV의 전원이 켜졌는지 ???
        if self.onOff:
            if self.volume == 1:      # 볼륨이 1이면
                print(f'현재 최소 볼륨입니다. ({self.volume})')
            else:                      # 볼륨이 1보다 크면
                self.volume -= 1
                print(f'볼륨을 1감소했습니다. ({self.volume})')
        else:
            print(self.tvOffMessage)      

    # 채널을 가져오는 메소드
    def getChannel(self):
        """
        현재 채널을 가져온다.
        매개 변수 : X
        리턴값 : X
        """        
        # print('getChannel() 메소드 실행')                

        if self.onOff:                 # TV의 전원이 켜졌는가 ?
            print(f'현재 채널 : {self.channel}')
        else:
            print(self.tvOffMessage)

    # 볼륨을 가져오는 메소드
    def getVolume(self):
        """
        현재 볼륨을 가져온다.
        매개 변수 : X
        리턴값 : X
        """        
        # print('getVolume() 메소드 실행')   
        if self.onOff:                 # TV의 전원이 켜졌는가 ?
            print(f'현재 볼륨 : {self.volume}')
        else:
            print(self.tvOffMessage)         

    # TV 메뉴 메소드
    def tvmenu(self):
        """
        TV 프로그램 메뉴
        매개 변수 : X
        리턴값 : O
        - menu : 메뉴가 저장된 문자열
        """

        menu  = f'>>> TV 프로그램 ({self.modelName}) <<<\n'
        menu += f'전원: { "On" if self.onOff == True else "Off" }  '
        menu += f'채널: {self.channel}  '
        menu += f'볼륨: {self.volume}\n'
        menu += '1. TV On/Off\n'
        menu += '2. 채널 증가 ▲\n'
        menu += '3. 채널 감소 ▼\n'
        menu += '4. 채널 직접 변경\n'
        menu += '5. 볼륨 증가 △\n'
        menu += '6. 볼륨 감소 ▽\n'
        menu += '7. 현재 볼륨 확인 ★\n'
        menu += '8. 현재 채널 확인 ☆\n'
        menu += '9. 프로그램 정보\n'
        menu += 'q. 프로그램 종료\n'
    
        return menu

    # 프로그램 정보    
    def tvAbout(self):
        """프로그램 정보"""
        print(">>> TV 프로그램 정보  <<<")

        aboutMsg  = "TV 프로그램\n"
        aboutMsg += "버전 : 0.1\n"
        aboutMsg += "프로그램 제작 : 홍길동(hong@naver.com)\n"

        print(aboutMsg)

    # main 함수
    def main(self):
        """main""" 

        while True:
        
            os.system('cls')  # 화면 지우기

            print(self.tvmenu())    # 메뉴 출력
            x = input('선택 >>> ')  # 메뉴 입력

            # 메뉴 체크
            if   x == '1' :  # TV On/Off
                self.tvOnOff()
            elif x == '2' :  # 채널 증가
                self.channelUp()    
            elif x == '3' :  # 채널 감소
                self.channelDown()
            elif x == '4' :  # 채널 직접 변경
                channel = input('변경할 채널 : ')
                channel = int(channel) if channel.isdigit() else ''
                if channel : 
                    if channel >= 1 and channel <= 100:
                        self.channelChange(channel)
                    else:
                        print('채널 번호는 1 ~ 100까지 입니다.')
                else:
                    print('채널 번호를 잘못 입력했습니다.')
            elif x == '5' :  # 볼륨 증가
                self.volumeUp()
            elif x == '6' :  # 볼륨 감소
                self.volumeDown()
            elif x == '7' :  # 현재 볼륨 확인
                self.getVolume()
            elif x == '8' :  # 현재 채널 확인
                self.getChannel()
            elif x == '9' :  # 프로그램 정보
                self.tvAbout()                                                
            elif x == 'q' :  # 프로그램 종료
                print("MyTV 프로그램을 종료합니다...")
                quit()
            else:            # 그외의 모든 값
                print('1 ~ 9 or q중에서 입력해야 합니다.')

            input()

# 객체(인스턴스) 생성
# mytv = MyTV()
# mytv.main()

# MyTV2 클래스에서는 새로운 기능이 하나 추가되었다.
# 볼륨을 0으로 설정하는 음소거 기능인 mute 가 추가되었다.
#
# 메소드명 : volumeMute
# 메소드 기능 : 음소거 self.volume = 0
# 매개 변수 : X
# 리턴값 : O
# 음소거는 메뉴에서 10번으로 추가한다.


class MyTV2(MyTV):
    """MyTV2 클래스"""

    # 생성자
    def __init__(self, modelName = "MyTV2",
                       modelColor = "Yellow", 
                       channel = 1, volume = 1, onOff = True):
        self.modelName  = modelName
        self.modelColor = modelColor
        self.channel    = channel
        self.volume     = volume
        self.onOff      = onOff
        self.tvOffMessage = 'TV의 전원이 꺼졌습니다.'
        self.tvOnMessage = 'TV의 전원이 켜졌습니다.'

    # 볼륨을 음소거하는 메소드
    def VolumeMute(self):
        """
        현재 볼륨을 음소거한다.
        매개 변수 : X
        리턴값 : X
        """        
        # print('VolumeMute() 메소드 실행')   
        if self.onOff:                 # TV의 전원이 켜졌는가 ?
            self.volume = 0 
            print(f'볼륨을 음소거 모드로 변경했습니다. ({self.volume})')
        else:
            print(self.tvOffMessage)     


    # TV 메뉴 메소드
    def tvmenu(self):
        """
        TV 프로그램 메뉴
        매개 변수 : X
        리턴값 : O
        - menu : 메뉴가 저장된 문자열
        """

        menu  = f'>>> TV 프로그램 ({self.modelName}) <<<\n'
        menu += f'전원: { "On" if self.onOff == True else "Off" }  '
        menu += f'채널: {self.channel}  '
        menu += f'볼륨: {self.volume}\n'
        menu += f'1. TV On/Off\n'
        menu += '2. 채널 증가 ▲\n'
        menu += '3. 채널 감소 ▼\n'
        menu += '4. 채널 직접 변경\n'
        menu += '5. 볼륨 증가 △\n'
        menu += '6. 볼륨 감소 ▽\n'
        menu += '7. 현재 볼륨 확인 ★\n'
        menu += '8. 현재 채널 확인 ☆\n'
        menu += '9. 프로그램 정보\n'
        menu += '10.음소거\n'
        menu += 'q. 프로그램 종료\n'
    
        return menu


    # main 함수
    def main(self):
        """main""" 

        while True:
        
            os.system('cls')  # 화면 지우기

            print(self.tvmenu())    # 메뉴 출력
            x = input('선택 >>> ')  # 메뉴 입력

            # 메뉴 체크
            if   x == '1' :  # TV On/Off
                self.tvOnOff()
            elif x == '2' :  # 채널 증가
                self.channelUp()    
            elif x == '3' :  # 채널 감소
                self.channelDown()
            elif x == '4' :  # 채널 직접 변경
                if self.onOff:
                    channel = input('변경할 채널 : ')
                    channel = int(channel) if channel.isdigit() else ''
                    if channel : 
                        if channel >= 1 and channel <= 100:
                            self.channelChange(channel)
                        else:
                            print('채널 번호는 1 ~ 100까지 입니다.')
                    else:
                        print('채널 번호를 잘못 입력했습니다.')
                else:
                    print(self.tvOffMessage)   
            elif x == '5' :  # 볼륨 증가
                self.volumeUp()
            elif x == '6' :  # 볼륨 감소
                self.volumeDown()
            elif x == '7' :  # 현재 볼륨 확인
                self.getVolume()
            elif x == '8' :  # 현재 채널 확인
                self.getChannel()
            elif x == '9' :  # 프로그램 정보
                self.tvAbout()     
            elif x == '10' :  # 음소거
                self.VolumeMute()                  
            elif x == 'q' :  # 프로그램 종료
                print("MyTV 프로그램을 종료합니다...")
                quit()
            else:            # 그외의 모든 값
                print('1 ~ 10 or q중에서 입력해야 합니다.')

            input()


if __name__ == "__main__":
    mytv2 = MyTV2('한국TV', 'RED', 20, 10)
    mytv2.main()