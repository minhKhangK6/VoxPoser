from manim import *


class VoxPoserScene3(Scene):
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
            "VoxPoser System Architecture",
            font_size=38,
            color=BLUE_C
        ).to_edge(UP, buff=0.45)

        self.play(Write(title))
        self.wait(1)

        # ============================================================
        # INPUTS
        # ============================================================

        prompt_box = RoundedRectangle(
            width=3.2,
            height=1.35,
            color=YELLOW_C,
            fill_opacity=0.08
        ).move_to(LEFT * 4.3 + UP * 1.4)

        prompt_text = Text(
            "Language\nInstruction",
            font_size=25,
            color=YELLOW_C
        ).move_to(prompt_box)

        rgbd_box = RoundedRectangle(
            width=3.2,
            height=1.35,
            color=ORANGE_C,
            fill_opacity=0.08
        ).move_to(LEFT * 4.3 + DOWN * 0.5)

        rgbd_text = Text(
            "RGB-D\nObservation",
            font_size=25,
            color=ORANGE_C
        ).move_to(rgbd_box)

        self.play(
            FadeIn(prompt_box),
            Write(prompt_text)
        )

        self.play(
            FadeIn(rgbd_box),
            Write(rgbd_text)
        )

        self.wait(1)

        # ============================================================
        # LLM
        # ============================================================

        llm_box = RoundedRectangle(
            width=2.8,
            height=2.1,
            color=GREEN_C,
            fill_opacity=0.08
        ).move_to(LEFT * 0.9)

        llm_text = VGroup(
            Text(
                "LLM",
                font_size=34,
                color=GREEN_C
            ),
            Text(
                "reasoning",
                font_size=23
            ),
            Text(
                "+ code",
                font_size=23
            )
        ).arrange(
            DOWN,
            buff=0.15
        ).move_to(llm_box)

        arrow_prompt = Arrow(
            prompt_box.get_right(),
            llm_box.get_left() + UP * 0.45,
            buff=0.12
        )

        arrow_rgbd = Arrow(
            rgbd_box.get_right(),
            llm_box.get_left() + DOWN * 0.45,
            buff=0.12
        )

        self.play(
            GrowArrow(arrow_prompt),
            GrowArrow(arrow_rgbd),
            run_time=1
        )

        self.play(
            FadeIn(llm_box),
            FadeIn(llm_text)
        )

        self.wait(2)

        # ============================================================
        # GENERATED CODE
        # ============================================================

        code_box = RoundedRectangle(
            width=4.0,
            height=1.8,
            color=BLUE_C,
            fill_opacity=0.08
        ).move_to(RIGHT * 2.2 + UP * 1.55)

        code_text = Text(
            "query object\nget affordance\nget avoidance\ncompose maps",
            font_size=21,
            color=BLUE_C
        ).move_to(code_box)

        arrow_code = Arrow(
            llm_box.get_top(),
            code_box.get_left(),
            buff=0.15
        )

        self.play(
            GrowArrow(arrow_code),
            FadeIn(code_box),
            FadeIn(code_text),
            run_time=1.3
        )

        self.wait(2)

        # ============================================================
        # VLM
        # ============================================================

        vlm_box = RoundedRectangle(
            width=3.3,
            height=1.65,
            color=ORANGE_C,
            fill_opacity=0.08
        ).move_to(RIGHT * 2.2 + DOWN * 0.7)

        vlm_text = VGroup(
            Text(
                "Vision-Language Model",
                font_size=21,
                color=ORANGE_C
            ),
            Text(
                "ground in the scene",
                font_size=20
            )
        ).arrange(
            DOWN,
            buff=0.2
        ).move_to(vlm_box)

        arrow_vlm = Arrow(
            llm_box.get_right(),
            vlm_box.get_left(),
            buff=0.15
        )

        self.play(
            GrowArrow(arrow_vlm),
            FadeIn(vlm_box),
            FadeIn(vlm_text),
            run_time=1.2
        )

        self.wait(2)

        # ============================================================
        # VALUE MAP
        # ============================================================

        map_box = RoundedRectangle(
            width=4.0,
            height=1.7,
            color=PURPLE_C,
            fill_opacity=0.08
        ).move_to(RIGHT * 4.25 + DOWN * 2.5)

        map_text = VGroup(
            Text(
                "3D Value Maps",
                font_size=30,
                color=PURPLE_C
            ),
            Text(
                "grounded in observation space",
                font_size=18
            )
        ).arrange(
            DOWN,
            buff=0.18
        ).move_to(map_box)

        arrow_map = Arrow(
            vlm_box.get_bottom(),
            map_box.get_top(),
            buff=0.15
        )

        self.play(
            GrowArrow(arrow_map),
            FadeIn(map_box),
            FadeIn(map_text),
            run_time=1.2
        )

        self.wait(3)

        # ============================================================
        # HIGHLIGHT
        # ============================================================

        highlight = SurroundingRectangle(
            VGroup(llm_box, llm_text, code_box, code_text),
            color=GREEN_C,
            buff=0.15,
            stroke_width=2
        )

        label = Text(
            "The LLM does not directly control the motors.",
            font_size=25,
            color=GREEN_C
        ).to_edge(DOWN, buff=0.7)

        self.play(
            Create(highlight),
            Write(label),
            run_time=1.4
        )

        self.wait(4)