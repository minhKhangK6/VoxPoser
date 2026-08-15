from manim import *


class VoxPoserScene17(Scene):
    def construct(self):

        # ============================================================
        # COLORS
        # ============================================================

        BLUE = "#5DADE2"
        GREEN = "#58D68D"
        RED = "#EC7063"
        ORANGE = "#F5B041"
        GRAY = "#BFC9CA"
        WHITE_C = "#FFFFFF"

        # ============================================================
        # HELPER — RESULT BAR
        # ============================================================

        def make_result_bar(
            label_text,
            percentage,
            color,
            y_position
        ):

            label = Text(
                label_text,
                font_size=22,
                color=WHITE_C
            )

            # Background bar
            bg = Rectangle(
                width=6.8,
                height=0.48,
                color=GRAY,
                fill_opacity=0.08,
                stroke_width=1.5
            )

            # Percentage of the background width
            fill_width = 6.8 * percentage

            fill = Rectangle(
                width=fill_width,
                height=0.48,
                color=color,
                fill_color=color,
                fill_opacity=0.65,
                stroke_width=0
            )

            # Put both bars at the exact same vertical position.
            bg.move_to(
                RIGHT * 0.55 + UP * y_position
            )

            fill.move_to(
                bg.get_center()
                + LEFT * (bg.width - fill.width) / 2
            )

            value = Text(
                f"{int(percentage * 100)}%",
                font_size=24,
                color=color
            ).next_to(
                bg,
                RIGHT,
                buff=0.22
            )

            label.move_to(
                bg.get_left()
                + LEFT * 2.05
            )

            return VGroup(
                label,
                bg,
                fill,
                value
            )

        # ============================================================
        # TITLE
        # ============================================================

        title = Text(
            "What Did the Experiments Show?",
            font_size=38,
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
        # SECTION TITLE
        # ============================================================

        real_title = Text(
            "Real-world manipulation",
            font_size=30,
            color=GREEN
        ).to_edge(
            UP,
            buff=1.35
        )

        self.play(
            Write(real_title)
        )

        self.wait(1)

        # ============================================================
        # STATIC RESULT — 88%
        # ============================================================

        static_result = make_result_bar(
            "VoxPoser — static",
            0.88,
            GREEN,
            0.45
        )

        self.play(
            FadeIn(static_result[0]),
            FadeIn(static_result[1]),
            GrowFromEdge(
                static_result[2],
                LEFT
            ),
            Write(static_result[3]),
            run_time=1.3
        )

        self.wait(1.5)

        # ============================================================
        # DISTURBANCES — 70%
        # ============================================================

        disturbance_result = make_result_bar(
            "VoxPoser — disturbances",
            0.70,
            ORANGE,
            -0.95
        )

        self.play(
            FadeIn(disturbance_result[0]),
            FadeIn(disturbance_result[1]),
            GrowFromEdge(
                disturbance_result[2],
                LEFT
            ),
            Write(disturbance_result[3]),
            run_time=1.3
        )

        self.wait(2)

        # ============================================================
        # BASELINE
        # ============================================================

        baseline_box = RoundedRectangle(
            width=9.0,
            height=1.35,
            corner_radius=0.15,
            color=RED,
            fill_opacity=0.05,
            stroke_width=1.8
        ).move_to(
            DOWN * 2.45
        )

        baseline_title = Text(
            "Baseline with action primitives",
            font_size=24,
            color=RED
        ).move_to(
            baseline_box.get_center() + UP * 0.28
        )

        baseline_value = Text(
            "24% static  →  0% under disturbances",
            font_size=25,
            color=RED
        ).move_to(
            baseline_box.get_center() + DOWN * 0.28
        )

        self.play(
            FadeIn(baseline_box),
            Write(baseline_title),
            Write(baseline_value),
            run_time=1.2
        )

        self.wait(2)

        # ============================================================
        # INTERPRETATION
        # ============================================================

        self.play(
            FadeOut(static_result),
            FadeOut(disturbance_result),
            FadeOut(real_title),
            FadeOut(baseline_box),
            FadeOut(baseline_title),
            FadeOut(baseline_value),
            run_time=0.8
        )

        interpretation = VGroup(
            Text(
                "The important result is not just success.",
                font_size=29,
                color=WHITE_C
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
            FadeIn(
                interpretation,
                shift=UP
            ),
            run_time=1.5
        )

        self.wait(3)

        # ============================================================
        # FINAL
        # ============================================================

        self.play(
            FadeOut(interpretation)
        )

        final = Text(
            "Closed-loop planning makes the system more flexible.",
            font_size=27,
            color=BLUE
        )

        self.play(
            Write(final),
            run_time=1.2
        )

        self.wait(4)