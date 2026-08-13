from manim import *


class VoxPoserScene13(Scene):
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
            "Multi-Step Visual Programs",
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
            '"Open the drawer precisely by half."',
            font_size=32,
            color=YELLOW
        )

        self.play(
            Write(task)
        )

        self.wait(2)

        # ============================================================
        # PROBLEM
        # ============================================================

        problem = Text(
            "But the robot does not know the drawer's exact displacement model.",
            font_size=24,
            color=RED
        ).next_to(
            task,
            DOWN,
            buff=0.5
        )

        self.play(
            Write(problem),
            run_time=1.3
        )

        self.wait(2)

        self.play(
            FadeOut(task),
            FadeOut(problem)
        )

        # ============================================================
        # DRAWER
        # ============================================================

        cabinet = Rectangle(
            width=6,
            height=3,
            color=GRAY,
            fill_opacity=0.05
        ).move_to(
            LEFT * 1
        )

        drawer = Rectangle(
            width=4,
            height=1,
            color=PURPLE,
            fill_opacity=0.15
        ).move_to(
            LEFT * 1
        )

        handle = Circle(
            radius=0.15,
            color=YELLOW,
            fill_opacity=1
        ).move_to(
            RIGHT * 0.7
        )

        self.play(
            Create(cabinet),
            Create(drawer),
            FadeIn(handle),
            run_time=1.3
        )

        # ============================================================
        # STEP 1
        # ============================================================

        step1 = Text(
            "Step 1 — Open fully",
            font_size=27,
            color=GREEN
        ).to_edge(
            UP,
            buff=1.5
        )

        arrow1 = Arrow(
            handle.get_center(),
            handle.get_center() + RIGHT * 2,
            color=GREEN,
            stroke_width=5
        )

        self.play(
            Write(step1),
            GrowArrow(arrow1),
            run_time=1.3
        )

        self.wait(2)

        # Move drawer
        self.play(
            drawer.animate.shift(RIGHT * 2),
            handle.animate.shift(RIGHT * 2),
            run_time=2
        )

        displacement = Text(
            "observe handle displacement",
            font_size=23,
            color=BLUE
        ).to_edge(
            DOWN,
            buff=0.7
        )

        self.play(
            Write(displacement)
        )

        self.wait(2)

        # ============================================================
        # STEP 2
        # ============================================================

        self.play(
            FadeOut(step1),
            FadeOut(arrow1),
            FadeOut(displacement)
        )

        step2 = Text(
            "Step 2 — Use visual feedback",
            font_size=27,
            color=ORANGE
        ).to_edge(
            UP,
            buff=1.5
        )

        measurement = MathTex(
            r"\Delta_{\mathrm{full}}"
        ).scale(
            1.3
        ).to_edge(
            DOWN,
            buff=0.7
        )

        self.play(
            Write(step2),
            Write(measurement),
            run_time=1.5
        )

        self.wait(2)

        # ============================================================
        # STEP 3
        # ============================================================

        self.play(
            FadeOut(step2),
            FadeOut(measurement)
        )

        step3 = Text(
            "Step 3 — Return to the midpoint",
            font_size=27,
            color=GREEN
        ).to_edge(
            UP,
            buff=1.5
        )

        midpoint = DashedLine(
            start=LEFT * 0.3 + DOWN * 1,
            end=LEFT * 0.3 + UP * 1,
            color=YELLOW
        )

        midpoint_label = Text(
            "50%",
            font_size=24,
            color=YELLOW
        ).next_to(
            midpoint,
            UP,
            buff=0.15
        )

        self.play(
            Write(step3),
            Create(midpoint),
            Write(midpoint_label),
            run_time=1.5
        )

        self.wait(2)

        self.play(
            drawer.animate.shift(LEFT * 1),
            handle.animate.shift(LEFT * 1),
            run_time=2
        )

        # ============================================================
        # PROGRAM REPRESENTATION
        # ============================================================

        program = VGroup(
            Text("Visual observation", font_size=24, color=BLUE),
            Arrow(LEFT, RIGHT, buff=0.2),
            Text("Measure", font_size=24, color=PURPLE),
            Arrow(LEFT, RIGHT, buff=0.2),
            Text("Act", font_size=24, color=GREEN),
            Arrow(LEFT, RIGHT, buff=0.2),
            Text("Observe again", font_size=24, color=ORANGE)
        ).arrange(
            RIGHT,
            buff=0.2
        ).scale(0.72).to_edge(
            DOWN,
            buff=0.5
        )

        self.play(
            FadeIn(program),
            run_time=1.8
        )

        self.wait(3)

        final = Text(
            "The system can compose several visual actions into one task.",
            font_size=27,
            color=BLUE
        ).to_edge(
            DOWN,
            buff=1.2
        )

        self.play(
            FadeOut(program),
            Write(final),
            run_time=1.3
        )

        self.wait(4)