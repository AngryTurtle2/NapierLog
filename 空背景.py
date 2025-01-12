from manim import *
class empty(Scene):
    def construct(self):
        self.wait(3)

if __name__ == "__main__":
    from os import system
    system("manim -p 空背景.py empty")