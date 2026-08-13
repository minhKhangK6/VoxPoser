from manim import *


class VoxPoserScene11(Scene):
    def construct(self):

        BLUE = "#5DADE2"
        GREEN = "#58D68D"
        YELLOW = "#F4D03F"
        ORANGE = "#F5B041"
        RED = "#EC7063"
        PURPLE = "#AF7AC5"
        GRAY = "#BFC9CA"

        # ============================================================
        # TITLE
        # ============================================================

        title = Text(
            "Behavioral Commonsense Reasoning",
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
        # TASK
        # ============================================================

        task = Text(
            "Task: Set the table",
            font_size=30,
            color=YELLOW
        )

        self.play(
            Write(task)
        )

        self.wait(1.5)

        # ============================================================
        # TABLE
        # ============================================================

        table = Rectangle(
            width=8,
            height=3.5,
            color=GRAY,
            fill_opacity=0.06
        ).move_to(
            DOWN * 0.5
        )

        bowl = Circle(
            radius=0.6,
            color=BLUE,
            fill_opacity=0.15
        ).move_to(
            ORIGIN
        )

        bowl_label = Text(
            "bowl",
            font_size=20,
            color=BLUE
        ).next_to(
            bowl,
            DOWN,
            buff=0.12
        )

        fork_right = Line(
            RIGHT * 1.1 + DOWN * 0.3,
            RIGHT * 1.7 + DOWN * 0.3,
            color=PURPLE,
            stroke_width=7
        )

        fork_right_label = Text(
            "fork",
            font_size=20,
            color=PURPLE
        ).next_to(
            fork_right,
            DOWN,
            buff=0.12
        )

        self.play(
            Create(table),
            FadeIn(bowl),
            Write(bowl_label),
            Create(fork_right),
            Write(fork_right_label),
            run_time=1.8
        )

        self.wait(2)

        # ============================================================
        # USER PREFERENCE
        # ============================================================

        preference = Text(
            '"I am left-handed."',
            font_size=34,
            color=ORANGE
        ).to_edge(
            UP,
            buff=1.4
        )

        self.play(
            Write(preference),
            run_time=1.2
        )

        self.wait(2)

        # ============================================================
        # REASONING
        # ============================================================

        reasoning = VGroup(
            Text(
                "Human preference",
                font_size=25,
                color=ORANGE
            ),
            Arrow(
                LEFT,
                RIGHT,
                buff=0.25
            ),
            Text(
                "Contextual meaning",
                font_size=25,
                color=GREEN
            ),
            Arrow(
                LEFT,
                RIGHT,
                buff=0.25
            ),
            Text(
                "Action changes",
                font_size=25,
                color=YELLOW
            )
        ).arrange(
            RIGHT,
            buff=0.3
        ).scale(0.78)

        reasoning.to_edge(
            DOWN,
            buff=0.7
        )

        self.play(
            FadeIn(reasoning),
            run_time=1.8
        )

        self.wait(2)

        # ============================================================
        # MOVE FORK
        # ============================================================

        fork_left = fork_right.copy()

        fork_left.shift(
            LEFT * 2.2
        )

        fork_left_label = Text(
            "fork",
            font_size=20,
            color=GREEN
        ).next_to(
            fork_left,
            DOWN,
            buff=0.12
        )

        arrow_move = Arrow(
            fork_right.get_center(),
            fork_left.get_center(),
            color=GREEN,
            stroke_width=3
        )

        self.play(
            Create(arrow_move),
            Transform(
                fork_right,
                fork_left
            ),
            FadeOut(fork_right_label),
            FadeIn(fork_left_label),
            run_time=2
        )

        self.wait(2)

        result = Text(
            "The robot changes the placement — "
            "without retraining a new task.",
            font_size=27,
            color=GREEN
        ).to_edge(
            DOWN,
            buff=0.65
        )

        self.play(
            Write(result),
            run_time=1.3
        )

        self.wait(4)