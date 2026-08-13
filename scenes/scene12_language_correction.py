from manim import *


class VoxPoserScene12(Scene):
    def construct(self):

        BLUE = "#5DADE2"
        GREEN = "#58D68D"
        YELLOW = "#F4D03F"
        RED = "#EC7063"
        PURPLE = "#AF7AC5"
        GRAY = "#BFC9BA"

        # ============================================================
        # TITLE
        # ============================================================

        title = Text(
            "Fine-Grained Language Correction",
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
            "Cover the teapot with the lid",
            font_size=30,
            color=YELLOW
        ).move_to(
            UP * 2
        )

        self.play(
            Write(task)
        )

        self.wait(1.5)

        # ============================================================
        # TEPOT + LID
        # ============================================================

        teapot = Circle(
            radius=1,
            color=PURPLE,
            fill_opacity=0.08
        ).move_to(
            LEFT * 2
        )

        teapot_label = Text(
            "teapot",
            font_size=22,
            color=PURPLE
        ).next_to(
            teapot,
            DOWN,
            buff=0.15
        )

        lid = Circle(
            radius=0.45,
            color=GREEN,
            fill_opacity=0.12
        ).move_to(
            RIGHT * 1.5 + UP * 0.4
        )

        lid_label = Text(
            "lid",
            font_size=22,
            color=GREEN
        ).next_to(
            lid,
            DOWN,
            buff=0.15
        )

        self.play(
            Create(teapot),
            Write(teapot_label),
            FadeIn(lid),
            Write(lid_label),
            run_time=1.5
        )

        # ============================================================
        # FIRST ATTEMPT
        # ============================================================

        path = Arrow(
            lid.get_center(),
            teapot.get_center(),
            color=YELLOW,
            stroke_width=5
        )

        self.play(
            GrowArrow(path),
            run_time=1.3
        )

        wrong_position = Dot(
            teapot.get_center() + RIGHT * 0.18,
            color=RED,
            radius=0.08
        )

        self.play(
            FadeIn(wrong_position)
        )

        self.wait(2)

        # ============================================================
        # USER CORRECTION
        # ============================================================

        correction_box = RoundedRectangle(
            width=7,
            height=1.1,
            color=RED,
            fill_opacity=0.08
        ).to_edge(
            DOWN,
            buff=0.8
        )

        correction = Text(
            '"You\'re off by 1cm."',
            font_size=32,
            color=RED
        ).move_to(
            correction_box
        )

        self.play(
            Create(correction_box),
            Write(correction),
            run_time=1.5
        )

        self.wait(2)

        # ============================================================
        # REPLAN
        # ============================================================

        self.play(
            FadeOut(path),
            FadeOut(wrong_position)
        )

        new_path = Arrow(
            lid.get_center(),
            teapot.get_center() + LEFT * 0.05,
            color=GREEN,
            stroke_width=5
        )

        correction_arrow = Arrow(
            teapot.get_center() + RIGHT * 0.18,
            teapot.get_center() + LEFT * 0.05,
            color=GREEN,
            stroke_width=4
        )

        self.play(
            GrowArrow(new_path),
            GrowArrow(correction_arrow),
            run_time=1.5
        )

        self.wait(2)

        improved = Text(
            "Small language correction → small trajectory correction",
            font_size=27,
            color=GREEN
        ).to_edge(
            UP,
            buff=1.35
        )

        self.play(
            FadeOut(task),
            Write(improved),
            run_time=1.4
        )

        self.wait(3)

        # ============================================================
        # FINAL
        # ============================================================

        final = Text(
            "The language interface can remain expressive and precise.",
            font_size=27,
            color=BLUE
        ).to_edge(
            DOWN,
            buff=0.65
        )

        self.play(
            FadeOut(correction_box),
            FadeOut(correction),
            Write(final),
            run_time=1.4
        )

        self.wait(4)
        