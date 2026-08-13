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

        self.play(Write(title))
        self.wait(2)

        # ============================================================
        # USER PROMPT
        # ============================================================

        prompt = RoundedRectangle(
            width=4.0,
            height=1.15,
            color=YELLOW,
            fill_opacity=0.08
        ).move_to(
            LEFT * 4.1 + UP * 1.0
        )

        prompt_text = Text(
            '"Close the top drawer."',
            font_size=25,
            color=YELLOW
        ).move_to(prompt)

        self.play(
            FadeIn(prompt),
            Write(prompt_text),
            run_time=1.5
        )

        self.wait(2)

        # ============================================================
        # LLM
        # ============================================================

        llm = RoundedRectangle(
            width=3.0,
            height=1.2,
            color=GREEN,
            fill_opacity=0.08
        ).move_to(
            ORIGIN + UP * 1.0
        )

        llm_text = Text(
            "LLM\nreasoning + code",
            font_size=24,
            color=GREEN
        ).move_to(llm)

        arrow1 = Arrow(
            prompt.get_right(),
            llm.get_left(),
            buff=0.12
        )

        self.play(
            GrowArrow(arrow1),
            FadeIn(llm),
            Write(llm_text),
            run_time=1.5
        )

        self.wait(2)

        # ============================================================
        # PROGRAM
        # ============================================================

        code_box = RoundedRectangle(
            width=7.2,
            height=3.2,
            color=PURPLE,
            fill_opacity=0.06
        ).move_to(
            DOWN * 1.0
        )

        code_title = Text(
            "Generated spatial program",
            font_size=24,
            color=PURPLE
        ).move_to(
            code_box.get_top() + DOWN * 0.4
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
            buff=0.18
        ).move_to(
            code_box.get_center() + DOWN * 0.2
        )

        arrow2 = Arrow(
            llm.get_bottom(),
            code_box.get_top(),
            buff=0.12
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

        self.wait(4)

        # ============================================================
        # EXPLANATION
        # ============================================================

        explanation = Text(
            "The LLM decides what spatial information is needed.",
            font_size=27,
            color=GREEN
        ).to_edge(
            DOWN,
            buff=1.0
        )

        explanation2 = Text(
            "The robotics system then turns that information into motion.",
            font_size=24,
            color=BLUE
        ).to_edge(
            DOWN,
            buff=0.55
        )

        self.play(
            Write(explanation),
            run_time=1.3
        )

        self.wait(2)

        self.play(
            Write(explanation2),
            run_time=1.2
        )

        self.wait(4)

        # ============================================================
        # FINAL
        # ============================================================

        self.play(
            FadeOut(explanation),
            FadeOut(explanation2),
            FadeOut(code_box),
            FadeOut(code_title),
            FadeOut(code_lines),
            FadeOut(arrow2),
            FadeOut(prompt),
            FadeOut(prompt_text),
            FadeOut(llm),
            FadeOut(llm_text),
            FadeOut(arrow1)
        )

        final = Text(
            "Language is converted into a structured spatial program.",
            font_size=29,
            color=YELLOW
        )

        self.play(
            FadeIn(final),
            run_time=1.5
        )

        self.wait(4)