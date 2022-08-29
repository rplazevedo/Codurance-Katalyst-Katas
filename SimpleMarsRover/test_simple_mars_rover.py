# -*- coding: utf-8 -*-
# @Project  : Codurance-Katalyst-Katas
# @File     : test_simple_mars_rover
# @Date     : 2022-08-29T12:00:59
# @Author   : R.P.L. Azevedo
# @Email    : rplazevedo@gmail.com
# @Software : PyCharm

import unittest

from SimpleMarsRover import MarsRover


class RoverTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.oppy = MarsRover()

    def test_create_rover(self):
        self.assertTrue(isinstance(self.oppy, MarsRover),
                        "Oppy is a Mars Rover")

    def test_init_position(self):
        self.assertEqual(self.oppy.x, 0)
        self.assertEqual(self.oppy.y, 0)
        self.assertEqual(self.oppy.dir, "N")

    def test_print_pos(self):
        self.assertEqual(self.oppy.pos(), "0:0:N")

    def test_move_north(self):
        self.oppy.exe("M")
        self.assertEqual(self.oppy.pos(), "0:1:N")
        self.oppy.exe("M")
        self.assertEqual(self.oppy.pos(), "0:2:N")

    def test_exe_MM(self):
        self.oppy.exe("MM")
        self.assertEqual(self.oppy.pos(), "0:2:N")

    def test_exe_MMM(self):
        self.oppy.exe("MMM")
        self.assertEqual(self.oppy.pos(), "0:3:N")


if __name__ == '__main__':
    unittest.main()
