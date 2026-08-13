from manim import *


class VoxPoserScene18(Scene):
    def construct(self):

        BLUE = "#5DADE2"
        GREEN = "#58D68D"
        YELLOW = "#F4D03F"
        PURPLE = "#AF7AC5"
        ORANGE = "#F5B041"
        GRAY = "#BFC9CA"

        # ============================================================
        # TITLE
        # ============================================================

        title = Text(
            "Simulation and Real-World Evaluation",
            font_size=36,
            color=BLUE
        ).to_edge(UP, buff=0.45)

        self.play(Write(title))
        self.wait(1)

        # ============================================================
        # SIMULATION
        # ============================================================

        sim = RoundedRectangle(
            width=5.0,
            height=4.0,
            color=PURPLE,
            fill_opacity=0.08
        ).move_to(LEFT * 3)

        sim_title = Text(
            "Simulation",
            font_size=30,
            color=PURPLE
        ).move_to(
            sim.get_top() + DOWN * 0.5
        )

        sim_points = VGroup(
            Text("many tasks", font_size=24),
            Text("seen instructions", font_size=24),
            Text("unseen instructions", font_size=24),
            Text("seen / unseen attributes", font_size=24),
            Text("repeatable evaluation", font_size=24)
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
            color=GREEN,
            fill_opacity=0.08
        ).move_to(RIGHT * 3)

        real_title = Text(
            "Real robot",
            font_size=30,
            color=GREEN
        ).move_to(
            real.get_top() + DOWN * 0.5
        )

        real_points = VGroup(
            Text("actual RGB-D input", font_size=24),
            Text("real manipulation", font_size=24),
            Text("moving obstacles", font_size=24),
            Text("contact interactions", font_size=24),
            Text("online replanning", font_size=24)
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

        bridge = Arrow(
            sim.get_right(),
            real.get_left(),
            color=YELLOW,
            stroke_width=5
        )

        bridge_text = Text(
            "same core idea",
            font_size=22,
            color=YELLOW
        ).next_to(
            bridge,
            UP,
            buff=0.15
        )

        self.play(
            GrowArrow(bridge),
            Write(bridge_text),
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
            FadeOut(bridge_text)
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

        outro = Text(
            "Together, they make the evaluation more convincing.",
            font_size=26,
            color=BLUE
        ).to_edge(DOWN, buff=0.7)

        self.play(
            Write(outro),
            run_time=1.2
        )

        self.wait(4)