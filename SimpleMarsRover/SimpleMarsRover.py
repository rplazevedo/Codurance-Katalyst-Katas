# -*- coding: utf-8 -*-
# @Project  : Codurance-Katalyst-Katas
# @File     : SimpleMarsRover
# @Date     : 2022-08-29T12:00:33
# @Author   : R.P.L. Azevedo
# @Email    : rplazevedo@gmail.com
# @Software : PyCharm

class MarsRover:
    def __init__(self, x_init=0, y_init=0, dir_init="N") -> None:
        self.x: int = x_init
        self.y: int = y_init
        self.dir: str = dir_init

    def pos(self) -> str:
        return f"{self.x}:{self.y}:{self.dir}"

    def exe(self, command: str) -> None:
        if command == "MM":
            self.y += 2
        if command == "M":
            self.y += 1
