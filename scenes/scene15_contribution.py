from manim import *


class VoxPoserScene15(Scene):
    def construct(self):

        BLUE = "#5DADE2"
        GREEN = "#58D68D"
        YELLOW = "#F4D03F"
        PURPLE = "#AF7AC5"
        RED = "#EC7063"
        GRAY = "#BFC9CA"

        # ============================================================
        # TITLE
        # ============================================================

        title = Text(
            "What Does VoxPoser Actually Contribute?",
            font_size=35,
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
        # WRONG INTERPRETATION
        # ============================================================

        wrong = Text(
            "LLM → Robot motors",
            font_size=32,
            color=RED
        )

        cross = Cross(
            wrong,
            stroke_width=5,
            color=RED
        )

        wrong_group = VGroup(
            wrong,
            cross
        ).move_to(
            UP * 1.2
        )

        self.play(
            FadeIn(wrong),
            Create(cross),
            run_time=1
        )

        self.wait(2)

        # ============================================================
        # REAL PIPELINE
        # ============================================================

        self.play(
            FadeOut(wrong_group)
        )

        boxes = VGroup(
            RoundedRectangle(
                width=2.5,
                height=1.05,
                color=YELLOW,
                fill_opacity=0.08
            ),
            RoundedRectangle(
                width=2.5,
                height=1.05,
                color=GREEN,
                fill_opacity=0.08
            ),
            RoundedRectangle(
                width=2.8,
                height=1.05,
                color=PURPLE,
                fill_opacity=0.08
            ),
            RoundedRectangle(
                width=2.8,
                height=1.05,
                color=RED,
                fill_opacity=0.08
            )
        )

        boxes.arrange(
            RIGHT,
            buff=0.45
        ).scale(
            0.88
        ).move_to(
            ORIGIN
        )

        # Quan trọng:
        # texts phải là VGroup, không phải Python list.
        texts = VGroup(
            Text(
                "Language",
                font_size=23,
                color=YELLOW
            ),
            Text(
                "LLM / VLM",
                font_size=23,
                color=GREEN
            ),
            Text(
                "3D Value\nMaps",
                font_size=22,
                color=PURPLE
            ),
            Text(
                "Motion\nPlanner",
                font_size=22,
                color=RED
            )
        )

        for text, box in zip(texts, boxes):
            text.move_to(box)

        arrows = VGroup(
            Arrow(
                boxes[0].get_right(),
                boxes[1].get_left(),
                buff=0.08
            ),
            Arrow(
                boxes[1].get_right(),
                boxes[2].get_left(),
                buff=0.08
            ),
            Arrow(
                boxes[2].get_right(),
                boxes[3].get_left(),
                buff=0.08
            )
        )

        self.play(
            FadeIn(boxes[0]),
            Write(texts[0]),
            run_time=0.7
        )

        self.play(
            GrowArrow(arrows[0]),
            FadeIn(boxes[1]),
            Write(texts[1]),
            run_time=0.7
        )

        self.play(
            GrowArrow(arrows[1]),
            FadeIn(boxes[2]),
            Write(texts[2]),
            run_time=0.7
        )

        self.play(
            GrowArrow(arrows[2]),
            FadeIn(boxes[3]),
            Write(texts[3]),
            run_time=0.7
        )

        self.wait(3)

        # ============================================================
        # THREE CORE CONTRIBUTIONS
        # ============================================================

        self.play(
            FadeOut(boxes),
            FadeOut(texts),
            FadeOut(arrows)
        )

        contributions = VGroup(
            VGroup(
                Text(
                    "1",
                    font_size=28,
                    color=YELLOW
                ),
                Text(
                    "Open-ended language",
                    font_size=23
                )
            ).arrange(
                RIGHT,
                buff=0.25
            ),

            VGroup(
                Text(
                    "2",
                    font_size=28,
                    color=PURPLE
                ),
                Text(
                    "Composable 3D value maps",
                    font_size=23
                )
            ).arrange(
                RIGHT,
                buff=0.25
            ),

            VGroup(
                Text(
                    "3",
                    font_size=28,
                    color=GREEN
                ),
                Text(
                    "Model-based robot planning",
                    font_size=23
                )
            ).arrange(
                RIGHT,
                buff=0.25
            )
        ).arrange(
            DOWN,
            buff=0.45,
            aligned_edge=LEFT
        )

        self.play(
            LaggedStart(
                *[
                    FadeIn(
                        c,
                        shift=RIGHT
                    )
                    for c in contributions
                ],
                lag_ratio=0.2
            ),
            run_time=2.2
        )

        self.wait(3)

        # ============================================================
        # FINAL STATEMENT
        # ============================================================

        final = Text(
            "Language reasoning becomes a structured physical objective.",
            font_size=27,
            color=BLUE
        ).to_edge(
            DOWN,
            buff=0.7
        )

        self.play(
            Write(final),
            run_time=1.3
        )

        self.wait(4)