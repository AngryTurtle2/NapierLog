from manim import *
from formula import *
from 自定义动画 import *
from manim.utils.rate_functions import unit_interval
import math


A = []
for i in range(0, 10):
    P = Dot(point=ORIGIN,color=MAROON_A, radius=0.04)
    text = MathTex(f"A_{i}")
    A.append([P , text])
P = Dot(point=ORIGIN,color=MAROON_A, radius=0.04)
text = MathTex("A_n")
A.append([P , text])

B = []
for i in range(0, 10):
    P = Dot(point=ORIGIN,color=MAROON_A, radius=0.04)
    text = MathTex(f"B_{i}")
    B.append([P , text])
P = Dot(point=ORIGIN,color=MAROON_A, radius=0.04)
text = MathTex("B_n")
B.append([P , text])
P = Dot(point=ORIGIN,color=MAROON_A, radius=0.04)
text = MathTex("B_i")
B.append([P , text])
del P, text


class 动画场景1(Scene):
    def construct(self):
        # 定义一个点P，一个速度向量v
        A0 = LEFT * 6.5
        v = RIGHT

        P = Dot(point=ORIGIN,color=GOLD, radius=0.1)
        P_text = Text("P").next_to(P, direction=DOWN*2)
        Pv = Arrow(start=P.get_center(), end = P.get_center()+RIGHT, color=RED)
        Pv.shift(LEFT*0.25)
        Pg = VGroup(P, P_text, Pv)
        bias = Pg.get_center() - P.get_center()
        
        A0_P = A[0][0]
        A0_text = A[0][1]

        self.play(FadeIn(P), run_time= .5),
        self.play(FadeIn(P_text), run_time= .5),
        self.play(FadeIn(Pv), run_time= .5),
        self.play(
            Rotate(Pv,
               angle=PI*2,
               about_point = P.get_center(),
               run_time = 4,
               rate_func=smooth)
        )
        self.wait()

        Pg.move_to(A0 + bias) 
        path = NumberLine(
            x_range=[0, 13, 1],
            length=13,
            color=BLUE,
            include_numbers=True,
            label_direction=UP,
        )

        A0_P.move_to(A0)
        A0_text.next_to(A0_P, direction=UP*2)
        self.add(A0_P)
        self.add(A0_text)

        self.time = 0
        self.last_update = 0
        totalg = Group()
        def update_markers(mob, dt):
            self.time += dt
            if self.time - self.last_update >= 1 and self.time <= 10:
                i  = int(self.time)
                Ptmp = A[i][0].move_to(P.get_center())
                Ptmp_text = A[i][1].next_to(Ptmp, direction=DOWN*2)
                self.add(Ptmp)
                self.add(Ptmp_text)
                totalg.add(Ptmp)
                totalg.add(Ptmp_text)
                self.last_update  = self.time
        
        self.play(FadeIn(path))
        path.add_updater(update_markers)
        self.play(
            运动(Pg, A0 + bias , end = A0 + 13 * RIGHT + bias ,run_time = 12.5)   
        )
        A0_text.next_to(A0_P, direction=DOWN*2)
        path.clear_updaters()
        self.wait()
        Pg.shift(LEFT*5.5)
        for mob in self.mobjects:
            totalg.add(mob)
        self.play(
            totalg.animate.shift(UP*2.5 + RIGHT*0.5)
        )
        self.wait(2)

        self.play(FadeOut(totalg))

        formu = [速度V,匀速距离1,匀速距离2,匀速距离3]
        for i in range(4):
            tmp = MathTex(formu[i])
            self.play(
                Write(tmp)
            )
            self.wait(1)
            self.play(
                FadeOut(tmp)
            )
            self.wait()


class 动画场景2(MovingCameraScene):
    def construct(self):
        Q = Dot(point=ORIGIN,color=GREEN_D, radius=0.1)
        Q_text = Text("Q").next_to(Q, direction=DOWN*2.5).scale(.7)
        C_text = Text("C")
        D_text = Text("D")
        L_text = Text("L")
        self.add(Q, Q_text)
        self.play(FadeIn(Q,run_time= .5))
        self.play(FadeIn(Q_text,run_time= .5))


        path = Line(
            start= LEFT * 6.5,
            end= RIGHT * 6.5,
            color=RED,
        )
        Q.move_to(path.get_left())
        Q_text.next_to(Q, direction=DOWN*2.5)
        self.play(
            FadeIn(L_text.move_to(path.get_center() + UP * 1.5)),
            FadeIn(path),
            FadeIn(C_text.move_to(path.get_left() + UP * 0.5)),
            FadeIn(D_text.move_to(path.get_right() + UP * 0.5)),
        )
        self.wait(2)
        self.play(
            MoveAlongPath(
                Q, path, rate_func=there_and_back, run_time=4
            )
        )

        B[0][0].move_to(path.get_left())
        B[0][1].next_to(B[0][0], direction=DOWN)

        self.play(
            FadeIn(B[0][0]),
            FadeIn(B[0][1]),
        )
        self.wait(1)

        Q.shift(RIGHT * 6.5)
        Q_text.next_to(Q, direction=DOWN*2.5)

        B[11][0].move_to(Q.get_center())
        B[11][1].next_to(Q, direction=DOWN*0.75).scale(0.75)

        self.play(
            FadeIn(B[11][0]),
            FadeIn(B[11][1]),
        )

        Q_move_text = Text("下一秒Q点需要移动的距离是：").scale(0.75)
        Q_move_formu = MathTex("r \cdot |B_iD|  ","  0 < r < 1").scale(0.75)
        Q_move_formu.arrange(DOWN)
        Q_move_text.next_to(Q, direction=DOWN*4.5)
        Q_move_formu.next_to(Q, direction=DOWN*8)
        self.play(
            Write(Q_move_text),
            Write(Q_move_formu),
        )
        self.wait(3)

        self.play(
            FadeOut(B[11][0]),
            FadeOut(B[11][1]),
            FadeOut(Q_move_text),
            FadeOut(Q_move_formu),
        )
        self.time = 0
        self.last_update = 0
        B_text_g = Group()
        B_text_g.add(B[0][0])
        B_text_g.add(B[0][1])
        def update_markers(mob, dt):
            self.time += dt
            if self.time - self.last_update >= 1 and self.time <= 10:
                i  = int(self.time)
                Ptmp = B[i][0].move_to(Q.get_center())
                Ptmp_text = B[i][1].next_to(Ptmp, direction=DOWN* 0.75).scale(0.75)
                self.add(Ptmp)
                self.add(Ptmp_text)
                B_text_g.add(Ptmp)
                B_text_g.add(Ptmp_text)
                self.last_update  = self.time        
        @unit_interval
        def rate_func_Q(t):
            r = 0.2
            # 20是一个等于动画播放时长的常数
            return (1 - (1 - r) ** (20 * t))
        
        Qg = Group(Q, Q_text)
        bias = Qg.get_center() - Q.get_center()

        path.add_updater(update_markers)
        self.play(
            运动(Qg, 
                start = path.get_left() + bias, 
                end = path.get_right() + bias,
                rate_func=rate_func_Q,
                run_time=20
            )
        )

        self.play(
            self.camera.frame.animate.shift(DOWN * 2)
        )
        self.wait(2)
        B0B1 = NumberLine(
            x_range=[0, 1, 1],
            length=13 / 5,
            color=BLUE,
            include_numbers=False
        ).move_to(path.get_left()+ DOWN * 2 + RIGHT * 13/5 / 2)
        tmp_l = []
        for i  in range(0,4):
            tmp = B0B1.copy()
            tmp_l.append(tmp)
        
        self.play(
            FadeIn(B0B1),
        )
        self.wait(2)
        self.play(
            tmp_l[0].animate.shift(RIGHT * 2.6),
            tmp_l[1].animate.shift(RIGHT * 2.6 * 2),
            tmp_l[2].animate.shift(RIGHT * 2.6 * 3),
            tmp_l[3].animate.shift(RIGHT * 2.6 * 4),
        )
        self.wait()

        B1B2 = B0B1.copy().scale(0.8).shift(DOWN + (1.3 +1.04) * RIGHT)
        tmp_l2 = [B1B2.copy() for tmp in tmp_l]

        self.play(
            FadeIn(B1B2),
        )
        self.wait(2) 
        self.play(
            tmp_l2[0].animate.shift(RIGHT * 2.08),
            tmp_l2[1].animate.shift(RIGHT * 2.08 * 2),
            tmp_l2[2].animate.shift(RIGHT * 2.08 * 3),
            tmp_l2[3].animate.shift(RIGHT * 2.08 * 4),
        )
        self.wait()
        path.clear_updaters()
        self.wait()



class 动画场景3(Scene):
    def construct(self):
        self.print_formu(衰减距离1)
        self.print_formu(剩余距离1)
        self.print_formu(衰减距离2)
        self.print_formu(剩余距离2)
        self.print_formu(衰减距离3)
        self.print_formu(剩余距离3)
        self.print_formu(衰减距离n)
        self.print_formu(剩余距离n)
        self.print_formu(纳皮尔对数定义)
        self.print_formu(对数为0)
        self.print_formu(对数为第一个单位)
        self.print_formu(对数为无穷大)


    
    def print_formu(self, formu):
        tmp = MathTex(formu)
        self.play(
            Write(tmp)
        )
        self.wait()
        self.play(
            FadeOut(tmp)
        )
        self.wait()
class 动画场景4(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-1, 1],
            y_range=[-5, 5],
            axis_config={"color": BLUE},
        )

        # Create Graph
        graph = axes.plot(lambda x: np.log(x),x_range=[0.0001, 1,  0.0001])
        graph_label = axes.get_graph_label(graph, label='ln(x)').shift(LEFT * 5)
        self.play(Create(axes), Create(graph), Write(graph_label))
        self.wait(1)
        self.wait()


class 动画场景5(Scene):
    def construct(self):
        xn_text = MathTex("x_n = ",剩余距离n)
        self.play(
            Write(xn_text,run_time=3)
        )
        self.wait(3)
        xt_text = MathTex(剩余距离公式)
        self.play(
            FadeOut(xn_text), 
            FadeIn(xt_text,run_time=3)
        )
        self.wait(3)

        xt_text2 = MathTex(剩余距离公式变换1)
        self.play(
            FadeOut(xt_text), 
            Write(xt_text2,run_time=3),
        )
        self.wait()     
        self.play(
            xt_text2.animate.shift(UP)
        )
        self.wait()

        yt_text = MathTex(匀速运动距离公式)
        self.play(
            Write(yt_text,run_time=3)
        )
        self.wait(3)
        t_text = MathTex(匀速运动时间t)
        self.play(
            FadeOut(yt_text),
            Write(t_text,run_time=3)
        )
        self.wait(3)
        yt_text2 = MathTex(两种运动联系公式)
        self.play(
            FadeOut(xt_text2),
            FadeOut(t_text),
            Write( yt_text2,run_time=3)
        )
        self.wait(3)
        yt_text3 = MathTex(纳皮尔对数定义的实质)
        self.play(
            Transform(yt_text2, yt_text3,run_time=3)
        )
        self.wait(3)




class 动画场景6(Scene):
    def construct(self):
        y_text = MathTex(纳皮尔对数定义的形式)
        self.play(
            Write(y_text,run_time=3)
        )
        self.wait()
        self.play(
            FadeOut(y_text)
        )
        self.wait()

        axes = Axes(
            x_range=[0, np.pi],
            y_range=[0, 1],
            axis_config={"color": BLUE},
        ).scale(.5)

        # Create Graph
        graph = axes.plot(lambda x: np.sin(x),x_range=[0, np.pi,  0.001])
        graph_label = axes.get_graph_label(graph, label='sin(x)').shift(LEFT * 5 + DOWN)

        self.play(
            Create(axes), 
            Create(graph), 
            Write(graph_label)
        )
        self.wait()
        self.clear()

        napsin_text = MathTex(纳皮尔正弦定义)
        self.play(
            Write(napsin_text,run_time=3)
        )
        self.wait()

        napsin30_text = MathTex(纳皮尔正弦30度角)
        self.play(
            napsin_text.animate.shift(UP),
            Write(napsin30_text,run_time=3)
        )
        self.wait()

        napsin1_text = MathTex(纳皮尔正弦1分角)
        napsin1_text.next_to(napsin30_text, direction=DOWN)
        self.play(
            Write(napsin1_text,run_time=3)
        )
        self.wait()


        self.wait(3)
if __name__ == "__main__":
    from os import system
    system("manim -ql 动画.py 动画场景1")
    system("manim -ql 动画.py 动画场景2")
    system("manim -ql 动画.py 动画场景3")
    system("manim -ql 动画.py 动画场景4")
    system("manim -ql 动画.py 动画场景5")
    system("manim -ql 动画.py 动画场景6")