# -*- coding: utf-8 -*-
# @Project  : Codurance-Katalyst-Katas
# @File     : MarsRover
# @Date     : 2022-08-30T18:06:06
# @Author   : R.P.L. Azevedo
# @Email    : rplazevedo@gmail.com
# @Software : PyCharm
import numpy as np


class MarsRover:
    dir_dic = {0: "N", 1: "E", 2: "S", 3: "W"}

    def __init__(self, x_init: int = 0, y_init: int = 0, dir_init: str = "N"):
        dir_dic_rev = {"N": 0, "E": 1, "S": 2, "W": 3}
        self.x: int = x_init
        self.y: int = y_init
        self.dir: str = dir_init
        self.__dir_int: int = dir_dic_rev[dir_init]
        self._obstacle_flag: bool = False

    def pos(self) -> str:
        return f"{self.x}:{self.y}:{self.dir}"

    def exe(self, command: str, plateau: object) -> str:
        for letter in command:
            self.exe_letter(letter, plateau)
            if self._obstacle_flag:
                self._obstacle_flag = False
                return f"O:{self.pos()}"
        else:
            return self.pos()

    def exe_letter(self, letter: str, plateau) -> None:
        if letter == "R":
            self.turn_right()
        if letter == "L":
            self.turn_left()
        if letter == "M":
            self.move(plateau)

    def turn_right(self):
        self.__dir_int = (self.__dir_int + 1) % 4
        self.dir = self.dir_dic[self.__dir_int]

    def turn_left(self):
        self.__dir_int = (self.__dir_int - 1) % 4
        self.dir = self.dir_dic[self.__dir_int]

    def move(self, plateau):
        move_direction = {"N": self.move_north,
                          "S": self.move_south,
                          "E": self.move_east,
                          "W": self.move_west}
        move_direction[self.dir](plateau)

    def move_west(self, plateau):
        if plateau.is_obstacle_at_coord((self.x - 1, self.y)):
            self._obstacle_flag = True
        else:
            self.x = (self.x - 1) % 10

    def move_south(self, plateau):
        if plateau.is_obstacle_at_coord((self.x, self.y - 1)):
            self._obstacle_flag = True
        else:
            self.y = (self.y - 1) % 10

    def move_east(self, plateau):
        if plateau.is_obstacle_at_coord((self.x + 1, self.y)):
            self._obstacle_flag = True
        else:
            self.x = (self.x + 1) % 10

    def move_north(self, plateau):
        if plateau.is_obstacle_at_coord((self.x, self.y + 1)):
            self._obstacle_flag = True
        else:
            self.y = (self.y + 1) % 10

    def check_grid_for_obs(self, next_coord: tuple[int, int], plateau):
        if plateau.is_obstacle_at_coord(next_coord):
            return f"O:{self.pos()}"


class MarsPlateau:
    def __init__(self, size_x: int = 10, size_y: int = 10):
        self._grid: np.ndarray = np.zeros((size_x, size_y))

    def add_mutiple_obstacles(self, list_coords: list[tuple[int, int]]):
        for coord in list_coords:
            self.add_obstacle(coord)

    def add_obstacle(self, coord: tuple[int, int]):
        self._grid[coord] = 1

    def is_obstacle_at_coord(self, coord: tuple[int, int]):
        return self._grid[coord]
