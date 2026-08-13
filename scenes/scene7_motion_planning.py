from manim import *


class VoxPoserScene7(ThreeDScene):
    def construct(self):

        BLUE = "#5DADE2"
        GREEN = "#58D68D"
        RED = "#EC7063"
        YELLOW = "#F4D03F"
        ORANGE = "#F5B041"
        PURPLE = "#AF7AC5"
        GRAY = "#BFC9CA"

        # ============================================================
        # CAMERA
        # ============================================================

        self.set_camera_orientation(
            phi=68 * DEGREES,
            theta=42 * DEGREES
        )

        # ============================================================
        # TITLE
        # ============================================================

        title = Text(
            "From Value Maps to a Robot Trajectory",
            font_size=34,
            color=BLUE
        ).to_corner(UL)

        self.add_fixed_in_frame_mobjects(title)

        self.play(
            Write(title)
        )

        self.wait(1)

        # ============================================================
        # AXES
        # ============================================================

        axes = ThreeDAxes(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            z_range=[0, 2, 1],
            x_length=5,
            y_length=5,
            z_length=2.5
        )

        self.play(
            Create(axes),
            run_time=1.5
        )

        # ============================================================
        # OBSTACLE + TARGET
        # ============================================================

        obstacle = Sphere(
            center=axes.c2p(0, 0, 0.55),
            radius=0.48,
            color=RED
        )

        target = Sphere(
            center=axes.c2p(1.45, 1.35, 0.55),
            radius=0.28,
            color=GREEN
        )

        start = Sphere(
            center=axes.c2p(-1.45, -1.35, 0.4),
            radius=0.18,
            color=YELLOW
        )

        self.play(
            FadeIn(obstacle),
            FadeIn(target),
            FadeIn(start),
            run_time=1.3
        )

        # ============================================================
        # LEGEND
        # ============================================================

        legend = VGroup(
            Text("start", font_size=20, color=YELLOW),
            Text("obstacle", font_size=20, color=RED),
            Text("goal", font_size=20, color=GREEN)
        ).arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.12
        ).to_corner(UR)

        self.add_fixed_in_frame_mobjects(legend)

        self.play(
            FadeIn(legend)
        )

        self.wait(1.5)

        # ============================================================
        # CANDIDATE 1 — COLLISION
        # ============================================================

        p1 = axes.c2p(-1.45, -1.35, 0.4)
        p2 = axes.c2p(-0.6, -0.5, 0.5)
        p3 = axes.c2p(0.45, 0.45, 0.55)
        p4 = axes.c2p(1.45, 1.35, 0.55)

        bad_path = VMobject(
            color=RED,
            stroke_width=5
        )

        bad_path.set_points_smoothly(
            [p1, p2, p3, p4]
        )

        bad_label = Text(
            "Candidate A: collision",
            font_size=24,
            color=RED
        ).to_edge(
            DOWN,
            buff=0.6
        )

        self.add_fixed_in_frame_mobjects(
            bad_label
        )

        self.play(
            Create(bad_path),
            Write(bad_label),
            run_time=2
        )

        self.wait(2)

        # ============================================================
        # CLEAR BAD PATH
        # ============================================================

        self.play(
            FadeOut(bad_path),
            FadeOut(bad_label)
        )

        # ============================================================
        # CANDIDATE 2 — SAFE BUT TOO LONG
        # ============================================================

        q1 = axes.c2p(-1.45, -1.35, 0.4)
        q2 = axes.c2p(-1.8, 1.5, 1.3)
        q3 = axes.c2p(0.0, 1.8, 1.2)
        q4 = axes.c2p(1.45, 1.35, 0.55)

        long_path = VMobject(
            color=ORANGE,
            stroke_width=5
        )

        long_path.set_points_smoothly(
            [q1, q2, q3, q4]
        )

        long_label = Text(
            "Candidate B: safe, but expensive",
            font_size=24,
            color=ORANGE
        ).to_edge(
            DOWN,
            buff=0.6
        )

        self.add_fixed_in_frame_mobjects(
            long_label
        )

        self.play(
            Create(long_path),
            Write(long_label),
            run_time=2
        )

        self.wait(2)

        self.play(
            FadeOut(long_path),
            FadeOut(long_label)
        )

        # ============================================================
        # CANDIDATE 3 — GOOD PATH
        # ============================================================

        r1 = axes.c2p(-1.45, -1.35, 0.4)
        r2 = axes.c2p(-1.25, -0.1, 1.0)
        r3 = axes.c2p(-0.4, 1.0, 1.0)
        r4 = axes.c2p(0.7, 1.45, 0.75)
        r5 = axes.c2p(1.45, 1.35, 0.55)

        good_path = VMobject(
            color=GREEN,
            stroke_width=6
        )

        good_path.set_points_smoothly(
            [r1, r2, r3, r4, r5]
        )

        good_label = Text(
            "Candidate C: low-cost collision-free path",
            font_size=24,
            color=GREEN
        ).to_edge(
            DOWN,
            buff=0.6
        )

        self.add_fixed_in_frame_mobjects(
            good_label
        )

        self.play(
            Create(good_path),
            Write(good_label),
            run_time=2
        )

        self.wait(2)

        # ============================================================
        # PAPER CONNECTION
        # ============================================================

        self.play(
            FadeOut(good_label)
        )

        cost_formula = MathTex(
            r"C(\mathbf{x})"
            r"\;=\;"
            r"-\left("
            r"2\,A(\mathbf{x})"
            r"+"
            r"1\,C_{\mathrm{avoid}}(\mathbf{x})"
            r"\right)",
            font_size=30
        ).to_edge(
            DOWN,
            buff=0.55
        )

        formula_note = Text(
            "illustrating the weighting used by the planner",
            font_size=19,
            color=GRAY
        ).next_to(
            cost_formula,
            UP,
            buff=0.12
        )

        self.add_fixed_in_frame_mobjects(
            cost_formula,
            formula_note
        )

        self.play(
            Write(formula_note),
            Write(cost_formula),
            run_time=1.6
        )

        self.wait(4)

        # ============================================================
        # END-EFFECTOR
        # ============================================================

        end_effector = Dot3D(
            point=r1,
            radius=0.13,
            color=YELLOW
        )

        self.play(
            FadeIn(end_effector),
            FadeOut(cost_formula),
            FadeOut(formula_note)
        )

        self.play(
            MoveAlongPath(
                end_effector,
                good_path
            ),
            run_time=5,
            rate_func=linear
        )

        self.wait(2)

        # ============================================================
        # SUMMARY
        # ============================================================

        summary = Text(
            "The value maps become an objective for motion planning.",
            font_size=27,
            color=BLUE
        ).to_edge(
            DOWN,
            buff=0.6
        )

        self.add_fixed_in_frame_mobjects(
            summary
        )

        self.play(
            Write(summary),
            run_time=1.3
        )

        self.wait(3)