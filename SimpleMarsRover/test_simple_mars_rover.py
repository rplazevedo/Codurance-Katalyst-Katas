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
        self.assertTrue(isinstance(self.oppy, MarsRover), "Oppy is a Mars Rover")

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

    def test_exe_R(self):
        self.oppy.exe("R")
        self.assertEqual(self.oppy.pos(), "0:0:E")

    def test_exe_RR(self):
        self.oppy.exe("RR")
        self.assertEqual(self.oppy.pos(), "0:0:S")

    def test_exe_RRR(self):
        self.oppy.exe("RRR")
        self.assertEqual(self.oppy.pos(), "0:0:W")

    def test_exe_RRRR(self):
        self.oppy.exe("RRRR")
        self.assertEqual(self.oppy.pos(), "0:0:N")

    def test_exe_L(self):
        self.oppy.exe("L")
        self.assertEqual(self.oppy.pos(), "0:0:W")

    def test_exe_LL(self):
        self.oppy.exe("LL")
        self.assertEqual(self.oppy.pos(), "0:0:S")

    def test_exe_LLL(self):
        self.oppy.exe("LLL")
        self.assertEqual(self.oppy.pos(), "0:0:E")

    def test_exe_LLLL(self):
        self.oppy.exe("LLLL")
        self.assertEqual(self.oppy.pos(), "0:0:N")

    def test_turn_right_move_1(self):
        self.oppy.exe("RM")
        self.assertEqual(self.oppy.pos(), "1:0:E")

    def test_turn_right_move_2(self):
        self.oppy.exe("RMM")
        self.assertEqual(self.oppy.pos(), "2:0:E")

    def test_turn_right_2_move_1(self):
        self.oppy.exe("RRM")
        self.assertEqual(self.oppy.pos(), "0:9:S")

    def test_turn_right_2_move_4(self):
        self.oppy.exe("RRMMMM")
        self.assertEqual(self.oppy.pos(), "0:6:S")

    def test_turn_left_1_move_3(self):
        self.oppy.exe("LMMM")
        self.assertEqual(self.oppy.pos(), "7:0:W")

    def test_exe_MMRMMLM(self):
        self.oppy.exe("MMRMMLM")
        self.assertEqual(self.oppy.pos(), "2:3:N")

    def test_wrap_around(self):
        self.oppy.exe("MMMMMMMMMM")
        self.assertEqual(self.oppy.pos(), "0:0:N")


if __name__ == "__main__":
    unittest.main()
