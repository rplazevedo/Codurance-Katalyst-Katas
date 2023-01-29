# -*- coding: utf-8 -*-
# @Project  : Codurance-Katalyst-Katas
# @File     : test_mars_rove
# @Date     : 2022-08-30T18:06:43
# @Author   : R.P.L. Azevedo
# @Email    : rplazevedo@gmail.com
# @Software : PyCharm

import pytest

from MarsRover import MarsPlateau, MarsRover


@pytest.fixture(name="plateau")
def fixture_plateau():
    # print("setup")
    yield MarsPlateau()
    # print("teardown")


@pytest.fixture(name="rover")
def fixture_rover():
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


@pytest.mark.parametrize(
    "command,expected_output",
    [
        ("RMMMLMMM", "O:3:2:N"),
        ("MMMRMMM", "O:2:3:E"),
        ("MMMMRMMMRM", "O:3:4:S"),
        ("RMMMMLMMMLM", "O:4:3:W"),
    ],
)
def test_rover_move_obs_at_3_3(plateau, rover, command, expected_output):
    plateau.add_obstacle((3, 3))
    assert rover.exe(command, plateau) == expected_output


def test_rover_move_after_obstacle(plateau, rover):
    plateau.add_obstacle((0, 3))
    rover.exe("MMMM", plateau)
    assert rover.exe("RMM", plateau) == "2:2:E"


def test_rover_move_into_obstacle_twice(plateau, rover):
    plateau.add_obstacle((0, 3))
    rover.exe("MMMM", plateau)
    assert rover.exe("MM", plateau) == "O:0:2:N"


def test_rover_move_into_two_obstacles(plateau, rover):
    plateau.add_mutiple_obstacles([(0, 3), (4, 2)])
    rover.exe("MMMM", plateau)
    assert rover.exe("RMMMMM", plateau) == "O:3:2:E"


def test_rover_move_up_obs_at_0_9(plateau, rover):
    plateau.add_obstacle((0, 9))
    assert rover.exe("RRM", plateau) == "O:0:0:S"


def test_rover_move_up_obs_at_1_0(plateau, rover):
    plateau.add_obstacle((1, 0))
    assert rover.exe("MRMLMMMMMMMMMM", plateau) == "O:1:9:N"


def test_rover_move_up_1000(plateau, rover):
    assert rover.exe(1000 * "M", plateau) == "0:0:N"
