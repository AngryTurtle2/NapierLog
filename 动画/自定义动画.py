from manim import *
from collections.abc import Callable
class 运动(Animation):
    # 参考MoveAlongPath
    def __init__(
        self,
        mobject: Mobject,
        start: Mobject,
        end: Mobject,
        rate_func: Callable[[float], float] = linear,
        suspend_mobject_updating: bool | None = False,
        **kwargs,
    ) -> None:
        super().__init__(
            mobject, suspend_mobject_updating=suspend_mobject_updating, **kwargs
        )
        self.start = start
        self.end = end
        self.vector = self.end - self.start
        self.rate_func = rate_func

    def interpolate_mobject(self, alpha: float) -> None:
        point = self.start + self.rate_func(alpha) * self.vector
        self.mobject.move_to(point)