# -*- coding: utf-8 -*-
# @Project  : Codurance-Katalyst-Katas
# @File     : SimpleMarsRover
# @Date     : 2022-08-29T12:00:33
# @Author   : R.P.L. Azevedo
# @Email    : rplazevedo@gmail.com
# @Software : PyCharm

class MarsRover:
    dir_dic = {0: "N", 1: "E", 2: "S", 3: "W"}
    dir_dic_rev = {"N": 0, "E": 1, "S": 2, "W": 3}

    def __init__(self, x_init: int = 0, y_init: int = 0, dir_init: str = "N") \
            -> None:
        self.x: int = x_init
        self.y: int = y_init
        self.dir: str = dir_init
        self.__dir_int: int = self.dir_dic_rev[dir_init]

    def pos(self) -> str:
        return f"{self.x}:{self.y}:{self.dir}"

    def exe(self, command: str) -> None:
        for letter in command:
            self.exe_letter(letter)

    def exe_letter(self, letter: str) -> None:
        if letter == "R":
            self.__dir_int = (self.__dir_int + 1) % 4
            self.dir = self.dir_dic[self.__dir_int]
        if letter == "M":
            self.y += 1
