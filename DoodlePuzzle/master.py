import os
import subprocess as sp
import random as rd
import numpy as np


def test_py(start_x, start_y):

  class point:
    x = 0
    y = 0

  def traverse_random(grid, start, count):
    grid[start.x][start.y] = count
    count += 1
    start = get_empty_point(grid, start)
    if start.x == 9 and start.y == 9:
      print(count)
      if count == 26:
        print(grid)
      return(grid)
    else:
      return(traverse_random(grid, start, count))

  def get_empty_point(grid, start):
    found = False
    count = 0
    p = point()
    while (not found) and count < 1000:
      f_p = get_valid_move(grid, start)
      if f_p.x == 9 and f_p.y == 9:
        return(f_p)
      elif grid[f_p.x][f_p.y] == 0:
        found = True
        p = f_p
      else:
        count += 1
    if (not found):
      p.x = 9
      p.y = 9
    return(p)

  def get_valid_move(grid, start):
    valid = False
    count = 0
    while (not valid) and (count < 1000):
      p = point()
      p.x = start.x
      p.y = start.y
      move_key = rd.randint(1,8)
      if move_key == 1:
        p.x += 3
      elif move_key == 2:
        p.x -= 3
      elif move_key == 3:
        p.y += 3
      elif move_key == 4:
        p.y -= 3
      elif move_key == 5:
        p.x += 2
        p.y += 2
      elif move_key == 6:
        p.x += 2
        p.y -= 2
      elif move_key == 7:
        p.x -= 2
        p.y += 2
      else:
        p.x -= 2
        p.y -= 2
      if (p.x > len(grid) - 1) or (p.y > len(grid) - 1) or (p.x < 0) or (p.y < 0) or (grid[p.x][p.y] > 0):
        count += 1
      else:
        valid = True
        return(p)
    p.x = 9
    p.y = 9
    return(p)

  t_grid = np.zeros((5,5), dtype = int)
  p1 = point()
  p1.x = start_x
  p1.y = start_y
  return(traverse_random(t_grid, p1, 1))

base_string = "python test.py "

win = False
for x in range(5):
  for y in range(5):
    print("trying " + str(x) + " " + str(y))
    count = 0
    while count < 100:
      result = test_py(x, y)
      count += 1
