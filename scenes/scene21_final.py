from manim import *


class VoxPoserScene21(Scene):
    def construct(self):

        BLUE = "#5DADE2"
        GREEN = "#58D68D"
        YELLOW = "#F4D03F"
        PURPLE = "#AF7AC5"
        RED = "#EC7063"
        GRAY = "#BFC9CA"

        # ============================================================
        # TITLE
        # ============================================================

        title = Text(
            "Why VoxPoser Matters",
            font_size=42,
            color=BLUE
        ).to_edge(
            UP,
            buff=0.55
        )

        self.play(
            Write(title)
        )

        self.wait(1)

        # ============================================================
        # THREE IDEAS
        # ============================================================

        idea1 = VGroup(
            Text(
                "Language",
                font_size=31,
                color=YELLOW
            ),
            Text(
                "can express high-level goals",
                font_size=23,
                color=GRAY
            )
        ).arrange(
            DOWN,
            buff=0.15
        )

        idea2 = VGroup(
            Text(
                "Value maps",
                font_size=31,
                color=PURPLE
            ),
            Text(
                "translate goals into spatial objectives",
                font_size=23,
                color=GRAY
            )
        ).arrange(
            DOWN,
            buff=0.15
        )

        idea3 = VGroup(
            Text(
                "Planning",
                font_size=31,
                color=GREEN
            ),
            Text(
                "turns those objectives into motion",
                font_size=23,
                color=GRAY
            )
        ).arrange(
            DOWN,
            buff=0.15
        )

        ideas = VGroup(
            idea1,
            idea2,
            idea3
        ).arrange(
            DOWN,
            buff=0.5
        ).move_to(
            ORIGIN
        )

        self.play(
            LaggedStart(
                *[
                    FadeIn(
                        x,
                        shift=RIGHT
                    )
                    for x in ideas
                ],
                lag_ratio=0.2
            ),
            run_time=2.5
        )

        self.wait(3)

        # ============================================================
        # BIG IDEA
        # ============================================================

        self.play(
            FadeOut(ideas)
        )

        big = VGroup(
            Text(
                "The important bridge is",
                font_size=28,
                color=GRAY
            ),
            Text(
                "language → geometry → action",
                font_size=38,
                color=YELLOW
            )
        ).arrange(
            DOWN,
            buff=0.25
        )

        self.play(
            FadeIn(big),
            run_time=1.5
        )

        self.wait(3)

        # ============================================================
        # PHYSICAL AI
        # ============================================================

        self.play(
            FadeOut(big)
        )

        physical_ai = Text(
            "This is the Physical AI perspective:",
            font_size=28,
            color=BLUE
        ).to_edge(
            UP,
            buff=1.7
        )

        self.play(
            Write(physical_ai),
            run_time=1
        )

        statement = Text(
            "reason about the world in language,\n"
            "but act through physical space.",
            font_size=32,
            color=GREEN
        ).move_to(
            ORIGIN
        )

        self.play(
            FadeIn(
                statement,
                shift=UP
            ),
            run_time=1.5
        )

        self.wait(4)

        # ============================================================
        # TRANSITION TO SCENE 22
        # ============================================================

        self.play(
            FadeOut(physical_ai),
            FadeOut(statement),
            FadeOut(title)
        )

        transition = VGroup(
            Text(
                "But what does the system actually generate?",
                font_size=29,
                color=BLUE
            ),
            Text(
                "Let's look inside the LLM.",
                font_size=31,
                color=GREEN
            )
        ).arrange(
            DOWN,
            buff=0.25
        )

        self.play(
            FadeIn(
                transition,
                shift=UP
            ),
            run_time=1.5
        )

        self.wait(4)