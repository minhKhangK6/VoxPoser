from manim import *


class VoxPoserScene24(Scene):
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
            "The Core Idea of VoxPoser",
            font_size=42,
            color=BLUE
        ).to_edge(
            UP,
            buff=0.5
        )

        self.play(
            Write(title)
        )

        self.wait(2)

        # ============================================================
        # LANGUAGE
        # ============================================================

        language = Text(
            '"Close the top drawer."',
            font_size=35,
            color=YELLOW
        )

        self.play(
            FadeIn(
                language,
                shift=UP
            ),
            run_time=1.3
        )

        self.wait(3)

        # ============================================================
        # MEANING
        # ============================================================

        self.play(
            language.animate.shift(
                UP * 1.2
            )
        )

        meaning_title = Text(
            "The instruction implies spatial requirements:",
            font_size=27,
            color=WHITE
        ).to_edge(
            UP,
            buff=1.6
        )

        meaning = VGroup(
            Text(
                "which object?",
                font_size=25,
                color=BLUE
            ),
            Text(
                "where should we act?",
                font_size=25,
                color=GREEN
            ),
            Text(
                "what should we avoid?",
                font_size=25,
                color=RED
            )
        ).arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.28
        ).move_to(
            ORIGIN
        )

        self.play(
            Write(meaning_title),
            LaggedStart(
                *[
                    FadeIn(
                        x,
                        shift=RIGHT
                    )
                    for x in meaning
                ],
                lag_ratio=0.2
            ),
            run_time=2
        )

        self.wait(3)

        # ============================================================
        # VALUE MAP
        # ============================================================

        self.play(
            FadeOut(meaning_title),
            FadeOut(meaning)
        )

        map_box = RoundedRectangle(
            width=7.5,
            height=1.35,
            color=PURPLE,
            fill_opacity=0.08
        ).move_to(
            ORIGIN
        )

        map_text = Text(
            "Composable 3D Value Maps",
            font_size=32,
            color=PURPLE
        ).move_to(map_box)

        self.play(
            Create(map_box),
            Write(map_text),
            run_time=1.4
        )

        self.wait(3)

        # ============================================================
        # PLANNING
        # ============================================================

        planner_box = RoundedRectangle(
            width=7.0,
            height=1.25,
            color=RED,
            fill_opacity=0.08
        ).move_to(
            DOWN * 1.8
        )

        planner_text = Text(
            "Model-based motion planning",
            font_size=30,
            color=RED
        ).move_to(planner_box)

        arrow = Arrow(
            map_box.get_bottom(),
            planner_box.get_top(),
            buff=0.15,
            color=WHITE
        )

        self.play(
            GrowArrow(arrow),
            FadeIn(planner_box),
            Write(planner_text),
            run_time=1.4
        )

        self.wait(3)

        # ============================================================
        # CLOSED LOOP
        # ============================================================

        self.play(
            FadeOut(language),
            FadeOut(map_box),
            FadeOut(map_text),
            FadeOut(planner_box),
            FadeOut(planner_text),
            FadeOut(arrow)
        )

        loop = VGroup(
            Text(
                "Observe",
                font_size=28,
                color=BLUE
            ),
            Arrow(
                LEFT,
                RIGHT,
                buff=0.25
            ),
            Text(
                "Plan",
                font_size=28,
                color=PURPLE
            ),
            Arrow(
                LEFT,
                RIGHT,
                buff=0.25
            ),
            Text(
                "Act",
                font_size=28,
                color=GREEN
            ),
            Arrow(
                LEFT,
                RIGHT,
                buff=0.25
            ),
            Text(
                "Re-observe",
                font_size=28,
                color=ORANGE
            )
        ).arrange(
            RIGHT,
            buff=0.2
        ).scale(0.9)

        self.play(
            FadeIn(loop),
            run_time=1.7
        )

        self.wait(3)

        # ============================================================
        # AHA
        # ============================================================

        self.play(
            FadeOut(loop)
        )

        aha = VGroup(
            Text(
                "Language gives the robot",
                font_size=30,
                color=YELLOW
            ),
            Text(
                "a spatial objective.",
                font_size=37,
                color=PURPLE
            ),
            Text(
                "Planning turns that objective",
                font_size=30,
                color=GREEN
            ),
            Text(
                "into physical motion.",
                font_size=37,
                color=BLUE
            )
        ).arrange(
            DOWN,
            buff=0.17
        )

        self.play(
            LaggedStart(
                *[
                    FadeIn(
                        x,
                        shift=UP
                    )
                    for x in aha
                ],
                lag_ratio=0.2
            ),
            run_time=2.5
        )

        self.wait(4)

        final = Text(
            "That is the bridge VoxPoser builds between language and the physical world.",
            font_size=25,
            color=GRAY
        ).to_edge(
            DOWN,
            buff=0.65
        )

        self.play(
            Write(final),
            run_time=1.5
        )

        self.wait(5)