# -*- coding: utf-8 -*-
# @Project  : Codurance-Katalyst-Katas
# @File     : test_mars_rove
# @Date     : 2022-08-30T18:06:43
# @Author   : R.P.L. Azevedo
# @Email    : rplazevedo@gmail.com
# @Software : PyCharm

from MarsRover import MarsPlateau


def test_can_create_grid():
    Plateau = MarsPlateau()
    assert isinstance(Plateau, MarsPlateau)


def test_grid_is_10_by_10():
    Plateau = MarsPlateau()
    assert Plateau._grid.shape == (10, 10)


def test_add_obstacle_at_2_2():
    Plateau = MarsPlateau()
    Plateau.add_obstacle((2, 2))
    assert Plateau._grid[2, 2] == 1


def test_add_multiple_obstacles():
    Plateau = MarsPlateau()
    Plateau.add_mutiple_obstacles([(1, 2), (2, 3)])
    assert Plateau._grid[1, 2] == 1
    assert Plateau._grid[2, 3] == 1
    assert Plateau._grid[2, 2] == 0
