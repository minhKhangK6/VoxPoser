from manim import *


class VoxPoserScene18(Scene):
    def construct(self):

        BLUE = "#5DADE2"
        GREEN = "#58D68D"
        YELLOW = "#F4D03F"
        PURPLE = "#AF7AC5"
        ORANGE = "#F5B041"
        GRAY = "#BFC9CA"
        WHITE_C = "#FFFFFF"

        # ============================================================
        # TITLE
        # ============================================================

        title = Text(
            "Simulation and Real-World Evaluation",
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
        # SIMULATION
        # ============================================================

        sim = RoundedRectangle(
            width=5.0,
            height=4.0,
            corner_radius=0.18,
            color=PURPLE,
            fill_opacity=0.08,
            stroke_width=2
        ).move_to(
            LEFT * 3.0
        )

        sim_title = Text(
            "Simulation",
            font_size=30,
            color=PURPLE
        ).move_to(
            sim.get_top() + DOWN * 0.5
        )

        sim_points = VGroup(
            Text(
                "many tasks",
                font_size=24
            ),
            Text(
                "seen instructions",
                font_size=24
            ),
            Text(
                "unseen instructions",
                font_size=24
            ),
            Text(
                "seen / unseen attributes",
                font_size=24
            ),
            Text(
                "repeatable evaluation",
                font_size=24
            )
        ).arrange(
            DOWN,
            buff=0.22
        ).move_to(
            sim.get_center() + DOWN * 0.15
        )

        self.play(
            FadeIn(sim),
            Write(sim_title),
            FadeIn(sim_points),
            run_time=1.5
        )

        self.wait(2)

        # ============================================================
        # REAL WORLD
        # ============================================================

        real = RoundedRectangle(
            width=5.0,
            height=4.0,
            corner_radius=0.18,
            color=GREEN,
            fill_opacity=0.08,
            stroke_width=2
        ).move_to(
            RIGHT * 3.0
        )

        real_title = Text(
            "Real robot",
            font_size=30,
            color=GREEN
        ).move_to(
            real.get_top() + DOWN * 0.5
        )

        real_points = VGroup(
            Text(
                "actual RGB-D input",
                font_size=24
            ),
            Text(
                "real manipulation",
                font_size=24
            ),
            Text(
                "moving obstacles",
                font_size=24
            ),
            Text(
                "contact interactions",
                font_size=24
            ),
            Text(
                "online replanning",
                font_size=24
            )
        ).arrange(
            DOWN,
            buff=0.22
        ).move_to(
            real.get_center() + DOWN * 0.15
        )

        self.play(
            FadeIn(real),
            Write(real_title),
            FadeIn(real_points),
            run_time=1.5
        )

        self.wait(2.5)

        # ============================================================
        # BRIDGE
        # ============================================================

        # Keep the arrow completely inside the gap between the panels.
        bridge = Arrow(
            sim.get_right() + RIGHT * 0.18,
            real.get_left() + LEFT * 0.18,
            color=YELLOW,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.16,
            buff=0.05
        )

        # Put the label above the arrow with generous spacing.
        bridge_text = Text(
            "same core idea",
            font_size=21,
            color=YELLOW
        ).move_to(
            bridge.get_center() + UP * 0.48
        )

        self.play(
            GrowArrow(bridge),
            FadeIn(bridge_text, shift=UP),
            run_time=1
        )

        self.wait(2)

        # ============================================================
        # FINAL
        # ============================================================

        self.play(
            FadeOut(sim),
            FadeOut(real),
            FadeOut(sim_title),
            FadeOut(real_title),
            FadeOut(sim_points),
            FadeOut(real_points),
            FadeOut(bridge),
            FadeOut(bridge_text),
            run_time=0.8
        )

        final = VGroup(
            Text(
                "Simulation tests generalization.",
                font_size=29,
                color=PURPLE
            ),
            Text(
                "The real robot tests physical execution.",
                font_size=29,
                color=GREEN
            )
        ).arrange(
            DOWN,
            buff=0.35
        )

        self.play(
            FadeIn(final),
            run_time=1.3
        )

        self.wait(3)

        # ============================================================
        # OUTRO
        # ============================================================

        outro = Text(
            "Together, they make the evaluation more convincing.",
            font_size=26,
            color=BLUE
        ).to_edge(
            DOWN,
            buff=0.7
        )

        self.play(
            Write(outro),
            run_time=1.2
        )

        self.wait(4)