from manim import *
from formula import *
from 自定义动画 import *

A = []
for i in range(0, 5):
    P = Dot(point=ORIGIN,color=MAROON_A, radius=0.04)
    text = MathTex(f"A_{i}")
    A.append([P , text])
P = Dot(point=ORIGIN,color=MAROON_A, radius=0.04)
text = MathTex("A_n")
A.append([P , text])

B = []
for i in range(0, 5):
    P = Dot(point=ORIGIN,color=MAROON_A, radius=0.04)
    text = MathTex(f"B_{i}")
    B.append([P , text])
P = Dot(point=ORIGIN,color=MAROON_A, radius=0.04)
text = MathTex("B_n")
B.append([P , text])
del P, text

class 动画场景1(Scene):
    def construct(self):
        # 定义一个点P，一个速度向量v
        A0 = LEFT * 6.5
        v = RIGHT

        P = Dot(point=ORIGIN,color=GOLD, radius=0.04)
        P_text = Text("P").next_to(P, direction=DOWN*2)
        Pv = Arrow(start=P.get_center() - 0.5 * LEFT, end = P.get_center()+RIGHT, color=RED, tip_length=0.2)
        Pg = VGroup(P, P_text, Pv)
        bias = Pg.get_center() - P.get_center()
        
        self.play(FadeIn(P), run_time= .5),
        self.play(FadeIn(P_text), run_time= .5),
        self.play(FadeIn(Pv), run_time= .5),
        self.play(
            Rotate(Pv,
               angle=PI*2,
               about_point = P.get_center(),
               run_time = 2,
               rate_func=smooth)
        )   
        self.add(A0_P)
        self.add(A0_text)

        self.wait()
        Pg.move_to(A0) 
        path = Line(start=A0 - bias, end = A0 + 13 * RIGHT - bias)
        self.add(path)
        self.wait(3)
        
        # 组合

        self.play(
            FadeIn(path),
            运动(Pg, A0 , end = A0 + 13 * RIGHT ,run_time = 5)
        )
        # 
        self.wait()

        
        title = MathTex(数列A)
        self.play(
            Write(title),
        )
        self.wait()

        transform_title = MathTex(数列B)
        transform_title.to_corner(UP + LEFT)
        self.play(
            Transform(title, transform_title),
        )
        self.wait()

class 动画场景2(Scene):
    def construct(self):
        self.wait(3)

class 动画场景3(Scene):
    def construct(self):
        self.wait(3)

if __name__ == "__main__":
    from os import system
    system("manim -pql 动画.py 动画场景1")
    #system("manim -p 动画.py 动画场景2")
    #system("manim -p 动画.py 动画场景3")