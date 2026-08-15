from manim import *


class VoxPoserScene22(Scene):
    def construct(self):

        BLUE = "#5DADE2"
        GREEN = "#58D68D"
        YELLOW = "#F4D03F"
        PURPLE = "#AF7AC5"
        RED = "#EC7063"
        ORANGE = "#F5B041"
        GRAY = "#BFC9CA"

        # ============================================================
        # TITLE
        # ============================================================

        title = Text(
            "What Does the LLM Actually Generate?",
            font_size=36,
            color=BLUE
        ).to_edge(
            UP,
            buff=0.45
        )

        self.play(
            Write(title)
        )

        self.wait(2)

        # ============================================================
        # USER PROMPT
        # ============================================================

        prompt = RoundedRectangle(
            width=4.0,
            height=1.15,
            corner_radius=0.16,
            color=YELLOW,
            fill_opacity=0.08,
            stroke_width=2
        ).move_to(
            LEFT * 3.0 + UP * 1.30
        )

        prompt_text = Text(
            '"Close the top drawer."',
            font_size=25,
            color=YELLOW
        ).move_to(
            prompt
        )

        self.play(
            FadeIn(prompt),
            Write(prompt_text),
            run_time=1.3
        )

        self.wait(1.5)

        # ============================================================
        # LLM
        # ============================================================

        llm = RoundedRectangle(
            width=3.0,
            height=1.2,
            corner_radius=0.16,
            color=GREEN,
            fill_opacity=0.08,
            stroke_width=2
        ).move_to(
            RIGHT * 1.8 + UP * 1.30
        )

        llm_text = Text(
            "LLM\nreasoning + code",
            font_size=24,
            color=GREEN
        ).move_to(
            llm
        )

        arrow1 = Arrow(
            prompt.get_right(),
            llm.get_left(),
            buff=0.12,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.14
        )

        self.play(
            GrowArrow(arrow1),
            FadeIn(llm),
            Write(llm_text),
            run_time=1.3
        )

        self.wait(2)

        # ============================================================
        # GENERATED PROGRAM
        # ============================================================

        code_box = RoundedRectangle(
            width=7.2,
            height=3.2,
            corner_radius=0.18,
            color=PURPLE,
            fill_opacity=0.06,
            stroke_width=2
        ).move_to(
            DOWN * 1.35
        )

        code_title = Text(
            "Generated spatial program",
            font_size=24,
            color=PURPLE
        ).move_to(
            code_box.get_top() + DOWN * 0.38
        )

        code_lines = VGroup(
            Text(
                "parse_query_object(...)",
                font_size=21
            ),
            Text(
                "get_affordance_maps(...)",
                font_size=21,
                color=GREEN
            ),
            Text(
                "get_avoidance_maps(...)",
                font_size=21,
                color=RED
            ),
            Text(
                "compose_maps(...)",
                font_size=21,
                color=PURPLE
            ),
            Text(
                "plan_trajectory(...)",
                font_size=21,
                color=BLUE
            )
        ).arrange(
            DOWN,
            buff=0.18,
            aligned_edge=LEFT
        ).move_to(
            code_box.get_center() + DOWN * 0.10
        )

        arrow2 = Arrow(
            llm.get_bottom(),
            code_box.get_top(),
            buff=0.12,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.14,
            color=PURPLE
        )

        self.play(
            GrowArrow(arrow2),
            FadeIn(code_box),
            Write(code_title),
            run_time=1.2
        )

        self.play(
            LaggedStart(
                *[
                    FadeIn(
                        line,
                        shift=RIGHT
                    )
                    for line in code_lines
                ],
                lag_ratio=0.18
            ),
            run_time=2.5
        )

        self.wait(3)

        # ============================================================
        # EXPLANATION
        # ============================================================

        # Remove the diagram BEFORE showing explanation text.
        self.play(
            FadeOut(
                prompt,
                prompt_text,
                llm,
                llm_text,
                arrow1,
                code_box,
                code_title,
                code_lines,
                arrow2
            ),
            run_time=0.8
        )

        explanation_title = Text(
            "What does the LLM decide?",
            font_size=30,
            color=GREEN
        ).to_edge(
            UP,
            buff=1.20
        )

        explanation1 = Text(
            "The LLM decides what spatial information is needed.",
            font_size=27,
            color=GREEN
        ).move_to(
            UP * 0.25
        )

        explanation2 = Text(
            "The robotics system then turns that information into motion.",
            font_size=24,
            color=BLUE
        ).move_to(
            DOWN * 0.55
        )

        explanation_arrow = Arrow(
            explanation1.get_bottom(),
            explanation2.get_top(),
            buff=0.15,
            color=GRAY,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.14
        )

        self.play(
            Write(explanation_title),
            FadeIn(explanation1, shift=UP),
            run_time=1.0
        )

        self.wait(1)

        self.play(
            GrowArrow(explanation_arrow),
            FadeIn(explanation2, shift=UP),
            run_time=1.0
        )

        self.wait(4)

        # ============================================================
        # FINAL
        # ============================================================

        self.play(
            FadeOut(
                explanation_title,
                explanation1,
                explanation2,
                explanation_arrow
            )
        )

        final = Text(
            "Language is converted into a structured spatial program.",
            font_size=29,
            color=YELLOW
        )

        self.play(
            FadeIn(
                final,
                shift=UP
            ),
            run_time=1.5
        )

        self.wait(4)