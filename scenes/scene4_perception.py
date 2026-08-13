from manim import *


class VoxPoserScene4(Scene):
    def construct(self):

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
        ).to_edge(UP, buff=0.45)

        self.play(Write(title))
        self.wait(1)

        # ============================================================
        # SCENE REPRESENTATION
        # ============================================================

        scene = Rectangle(
            width=5.5,
            height=3.6,
            color=GRAY_C,
            stroke_width=2
        ).move_to(LEFT * 3)

        drawer = Rectangle(
            width=2.5,
            height=0.8,
            color=BLUE_C,
            fill_opacity=0.25
        ).move_to(LEFT * 3 + DOWN * 0.3)

        vase = Circle(
            radius=0.45,
            color=RED_C,
            fill_opacity=0.25
        ).move_to(LEFT * 1.3 + UP * 0.7)

        drawer_label = Text(
            "drawer",
            font_size=20,
            color=BLUE_C
        ).next_to(drawer, DOWN, buff=0.12)

        vase_label = Text(
            "vase",
            font_size=20,
            color=RED_C
        ).next_to(vase, DOWN, buff=0.12)

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
        ).move_to(RIGHT * 3.5 + UP * 2)

        self.play(
            Write(query),
            run_time=1
        )

        # ============================================================
        # DETECTOR
        # ============================================================

        detector = RoundedRectangle(
            width=4.0,
            height=1.0,
            color=GREEN_C,
            fill_opacity=0.08
        ).move_to(RIGHT * 3.5 + UP * 0.9)

        detector_text = VGroup(
            Text(
                "Open-vocabulary detector",
                font_size=21,
                color=GREEN_C
            ),
            Text(
                "→ bounding box",
                font_size=19
            )
        ).arrange(
            DOWN,
            buff=0.12
        ).move_to(detector)

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
        # SEGMENT ANYTHING
        # ============================================================

        segment = RoundedRectangle(
            width=4.0,
            height=1.0,
            color=PURPLE_C,
            fill_opacity=0.08
        ).move_to(RIGHT * 3.5 + DOWN * 0.5)

        segment_text = VGroup(
            Text(
                "Segmentation",
                font_size=22,
                color=PURPLE_C
            ),
            Text(
                "→ object / part mask",
                font_size=19
            )
        ).arrange(
            DOWN,
            buff=0.12
        ).move_to(segment)

        self.play(
            FadeIn(segment),
            FadeIn(segment_text),
            run_time=1
        )

        self.wait(2)

        # mask overlay
        mask = Rectangle(
            width=2.65,
            height=0.92,
            color=PURPLE_C,
            fill_opacity=0.35,
            stroke_width=3
        ).move_to(drawer)

        self.play(
            FadeIn(mask),
            run_time=1
        )

        # ============================================================
        # RGB-D
        # ============================================================

        rgbd = RoundedRectangle(
            width=4.0,
            height=1.0,
            color=ORANGE_C,
            fill_opacity=0.08
        ).move_to(RIGHT * 3.5 + DOWN * 1.9)

        rgbd_text = VGroup(
            Text(
                "RGB-D observation",
                font_size=22,
                color=ORANGE_C
            ),
            Text(
                "→ 3D point cloud",
                font_size=19
            )
        ).arrange(
            DOWN,
            buff=0.12
        ).move_to(rgbd)

        self.play(
            FadeIn(rgbd),
            FadeIn(rgbd_text),
            run_time=1
        )

        self.wait(2)

        # ============================================================
        # POINT CLOUD
        # ============================================================

        dots = VGroup()

        points = [
            (-0.8, 0.8),
            (-0.4, 1.0),
            (0.0, 0.85),
            (0.4, 0.95),
            (0.8, 0.7),
            (-0.6, 0.35),
            (-0.2, 0.5),
            (0.25, 0.4),
            (0.65, 0.35),
            (-0.4, 0.05),
            (0.0, 0.15),
            (0.4, 0.1)
        ]

        for x, y in points:
            dots.add(
                Dot(
                    point=RIGHT * 3.5
                    + RIGHT * x
                    + UP * y,
                    radius=0.045,
                    color=BLUE_C
                )
            )

        cloud_label = Text(
            "3D object / part geometry",
            font_size=23,
            color=BLUE_C
        ).move_to(
            RIGHT * 3.5 + DOWN * 2.75
        )

        self.play(
            LaggedStart(
                *[
                    FadeIn(d)
                    for d in dots
                ],
                lag_ratio=0.08
            ),
            Write(cloud_label),
            run_time=1.5
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
            FadeOut(bbox)
        )

        final = Text(
            "The language instruction is now grounded in 3D space.",
            font_size=30,
            color=GREEN_C
        ).to_edge(DOWN, buff=0.65)

        self.play(
            Write(final),
            run_time=1.4
        )

        self.wait(4)