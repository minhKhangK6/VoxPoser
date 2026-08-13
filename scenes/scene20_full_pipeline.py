from manim import *


class VoxPoserScene20(Scene):
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
            "VoxPoser: The Entire Idea in One Run",
            font_size=38,
            color=BLUE
        ).to_edge(UP, buff=0.45)

        self.play(Write(title))
        self.wait(1)

        # ============================================================
        # STEP 1
        # ============================================================

        prompt = RoundedRectangle(
            width=3.0,
            height=1.1,
            color=YELLOW,
            fill_opacity=0.08
        ).move_to(LEFT * 5)

        prompt_text = Text(
            '"Close the\ntop drawer"',
            font_size=23,
            color=YELLOW
        ).move_to(prompt)

        self.play(
            FadeIn(prompt),
            Write(prompt_text)
        )

        self.wait(1.5)

        # ============================================================
        # STEP 2
        # ============================================================

        llm = RoundedRectangle(
            width=2.8,
            height=1.1,
            color=GREEN,
            fill_opacity=0.08
        ).move_to(LEFT * 2.4)

        llm_text = Text(
            "LLM / VLM",
            font_size=24,
            color=GREEN
        ).move_to(llm)

        a1 = Arrow(
            prompt.get_right(),
            llm.get_left(),
            buff=0.1
        )

        self.play(
            GrowArrow(a1),
            FadeIn(llm),
            Write(llm_text),
            run_time=1
        )

        self.wait(1.5)

        # ============================================================
        # STEP 3
        # ============================================================

        maps = RoundedRectangle(
            width=3.0,
            height=1.1,
            color=PURPLE,
            fill_opacity=0.08
        ).move_to(RIGHT * 0.2)

        maps_text = Text(
            "3D value\nmaps",
            font_size=23,
            color=PURPLE
        ).move_to(maps)

        a2 = Arrow(
            llm.get_right(),
            maps.get_left(),
            buff=0.1
        )

        self.play(
            GrowArrow(a2),
            FadeIn(maps),
            Write(maps_text),
            run_time=1
        )

        self.wait(1.5)

        # ============================================================
        # STEP 4
        # ============================================================

        planner = RoundedRectangle(
            width=3.0,
            height=1.1,
            color=RED,
            fill_opacity=0.08
        ).move_to(RIGHT * 2.9)

        planner_text = Text(
            "Motion\nplanner",
            font_size=23,
            color=RED
        ).move_to(planner)

        a3 = Arrow(
            maps.get_right(),
            planner.get_left(),
            buff=0.1
        )

        self.play(
            GrowArrow(a3),
            FadeIn(planner),
            Write(planner_text),
            run_time=1
        )

        self.wait(1.5)

        # ============================================================
        # STEP 5
        # ============================================================

        robot = RoundedRectangle(
            width=2.6,
            height=1.1,
            color=BLUE,
            fill_opacity=0.08
        ).move_to(RIGHT * 5.2)

        robot_text = Text(
            "Robot",
            font_size=25,
            color=BLUE
        ).move_to(robot)

        a4 = Arrow(
            planner.get_right(),
            robot.get_left(),
            buff=0.1
        )

        self.play(
            GrowArrow(a4),
            FadeIn(robot),
            Write(robot_text),
            run_time=1
        )

        self.wait(2)

        # ============================================================
        # VALUE MAP DETAIL
        # ============================================================

        self.play(
            FadeOut(prompt),
            FadeOut(prompt_text),
            FadeOut(llm),
            FadeOut(llm_text),
            FadeOut(maps),
            FadeOut(maps_text),
            FadeOut(planner),
            FadeOut(planner_text),
            FadeOut(robot),
            FadeOut(robot_text),
            FadeOut(a1),
            FadeOut(a2),
            FadeOut(a3),
            FadeOut(a4)
        )

        detail_title = Text(
            "What happens inside the value-map stage?",
            font_size=30,
            color=PURPLE
        )

        self.play(
            Write(detail_title)
        )

        self.wait(1.5)

        detail = VGroup(
            Text(
                "Affordance",
                font_size=26,
                color=GREEN
            ),
            Text(
                "Avoidance",
                font_size=26,
                color=RED
            ),
            Text(
                "Rotation",
                font_size=26,
                color=PURPLE
            ),
            Text(
                "Velocity",
                font_size=26,
                color=ORANGE
            ),
            Text(
                "Gripper",
                font_size=26,
                color=YELLOW
            )
        ).arrange(
            RIGHT,
            buff=0.32
        ).scale(0.9).to_edge(
            DOWN,
            buff=1.0
        )

        self.play(
            LaggedStart(
                *[
                    FadeIn(x, shift=UP)
                    for x in detail
                ],
                lag_ratio=0.15
            ),
            run_time=2.2
        )

        self.wait(2.5)

        # ============================================================
        # CLOSED LOOP
        # ============================================================

        self.play(
            FadeOut(detail_title),
            FadeOut(detail)
        )

        loop = VGroup(
            Text("Observe", font_size=25, color=BLUE),
            Arrow(LEFT, RIGHT, buff=0.25),
            Text("Plan", font_size=25, color=PURPLE),
            Arrow(LEFT, RIGHT, buff=0.25),
            Text("Execute", font_size=25, color=GREEN),
            Arrow(LEFT, RIGHT, buff=0.25),
            Text("Re-observe", font_size=25, color=ORANGE)
        ).arrange(
            RIGHT,
            buff=0.18
        ).scale(0.84)

        self.play(
            FadeIn(loop),
            run_time=1.6
        )

        self.wait(2)

        loop_note = Text(
            "The loop repeats as the world changes.",
            font_size=27,
            color=BLUE
        ).to_edge(
            DOWN,
            buff=0.8
        )

        self.play(
            Write(loop_note),
            run_time=1.2
        )

        self.wait(4)

        # ============================================================
        # FINAL MESSAGE
        # ============================================================

        self.play(
            FadeOut(loop),
            FadeOut(loop_note)
        )

        final = VGroup(
            Text(
                "Language provides the meaning.",
                font_size=28,
                color=YELLOW
            ),
            Text(
                "Value maps provide the geometry.",
                font_size=28,
                color=PURPLE
            ),
            Text(
                "Planning provides the motion.",
                font_size=28,
                color=RED
            ),
            Text(
                "Feedback provides the adaptation.",
                font_size=28,
                color=GREEN
            )
        ).arrange(
            DOWN,
            buff=0.3
        )

        self.play(
            LaggedStart(
                *[
                    FadeIn(x, shift=UP)
                    for x in final
                ],
                lag_ratio=0.18
            ),
            run_time=2.2
        )

        self.wait(4)