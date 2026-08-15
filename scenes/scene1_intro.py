from manim import *


class VoxPoserScene1(Scene):
    def construct(self):

        # ============================================================
        # COLORS
        # ============================================================

        BLUE_C1 = "#5DADE2"
        YELLOW_C1 = "#F4D03F"
        GREEN_C1 = "#58D68D"
        RED_C1 = "#EC7063"
        PURPLE_C1 = "#AF7AC5"
        GRAY_C1 = "#BFC9CA"

        # ============================================================
        # HELPER: TOP BAR
        # ============================================================

        def make_top_bar():
            # The line is intentionally lower than the logo
            # and starts to the right of it.
            line = Line(
                LEFT * 4.35,
                RIGHT * 6.2,
                stroke_width=1.5,
                color=GRAY_C1
            )

            line.move_to(
                UP * 3.30
            )

            return line

        # ============================================================
        # PART 1 — OPENING TITLE
        # ============================================================

        title = Text(
            "VoxPoser",
            font_size=58,
            color=BLUE_C1
        )

        subtitle = Text(
            "From Language to Robot Motion",
            font_size=30,
            color=WHITE
        )

        paper_title = Text(
            "Composable 3D Value Maps for Robotic Manipulation",
            font_size=21,
            color=GRAY_C1
        )

        opening = VGroup(
            title,
            subtitle,
            paper_title
        ).arrange(
            DOWN,
            buff=0.25
        )

        self.play(
            FadeIn(title, shift=UP),
            FadeIn(subtitle, shift=UP),
            FadeIn(paper_title, shift=UP),
            run_time=2
        )

        self.wait(2)

        # Move title to small corner title
        mini = Text(
            "VoxPoser",
            font_size=27,
            color=BLUE_C1
        ).to_corner(
            UL,
            buff=0.28
        )

        self.play(
            Transform(title, mini),
            FadeOut(subtitle),
            FadeOut(paper_title),
            run_time=1
        )

        top_bar = make_top_bar()

        self.play(
            FadeIn(top_bar),
            run_time=0.5
        )

        self.wait(1)

        # ============================================================
        # PART 2 — THE HUMAN INSTRUCTION
        # ============================================================

        instruction_label = Text(
            "A human gives the robot a simple instruction.",
            font_size=28,
            color=GRAY_C1
        ).to_edge(
            UP,
            buff=1.35
        )

        command_box = RoundedRectangle(
            corner_radius=0.18,
            width=9.0,
            height=1.45,
            color=YELLOW_C1,
            fill_color=YELLOW_C1,
            fill_opacity=0.08,
            stroke_width=2
        )

        command = Text(
            '"Close the top drawer."',
            font_size=40,
            color=YELLOW_C1
        )

        command.move_to(command_box)

        command_group = VGroup(
            command_box,
            command
        )

        # Move the whole command block upward.
        # This creates more room for the question list below
        # and keeps subtitles away from the content.
        command_group.move_to(
            UP * 0.95
        )

        self.play(
            Write(instruction_label),
            Create(command_box),
            Write(command),
            run_time=2
        )

        self.wait(2)

        # ============================================================
        # PART 3 — WHY THIS IS NOT TRIVIAL
        # ============================================================

        question = Text(
            "To execute it, the robot must answer several questions.",
            font_size=27,
            color=WHITE
        )

        question.next_to(
            command_group,
            DOWN,
            buff=0.32
        )

        self.play(
            Write(question),
            run_time=1.2
        )

        # Slightly smaller and more compact than before.
        # The lower part of the frame is intentionally kept free
        # for subtitles.
        questions = VGroup(
            Text(
                "Which object?",
                font_size=23,
                color=BLUE_C1
            ),
            Text(
                "Which part?",
                font_size=23,
                color=PURPLE_C1
            ),
            Text(
                "Where should the gripper go?",
                font_size=23,
                color=GREEN_C1
            ),
            Text(
                "How should the robot move?",
                font_size=23,
                color=YELLOW_C1
            ),
            Text(
                "What should it avoid?",
                font_size=23,
                color=RED_C1
            )
        ).arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.13
        )

        questions.next_to(
            question,
            DOWN,
            buff=0.18
        )

        # Slight upward adjustment for subtitle-safe composition.
        questions.shift(
            UP * 0.10
        )

        self.play(
            LaggedStart(
                *[
                    FadeIn(q, shift=RIGHT)
                    for q in questions
                ],
                lag_ratio=0.18
            ),
            run_time=2.5
        )

        self.wait(2.5)

        # ============================================================
        # PART 4 — TRADITIONAL ROBOTICS
        # ============================================================

        self.play(
            FadeOut(instruction_label),
            FadeOut(command_group),
            FadeOut(question),
            FadeOut(questions)
        )

        trad_title = Text(
            "Traditional robotics",
            font_size=32,
            color=RED_C1
        ).to_edge(
            UP,
            buff=1.4
        )

        self.play(
            Write(trad_title)
        )

        # ------------------------------------------------------------
        # Three large boxes
        # ------------------------------------------------------------

        box1 = RoundedRectangle(
            width=3.5,
            height=1.2,
            color=GRAY_C1,
            fill_opacity=0.08
        )

        box2 = RoundedRectangle(
            width=3.5,
            height=1.2,
            color=GRAY_C1,
            fill_opacity=0.08
        )

        box3 = RoundedRectangle(
            width=3.5,
            height=1.2,
            color=GRAY_C1,
            fill_opacity=0.08
        )

        txt1 = Text(
            "Task-specific\nprogramming",
            font_size=24
        ).move_to(box1)

        txt2 = Text(
            "Hand-designed\nmotion",
            font_size=24
        ).move_to(box2)

        txt3 = Text(
            "Robot\nexecution",
            font_size=24
        ).move_to(box3)

        b1 = VGroup(
            box1,
            txt1
        )

        b2 = VGroup(
            box2,
            txt2
        )

        b3 = VGroup(
            box3,
            txt3
        )

        boxes = VGroup(
            b1,
            b2,
            b3
        ).arrange(
            RIGHT,
            buff=0.65
        )

        arrows = VGroup(
            Arrow(
                b1.get_right(),
                b2.get_left(),
                buff=0.12,
                color=GRAY_C1
            ),
            Arrow(
                b2.get_right(),
                b3.get_left(),
                buff=0.12,
                color=GRAY_C1
            )
        )

        self.play(
            FadeIn(b1),
            run_time=0.8
        )

        self.play(
            GrowArrow(arrows[0]),
            FadeIn(b2),
            run_time=0.8
        )

        self.play(
            GrowArrow(arrows[1]),
            FadeIn(b3),
            run_time=0.8
        )

        self.wait(1.5)

        warning = Text(
            "Change the task or object → the solution often needs to be redesigned.",
            font_size=25,
            color=RED_C1
        ).to_edge(
            DOWN,
            buff=0.9
        )

        self.play(
            Write(warning),
            run_time=1.3
        )

        self.wait(2.5)

        # ============================================================
        # PART 5 — THE VOXPOSER QUESTION
        # ============================================================

        self.play(
            FadeOut(trad_title),
            FadeOut(boxes),
            FadeOut(arrows),
            FadeOut(warning)
        )

        main_question = Text(
            "VoxPoser asks a different question:",
            font_size=32,
            color=GREEN_C1
        ).to_edge(
            UP,
            buff=1.5
        )

        question1 = Text(
            "Can language describe",
            font_size=34,
            color=WHITE
        )

        question2 = Text(
            "what matters in 3D space?",
            font_size=42,
            color=YELLOW_C1
        )

        question_group = VGroup(
            question1,
            question2
        ).arrange(
            DOWN,
            buff=0.2
        )

        self.play(
            Write(main_question),
            FadeIn(question1, shift=UP),
            FadeIn(question2, shift=UP),
            run_time=2
        )

        self.wait(2)

        # ============================================================
        # PART 6 — CORE BRIDGE
        # ============================================================

        self.play(
            FadeOut(main_question),
            FadeOut(question_group)
        )

        lang_box = RoundedRectangle(
            width=2.7,
            height=1.3,
            color=YELLOW_C1,
            fill_opacity=0.08
        )

        llm_box = RoundedRectangle(
            width=2.5,
            height=1.3,
            color=GREEN_C1,
            fill_opacity=0.08
        )

        map_box = RoundedRectangle(
            width=2.7,
            height=1.3,
            color=PURPLE_C1,
            fill_opacity=0.08
        )

        robot_box = RoundedRectangle(
            width=2.5,
            height=1.3,
            color=RED_C1,
            fill_opacity=0.08
        )

        # Slightly narrower spacing to keep everything inside screen
        lang_box.move_to(LEFT * 4.0)
        llm_box.move_to(LEFT * 1.35)
        map_box.move_to(RIGHT * 1.35)
        robot_box.move_to(RIGHT * 4.0)

        lang_text = Text(
            "Language",
            font_size=25,
            color=YELLOW_C1
        ).move_to(lang_box)

        llm_text = Text(
            "LLM\nreasoning",
            font_size=24,
            color=GREEN_C1
        ).move_to(llm_box)

        map_text = Text(
            "3D value\nmaps",
            font_size=24,
            color=PURPLE_C1
        ).move_to(map_box)

        robot_text = Text(
            "Robot\nmotion",
            font_size=24,
            color=RED_C1
        ).move_to(robot_box)

        boxes = VGroup(
            lang_box,
            llm_box,
            map_box,
            robot_box
        )

        texts = VGroup(
            lang_text,
            llm_text,
            map_text,
            robot_text
        )

        arrows = VGroup(
            Arrow(
                lang_box.get_right(),
                llm_box.get_left(),
                buff=0.15,
                color=WHITE
            ),
            Arrow(
                llm_box.get_right(),
                map_box.get_left(),
                buff=0.15,
                color=WHITE
            ),
            Arrow(
                map_box.get_right(),
                robot_box.get_left(),
                buff=0.15,
                color=WHITE
            )
        )

        self.play(
            FadeIn(lang_box),
            Write(lang_text),
            run_time=0.8
        )

        self.play(
            GrowArrow(arrows[0]),
            FadeIn(llm_box),
            Write(llm_text),
            run_time=0.8
        )

        self.play(
            GrowArrow(arrows[1]),
            FadeIn(map_box),
            Write(map_text),
            run_time=0.8
        )

        self.play(
            GrowArrow(arrows[2]),
            FadeIn(robot_box),
            Write(robot_text),
            run_time=0.8
        )

        self.wait(2)

        # ============================================================
        # PART 7 — WHAT WE WILL EXPLAIN
        # ============================================================

        self.play(
            FadeOut(boxes),
            FadeOut(texts),
            FadeOut(arrows)
        )

        summary_title = Text(
            "The central idea of VoxPoser",
            font_size=34,
            color=BLUE_C1
        ).to_edge(
            UP,
            buff=1.4
        )

        summary = VGroup(
            Text(
                "1. Interpret the instruction",
                font_size=26
            ),
            Text(
                "2. Ground it into 3D space",
                font_size=26
            ),
            Text(
                "3. Build and compose value maps",
                font_size=26
            ),
            Text(
                "4. Plan a robot trajectory",
                font_size=26
            ),
            Text(
                "5. Re-plan when the world changes",
                font_size=26
            )
        ).arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.25
        )

        summary.move_to(ORIGIN)
        summary.shift(DOWN * 0.15)

        self.play(
            Write(summary_title),
            LaggedStart(
                *[
                    FadeIn(
                        item,
                        shift=RIGHT
                    )
                    for item in summary
                ],
                lag_ratio=0.2
            ),
            run_time=2.5
        )

        self.wait(2.5)

        # Highlight the central value-map idea
        highlight_box = SurroundingRectangle(
            summary[2],
            color=PURPLE_C1,
            buff=0.12,
            stroke_width=2
        )

        self.play(
            Create(highlight_box),
            run_time=0.8
        )

        self.wait(1.5)

        # ============================================================
        # OUTRO
        # ============================================================

        outro = Text(
            "Let's see how language becomes a physical trajectory.",
            font_size=28,
            color=YELLOW_C1
        ).to_edge(
            DOWN,
            buff=0.8
        )

        self.play(
            Write(outro),
            run_time=1.2
        )

        self.wait(3)

        self.play(
            FadeOut(highlight_box),
            FadeOut(outro),
            run_time=0.8
        )