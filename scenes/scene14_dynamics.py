from manim import *


class VoxPoserScene14(Scene):
    def construct(self):

        # ============================================================
        # COLORS
        # ============================================================

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

        self.play(
            Write(title)
        )

        self.wait(1)

        # ============================================================
        # STATE 1 — PROBLEM
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

        # Remove the problem sentence before introducing
        # the visual example.
        self.play(
            FadeOut(problem),
            run_time=0.6
        )

        # ============================================================
        # STATE 2 — EXAMPLE
        # ============================================================

        example_title = Text(
            "Interaction with an unknown object",
            font_size=27,
            color=GRAY
        ).to_edge(
            UP,
            buff=1.35
        )

        self.play(
            Write(example_title),
            run_time=0.9
        )

        # ------------------------------------------------------------
        # TABLE
        # ------------------------------------------------------------

        table = Rectangle(
            width=8.2,
            height=1.0,
            color=GRAY,
            fill_opacity=0.05,
            stroke_width=2
        ).move_to(
            DOWN * 1.0
        )

        # ------------------------------------------------------------
        # OBJECT
        # ------------------------------------------------------------

        object_box = RoundedRectangle(
            width=2.3,
            height=1.2,
            corner_radius=0.15,
            color=PURPLE,
            fill_opacity=0.15,
            stroke_width=2
        ).move_to(
            LEFT * 1.7 + DOWN * 0.35
        )

        object_label = Text(
            "object",
            font_size=23,
            color=PURPLE
        ).move_to(
            object_box
        )

        # ------------------------------------------------------------
        # ROBOT
        # ------------------------------------------------------------

        robot = Circle(
            radius=0.18,
            color=YELLOW,
            fill_opacity=1
        ).move_to(
            LEFT * 3.6 + DOWN * 0.35
        )

        robot_label = Text(
            "robot",
            font_size=19,
            color=YELLOW
        ).next_to(
            robot,
            DOWN,
            buff=0.12
        )

        # ------------------------------------------------------------
        # MOTION
        # ------------------------------------------------------------

        motion = Arrow(
            robot.get_center(),
            object_box.get_left() + LEFT * 0.10,
            color=YELLOW,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.13,
            buff=0.08
        )

        example_group = VGroup(
            table,
            object_box,
            object_label,
            robot,
            robot_label,
            motion
        )

        self.play(
            Create(table),
            FadeIn(object_box),
            Write(object_label),
            FadeIn(robot),
            Write(robot_label),
            GrowArrow(motion),
            run_time=1.6
        )

        self.wait(2)

        # ============================================================
        # STATE 3 — OBSERVATION
        # ============================================================

        observation = Text(
            "Observe what actually happens.",
            font_size=27,
            color=GREEN
        ).to_edge(
            DOWN,
            buff=0.75
        )

        self.play(
            Write(observation),
            run_time=1
        )

        self.wait(1.5)

        # ------------------------------------------------------------
        # OBJECT MOVES AFTER CONTACT
        # ------------------------------------------------------------

        object_after = object_box.copy().shift(
            RIGHT * 1.0
        )

        object_after_label = object_label.copy().move_to(
            object_after
        )

        contact_arrow = Arrow(
            object_box.get_right(),
            object_after.get_left(),
            color=GREEN,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.13,
            buff=0.08
        )

        self.play(
            GrowArrow(contact_arrow),
            Transform(
                object_box,
                object_after
            ),
            Transform(
                object_label,
                object_after_label
            ),
            run_time=1.5
        )

        self.wait(2)

        # ============================================================
        # STATE 4 — LEARNED MODEL
        # ============================================================

        # Clear the visual interaction before showing
        # the learned model.
        self.play(
            FadeOut(example_group),
            FadeOut(object_box),
            FadeOut(object_label),
            FadeOut(observation),
            FadeOut(contact_arrow),
            FadeOut(example_title),
            run_time=0.8
        )

        model_title = Text(
            "Learning from interaction",
            font_size=28,
            color=ORANGE
        ).to_edge(
            UP,
            buff=1.35
        )

        self.play(
            Write(model_title),
            run_time=0.9
        )

        # ------------------------------------------------------------
        # MODEL BOX
        # ------------------------------------------------------------

        model_box = RoundedRectangle(
            width=5.0,
            height=1.75,
            corner_radius=0.18,
            color=ORANGE,
            fill_opacity=0.08,
            stroke_width=2
        ).move_to(
            ORIGIN
        )

        model_text = VGroup(
            Text(
                "Online dynamics model",
                font_size=27,
                color=ORANGE
            ),
            Text(
                "learn from visual interaction",
                font_size=21,
                color=GRAY
            )
        ).arrange(
            DOWN,
            buff=0.18
        ).move_to(
            model_box
        )

        self.play(
            FadeIn(model_box),
            FadeIn(model_text),
            run_time=1
        )

        self.wait(2)

        # ============================================================
        # STATE 5 — FEEDBACK LOOP
        # ============================================================

        self.play(
            FadeOut(model_box),
            FadeOut(model_text),
            FadeOut(model_title),
            run_time=0.7
        )

        loop_title = Text(
            "Interaction creates a feedback loop",
            font_size=28,
            color=BLUE
        ).to_edge(
            UP,
            buff=1.35
        )

        self.play(
            Write(loop_title),
            run_time=0.9
        )

        # ------------------------------------------------------------
        # THREE STEP LOOP
        # ------------------------------------------------------------

        observe_box = RoundedRectangle(
            width=2.4,
            height=0.9,
            corner_radius=0.14,
            color=BLUE,
            fill_opacity=0.08,
            stroke_width=2
        ).move_to(
            LEFT * 3.0
        )

        learn_box = RoundedRectangle(
            width=2.4,
            height=0.9,
            corner_radius=0.14,
            color=ORANGE,
            fill_opacity=0.08,
            stroke_width=2
        ).move_to(
            ORIGIN
        )

        plan_box = RoundedRectangle(
            width=2.4,
            height=0.9,
            corner_radius=0.14,
            color=GREEN,
            fill_opacity=0.08,
            stroke_width=2
        ).move_to(
            RIGHT * 3.0
        )

        observe_text = Text(
            "Observe",
            font_size=24,
            color=BLUE
        ).move_to(
            observe_box
        )

        learn_text = Text(
            "Learn",
            font_size=24,
            color=ORANGE
        ).move_to(
            learn_box
        )

        plan_text = Text(
            "Plan better",
            font_size=24,
            color=GREEN
        ).move_to(
            plan_box
        )

        arrow_1 = Arrow(
            observe_box.get_right(),
            learn_box.get_left(),
            buff=0.12,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.14
        )

        arrow_2 = Arrow(
            learn_box.get_right(),
            plan_box.get_left(),
            buff=0.12,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.14
        )

        self.play(
            FadeIn(observe_box),
            Write(observe_text),
            run_time=0.7
        )

        self.play(
            GrowArrow(arrow_1),
            FadeIn(learn_box),
            Write(learn_text),
            run_time=0.7
        )

        self.play(
            GrowArrow(arrow_2),
            FadeIn(plan_box),
            Write(plan_text),
            run_time=0.7
        )

        self.wait(3)

        # ============================================================
        # STATE 6 — SUMMARY
        # ============================================================

        self.play(
            FadeOut(observe_box),
            FadeOut(learn_box),
            FadeOut(plan_box),
            FadeOut(observe_text),
            FadeOut(learn_text),
            FadeOut(plan_text),
            FadeOut(arrow_1),
            FadeOut(arrow_2),
            FadeOut(loop_title),
            run_time=0.7
        )

        summary = Text(
            "The robot does not need a perfect dynamics model from the start.",
            font_size=25,
            color=BLUE
        )

        self.play(
            FadeIn(summary),
            run_time=1.3
        )

        self.wait(4)