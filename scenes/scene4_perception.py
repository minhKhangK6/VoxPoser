from manim import *


class VoxPoserScene4(Scene):
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
        # TITLE
        # ============================================================

        title = Text(
            "Grounding Language in the Physical Scene",
            font_size=36,
            color=BLUE_C
        ).to_edge(
            UP,
            buff=0.45
        )

        self.play(
            Write(title)
        )

        self.wait(1)

        # ============================================================
        # SCENE REPRESENTATION
        # ============================================================

        scene = Rectangle(
            width=5.2,
            height=3.5,
            color=GRAY_C,
            stroke_width=2
        ).move_to(
            LEFT * 3.05
        )

        drawer = Rectangle(
            width=2.4,
            height=0.75,
            color=BLUE_C,
            fill_opacity=0.25
        ).move_to(
            LEFT * 3.05 + DOWN * 0.3
        )

        vase = Circle(
            radius=0.42,
            color=RED_C,
            fill_opacity=0.25
        ).move_to(
            LEFT * 1.45 + UP * 0.7
        )

        drawer_label = Text(
            "drawer",
            font_size=20,
            color=BLUE_C
        ).next_to(
            drawer,
            DOWN,
            buff=0.10
        )

        vase_label = Text(
            "vase",
            font_size=20,
            color=RED_C
        ).next_to(
            vase,
            DOWN,
            buff=0.10
        )

        self.play(
            Create(scene),
            FadeIn(drawer),
            FadeIn(vase),
            Write(drawer_label),
            Write(vase_label),
            run_time=1.8
        )

        self.wait(2)

        # ============================================================
        # QUERY
        # ============================================================

        query = Text(
            'Query: "top drawer"',
            font_size=27,
            color=YELLOW_C
        ).move_to(
            RIGHT * 3.65 + UP * 2.0
        )

        self.play(
            Write(query),
            run_time=1
        )

        # ============================================================
        # DETECTOR
        # ============================================================

        detector = RoundedRectangle(
            width=3.8,
            height=1.0,
            corner_radius=0.16,
            color=GREEN_C,
            fill_opacity=0.08,
            stroke_width=2
        ).move_to(
            RIGHT * 3.65 + UP * 0.9
        )

        detector_text = VGroup(
            Text(
                "Open-vocabulary detector",
                font_size=20,
                color=GREEN_C
            ),
            Text(
                "→ bounding box",
                font_size=18
            )
        ).arrange(
            DOWN,
            buff=0.12
        ).move_to(
            detector
        )

        self.play(
            FadeIn(detector),
            FadeIn(detector_text),
            run_time=1
        )

        self.wait(2)

        # Highlight drawer
        bbox = SurroundingRectangle(
            drawer,
            color=GREEN_C,
            buff=0.08,
            stroke_width=3
        )

        self.play(
            Create(bbox),
            run_time=1
        )

        self.wait(1)

        # ============================================================
        # SEGMENTATION
        # ============================================================

        segment = RoundedRectangle(
            width=3.8,
            height=1.0,
            corner_radius=0.16,
            color=PURPLE_C,
            fill_opacity=0.08,
            stroke_width=2
        ).move_to(
            RIGHT * 3.65 + DOWN * 0.45
        )

        segment_text = VGroup(
            Text(
                "Segmentation",
                font_size=22,
                color=PURPLE_C
            ),
            Text(
                "→ object / part mask",
                font_size=18
            )
        ).arrange(
            DOWN,
            buff=0.12
        ).move_to(
            segment
        )

        self.play(
            FadeIn(segment),
            FadeIn(segment_text),
            run_time=1
        )

        self.wait(2)

        # ============================================================
        # MASK OVERLAY
        # ============================================================

        mask = Rectangle(
            width=2.48,
            height=0.84,
            color=PURPLE_C,
            fill_opacity=0.35,
            stroke_width=3
        ).move_to(
            drawer
        )

        self.play(
            FadeIn(mask),
            run_time=1
        )

        # ============================================================
        # RGB-D
        # ============================================================

        rgbd = RoundedRectangle(
            width=3.8,
            height=1.0,
            corner_radius=0.16,
            color=ORANGE_C,
            fill_opacity=0.08,
            stroke_width=2
        ).move_to(
            RIGHT * 3.65 + DOWN * 1.75
        )

        rgbd_text = VGroup(
            Text(
                "RGB-D observation",
                font_size=22,
                color=ORANGE_C
            ),
            Text(
                "→ 3D point cloud",
                font_size=18
            )
        ).arrange(
            DOWN,
            buff=0.12
        ).move_to(
            rgbd
        )

        self.play(
            FadeIn(rgbd),
            FadeIn(rgbd_text),
            run_time=1
        )

        self.wait(2)

        # ============================================================
        # POINT CLOUD
        # ============================================================

        # The point-cloud area is deliberately placed lower,
        # with enough separation from the RGB-D panel above.

        cloud_frame = RoundedRectangle(
            width=3.95,
            height=1.65,
            corner_radius=0.12,
            color=BLUE_C,
            fill_opacity=0.035,
            stroke_width=1.5
        ).move_to(
            RIGHT * 3.65 + DOWN * 3.15
        )

        self.play(
            Create(cloud_frame),
            run_time=0.7
        )

        # Point pattern stays comfortably inside the frame.
        points = [
            (-1.35, 0.45),
            (-0.95, 0.62),
            (-0.55, 0.50),
            (-0.15, 0.64),
            (0.25, 0.46),
            (0.65, 0.56),
            (1.05, 0.38),

            (-1.10, 0.16),
            (-0.70, 0.30),
            (-0.30, 0.13),
            (0.12, 0.25),
            (0.52, 0.12),
            (0.92, 0.22),

            (-0.82, -0.12),
            (-0.40, -0.02),
            (0.00, -0.14),
            (0.42, -0.04),
            (0.82, -0.16)
        ]

        dots = VGroup()

        for x, y in points:
            dots.add(
                Dot(
                    point=(
                        cloud_frame.get_center()
                        + RIGHT * x
                        + UP * y
                    ),
                    radius=0.045,
                    color=BLUE_C
                )
            )

        self.play(
            LaggedStart(
                *[
                    FadeIn(d, scale=0.6)
                    for d in dots
                ],
                lag_ratio=0.07
            ),
            run_time=1.8
        )

        # Label is placed BELOW the frame,
        # so it cannot collide with the RGB-D panel.
        cloud_label = Text(
            "3D object / part geometry",
            font_size=20,
            color=BLUE_C
        ).next_to(
            cloud_frame,
            DOWN,
            buff=0.12
        )

        self.play(
            Write(cloud_label),
            run_time=0.8
        )

        self.wait(3)

        # ============================================================
        # FINAL MESSAGE
        # ============================================================

        self.play(
            FadeOut(query),
            FadeOut(detector),
            FadeOut(detector_text),
            FadeOut(segment),
            FadeOut(segment_text),
            FadeOut(rgbd),
            FadeOut(rgbd_text),
            FadeOut(bbox),
            FadeOut(mask),
            FadeOut(cloud_frame),
            FadeOut(cloud_label),
            FadeOut(dots)
        )

        final = Text(
            "The language instruction is now grounded in 3D space.",
            font_size=30,
            color=GREEN_C
        ).to_edge(
            DOWN,
            buff=0.65
        )

        self.play(
            Write(final),
            run_time=1.4
        )

        self.wait(4)