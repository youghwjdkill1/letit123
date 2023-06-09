class ClassTest3:
    
    def __test(self):
        """ 외부에서 호출금지 (객체 내부에서는 호출 가능) """
        print("test!")
    
    def test2(self):
        """ 외부에서 호출가능 """
        self.__test()        

ct3 = ClassTest3()
# ct3.__test()  # 에러(외부에서 접근이 안된다.)
ct3.test2()