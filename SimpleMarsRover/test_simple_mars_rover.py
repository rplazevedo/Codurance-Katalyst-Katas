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
    def test_create_rover(self):
        oppy = MarsRover()
        self.assertTrue(isinstance(oppy, MarsRover), "Oppy is a Mars Rover")

    def test_init_position(self):
        oppy = MarsRover(0, 0)
        self.assertEqual(oppy.x, 0)
        self.assertEqual(oppy.y, 0)


if __name__ == '__main__':
    unittest.main()
