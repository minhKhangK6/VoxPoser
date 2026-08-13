from manim import *


class VoxPoserScene14(Scene):
    def construct(self):

        BLUE = "#5DADE2"
        GREEN = "#58D68D"
        YELLOW = "#F4D03F"
        RED = "#EC7063"
        PURPLE = "#AF7AC5"
        ORANGE = "#F5B041"
        GRAY = "#BFC9CA"

        # ============================================================
        # TITLE
        # ============================================================

        title = Text(
            "Learning Dynamics from Interaction",
            font_size=36,
            color=BLUE
        ).to_edge(
            UP,
            buff=0.45
        )

        self.play(Write(title))
        self.wait(1)

        # ============================================================
        # PROBLEM
        # ============================================================

        problem = Text(
            "Some robot interactions are difficult to model beforehand.",
            font_size=27,
            color=YELLOW
        )

        self.play(
            Write(problem),
            run_time=1.2
        )

        self.wait(2)

        # ============================================================
        # EXAMPLE
        # ============================================================

        table = Rectangle(
            width=8,
            height=1.1,
            color=GRAY,
            fill_opacity=0.05
        ).shift(DOWN * 1.2)

        object_box = RoundedRectangle(
            width=2.3,
            height=1.2,
            color=PURPLE,
            fill_opacity=0.15
        ).move_to(
            LEFT * 2.3 + DOWN * 0.35
        )

        object_label = Text(
            "object",
            font_size=23,
            color=PURPLE
        ).move_to(object_box)

        robot = Circle(
            radius=0.18,
            color=YELLOW
        ).move_to(
            LEFT * 3.8 + DOWN * 0.35
        )

        motion = Arrow(
            robot.get_center(),
            object_box.get_left(),
            color=YELLOW,
            stroke_width=4
        )

        self.play(
            Create(table),
            FadeIn(object_box),
            Write(object_label),
            FadeIn(robot),
            GrowArrow(motion),
            run_time=1.6
        )

        self.wait(2)

        # ============================================================
        # OBSERVATION
        # ============================================================

        observation = Text(
            "Observe what actually happens.",
            font_size=26,
            color=GREEN
        ).to_edge(
            DOWN,
            buff=0.8
        )

        self.play(
            Write(observation)
        )

        self.wait(2)

        # Move object after contact
        object_after = object_box.copy().shift(
            RIGHT * 1.0
        )

        self.play(
            Transform(object_box, object_after),
            run_time=1.5
        )

        self.wait(1.5)

        # ============================================================
        # LEARNED MODEL
        # ============================================================

        self.play(
            FadeOut(observation),
            FadeOut(motion),
            FadeOut(robot)
        )

        model_box = RoundedRectangle(
            width=4.2,
            height=1.5,
            color=ORANGE,
            fill_opacity=0.08
        ).move_to(
            DOWN * 2.1
        )

        model_text = VGroup(
            Text(
                "Online dynamics model",
                font_size=25,
                color=ORANGE
            ),
            Text(
                "learn from visual interaction",
                font_size=20,
                color=GRAY
            )
        ).arrange(
            DOWN,
            buff=0.15
        ).move_to(model_box)

        self.play(
            FadeIn(model_box),
            FadeIn(model_text),
            run_time=1
        )

        self.wait(2)

        # ============================================================
        # FEEDBACK LOOP
        # ============================================================

        loop_text = VGroup(
            Text("observe", font_size=23, color=BLUE),
            Arrow(LEFT, RIGHT, buff=0.25),
            Text("learn", font_size=23, color=ORANGE),
            Arrow(LEFT, RIGHT, buff=0.25),
            Text("plan better", font_size=23, color=GREEN)
        ).arrange(
            RIGHT,
            buff=0.25
        ).scale(0.9).to_edge(
            UP,
            buff=1.45
        )

        self.play(
            FadeIn(loop_text),
            run_time=1.5
        )

        self.wait(3)

        # ============================================================
        # SUMMARY
        # ============================================================

        summary = Text(
            "The robot does not need a perfect dynamics model from the start.",
            font_size=25,
            color=BLUE
        ).to_edge(
            DOWN,
            buff=0.55
        )

        self.play(
            Write(summary),
            run_time=1.3
        )

        self.wait(4)