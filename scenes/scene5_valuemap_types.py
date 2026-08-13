from manim import *


class VoxPoserScene5(ThreeDScene):
    def construct(self):

        BLUE_C = "#5DADE2"
        YELLOW_C = "#F4D03F"
        GREEN_C = "#58D68D"
        ORANGE_C = "#F5B041"
        PURPLE_C = "#AF7AC5"
        RED_C = "#EC7063"
        GRAY_C = "#BFC9CA"

        # ============================================================
        # CAMERA
        # ============================================================

        self.set_camera_orientation(
            phi=65 * DEGREES,
            theta=40 * DEGREES
        )

        # ============================================================
        # TITLE
        # ============================================================

        title = Text(
            "What Is a 3D Value Map?",
            font_size=34,
            color=BLUE_C
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
            x_length=4.5,
            y_length=4.5,
            z_length=2.5
        )

        self.play(
            Create(axes),
            run_time=1.5
        )

        # ============================================================
        # VOXEL GRID
        # ============================================================

        voxels = VGroup()

        for x in np.linspace(-1.2, 1.2, 5):
            for y in np.linspace(-1.2, 1.2, 5):
                for z in np.linspace(0.2, 1.2, 3):

                    if (x > 0.5 and y > 0.5):
                        col = GREEN_C
                        opacity = 0.35
                    elif (x < -0.4 and y < -0.4):
                        col = RED_C
                        opacity = 0.35
                    else:
                        col = BLUE_C
                        opacity = 0.08

                    cube = Cube(
                        side_length=0.22,
                        fill_color=col,
                        fill_opacity=opacity,
                        stroke_width=0.4
                    )

                    cube.move_to(
                        axes.c2p(x, y, z)
                    )

                    voxels.add(cube)

        self.play(
            LaggedStart(
                *[
                    FadeIn(v)
                    for v in voxels
                ],
                lag_ratio=0.01
            ),
            run_time=3
        )

        self.wait(1)

        # ============================================================
        # TARGET
        # ============================================================

        target = Sphere(
            center=axes.c2p(1, 1, 0.6),
            radius=0.3,
            color=GREEN_C
        )

        target_label = Text(
            "high-value region",
            font_size=22,
            color=GREEN_C
        ).to_corner(UR)

        self.add_fixed_in_frame_mobjects(target_label)

        self.play(
            FadeIn(target),
            Write(target_label),
            run_time=1.2
        )

        self.wait(2)

        # ============================================================
        # OBSTACLE
        # ============================================================

        obstacle = Sphere(
            center=axes.c2p(-1, -1, 0.6),
            radius=0.35,
            color=RED_C
        )

        obstacle_label = Text(
            "high-cost region",
            font_size=22,
            color=RED_C
        ).next_to(
            target_label,
            DOWN,
            buff=0.2
        )

        self.add_fixed_in_frame_mobjects(
            obstacle_label
        )

        self.play(
            FadeIn(obstacle),
            Write(obstacle_label),
            run_time=1.2
        )

        self.wait(2)

        # ============================================================
        # MATHEMATICAL IDEA
        # ============================================================

        formula = MathTex(
            r"V(\mathbf{x})",
            font_size=38,
            color=YELLOW_C
        ).to_corner(DR)

        formula_text = Text(
            "assigns a value to each location",
            font_size=21,
            color=WHITE
        ).next_to(
            formula,
            UP,
            buff=0.15
        )

        self.add_fixed_in_frame_mobjects(
            formula,
            formula_text
        )

        self.play(
            Write(formula),
            Write(formula_text),
            run_time=1
        )

        self.wait(3)

        # ============================================================
        # ROTATE CAMERA
        # ============================================================

        self.begin_ambient_camera_rotation(
            rate=0.18
        )

        self.wait(4)

        self.stop_ambient_camera_rotation()

        # ============================================================
        # MAP TYPES
        # ============================================================

        self.play(
            FadeOut(voxels),
            FadeOut(target),
            FadeOut(obstacle),
            FadeOut(formula),
            FadeOut(formula_text),
            FadeOut(target_label),
            FadeOut(obstacle_label)
        )

        map_title = Text(
            "VoxPoser uses several types of value maps",
            font_size=30,
            color=BLUE_C
        ).to_edge(
            DOWN,
            buff=0.5
        )

        self.add_fixed_in_frame_mobjects(
            map_title
        )

        # The five value map types
        labels = VGroup(
            Text("Affordance", font_size=22, color=GREEN_C),
            Text("Avoidance", font_size=22, color=RED_C),
            Text("Velocity", font_size=22, color=ORANGE_C),
            Text("Rotation", font_size=22, color=PURPLE_C),
            Text("Gripper", font_size=22, color=YELLOW_C)
        ).arrange(
            RIGHT,
            buff=0.35
        )

        # 3D scene reset
        map_axes = ThreeDAxes(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            z_range=[0, 2, 1],
            x_length=4.5,
            y_length=4.5,
            z_length=2.5
        )

        self.add(map_axes)

        self.play(
            Write(map_title),
            FadeIn(labels),
            run_time=1.5
        )

        self.wait(4)

        # ============================================================
        # FINAL MESSAGE
        # ============================================================

        final = Text(
            "Each map describes one aspect of the desired manipulation.",
            font_size=26,
            color=GREEN_C
        ).to_edge(
            DOWN,
            buff=1.15
        )

        self.play(
            FadeIn(final),
            run_time=1
        )

        self.wait(4)