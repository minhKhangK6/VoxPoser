from manim import *


class VoxPoserScene16(Scene):
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
            "VoxPoser in One Picture",
            font_size=40,
            color=BLUE
        ).to_edge(
            UP,
            buff=0.5
        )

        self.play(
            Write(title)
        )

        self.wait(1)

        # ============================================================
        # MAIN PIPELINE
        # ============================================================

        names = [
            ("Language", YELLOW),
            ("LLM / VLM", GREEN),
            ("3D Value Maps", PURPLE),
            ("Motion Planning", RED),
            ("Robot", BLUE)
        ]

        boxes = VGroup()

        texts = VGroup()

        for name, color in names:

            box = RoundedRectangle(
                width=2.25,
                height=1.05,
                color=color,
                fill_opacity=0.08
            )

            text = Text(
                name,
                font_size=22
            ).move_to(box)

            boxes.add(box)
            texts.add(text)

        boxes.arrange(
            RIGHT,
            buff=0.28
        ).scale(0.78).center()

        for text, box in zip(texts, boxes):
            text.move_to(box)

        arrows = VGroup()

        for i in range(len(boxes) - 1):
            arrows.add(
                Arrow(
                    boxes[i].get_right(),
                    boxes[i + 1].get_left(),
                    buff=0.08,
                    color=GRAY
                )
            )

        for i in range(len(boxes)):

            self.play(
                FadeIn(boxes[i]),
                Write(texts[i]),
                run_time=0.6
            )

            if i < len(boxes) - 1:
                self.play(
                    GrowArrow(arrows[i]),
                    run_time=0.5
                )

        self.wait(3)

        # ============================================================
        # THREE QUESTIONS
        # ============================================================

        questions = VGroup(
            Text(
                "What should the robot do?",
                font_size=24,
                color=YELLOW
            ),
            Text(
                "Where should it move?",
                font_size=24,
                color=PURPLE
            ),
            Text(
                "How should it adapt?",
                font_size=24,
                color=GREEN
            )
        ).arrange(
            DOWN,
            buff=0.25
        ).to_edge(
            DOWN,
            buff=0.8
        )

        self.play(
            LaggedStart(
                *[
                    FadeIn(q, shift=UP)
                    for q in questions
                ],
                lag_ratio=0.18
            ),
            run_time=1.8
        )

        self.wait(3)

        # ============================================================
        # FINAL MESSAGE
        # ============================================================

        self.play(
            FadeOut(questions)
        )

        final = VGroup(
            Text(
                "VoxPoser connects",
                font_size=30,
                color=WHITE
            ),
            Text(
                "language reasoning",
                font_size=34,
                color=YELLOW
            ),
            Text(
                "with",
                font_size=28,
                color=WHITE
            ),
            Text(
                "physical robot motion.",
                font_size=34,
                color=BLUE
            )
        ).arrange(
            DOWN,
            buff=0.15
        )

        self.play(
            FadeIn(final, shift=UP),
            run_time=1.8
        )

        self.wait(4)

        thank_you = Text(
            "Thank you.",
            font_size=30,
            color=GRAY
        ).to_edge(
            DOWN,
            buff=0.6
        )

        self.play(
            FadeIn(thank_you),
            run_time=1
        )

        self.wait(4)