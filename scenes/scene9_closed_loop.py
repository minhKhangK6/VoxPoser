from manim import *


class VoxPoserScene9(Scene):
    def construct(self):

        # ============================================================
        # COLORS
        # ============================================================

        BLUE = "#5DADE2"
        GREEN = "#58D68D"
        RED = "#EC7063"
        YELLOW = "#F4D03F"
        PURPLE = "#AF7AC5"
        ORANGE = "#F5B041"
        GRAY = "#BFC9CA"

        # ============================================================
        # TITLE
        # ============================================================

        title = Text(
            "Why Closed-Loop Replanning Matters",
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
        # OPEN-LOOP
        # ============================================================

        open_title = Text(
            "Open-loop execution",
            font_size=29,
            color=RED
        ).move_to(
            LEFT * 3.3 + UP * 1.8
        )

        self.play(
            Write(open_title)
        )

        # ------------------------------------------------------------
        # PLAN
        # ------------------------------------------------------------

        plan_box = RoundedRectangle(
            width=3.0,
            height=0.95,
            corner_radius=0.14,
            color=YELLOW,
            fill_opacity=0.08,
            stroke_width=2
        ).move_to(
            LEFT * 3.3 + UP * 0.85
        )

        plan_text = Text(
            "Plan",
            font_size=26,
            color=YELLOW
        ).move_to(
            plan_box
        )

        # ------------------------------------------------------------
        # EXECUTE
        # ------------------------------------------------------------

        execute_box = RoundedRectangle(
            width=3.0,
            height=0.95,
            corner_radius=0.14,
            color=GREEN,
            fill_opacity=0.08,
            stroke_width=2
        ).move_to(
            LEFT * 3.3 + DOWN * 0.15
        )

        execute_text = Text(
            "Execute",
            font_size=26,
            color=GREEN
        ).move_to(
            execute_box
        )

        # ------------------------------------------------------------
        # HOPE
        # ------------------------------------------------------------

        hope_box = RoundedRectangle(
            width=3.0,
            height=0.95,
            corner_radius=0.14,
            color=BLUE,
            fill_opacity=0.08,
            stroke_width=2
        ).move_to(
            LEFT * 3.3 + DOWN * 1.15
        )

        hope_text = Text(
            "Hope nothing\nchanges",
            font_size=21,
            color=RED
        ).move_to(
            hope_box
        )

        # ------------------------------------------------------------
        # OPEN-LOOP ARROWS
        # ------------------------------------------------------------

        arrow1 = Arrow(
            plan_box.get_bottom(),
            execute_box.get_top(),
            buff=0.06,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.16
        )

        arrow2 = Arrow(
            execute_box.get_bottom(),
            hope_box.get_top(),
            buff=0.06,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.16
        )

        # ------------------------------------------------------------
        # ANIMATION
        # ------------------------------------------------------------

        self.play(
            FadeIn(plan_box),
            Write(plan_text),
            run_time=0.7
        )

        self.play(
            GrowArrow(arrow1),
            FadeIn(execute_box),
            Write(execute_text),
            run_time=0.7
        )

        self.play(
            GrowArrow(arrow2),
            FadeIn(hope_box),
            Write(hope_text),
            run_time=0.7
        )

        self.wait(2)

        # ============================================================
        # DISTURBANCE
        # ============================================================

        disturbance = Text(
            "But the world can change.",
            font_size=26,
            color=ORANGE
        ).move_to(
            RIGHT * 3.2 + UP * 1.8
        )

        self.play(
            Write(disturbance)
        )

        # ------------------------------------------------------------
        # ROBOT / OBSTACLE / TARGET
        # ------------------------------------------------------------

        robot = Circle(
            radius=0.18,
            color=YELLOW,
            fill_opacity=1
        ).move_to(
            RIGHT * 2.0 + DOWN * 0.3
        )

        obstacle = Circle(
            radius=0.48,
            color=RED,
            fill_opacity=0.35
        ).move_to(
            RIGHT * 3.5 + DOWN * 0.3
        )

        target = Circle(
            radius=0.25,
            color=GREEN,
            fill_opacity=0.25
        ).move_to(
            RIGHT * 5.0 + DOWN * 0.3
        )

        target_text = Text(
            "goal",
            font_size=19,
            color=GREEN
        ).next_to(
            target,
            DOWN,
            buff=0.15
        )

        self.play(
            FadeIn(robot),
            FadeIn(obstacle),
            FadeIn(target),
            Write(target_text),
            run_time=1
        )

        # ------------------------------------------------------------
        # OLD TRAJECTORY
        # ------------------------------------------------------------

        old_path = VMobject(
            color=RED,
            stroke_width=4
        )

        old_path.set_points_as_corners(
            [
                robot.get_center(),
                RIGHT * 3.0 + DOWN * 0.3,
                target.get_center()
            ]
        )

        self.play(
            Create(old_path),
            run_time=1.5
        )

        self.wait(2)

        collision_text = Text(
            "Old plan is no longer safe.",
            font_size=23,
            color=RED
        ).to_edge(
            DOWN,
            buff=0.65
        )

        self.play(
            Write(collision_text)
        )

        self.wait(2)

        # ============================================================
        # CLOSED LOOP
        # ============================================================

        self.play(
            FadeOut(open_title),
            FadeOut(plan_box),
            FadeOut(execute_box),
            FadeOut(hope_box),
            FadeOut(plan_text),
            FadeOut(execute_text),
            FadeOut(hope_text),
            FadeOut(arrow1),
            FadeOut(arrow2),
            FadeOut(disturbance),
            FadeOut(robot),
            FadeOut(obstacle),
            FadeOut(target),
            FadeOut(target_text),
            FadeOut(old_path),
            FadeOut(collision_text)
        )

        closed_title = Text(
            "Closed-loop execution",
            font_size=30,
            color=GREEN
        ).to_edge(
            UP,
            buff=1.25
        )

        self.play(
            Write(closed_title)
        )

        # ============================================================
        # CLOSED-LOOP — 2 x 2 LAYOUT
        # ============================================================

        observe = RoundedRectangle(
            width=3.0,
            height=1.0,
            corner_radius=0.16,
            color=BLUE,
            fill_opacity=0.08,
            stroke_width=2.2
        ).move_to(
            LEFT * 3.0 + UP * 0.35
        )

        plan = RoundedRectangle(
            width=3.0,
            height=1.0,
            corner_radius=0.16,
            color=PURPLE,
            fill_opacity=0.08,
            stroke_width=2.2
        ).move_to(
            RIGHT * 3.0 + UP * 0.35
        )

        execute = RoundedRectangle(
            width=3.0,
            height=1.0,
            corner_radius=0.16,
            color=YELLOW,
            fill_opacity=0.08,
            stroke_width=2.2
        ).move_to(
            RIGHT * 3.0 + DOWN * 1.25
        )

        feedback = RoundedRectangle(
            width=3.0,
            height=1.0,
            corner_radius=0.16,
            color=ORANGE,
            fill_opacity=0.08,
            stroke_width=2.2
        ).move_to(
            LEFT * 3.0 + DOWN * 1.25
        )

        # ------------------------------------------------------------
        # TEXT
        # ------------------------------------------------------------

        observe_text = Text(
            "Observe",
            font_size=25,
            color=BLUE
        ).move_to(
            observe
        )

        plan_text2 = Text(
            "Plan",
            font_size=25,
            color=PURPLE
        ).move_to(
            plan
        )

        execute_text2 = Text(
            "Execute",
            font_size=25,
            color=YELLOW
        ).move_to(
            execute
        )

        feedback_text = Text(
            "Visual\nfeedback",
            font_size=21,
            color=ORANGE,
            line_spacing=0.85
        ).move_to(
            feedback
        )

        # ------------------------------------------------------------
        # LOOP ARROWS
        # ------------------------------------------------------------

        arrow_observe_plan = Arrow(
            observe.get_right(),
            plan.get_left(),
            buff=0.14,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.14
        )

        arrow_plan_execute = Arrow(
            plan.get_bottom(),
            execute.get_top(),
            buff=0.14,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.14
        )

        arrow_execute_feedback = Arrow(
            execute.get_left(),
            feedback.get_right(),
            buff=0.14,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.14
        )

        arrow_feedback_observe = Arrow(
            feedback.get_top(),
            observe.get_bottom(),
            buff=0.14,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.14
        )

        # ------------------------------------------------------------
        # ANIMATE LOOP
        # ------------------------------------------------------------

        self.play(
            FadeIn(observe),
            Write(observe_text),
            run_time=0.7
        )

        self.play(
            GrowArrow(arrow_observe_plan),
            FadeIn(plan),
            Write(plan_text2),
            run_time=0.7
        )

        self.play(
            GrowArrow(arrow_plan_execute),
            FadeIn(execute),
            Write(execute_text2),
            run_time=0.7
        )

        self.play(
            GrowArrow(arrow_execute_feedback),
            FadeIn(feedback),
            Write(feedback_text),
            run_time=0.7
        )

        self.play(
            GrowArrow(arrow_feedback_observe),
            run_time=0.9
        )

        self.wait(2)

        # ============================================================
        # 5 HZ
        # ============================================================

        frequency = MathTex(
            r"5\ \mathrm{Hz}"
        ).scale(
            1.2
        ).move_to(
            DOWN * 2.55
        )

        frequency_text = Text(
            "replanning frequency reported in the paper",
            font_size=20,
            color=GRAY
        ).next_to(
            frequency,
            DOWN,
            buff=0.12
        )

        self.play(
            Write(frequency),
            Write(frequency_text),
            run_time=1.2
        )

        self.wait(3)

        # ============================================================
        # CACHED LANGUAGE MODEL OUTPUT
        # ============================================================

        self.play(
            FadeOut(frequency),
            FadeOut(frequency_text)
        )

        cache_text = Text(
            "The language-model output can stay fixed;",
            font_size=25,
            color=BLUE
        )

        cache_text2 = Text(
            "the generated program is re-evaluated from new visual feedback.",
            font_size=23,
            color=GREEN
        )

        cache = VGroup(
            cache_text,
            cache_text2
        ).arrange(
            DOWN,
            buff=0.18
        ).move_to(
            DOWN * 2.25
        )

        self.play(
            FadeIn(cache[0]),
            FadeIn(cache[1]),
            run_time=1.5
        )

        self.wait(4)