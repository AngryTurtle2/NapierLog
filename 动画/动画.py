from manim import *
from formula import *
class 动画场景1(Scene):
    def construct(self):
        # 定义一个点P，一个速度向量v
        A0 = LEFT * 6
        v = RIGHT

        P = Dot(point=ORIGIN,color=GREEN, radius=0.04)
        P_text = Text("P").next_to(P, direction=DOWN*2)
        Pv = Arrow(start=P.get_center(), end = P.get_center()+RIGHT, color=RED)
        Pg = VGroup(P, P_text, Pv)
        self.play(FadeIn(P), run_time= 2),
        self.play(FadeIn(P_text), run_time= 2),
        self.play(FadeIn(Pv), run_time= 2),
        self.play(
            Rotate(Pv,
               angle=PI*2,
               about_point = P.get_center(),
               run_time = 4,
               rate_func=smooth)
        )
        

        self.wait()
        bias = Pg.get_center() - P.get_center() 
        Pg.move_to(A0) 
        path = Line(start=A0 + bias, end = A0 + 12 * v + bias)
        self.add((path))
        self.wait(3)
        # 组合
        # group = VGroup(Pg, path)
        linear_animation = MoveAlongPath(Pg, 
                                         path, 
                                         rate_func=linear, 
                                         run_time=5)

        self.play(
            FadeIn(path),
            linear_animation
        )
        # 
        self.wait()

        ''' 
        title = Tex(数列A)
        self.play(
            Write(title),
        )
        self.wait()

        transform_title = Tex(数列B)
        transform_title.to_corner(UP + LEFT)
        self.play(
            Transform(title, transform_title),
        )'''
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