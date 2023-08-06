#!/usr/bin/python3
""" 5-main """
import sys
sys.path.append("./python-almost_a_circle")
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(4, 6, 2, 1, 12)
    print(r1)

    r2 = Rectangle(5, 5, 1)
    print(r2)
