from manim import *


class VoxPoserScene2(Scene):
    def construct(self):

        BLUE_C = "#5DADE2"
        YELLOW_C = "#F4D03F"
        GREEN_C = "#58D68D"
        RED_C = "#EC7063"
        PURPLE_C = "#AF7AC5"
        GRAY_C = "#BFC9CA"

        # ============================================================
        # TITLE
        # ============================================================

        title = Text(
            "From Language to Geometry",
            font_size=38,
            color=BLUE_C
        ).to_edge(
            UP,
            buff=0.5
        )

        self.play(
            Write(title)
        )

        self.wait(1.5)

        # ============================================================
        # INSTRUCTION
        # ============================================================

        command = Text(
            '"Close the top drawer."',
            font_size=40,
            color=YELLOW_C
        )

        self.play(
            FadeIn(command, shift=UP),
            run_time=1.2
        )

        self.wait(2)

        # Move the instruction upward, but leave enough
        # vertical space for the next explanatory sentence.
        self.play(
            command.animate.to_edge(
                UP,
                buff=1.35
            ),
            run_time=1
        )

        # ============================================================
        # WHAT DOES THE ROBOT NEED?
        # ============================================================

        question = Text(
            "What information does the robot actually need?",
            font_size=30,
            color=WHITE
        )

        self.play(
            Write(question),
            run_time=1.2
        )

        needs = VGroup(
            Text(
                "Where is the drawer?",
                font_size=27,
                color=BLUE_C
            ),
            Text(
                "Which part should I touch?",
                font_size=27,
                color=GREEN_C
            ),
            Text(
                "Where can the gripper move?",
                font_size=27,
                color=PURPLE_C
            ),
            Text(
                "What regions should be avoided?",
                font_size=27,
                color=RED_C
            )
        ).arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.3
        )

        needs.next_to(
            question,
            DOWN,
            buff=0.5
        )

        self.play(
            LaggedStart(
                *[
                    FadeIn(x, shift=RIGHT)
                    for x in needs
                ],
                lag_ratio=0.2
            ),
            run_time=2
        )

        self.wait(2)

        # ============================================================
        # TEXT -> SPATIAL CONCEPTS
        # ============================================================

        self.play(
            FadeOut(question),
            FadeOut(needs)
        )

        center_text = Text(
            "The instruction must become spatial constraints.",
            font_size=30,
            color=WHITE
        )

        # Put this sentence below the instruction instead of
        # sending it to the same top position.
        center_text.move_to(
            UP * 0.95
        )

        self.play(
            Write(center_text),
            run_time=1
        )

        self.wait(1.5)

        # Keep the message in this safe middle position.
        # No longer move it to the top edge.

        # ============================================================
        # LEFT: LANGUAGE
        # ============================================================

        language_box = RoundedRectangle(
            width=3.2,
            height=1.5,
            color=YELLOW_C,
            fill_opacity=0.08
        ).move_to(
            LEFT * 3.9 + DOWN * 1.0
        )

        language_text = Text(
            "Natural\nLanguage",
            font_size=27,
            color=YELLOW_C
        ).move_to(
            language_box
        )

        # ============================================================
        # MIDDLE: CONCEPTS
        # ============================================================

        concept_box = RoundedRectangle(
            width=3.4,
            height=2.6,
            color=GREEN_C,
            fill_opacity=0.08
        ).move_to(
            DOWN * 1.0
        )

        concept_text = VGroup(
            Text(
                "target object",
                font_size=22
            ),
            Text(
                "contact region",
                font_size=22
            ),
            Text(
                "desired motion",
                font_size=22
            ),
            Text(
                "avoidance constraints",
                font_size=22
            )
        ).arrange(
            DOWN,
            buff=0.14
        ).move_to(
            concept_box
        )

        # ============================================================
        # RIGHT: GEOMETRY
        # ============================================================

        geometry_box = RoundedRectangle(
            width=3.2,
            height=1.5,
            color=PURPLE_C,
            fill_opacity=0.08
        ).move_to(
            RIGHT * 3.9 + DOWN * 1.0
        )

        geometry_text = Text(
            "3D Spatial\nRepresentation",
            font_size=25,
            color=PURPLE_C
        ).move_to(
            geometry_box
        )

        arrow1 = Arrow(
            language_box.get_right(),
            concept_box.get_left(),
            buff=0.15
        )

        arrow2 = Arrow(
            concept_box.get_right(),
            geometry_box.get_left(),
            buff=0.15
        )

        self.play(
            FadeIn(language_box),
            Write(language_text)
        )

        self.play(
            GrowArrow(arrow1),
            FadeIn(concept_box),
            FadeIn(concept_text),
            run_time=1.2
        )

        self.play(
            GrowArrow(arrow2),
            FadeIn(geometry_box),
            Write(geometry_text),
            run_time=1.2
        )

        self.wait(3)

        # ============================================================
        # CORE MESSAGE
        # ============================================================

        self.play(
            FadeOut(center_text),
            FadeOut(language_box),
            FadeOut(language_text),
            FadeOut(concept_box),
            FadeOut(concept_text),
            FadeOut(geometry_box),
            FadeOut(geometry_text),
            FadeOut(arrow1),
            FadeOut(arrow2)
        )

        final = VGroup(
            Text(
                "Language tells us what should happen.",
                font_size=30,
                color=YELLOW_C
            ),
            Text(
                "Geometry tells the robot where and how.",
                font_size=30,
                color=PURPLE_C
            )
        ).arrange(
            DOWN,
            buff=0.45
        )

        self.play(
            FadeIn(final[0], shift=UP),
            FadeIn(final[1], shift=DOWN),
            run_time=1.5
        )

        self.wait(3)

        outro = Text(
            "VoxPoser builds the bridge between them.",
            font_size=28,
            color=GREEN_C
        ).to_edge(
            DOWN,
            buff=0.8
        )

        self.play(
            Write(outro),
            run_time=1.2
        )

        self.wait(4)