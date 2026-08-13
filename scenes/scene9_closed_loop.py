from manim import *


class VoxPoserScene9(Scene):
    def construct(self):

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

        stages = VGroup(
            RoundedRectangle(
                width=2.4,
                height=0.8,
                color=YELLOW,
                fill_opacity=0.08
            ),
            RoundedRectangle(
                width=2.4,
                height=0.8,
                color=GREEN,
                fill_opacity=0.08
            ),
            RoundedRectangle(
                width=2.4,
                height=0.8,
                color=BLUE,
                fill_opacity=0.08
            )
        ).arrange(
            DOWN,
            buff=0.35
        ).move_to(
            LEFT * 3.3
        )

        stage_text = VGroup(
            Text("Plan", font_size=24),
            Text("Execute", font_size=24),
            Text("Hope nothing changes", font_size=20, color=RED)
        )

        for text, box in zip(stage_text, stages):
            text.move_to(box)

        self.play(
            FadeIn(stages[0]),
            Write(stage_text[0]),
            run_time=0.7
        )

        self.play(
            FadeIn(stages[1]),
            Write(stage_text[1]),
            run_time=0.7
        )

        self.play(
            FadeIn(stages[2]),
            Write(stage_text[2]),
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

        # Robot and obstacle
        robot = Circle(
            radius=0.18,
            color=YELLOW,
            fill_opacity=1
        ).move_to(
            RIGHT * 2.2 + DOWN * 0.3
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

        # Old trajectory
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
            FadeOut(stages),
            FadeOut(stage_text),
            FadeOut(disturbance),
            FadeOut(old_path),
            FadeOut(collision_text)
        )

        closed_title = Text(
            "Closed-loop execution",
            font_size=29,
            color=GREEN
        ).to_edge(
            UP,
            buff=1.35
        )

        self.play(
            Write(closed_title)
        )

        # Circular pipeline
        observe = RoundedRectangle(
            width=2.3,
            height=0.8,
            color=BLUE,
            fill_opacity=0.08
        ).move_to(
            LEFT * 3.7
        )

        plan = RoundedRectangle(
            width=2.3,
            height=0.8,
            color=PURPLE,
            fill_opacity=0.08
        ).move_to(
            LEFT * 1.2
        )

        execute = RoundedRectangle(
            width=2.3,
            height=0.8,
            color=YELLOW,
            fill_opacity=0.08
        ).move_to(
            RIGHT * 1.3
        )

        feedback = RoundedRectangle(
            width=2.3,
            height=0.8,
            color=ORANGE,
            fill_opacity=0.08
        ).move_to(
            RIGHT * 3.9
        )

        boxes = VGroup(
            observe,
            plan,
            execute,
            feedback
        )

        texts = VGroup(
            Text("Observe", font_size=22, color=BLUE),
            Text("Plan", font_size=22, color=PURPLE),
            Text("Execute", font_size=22, color=YELLOW),
            Text("Visual feedback", font_size=20, color=ORANGE)
        )

        for text, box in zip(texts, boxes):
            text.move_to(box)

        arrows = VGroup(
            Arrow(
                observe.get_right(),
                plan.get_left(),
                buff=0.1
            ),
            Arrow(
                plan.get_right(),
                execute.get_left(),
                buff=0.1
            ),
            Arrow(
                execute.get_right(),
                feedback.get_left(),
                buff=0.1
            ),
            Arrow(
                feedback.get_bottom(),
                observe.get_bottom(),
                buff=0.1
            )
        )

        self.play(
            FadeIn(observe),
            Write(texts[0]),
            run_time=0.6
        )

        self.play(
            GrowArrow(arrows[0]),
            FadeIn(plan),
            Write(texts[1]),
            run_time=0.6
        )

        self.play(
            GrowArrow(arrows[1]),
            FadeIn(execute),
            Write(texts[2]),
            run_time=0.6
        )

        self.play(
            GrowArrow(arrows[2]),
            FadeIn(feedback),
            Write(texts[3]),
            run_time=0.6
        )

        self.play(
            GrowArrow(arrows[3]),
            run_time=0.8
        )

        self.wait(2)

        # ============================================================
        # 5 HZ
        # ============================================================

        frequency = MathTex(
            r"5\ \mathrm{Hz}"
        ).scale(1.2).to_edge(
            DOWN,
            buff=0.8
        )

        frequency_text = Text(
            "replanning frequency reported in the paper",
            font_size=20,
            color=GRAY
        ).next_to(
            frequency,
            DOWN,
            buff=0.15
        )

        self.add(
            frequency,
            frequency_text
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
            DOWN * 2.2
        )

        self.play(
            FadeIn(cache[0]),
            FadeIn(cache[1]),
            run_time=1.5
        )

        self.wait(4)