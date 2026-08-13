from manim import *


class VoxPoserScene19(Scene):
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
            "Where Can the Pipeline Fail?",
            font_size=38,
            color=BLUE
        ).to_edge(UP, buff=0.45)

        self.play(Write(title))
        self.wait(1)

        # ============================================================
        # PIPELINE
        # ============================================================

        boxes = VGroup(
            RoundedRectangle(
                width=2.5,
                height=1.0,
                color=YELLOW,
                fill_opacity=0.08
            ),
            RoundedRectangle(
                width=2.5,
                height=1.0,
                color=GREEN,
                fill_opacity=0.08
            ),
            RoundedRectangle(
                width=2.8,
                height=1.0,
                color=PURPLE,
                fill_opacity=0.08
            ),
            RoundedRectangle(
                width=2.8,
                height=1.0,
                color=RED,
                fill_opacity=0.08
            )
        ).arrange(
            RIGHT,
            buff=0.35
        ).scale(0.84)

        labels = VGroup(
            Text("Language", font_size=23),
            Text("LLM / VLM", font_size=23),
            Text("Value map", font_size=23),
            Text("Trajectory", font_size=23)
        )

        for label, box in zip(labels, boxes):
            label.move_to(box)

        arrows = VGroup()

        for i in range(3):
            arrows.add(
                Arrow(
                    boxes[i].get_right(),
                    boxes[i + 1].get_left(),
                    buff=0.08
                )
            )

        for i in range(4):

            self.play(
                FadeIn(boxes[i]),
                Write(labels[i]),
                run_time=0.6
            )

            if i < 3:
                self.play(
                    GrowArrow(arrows[i]),
                    run_time=0.5
                )

        self.wait(2)

        # ============================================================
        # FAILURE CHAIN
        # ============================================================

        failure = VGroup(
            Text(
                "1. Perception error",
                font_size=27,
                color=RED
            ),
            Text(
                "2. Wrong affordance / constraint",
                font_size=27,
                color=ORANGE
            ),
            Text(
                "3. Wrong value map",
                font_size=27,
                color=PURPLE
            ),
            Text(
                "4. Wrong motion",
                font_size=27,
                color=RED
            )
        ).arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.25
        ).move_to(
            DOWN * 1.7
        )

        self.play(
            FadeOut(boxes),
            FadeOut(labels),
            FadeOut(arrows)
        )

        self.play(
            LaggedStart(
                *[
                    FadeIn(x, shift=RIGHT)
                    for x in failure
                ],
                lag_ratio=0.18
            ),
            run_time=2
        )

        self.wait(3)

        # ============================================================
        # THREE PRACTICAL CHALLENGES
        # ============================================================

        self.play(
            FadeOut(failure)
        )

        challenges = VGroup(
            VGroup(
                Text(
                    "Perception",
                    font_size=26,
                    color=GREEN
                ),
                Text(
                    "Grounding must be correct.",
                    font_size=21,
                    color=GRAY
                )
            ).arrange(
                DOWN,
                buff=0.12
            ),

            VGroup(
                Text(
                    "Language",
                    font_size=26,
                    color=YELLOW
                ),
                Text(
                    "Ambiguous instructions remain difficult.",
                    font_size=21,
                    color=GRAY
                )
            ).arrange(
                DOWN,
                buff=0.12
            ),

            VGroup(
                Text(
                    "Control",
                    font_size=26,
                    color=RED
                ),
                Text(
                    "Physical contact can be unpredictable.",
                    font_size=21,
                    color=GRAY
                )
            ).arrange(
                DOWN,
                buff=0.12
            )
        ).arrange(
            DOWN,
            buff=0.45
        )

        self.play(
            LaggedStart(
                *[
                    FadeIn(c, shift=UP)
                    for c in challenges
                ],
                lag_ratio=0.2
            ),
            run_time=2
        )

        self.wait(3)

        final = Text(
            "VoxPoser reduces engineering effort — it does not remove every failure mode.",
            font_size=25,
            color=BLUE
        ).to_edge(
            DOWN,
            buff=0.65
        )

        self.play(
            Write(final),
            run_time=1.4
        )

        self.wait(4)