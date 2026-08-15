from manim import *


class VoxPoserScene11(Scene):
    def construct(self):

        # ============================================================
        # COLORS
        # ============================================================

        BLUE = "#5DADE2"
        GREEN = "#58D68D"
        YELLOW = "#F4D03F"
        ORANGE = "#F5B041"
        RED = "#EC7063"
        PURPLE = "#AF7AC5"
        GRAY = "#BFC9CA"

        # ============================================================
        # TITLE
        # ============================================================

        title = Text(
            "Behavioral Commonsense Reasoning",
            font_size=36,
            color=BLUE
        ).to_edge(
            UP,
            buff=0.45
        )

        self.play(
            Write(title)
        )

        self.wait(1)

        # ============================================================
        # STATE 1 — TASK + TABLE ILLUSTRATION
        # ============================================================

        task = Text(
            "Task: Set the table",
            font_size=30,
            color=YELLOW
        ).to_edge(
            UP,
            buff=1.35
        )

        self.play(
            Write(task),
            run_time=1
        )

        self.wait(1.5)

        # ------------------------------------------------------------
        # TABLE
        # ------------------------------------------------------------

        table = Rectangle(
            width=8.0,
            height=3.4,
            color=GRAY,
            fill_opacity=0.06,
            stroke_width=2
        ).move_to(
            DOWN * 0.55
        )

        # Bowl on the table
        bowl = Circle(
            radius=0.6,
            color=BLUE,
            fill_opacity=0.15
        ).move_to(
            LEFT * 0.75 + DOWN * 0.2
        )

        bowl_label = Text(
            "bowl",
            font_size=20,
            color=BLUE
        ).next_to(
            bowl,
            DOWN,
            buff=0.12
        )

        # Fork on the right
        fork_right = Line(
            RIGHT * 1.5 + DOWN * 0.2,
            RIGHT * 2.25 + DOWN * 0.2,
            color=PURPLE,
            stroke_width=7
        )

        fork_right_label = Text(
            "fork",
            font_size=20,
            color=PURPLE
        ).next_to(
            fork_right,
            DOWN,
            buff=0.12
        )

        table_group = VGroup(
            table,
            bowl,
            bowl_label,
            fork_right,
            fork_right_label
        )

        self.play(
            Create(table),
            FadeIn(bowl),
            Write(bowl_label),
            Create(fork_right),
            Write(fork_right_label),
            run_time=1.8
        )

        self.wait(2)

        # ============================================================
        # STATE 2 — USER PREFERENCE
        # ============================================================

        # Hide the visual scene before showing the sentence.
        self.play(
            FadeOut(table_group),
            FadeOut(task),
            run_time=0.8
        )

        preference = Text(
            '"I am left-handed."',
            font_size=36,
            color=ORANGE
        )

        self.play(
            FadeIn(preference, scale=0.9),
            run_time=1.2
        )

        self.wait(2.5)

        # ============================================================
        # STATE 3 — RE-INTRODUCE THE SCENE FOR THE ACTION
        # ============================================================

        # Hide the sentence before returning to the visual example.
        self.play(
            FadeOut(preference),
            run_time=0.6
        )

        action_title = Text(
            "The preference changes the placement.",
            font_size=28,
            color=GREEN
        ).to_edge(
            UP,
            buff=1.35
        )

        self.play(
            Write(action_title),
            run_time=1
        )

        # Recreate the table
        action_table = Rectangle(
            width=8.0,
            height=3.4,
            color=GRAY,
            fill_opacity=0.06,
            stroke_width=2
        ).move_to(
            DOWN * 0.65
        )

        action_bowl = Circle(
            radius=0.6,
            color=BLUE,
            fill_opacity=0.15
        ).move_to(
            LEFT * 0.75 + DOWN * 0.3
        )

        action_bowl_label = Text(
            "bowl",
            font_size=20,
            color=BLUE
        ).next_to(
            action_bowl,
            DOWN,
            buff=0.12
        )

        # Original fork position
        fork_original = Line(
            RIGHT * 1.5 + DOWN * 0.3,
            RIGHT * 2.25 + DOWN * 0.3,
            color=PURPLE,
            stroke_width=7
        )

        fork_original_label = Text(
            "fork",
            font_size=20,
            color=PURPLE
        ).next_to(
            fork_original,
            DOWN,
            buff=0.12
        )

        # New fork position
        fork_new = fork_original.copy().shift(
            LEFT * 3.0
        )

        fork_new_label = Text(
            "fork",
            font_size=20,
            color=GREEN
        ).next_to(
            fork_new,
            DOWN,
            buff=0.12
        )

        self.play(
            Create(action_table),
            FadeIn(action_bowl),
            Write(action_bowl_label),
            Create(fork_original),
            Write(fork_original_label),
            run_time=1.5
        )

        self.wait(1)

        # ============================================================
        # FORK MOVEMENT
        # ============================================================

        move_arrow = Arrow(
            fork_original.get_center(),
            fork_new.get_center(),
            color=GREEN,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.12,
            buff=0.08
        )

        move_label = Text(
            "adjust placement for the user",
            font_size=23,
            color=GREEN
        ).to_edge(
            DOWN,
            buff=0.55
        )

        self.play(
            GrowArrow(move_arrow),
            Write(move_label),
            run_time=1.2
        )

        self.wait(1)

        self.play(
            Transform(
                fork_original,
                fork_new
            ),
            FadeOut(fork_original_label),
            FadeIn(fork_new_label),
            run_time=1.5
        )

        self.wait(2)

        # ============================================================
        # STATE 4 — CONCLUSION
        # ============================================================

        self.play(
            FadeOut(action_table),
            FadeOut(action_bowl),
            FadeOut(action_bowl_label),
            FadeOut(fork_original),
            FadeOut(fork_new_label),
            FadeOut(move_arrow),
            FadeOut(action_title),
            FadeOut(move_label),
            run_time=0.8
        )

        result = Text(
            "The robot changes the placement —\n"
            "without retraining a new task.",
            font_size=29,
            color=GREEN
        )

        self.play(
            FadeIn(result, shift=UP),
            run_time=1.3
        )

        self.wait(4)