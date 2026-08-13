from manim import *


class VoxPoserScene8(Scene):
    def construct(self):

        BLUE = "#5DADE2"
        GREEN = "#58D68D"
        RED = "#EC7063"
        YELLOW = "#F4D03F"
        PURPLE = "#AF7AC5"
        ORANGE = "#F5B041"
        GRAY = "#BFC9CA"

        # ============================================================
        # TITLE
        # ============================================================

        title = Text(
            "A Robot Trajectory Is More Than XYZ",
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
        # WAYPOINT
        # ============================================================

        waypoint = Dot(
            point=LEFT * 3.8,
            radius=0.12,
            color=YELLOW
        )

        waypoint_label = Text(
            "End-effector waypoint",
            font_size=23,
            color=YELLOW
        ).next_to(
            waypoint,
            UP,
            buff=0.25
        )

        self.play(
            FadeIn(waypoint),
            Write(waypoint_label)
        )

        # ============================================================
        # XYZ
        # ============================================================

        axes = ThreeDAxes(
            x_range=[-1, 1, 1],
            y_range=[-1, 1, 1],
            z_range=[-1, 1, 1],
            x_length=2.5,
            y_length=2.5,
            z_length=2.5
        ).scale(0.55).move_to(LEFT * 2.0)

        point = Sphere(
            radius=0.16,
            color=YELLOW
        ).move_to(
            axes.get_origin()
        )

        xyz_label = Text(
            "Position",
            font_size=24,
            color=GREEN
        ).next_to(
            axes,
            DOWN,
            buff=0.2
        )

        xyz_formula = MathTex(
            r"(x,y,z)"
        ).next_to(
            xyz_label,
            DOWN,
            buff=0.12
        )

        self.play(
            Create(axes),
            FadeIn(point),
            Write(xyz_label),
            Write(xyz_formula),
            run_time=1.8
        )

        self.wait(2)

        # ============================================================
        # ORIENTATION
        # ============================================================

        orientation_group = VGroup(
            Text(
                "Orientation",
                font_size=25,
                color=PURPLE
            ),
            MathTex(
                r"(R_x,R_y,R_z)"
            ),
            Text(
                "which way should the gripper face?",
                font_size=18,
                color=GRAY
            )
        ).arrange(
            DOWN,
            buff=0.16
        ).move_to(
            ORIGIN
        ).shift(
            RIGHT * 1.0
        )

        # orientation circle
        circle = Circle(
            radius=0.65,
            color=PURPLE,
            stroke_width=3
        ).move_to(
            RIGHT * 1.8
        )

        arrow = Arrow(
            circle.get_center() + LEFT * 0.1,
            circle.get_center() + UP * 0.5,
            color=PURPLE
        )

        self.play(
            Write(orientation_group),
            Create(circle),
            GrowArrow(arrow),
            run_time=1.8
        )

        self.wait(2)

        # ============================================================
        # VELOCITY
        # ============================================================

        velocity = VGroup(
            Text(
                "Velocity",
                font_size=25,
                color=ORANGE
            ),
            MathTex(
                r"v"
            ),
            Text(
                "how fast should it move?",
                font_size=18,
                color=GRAY
            )
        ).arrange(
            DOWN,
            buff=0.16
        ).move_to(
            RIGHT * 4.2 + UP * 1.3
        )

        velocity_arrow = Arrow(
            RIGHT * 3.4 + DOWN * 0.2,
            RIGHT * 4.7 + DOWN * 0.2,
            color=ORANGE,
            stroke_width=5
        )

        self.play(
            Write(velocity),
            GrowArrow(velocity_arrow),
            run_time=1.5
        )

        self.wait(2)

        # ============================================================
        # GRIPPER
        # ============================================================

        gripper = VGroup(
            Text(
                "Gripper",
                font_size=25,
                color=RED
            ),
            Text(
                "open / close",
                font_size=20
            )
        ).arrange(
            DOWN,
            buff=0.18
        ).move_to(
            RIGHT * 4.0 + DOWN * 1.7
        )

        left_finger = Line(
            RIGHT * 3.3 + DOWN * 1.0,
            RIGHT * 3.3 + DOWN * 2.0,
            color=RED,
            stroke_width=7
        )

        right_finger = Line(
            RIGHT * 4.0 + DOWN * 1.0,
            RIGHT * 4.0 + DOWN * 2.0,
            color=RED,
            stroke_width=7
        )

        self.play(
            Write(gripper),
            Create(left_finger),
            Create(right_finger),
            run_time=1.5
        )

        self.wait(2)

        # ============================================================
        # SIX DOF IDEA
        # ============================================================

        self.play(
            FadeOut(waypoint),
            FadeOut(waypoint_label),
            FadeOut(axes),
            FadeOut(point),
            FadeOut(xyz_label),
            FadeOut(xyz_formula),
            FadeOut(orientation_group),
            FadeOut(circle),
            FadeOut(arrow),
            FadeOut(velocity),
            FadeOut(velocity_arrow),
            FadeOut(gripper),
            FadeOut(left_finger),
            FadeOut(right_finger)
        )

        sixdof_title = Text(
            "One waypoint can encode a full robot action.",
            font_size=31,
            color=WHITE
        )

        self.play(
            Write(sixdof_title)
        )

        self.wait(1.5)

        components = VGroup(
            Text("Position", font_size=27, color=GREEN),
            MathTex(r"(x,y,z)"),
            Text("Orientation", font_size=27, color=PURPLE),
            MathTex(r"R"),
            Text("Velocity", font_size=27, color=ORANGE),
            MathTex(r"v"),
            Text("Gripper", font_size=27, color=RED),
            Text("open / close", font_size=23)
        ).arrange(
            RIGHT,
            buff=0.28
        ).scale(0.9)

        components.move_to(
            ORIGIN + DOWN * 0.5
        )

        self.play(
            LaggedStart(
                *[
                    FadeIn(c, shift=UP)
                    for c in components
                ],
                lag_ratio=0.12
            ),
            run_time=2.5
        )

        self.wait(3)

        # ============================================================
        # FINAL
        # ============================================================

        final = Text(
            "This is how a 3D plan becomes an executable manipulation action.",
            font_size=27,
            color=YELLOW
        ).to_edge(
            DOWN,
            buff=0.7
        )

        self.play(
            Write(final),
            run_time=1.4
        )

        self.wait(4)