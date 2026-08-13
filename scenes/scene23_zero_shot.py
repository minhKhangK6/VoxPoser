from manim import *


class VoxPoserScene23(Scene):
    def construct(self):

        BLUE = "#5DADE2"
        GREEN = "#58D68D"
        YELLOW = "#F4D03F"
        RED = "#EC7063"
        PURPLE = "#AF7AC5"
        GRAY = "#BFC9CA"

        # ============================================================
        # TITLE
        # ============================================================

        title = Text(
            "What Does Zero-Shot Mean Here?",
            font_size=38,
            color=BLUE
        ).to_edge(
            UP,
            buff=0.45
        )

        self.play(
            Write(title)
        )

        self.wait(2)

        # ============================================================
        # TRADITIONAL APPROACH
        # ============================================================

        traditional_title = Text(
            "Task-specific approach",
            font_size=29,
            color=RED
        ).move_to(
            LEFT * 3.3 + UP * 1.45
        )

        traditional = VGroup(
            Text(
                "collect task data",
                font_size=23
            ),
            Text(
                "train / tune",
                font_size=23
            ),
            Text(
                "execute learned policy",
                font_size=23
            ),
            Text(
                "new task → often retraining",
                font_size=23,
                color=RED
            )
        ).arrange(
            DOWN,
            buff=0.25
        ).move_to(
            LEFT * 3.3 + DOWN * 0.25
        )

        self.play(
            Write(traditional_title),
            LaggedStart(
                *[
                    FadeIn(
                        x,
                        shift=RIGHT
                    )
                    for x in traditional
                ],
                lag_ratio=0.18
            ),
            run_time=2.3
        )

        self.wait(3)

        # ============================================================
        # VOXPOSER
        # ============================================================

        zero_title = Text(
            "VoxPoser",
            font_size=29,
            color=GREEN
        ).move_to(
            RIGHT * 3.3 + UP * 1.45
        )

        zero = VGroup(
            Text(
                "new language instruction",
                font_size=23
            ),
            Text(
                "new / open-set object",
                font_size=23
            ),
            Text(
                "compose value maps",
                font_size=23
            ),
            Text(
                "plan a trajectory",
                font_size=23,
                color=GREEN
            )
        ).arrange(
            DOWN,
            buff=0.25
        ).move_to(
            RIGHT * 3.3 + DOWN * 0.25
        )

        self.play(
            Write(zero_title),
            LaggedStart(
                *[
                    FadeIn(
                        x,
                        shift=LEFT
                    )
                    for x in zero
                ],
                lag_ratio=0.18
            ),
            run_time=2.3
        )

        self.wait(3)

        # ============================================================
        # CENTER IDEA
        # ============================================================

        self.play(
            FadeOut(traditional_title),
            FadeOut(traditional),
            FadeOut(zero_title),
            FadeOut(zero)
        )

        equation = VGroup(
            Text(
                "Zero-shot",
                font_size=34,
                color=GREEN
            ),
            Text(
                "≠",
                font_size=42,
                color=WHITE
            ),
            Text(
                "zero computation",
                font_size=34,
                color=RED
            )
        ).arrange(
            RIGHT,
            buff=0.3
        )

        self.play(
            FadeIn(equation),
            run_time=1.5
        )

        self.wait(3)

        explanation = Text(
            "The system can synthesize a new solution without",
            font_size=27,
            color=BLUE
        ).to_edge(
            DOWN,
            buff=1.0
        )

        explanation2 = Text(
            "task-specific additional training.",
            font_size=29,
            color=GREEN
        ).to_edge(
            DOWN,
            buff=0.55
        )

        self.play(
            Write(explanation),
            run_time=1.2
        )

        self.wait(2)

        self.play(
            Write(explanation2),
            run_time=1.2
        )

        self.wait(4)

        # ============================================================
        # FINAL
        # ============================================================

        self.play(
            FadeOut(equation),
            FadeOut(explanation),
            FadeOut(explanation2)
        )

        final = VGroup(
            Text(
                "New instruction",
                font_size=28,
                color=YELLOW
            ),
            Arrow(
                LEFT,
                RIGHT,
                buff=0.3
            ),
            Text(
                "new value maps",
                font_size=28,
                color=PURPLE
            ),
            Arrow(
                LEFT,
                RIGHT,
                buff=0.3
            ),
            Text(
                "new trajectory",
                font_size=28,
                color=GREEN
            )
        ).arrange(
            RIGHT,
            buff=0.2
        ).scale(0.82)

        self.play(
            FadeIn(final),
            run_time=1.5
        )

        self.wait(4)