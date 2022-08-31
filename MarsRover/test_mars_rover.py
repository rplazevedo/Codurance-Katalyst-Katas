# -*- coding: utf-8 -*-
# @Project  : Codurance-Katalyst-Katas
# @File     : test_mars_rove
# @Date     : 2022-08-30T18:06:43
# @Author   : R.P.L. Azevedo
# @Email    : rplazevedo@gmail.com
# @Software : PyCharm

import pytest

from MarsRover import MarsPlateau, MarsRover


@pytest.fixture()
def plateau():
    # print("setup")
    yield MarsPlateau()
    # print("teardown")


@pytest.fixture()
def rover():
    # print("setup")
    yield MarsRover()
    # print("teardown")


def test_can_create_grid(plateau):
    # Plateau = MarsPlateau()
    assert isinstance(plateau, MarsPlateau)


def test_grid_is_10_by_10(plateau):
    assert plateau._grid.shape == (10, 10)


def test_add_obstacle_at_2_2(plateau):
    plateau.add_obstacle((2, 2))
    assert plateau._grid[2, 2] == 1


def test_add_multiple_obstacles(plateau):
    plateau.add_mutiple_obstacles([(1, 2), (2, 3)])
    assert plateau._grid[1, 2] == 1
    assert plateau._grid[2, 3] == 1
    assert plateau._grid[2, 2] == 0


def test_is_obstacle_at_coord(plateau):
    plateau.add_obstacle((2, 2))
    plateau.is_obstacle_at_coord((2, 2))
    assert plateau.is_obstacle_at_coord((2, 2))


def test_rover_move_up_obs_at_0_1(plateau, rover):
    plateau.add_obstacle((0, 1))
    assert rover.exe("M", plateau) == "O:0:0:N"


def test_rover_move_up_obs_at_0_3(plateau, rover):
    plateau.add_obstacle((0, 3))
    assert rover.exe("MMMM", plateau) == "O:0:2:N"


def test_rover_move_up_obs_at_3_3(plateau, rover):
    plateau.add_obstacle((3, 3))
    assert rover.exe("RMMMLMMM", plateau) == "O:3:2:N"
