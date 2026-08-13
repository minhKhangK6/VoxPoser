from manim import *


class VoxPoserScene17(Scene):
    def construct(self):

        BLUE = "#5DADE2"
        GREEN = "#58D68D"
        RED = "#EC7063"
        YELLOW = "#F4D03F"
        ORANGE = "#F5B041"
        PURPLE = "#AF7AC5"
        GRAY = "#BFC9CA"

        # ============================================================
        # TITLE
        # ============================================================

        title = Text(
            "What Did the Experiments Show?",
            font_size=38,
            color=BLUE
        ).to_edge(UP, buff=0.45)

        self.play(Write(title))
        self.wait(1)

        # ============================================================
        # REAL WORLD RESULT
        # ============================================================

        real_title = Text(
            "Real-world manipulation",
            font_size=30,
            color=GREEN
        ).move_to(UP * 2.0)

        self.play(Write(real_title))

        # Bars: static
        static_label = Text(
            "VoxPoser — static",
            font_size=22
        )

        static_bar = Rectangle(
            width=7.0,
            height=0.55,
            color=GREEN,
            fill_opacity=0.7,
            stroke_width=0
        )

        static_value = Text(
            "88%",
            font_size=24,
            color=GREEN
        ).next_to(
            static_bar,
            RIGHT,
            buff=0.2
        )

        static_group = VGroup(
            static_label,
            static_bar
        ).arrange(
            RIGHT,
            buff=0.25
        ).move_to(
            UP * 0.9
        )

        self.play(
            FadeIn(static_group),
            Write(static_value),
            run_time=1.2
        )

        self.wait(1.5)

        # Bars: disturbances
        dist_label = Text(
            "VoxPoser — disturbances",
            font_size=22
        )

        dist_bar = Rectangle(
            width=5.6,
            height=0.55,
            color=ORANGE,
            fill_opacity=0.7,
            stroke_width=0
        )

        dist_value = Text(
            "70%",
            font_size=24,
            color=ORANGE
        ).next_to(
            dist_bar,
            RIGHT,
            buff=0.2
        )

        dist_group = VGroup(
            dist_label,
            dist_bar
        ).arrange(
            RIGHT,
            buff=0.25
        ).move_to(
            DOWN * 0.05
        )

        self.play(
            FadeIn(dist_group),
            Write(dist_value),
            run_time=1.2
        )

        self.wait(2)

        # ============================================================
        # BASELINE
        # ============================================================

        baseline = Text(
            "Baseline with action primitives",
            font_size=24,
            color=RED
        ).move_to(
            DOWN * 1.15
        )

        baseline_text = Text(
            "24% static  →  0% under disturbances",
            font_size=25,
            color=RED
        ).next_to(
            baseline,
            DOWN,
            buff=0.2
        )

        self.play(
            Write(baseline),
            Write(baseline_text),
            run_time=1.2
        )

        self.wait(2)

        # ============================================================
        # INTERPRETATION
        # ============================================================

        self.play(
            FadeOut(static_group),
            FadeOut(static_value),
            FadeOut(dist_group),
            FadeOut(dist_value),
            FadeOut(real_title),
            FadeOut(baseline),
            FadeOut(baseline_text)
        )

        interpretation = VGroup(
            Text(
                "The important result is not just success.",
                font_size=29,
                color=WHITE
            ),
            Text(
                "It is robustness when the world changes.",
                font_size=32,
                color=GREEN
            )
        ).arrange(
            DOWN,
            buff=0.25
        )

        self.play(
            FadeIn(interpretation),
            run_time=1.5
        )

        self.wait(3)

        # ============================================================
        # FINAL
        # ============================================================

        final = Text(
            "Closed-loop planning makes the system more flexible.",
            font_size=27,
            color=BLUE
        ).to_edge(DOWN, buff=0.7)

        self.play(
            Write(final),
            run_time=1.2
        )

        self.wait(4)