from manim import *


class VoxPoserScene10(Scene):
    def construct(self):

        # ============================================================
        # COLORS
        # ============================================================

        BLUE = "#5DADE2"
        GREEN = "#58D68D"
        YELLOW = "#F4D03F"
        ORANGE = "#F5B041"
        PURPLE = "#AF7AC5"
        RED = "#EC7063"
        GRAY = "#BFC9CA"

        # ============================================================
        # TITLE
        # ============================================================

        title = Text(
            "From the Idea to Real Robot Tasks",
            font_size=36,
            color=BLUE
        ).to_edge(
            UP,
            buff=0.45
        )

        self.play(
            Write(title)
        )

        self.wait(1)

        # ============================================================
        # SIMULATION / REAL ROBOT
        # ============================================================

        sim_box = RoundedRectangle(
            width=4.2,
            height=3.0,
            corner_radius=0.18,
            color=PURPLE,
            fill_opacity=0.08,
            stroke_width=2
        ).move_to(
            LEFT * 3
        )

        real_box = RoundedRectangle(
            width=4.2,
            height=3.0,
            corner_radius=0.18,
            color=GREEN,
            fill_opacity=0.08,
            stroke_width=2
        ).move_to(
            RIGHT * 3
        )

        sim_title = Text(
            "Simulation",
            font_size=30,
            color=PURPLE
        ).move_to(
            sim_box.get_top() + DOWN * 0.45
        )

        real_title = Text(
            "Real Robot",
            font_size=30,
            color=GREEN
        ).move_to(
            real_box.get_top() + DOWN * 0.45
        )

        self.play(
            FadeIn(sim_box),
            FadeIn(real_box),
            Write(sim_title),
            Write(real_title),
            run_time=1.3
        )

        # ============================================================
        # SIMULATION TASKS
        # ============================================================

        sim_tasks = VGroup(
            Text(
                "pick and place",
                font_size=22
            ),
            Text(
                "sorting",
                font_size=22
            ),
            Text(
                "opening objects",
                font_size=22
            ),
            Text(
                "spatial manipulation",
                font_size=22
            )
        ).arrange(
            DOWN,
            buff=0.22
        ).move_to(
            sim_box.get_center() + DOWN * 0.2
        )

        # ============================================================
        # REAL ROBOT TASKS
        # ============================================================

        real_tasks = VGroup(
            Text(
                "drawer manipulation",
                font_size=22
            ),
            Text(
                "table setting",
                font_size=22
            ),
            Text(
                "trash sorting",
                font_size=22
            ),
            Text(
                "contact-rich tasks",
                font_size=22
            )
        ).arrange(
            DOWN,
            buff=0.22
        ).move_to(
            real_box.get_center() + DOWN * 0.2
        )

        self.play(
            LaggedStart(
                *[
                    FadeIn(
                        x,
                        shift=RIGHT
                    )
                    for x in sim_tasks
                ],
                lag_ratio=0.15
            ),
            LaggedStart(
                *[
                    FadeIn(
                        x,
                        shift=LEFT
                    )
                    for x in real_tasks
                ],
                lag_ratio=0.15
            ),
            run_time=2.2
        )

        self.wait(3)

        # ============================================================
        # FREE-FORM LANGUAGE
        # ============================================================

        # Remove the two large panels completely.
        # Only the language instruction remains.

        self.play(
            FadeOut(sim_tasks),
            FadeOut(real_tasks),
            FadeOut(sim_box),
            FadeOut(real_box),
            FadeOut(sim_title),
            FadeOut(real_title),
            run_time=0.8
        )

        language = Text(
            '"Sort the paper trash into the blue tray."',
            font_size=30,
            color=YELLOW
        )

        self.play(
            Write(language),
            run_time=1.4
        )

        self.wait(2)

        # ============================================================
        # OPEN-SET IDEA
        # ============================================================

        open_set = VGroup(
            Text(
                "Open-set instructions",
                font_size=27,
                color=YELLOW
            ),
            Text(
                "Open-set objects",
                font_size=27,
                color=GREEN
            ),
            Text(
                "No task-specific retraining",
                font_size=27,
                color=ORANGE
            )
        ).arrange(
            DOWN,
            buff=0.3
        )

        open_set.next_to(
            language,
            DOWN,
            buff=0.7
        )

        self.play(
            LaggedStart(
                *[
                    FadeIn(
                        x,
                        shift=UP
                    )
                    for x in open_set
                ],
                lag_ratio=0.18
            ),
            run_time=2
        )

        self.wait(3)

        # ============================================================
        # FINAL MESSAGE
        # ============================================================

        self.play(
            FadeOut(language),
            FadeOut(open_set),
            FadeOut(title)
        )

        final = Text(
            "The point is not one scripted task — "
            "it is generalization across tasks.",
            font_size=29,
            color=BLUE
        )

        self.play(
            FadeIn(final),
            run_time=1.4
        )

        self.wait(4)