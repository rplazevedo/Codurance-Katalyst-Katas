# -*- coding: utf-8 -*-
# @Project  : Codurance-Katalyst-Katas
# @File     : test_mars_rove
# @Date     : 2022-08-30T18:06:43
# @Author   : R.P.L. Azevedo
# @Email    : rplazevedo@gmail.com
# @Software : PyCharm

from MarsRover import MarsPlateau, MarsRover

Spirit = MarsRover()

Grid = MarsPlateau()


def test_can_create_grid():
    assert isinstance(Grid, MarsPlateau)


def test_grid_is_10_by_10():
    assert Grid._grid.shape == (10, 10)
