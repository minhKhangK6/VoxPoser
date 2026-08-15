from manim import *


class VoxPoserScene16(Scene):
    def construct(self):

        # ============================================================
        # COLORS
        # ============================================================

        BLUE = "#5DADE2"
        GREEN = "#58D68D"
        YELLOW = "#F4D03F"
        PURPLE = "#AF7AC5"
        RED = "#EC7063"
        GRAY = "#BFC9CA"
        WHITE_C = "#FFFFFF"

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

        language_box = RoundedRectangle(
            width=2.7,
            height=1.15,
            corner_radius=0.15,
            color=YELLOW,
            fill_opacity=0.08,
            stroke_width=2
        )

        llm_box = RoundedRectangle(
            width=2.7,
            height=1.15,
            corner_radius=0.15,
            color=GREEN,
            fill_opacity=0.08,
            stroke_width=2
        )

        value_map_box = RoundedRectangle(
            width=2.7,
            height=1.15,
            corner_radius=0.15,
            color=PURPLE,
            fill_opacity=0.08,
            stroke_width=2
        )

        motion_box = RoundedRectangle(
            width=2.7,
            height=1.15,
            corner_radius=0.15,
            color=RED,
            fill_opacity=0.08,
            stroke_width=2
        )

        robot_box = RoundedRectangle(
            width=2.7,
            height=1.15,
            corner_radius=0.15,
            color=BLUE,
            fill_opacity=0.08,
            stroke_width=2
        )

        # ============================================================
        # TEXT
        # ============================================================

        language_text = Text(
            "Language",
            font_size=24,
            color=YELLOW
        )

        llm_text = Text(
            "LLM / VLM",
            font_size=24,
            color=GREEN
        )

        value_map_text = Text(
            "3D Value Maps",
            font_size=21,
            color=PURPLE
        )

        motion_text = Text(
            "Motion Planning",
            font_size=20,
            color=RED
        )

        robot_text = Text(
            "Robot",
            font_size=24,
            color=BLUE
        )

        # ============================================================
        # POSITION
        # ============================================================

        language_box.move_to(
            LEFT * 3.2 + UP * 0.85
        )

        llm_box.move_to(
            ORIGIN + UP * 0.85
        )

        value_map_box.move_to(
            RIGHT * 3.2 + UP * 0.85
        )

        motion_box.move_to(
            LEFT * 1.6 + DOWN * 1.0
        )

        robot_box.move_to(
            RIGHT * 1.6 + DOWN * 1.0
        )

        language_text.move_to(language_box)
        llm_text.move_to(llm_box)
        value_map_text.move_to(value_map_box)
        motion_text.move_to(motion_box)
        robot_text.move_to(robot_box)

        boxes = VGroup(
            language_box,
            llm_box,
            value_map_box,
            motion_box,
            robot_box
        )

        texts = VGroup(
            language_text,
            llm_text,
            value_map_text,
            motion_text,
            robot_text
        )

        # ============================================================
        # ARROWS
        # ============================================================

        arrow_1 = Arrow(
            language_box.get_right(),
            llm_box.get_left(),
            buff=0.14,
            color=GRAY,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.14
        )

        arrow_2 = Arrow(
            llm_box.get_right(),
            value_map_box.get_left(),
            buff=0.14,
            color=GRAY,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.14
        )

        arrow_4 = Arrow(
            motion_box.get_right(),
            robot_box.get_left(),
            buff=0.14,
            color=GRAY,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.14
        )

        arrow_5 = Arrow(
            llm_box.get_bottom(),
            motion_box.get_top(),
            color=GRAY,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.14,
            buff=0.12
        )

        arrows = VGroup(
            arrow_1,
            arrow_2,
            arrow_4,
            arrow_5
        )

        # ============================================================
        # ANIMATE PIPELINE
        # ============================================================

        self.play(
            FadeIn(language_box),
            Write(language_text),
            run_time=0.7
        )

        self.play(
            GrowArrow(arrow_1),
            FadeIn(llm_box),
            Write(llm_text),
            run_time=0.7
        )

        self.play(
            GrowArrow(arrow_2),
            FadeIn(value_map_box),
            Write(value_map_text),
            run_time=0.7
        )

        self.play(
            GrowArrow(arrow_5),
            FadeIn(motion_box),
            Write(motion_text),
            run_time=0.7
        )

        self.play(
            GrowArrow(arrow_4),
            FadeIn(robot_box),
            Write(robot_text),
            run_time=0.7
        )

        self.wait(2)

        # ============================================================
        # THREE QUESTIONS
        # ============================================================

        self.play(
            FadeOut(boxes),
            FadeOut(texts),
            FadeOut(arrows),
            run_time=0.8
        )

        questions_title = Text(
            "Three questions VoxPoser answers",
            font_size=29,
            color=GRAY
        ).to_edge(
            UP,
            buff=1.35
        )

        self.play(
            Write(questions_title),
            run_time=0.9
        )

        questions = VGroup(
            Text(
                "What should the robot do?",
                font_size=28,
                color=YELLOW
            ),
            Text(
                "Where should it move?",
                font_size=28,
                color=PURPLE
            ),
            Text(
                "How should it adapt?",
                font_size=28,
                color=GREEN
            )
        ).arrange(
            DOWN,
            buff=0.35
        ).move_to(
            DOWN * 0.45
        )

        self.play(
            LaggedStart(
                *[
                    FadeIn(
                        q,
                        shift=RIGHT
                    )
                    for q in questions
                ],
                lag_ratio=0.2
            ),
            run_time=1.8
        )

        self.wait(3)

        # ============================================================
        # TRANSITION — NOT THE END
        # ============================================================

        self.play(
            FadeOut(questions_title),
            FadeOut(questions),
            FadeOut(title),
            run_time=0.8
        )

        transition = VGroup(
            Text(
                "So far, we've seen how VoxPoser works.",
                font_size=28,
                color=WHITE_C
            ),
            Text(
                "Now let's see what the experiments reveal.",
                font_size=31,
                color=BLUE
            )
        ).arrange(
            DOWN,
            buff=0.25
        )

        self.play(
            FadeIn(
                transition,
                shift=UP
            ),
            run_time=1.5
        )

        self.wait(4)