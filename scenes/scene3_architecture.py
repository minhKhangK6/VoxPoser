from manim import *


class VoxPoserScene3(Scene):
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
            "VoxPoser System Architecture",
            font_size=38,
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
        # INPUTS — LEFT COLUMN
        # ============================================================

        prompt_box = RoundedRectangle(
            width=2.8,
            height=1.25,
            corner_radius=0.16,
            color=YELLOW_C,
            fill_opacity=0.08,
            stroke_width=2
        ).move_to(
            LEFT * 5.0 + UP * 1.0
        )

        prompt_text = Text(
            "Language\nInstruction",
            font_size=24,
            color=YELLOW_C,
            line_spacing=0.9
        ).move_to(
            prompt_box
        )

        rgbd_box = RoundedRectangle(
            width=2.8,
            height=1.25,
            corner_radius=0.16,
            color=ORANGE_C,
            fill_opacity=0.08,
            stroke_width=2
        ).move_to(
            LEFT * 5.0 + DOWN * 0.75
        )

        rgbd_text = Text(
            "RGB-D\nObservation",
            font_size=24,
            color=ORANGE_C,
            line_spacing=0.9
        ).move_to(
            rgbd_box
        )

        self.play(
            FadeIn(prompt_box),
            Write(prompt_text),
            run_time=0.8
        )

        self.play(
            FadeIn(rgbd_box),
            Write(rgbd_text),
            run_time=0.8
        )

        self.wait(1)

        # ============================================================
        # LLM — CENTER
        # ============================================================

        llm_box = RoundedRectangle(
            width=2.8,
            height=2.15,
            corner_radius=0.18,
            color=GREEN_C,
            fill_opacity=0.09,
            stroke_width=2.5
        ).move_to(
            LEFT * 1.65 + DOWN * 0.05
        )

        llm_text = VGroup(
            Text(
                "LLM",
                font_size=35,
                color=GREEN_C
            ),
            Text(
                "reasoning",
                font_size=22
            ),
            Text(
                "+ code",
                font_size=22
            )
        ).arrange(
            DOWN,
            buff=0.14
        ).move_to(
            llm_box
        )

        # ============================================================
        # INPUT ARROWS
        # ============================================================

        prompt_target = (
            llm_box.get_left()
            + UP * 0.45
        )

        rgbd_target = (
            llm_box.get_left()
            + DOWN * 0.45
        )

        arrow_prompt = Arrow(
            prompt_box.get_right() + RIGHT * 0.05,
            prompt_target + LEFT * 0.12,
            buff=0.05,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.18,
            color=YELLOW_C
        )

        arrow_rgbd = Arrow(
            rgbd_box.get_right() + RIGHT * 0.05,
            rgbd_target + LEFT * 0.12,
            buff=0.05,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.18,
            color=ORANGE_C
        )

        self.play(
            GrowArrow(arrow_prompt),
            GrowArrow(arrow_rgbd),
            run_time=0.9
        )

        self.play(
            FadeIn(llm_box),
            FadeIn(llm_text),
            run_time=0.8
        )

        self.wait(2)

        # ============================================================
        # GENERATED CODE — TOP RIGHT
        # ============================================================

        code_box = RoundedRectangle(
            width=3.7,
            height=1.65,
            corner_radius=0.16,
            color=BLUE_C,
            fill_opacity=0.08,
            stroke_width=2
        ).move_to(
            RIGHT * 2.05 + UP * 1.35
        )

        code_title = Text(
            "Generated code",
            font_size=23,
            color=BLUE_C
        )

        code_body = Text(
            "query object\n"
            "get affordance\n"
            "get avoidance\n"
            "compose maps",
            font_size=19,
            color=BLUE_C,
            line_spacing=0.85
        )

        code_text = VGroup(
            code_title,
            code_body
        ).arrange(
            DOWN,
            buff=0.10
        ).move_to(
            code_box
        )

        arrow_code = Arrow(
            llm_box.get_top() + UP * 0.02,
            code_box.get_left() + LEFT * 0.12 + DOWN * 0.20,
            buff=0.06,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.17,
            color=BLUE_C
        )

        self.play(
            GrowArrow(arrow_code),
            FadeIn(code_box),
            FadeIn(code_text),
            run_time=1.2
        )

        self.wait(2)

        # ============================================================
        # VISION-LANGUAGE MODEL — LOWER RIGHT
        # ============================================================

        vlm_box = RoundedRectangle(
            width=3.7,
            height=1.45,
            corner_radius=0.16,
            color=ORANGE_C,
            fill_opacity=0.08,
            stroke_width=2
        ).move_to(
            RIGHT * 2.05 + DOWN * 0.75
        )

        vlm_text = VGroup(
            Text(
                "Vision-Language Model",
                font_size=21,
                color=ORANGE_C
            ),
            Text(
                "ground in the scene",
                font_size=19
            )
        ).arrange(
            DOWN,
            buff=0.16
        ).move_to(
            vlm_box
        )

        arrow_vlm = Arrow(
            llm_box.get_right() + RIGHT * 0.12,
            vlm_box.get_left() + LEFT * 0.12,
            buff=0.06,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.17,
            color=ORANGE_C
        )

        self.play(
            GrowArrow(arrow_vlm),
            FadeIn(vlm_box),
            FadeIn(vlm_text),
            run_time=1.1
        )

        self.wait(2)

        # ============================================================
        # 3D VALUE MAPS — BOTTOM RIGHT
        # ============================================================

        map_box = RoundedRectangle(
            width=4.15,
            height=1.65,
            corner_radius=0.18,
            color=PURPLE_C,
            fill_opacity=0.08,
            stroke_width=2.2
        ).move_to(
            RIGHT * 4.35 + DOWN * 2.45
        )

        map_text = VGroup(
            Text(
                "3D Value Maps",
                font_size=29,
                color=PURPLE_C
            ),
            Text(
                "grounded in observation space",
                font_size=18
            )
        ).arrange(
            DOWN,
            buff=0.16
        ).move_to(
            map_box
        )

        arrow_map = Arrow(
            vlm_box.get_bottom() + DOWN * 0.08,
            map_box.get_top() + UP * 0.12,
            buff=0.06,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.17,
            color=PURPLE_C
        )

        self.play(
            GrowArrow(arrow_map),
            FadeIn(map_box),
            FadeIn(map_text),
            run_time=1.2
        )

        self.wait(3)

        # ============================================================
        # HIGHLIGHT — LLM + GENERATED CODE
        # ============================================================

        highlight = SurroundingRectangle(
            VGroup(
                llm_box,
                code_box
            ),
            color=GREEN_C,
            buff=0.22,
            corner_radius=0.12,
            stroke_width=2.5
        )

        label = Text(
            "The LLM does not directly control the motors.",
            font_size=25,
            color=GREEN_C
        ).to_edge(
            DOWN,
            buff=0.82
        )

        self.play(
            Create(highlight),
            Write(label),
            run_time=1.4
        )

        self.wait(4)