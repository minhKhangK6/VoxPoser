from manim import *


class VoxPoserScene5(ThreeDScene):
    def construct(self):

        # ============================================================
        # COLORS
        # ============================================================

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
        ).to_corner(
            UL,
            buff=0.35
        )

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

                    if x > 0.5 and y > 0.5:
                        col = GREEN_C
                        opacity = 0.35

                    elif x < -0.4 and y < -0.4:
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
        ).to_corner(
            UR,
            buff=0.4
        )

        self.add_fixed_in_frame_mobjects(
            target_label
        )

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
        ).to_corner(
            DR,
            buff=0.42
        )

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

        # Fade out the original title too.
        # Otherwise it remains fixed in the upper-left corner
        # and overlaps the new MAP TYPES title.
        self.play(
            FadeOut(title),
            FadeOut(axes),
            FadeOut(voxels),
            FadeOut(target),
            FadeOut(obstacle),
            FadeOut(formula),
            FadeOut(formula_text),
            FadeOut(target_label),
            FadeOut(obstacle_label),
            run_time=0.8
        )

        # ------------------------------------------------------------
        # MAP TYPES TITLE
        # ------------------------------------------------------------

        map_title = Text(
            "VoxPoser uses several types of value maps",
            font_size=30,
            color=BLUE_C
        ).to_edge(
            UP,
            buff=0.55
        )

        self.add_fixed_in_frame_mobjects(
            map_title
        )

        # ------------------------------------------------------------
        # ONE CENTRAL 3D MAP
        # ------------------------------------------------------------

        map_axes = ThreeDAxes(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            z_range=[0, 2, 1],
            x_length=3.5,
            y_length=3.5,
            z_length=2.2
        ).shift(
            DOWN * 0.35
        )

        self.play(
            Write(map_title),
            Create(map_axes),
            run_time=1.4
        )

        # ------------------------------------------------------------
        # LEGEND CARD HELPER
        # ------------------------------------------------------------

        def make_card(label, color):
            box = RoundedRectangle(
                width=2.25,
                height=0.68,
                corner_radius=0.12,
                color=color,
                fill_opacity=0.08,
                stroke_width=2
            )

            text = Text(
                label,
                font_size=20,
                color=color
            ).move_to(
                box
            )

            return VGroup(
                box,
                text
            )

        # ------------------------------------------------------------
        # LEGEND CARDS
        # ------------------------------------------------------------

        affordance_card = make_card(
            "Affordance",
            GREEN_C
        )

        avoidance_card = make_card(
            "Avoidance",
            RED_C
        )

        velocity_card = make_card(
            "Velocity",
            ORANGE_C
        )

        rotation_card = make_card(
            "Rotation",
            PURPLE_C
        )

        gripper_card = make_card(
            "Gripper",
            YELLOW_C
        )

        # ------------------------------------------------------------
        # POSITION LEGEND
        # ------------------------------------------------------------

        affordance_card.to_edge(
            LEFT,
            buff=0.45
        ).shift(
            UP * 1.0
        )

        avoidance_card.to_edge(
            LEFT,
            buff=0.45
        ).shift(
            DOWN * 0.05
        )

        velocity_card.to_edge(
            RIGHT,
            buff=0.45
        ).shift(
            UP * 1.0
        )

        rotation_card.to_edge(
            RIGHT,
            buff=0.45
        ).shift(
            DOWN * 0.05
        )

        gripper_card.to_edge(
            DOWN,
            buff=0.75
        )

        legend = VGroup(
            affordance_card,
            avoidance_card,
            velocity_card,
            rotation_card,
            gripper_card
        )

        self.add_fixed_in_frame_mobjects(
            legend
        )

        # ------------------------------------------------------------
        # ANIMATE LEGEND
        # ------------------------------------------------------------

        self.play(
            FadeIn(
                affordance_card,
                shift=RIGHT
            ),
            FadeIn(
                avoidance_card,
                shift=RIGHT
            ),
            FadeIn(
                velocity_card,
                shift=LEFT
            ),
            FadeIn(
                rotation_card,
                shift=LEFT
            ),
            run_time=1.4
        )

        self.play(
            FadeIn(
                gripper_card,
                shift=UP
            ),
            run_time=0.8
        )

        self.wait(3)

        # ============================================================
        # FINAL MESSAGE
        # ============================================================

        final = Text(
            "Each map describes one aspect of the desired manipulation.",
            font_size=25,
            color=GREEN_C
        ).to_edge(
            DOWN,
            buff=0.30
        )

        self.add_fixed_in_frame_mobjects(
            final
        )

        self.play(
            gripper_card.animate.shift(UP * 0.35),
            FadeIn(final),
            run_time=1
        )

        self.wait(4)