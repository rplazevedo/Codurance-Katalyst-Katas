# -*- coding: utf-8 -*-
# @Project  : Codurance-Katalyst-Katas
# @File     : SimpleMarsRover
# @Date     : 2022-08-29T12:00:33
# @Author   : R.P.L. Azevedo
# @Email    : rplazevedo@gmail.com
# @Software : PyCharm

class MarsRover:
    dir_dic = {0: "N", 1: "E", 2: "S", 3: "W"}

    def __init__(self, x_init: int = 0, y_init: int = 0, dir_init: str = "N") \
            -> None:
        dir_dic_rev = {"N": 0, "E": 1, "S": 2, "W": 3}
        self.x: int = x_init
        self.y: int = y_init
        self.dir: str = dir_init
        self.__dir_int: int = dir_dic_rev[dir_init]

    def pos(self) -> str:
        return f"{self.x}:{self.y}:{self.dir}"

    def exe(self, command: str) -> None:
        for letter in command:
            self.exe_letter(letter)

    def exe_letter(self, letter: str) -> None:
        if letter == "R":
            self.turn_right()
        if letter == "L":
            self.turn_left()
        if letter == "M":
            self.move()

    def turn_right(self):
        self.__dir_int = (self.__dir_int + 1) % 4
        self.dir = self.dir_dic[self.__dir_int]

    def turn_left(self):
        self.__dir_int = (self.__dir_int - 1) % 4
        self.dir = self.dir_dic[self.__dir_int]

    def move(self):
        if self.dir == "N":
            self.y += 1
        if self.dir == "E":
            self.x += 1
        if self.dir == "S":
            self.y -= 1
        if self.dir == "W":
            self.x -= 1
