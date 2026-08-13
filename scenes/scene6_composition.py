from manim import *


class VoxPoserScene6(ThreeDScene):
    def construct(self):

        BLUE = "#5DADE2"
        GREEN = "#58D68D"
        RED = "#EC7063"
        YELLOW = "#F4D03F"
        PURPLE = "#AF7AC5"
        GRAY = "#BFC9CA"
        WHITE = "#FFFFFF"

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
            "Composing Value Maps",
            font_size=36,
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
            x_length=4.8,
            y_length=4.8,
            z_length=2.5
        )

        self.play(
            Create(axes),
            run_time=1.5
        )

        # ============================================================
        # AFFORDANCE REGION
        # ============================================================

        affordance_voxels = VGroup()

        for x in np.linspace(-0.2, 1.4, 5):
            for y in np.linspace(0.3, 1.4, 4):
                z = 0.5

                cube = Cube(
                    side_length=0.24,
                    fill_color=GREEN,
                    fill_opacity=0.35,
                    stroke_width=0.5
                )

                cube.move_to(
                    axes.c2p(x, y, z)
                )

                affordance_voxels.add(cube)

        self.play(
            LaggedStart(
                *[
                    FadeIn(v)
                    for v in affordance_voxels
                ],
                lag_ratio=0.05
            ),
            run_time=2
        )

        target = Sphere(
            center=axes.c2p(1.1, 1.0, 0.5),
            radius=0.3,
            color=GREEN
        )

        self.play(
            FadeIn(target)
        )

        affordance_label = Text(
            "Affordance map\n"
            "good places to act",
            font_size=21,
            color=GREEN
        ).to_edge(
            RIGHT,
            buff=0.4
        ).shift(
            UP * 1.4
        )

        self.add_fixed_in_frame_mobjects(
            affordance_label
        )

        self.play(
            Write(affordance_label)
        )

        self.wait(3)

        # ============================================================
        # CLEAR AFFORDANCE
        # ============================================================

        self.play(
            FadeOut(affordance_voxels),
            FadeOut(target),
            FadeOut(affordance_label)
        )

        # ============================================================
        # AVOIDANCE REGION
        # ============================================================

        avoidance_voxels = VGroup()

        for x in np.linspace(-1.4, -0.2, 5):
            for y in np.linspace(-1.4, -0.2, 4):
                z = 0.5

                cube = Cube(
                    side_length=0.24,
                    fill_color=RED,
                    fill_opacity=0.35,
                    stroke_width=0.5
                )

                cube.move_to(
                    axes.c2p(x, y, z)
                )

                avoidance_voxels.add(cube)

        obstacle = Sphere(
            center=axes.c2p(-0.8, -0.7, 0.5),
            radius=0.4,
            color=RED
        )

        self.play(
            LaggedStart(
                *[
                    FadeIn(v)
                    for v in avoidance_voxels
                ],
                lag_ratio=0.05
            ),
            FadeIn(obstacle),
            run_time=2
        )

        avoidance_label = Text(
            "Avoidance map\n"
            "bad places to enter",
            font_size=21,
            color=RED
        ).to_edge(
            RIGHT,
            buff=0.4
        ).shift(
            UP * 1.4
        )

        self.add_fixed_in_frame_mobjects(
            avoidance_label
        )

        self.play(
            Write(avoidance_label)
        )

        self.wait(3)

        # ============================================================
        # COMBINE BOTH
        # ============================================================

        self.play(
            FadeOut(avoidance_voxels),
            FadeOut(obstacle),
            FadeOut(avoidance_label)
        )

        # Recreate affordance
        affordance_voxels = VGroup()

        for x in np.linspace(-0.2, 1.4, 5):
            for y in np.linspace(0.3, 1.4, 4):
                z = 0.5

                cube = Cube(
                    side_length=0.24,
                    fill_color=GREEN,
                    fill_opacity=0.28,
                    stroke_width=0.4
                )

                cube.move_to(
                    axes.c2p(x, y, z)
                )

                affordance_voxels.add(cube)

        avoidance_voxels = VGroup()

        for x in np.linspace(-1.4, -0.2, 5):
            for y in np.linspace(-1.4, -0.2, 4):
                z = 0.5

                cube = Cube(
                    side_length=0.24,
                    fill_color=RED,
                    fill_opacity=0.28,
                    stroke_width=0.4
                )

                cube.move_to(
                    axes.c2p(x, y, z)
                )

                avoidance_voxels.add(cube)

        self.play(
            LaggedStart(
                *[
                    FadeIn(v)
                    for v in affordance_voxels
                ],
                lag_ratio=0.02
            ),
            LaggedStart(
                *[
                    FadeIn(v)
                    for v in avoidance_voxels
                ],
                lag_ratio=0.02
            ),
            run_time=2.5
        )

        target = Sphere(
            center=axes.c2p(1.1, 1.0, 0.5),
            radius=0.3,
            color=GREEN
        )

        obstacle = Sphere(
            center=axes.c2p(-0.8, -0.7, 0.5),
            radius=0.4,
            color=RED
        )

        self.play(
            FadeIn(target),
            FadeIn(obstacle)
        )

        # ============================================================
        # INTUITION FORMULA
        # ============================================================

        formula = MathTex(
            r"J(\mathbf{x})"
            r"\;=\;"
            r"w_a A(\mathbf{x})"
            r"\;+\;"
            r"w_c C(\mathbf{x})",
            font_size=32
        ).to_edge(
            DOWN,
            buff=0.5
        )

        formula_label = Text(
            "A simple way to visualize the combined objective",
            font_size=20,
            color=GRAY
        ).next_to(
            formula,
            UP,
            buff=0.15
        )

        self.add_fixed_in_frame_mobjects(
            formula,
            formula_label
        )

        self.play(
            Write(formula_label),
            Write(formula),
            run_time=1.8
        )

        self.wait(4)

        # ============================================================
        # CHOOSE PATH
        # ============================================================

        self.play(
            FadeOut(formula),
            FadeOut(formula_label)
        )

        start = axes.c2p(-1.5, -1.5, 0.4)
        p1 = axes.c2p(-1.0, 0.0, 1.0)
        p2 = axes.c2p(0.0, 1.0, 0.9)
        p3 = axes.c2p(0.8, 1.2, 0.7)
        goal = axes.c2p(1.1, 1.0, 0.5)

        path = VMobject(
            color=YELLOW,
            stroke_width=5
        )

        path.set_points_smoothly(
            [
                start,
                p1,
                p2,
                p3,
                goal
            ]
        )

        self.play(
            Create(path),
            run_time=2.5
        )

        dot = Dot3D(
            point=start,
            radius=0.12,
            color=YELLOW
        )

        self.play(
            FadeIn(dot)
        )

        self.play(
            MoveAlongPath(
                dot,
                path
            ),
            run_time=4,
            rate_func=linear
        )

        self.wait(2)

        # ============================================================
        # SUMMARY
        # ============================================================

        summary = Text(
            "The maps turn language into an objective for planning.",
            font_size=27,
            color=GREEN
        ).to_edge(
            DOWN,
            buff=0.55
        )

        self.add_fixed_in_frame_mobjects(
            summary
        )

        self.play(
            Write(summary),
            run_time=1.2
        )

        self.wait(4)

        self.begin_ambient_camera_rotation(
            rate=0.15
        )

        self.wait(3)

        self.stop_ambient_camera_rotation()