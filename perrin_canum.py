# CANUM22 presentation
# Lucas Perrin - INRIA Paris - LJLL
# lucas.perrin@inria.fr / lucas.perrin@dauphine.eu
# June 2022
#
# ==============================
# /!\ abstract is at the end /!\
# ==============================
#
# This presentation was done using Manim :
# The Manim Community Developers. (2022). Manim – Mathematical Animation Framework (Version v0.15.2) [Computer software]. https://www.manim.community/
#
#
# personal notes for the repository and command lines to execute :
#
# cd Documents/presentations/canum
# manim -pql perrin_canum.py
# manim --save_sections perrin_canum.py
# manedit
#
# python3 -m http.server

from manim import *
from manim_editor import PresentationSectionType

# =======================
# GENERAL COLOR MANAGMENT
# =======================

# 1 for white background and black text
# 0 for the usual manim style
black_and_white = 1

# plot a grid to have some coordinates to place easily MObjects
grid            = 0

if black_and_white == 1:
    FRONT_COLOR = BLACK
    BACK_COLOR = "#f6f3f1" # WHITE
    RED = "#ff0000"
    BLUE = "#0000ff"
    GREEN = "#2fa222"
    DEMARK_COLOR = '#FF00FF'
    BROWN = '#f56e0f'
    config.background_color = BACK_COLOR
else:
    FRONT_COLOR = WHITE
    BACK_COLOR = BLACK
    DEMARK_COLOR = YELLOW
    BROWN = '#e17223'

OBS_COLOR = RED
STATE_COLOR = BLUE

# ==============================================
# INTRODUCTION SCENE
# Names, Lab, etc...
# ==============================================

class A_Intro(Scene):
    def construct(self):

        # ===============
        # COLOR MANAGMENT
        # ===============

        Tex.set_default(color = FRONT_COLOR,font_size = 30)
        MathTex.set_default(color = FRONT_COLOR,font_size = 30)
        Mobject.set_default(color = FRONT_COLOR)

        # ===============
        # GRID FOR CONSTRUCTION PURPUSE ONLY
        # ===============

        L1 = Line(start=[- 7.1, 0., 0.], end=[7.1, 0., 0.],stroke_opacity =0.2)
        for i in range(-3,4):
            L1 = VGroup(L1,Line(start=[- 7.1, i, 0.], end=[7.1, i, 0.],stroke_opacity =0.1))

        L2 = Line(start=[0., -4., 0.], end=[0., 4., 0.],stroke_opacity =0.2)
        for i in range(-6,7):
            L2 = VGroup(L2,Line(start=[i, -4., 0.], end=[i, 4., 0.],stroke_opacity =0.1))

        if grid == 1 :
            self.add(L1,L2)

        # ===============
        # TITLE
        # ===============

        pres_title = Tex("Time parallelisation for data assimilation",font_size=48)
        pres_subtitle = Tex("Paraexp and Luenberger observer",font_size=30)
        author_1_tex = Tex("Lucas Perrin",font_size=30)
        author_1_ul = Underline(author_1_tex,buff=0.1)
        author_1 = VGroup(author_1_tex,author_1_ul)
        author_2 = Tex("Julien Salomon",font_size=30)
        team = Tex("INRIA Paris, ANGE Team / Laboratoire Jacques-Louis Lions", font_size=25)
        date = Tex("30 Mai 2022",font_size=25)

        #logo_canum = ImageMobject("logos/canum_logo.png").scale(0.8).move_to([0,3.1,0])

        title_intro = VGroup(pres_title,pres_subtitle).arrange(DOWN).move_to([0,1.5,0])
        infos = VGroup(author_1,author_2,team,date).arrange(DOWN,buff=0.3).move_to([0,-0.5,0])

        logo_cnrs = ImageMobject("logos/logo_cnrs.png").scale(0.15)
        logo_su   = ImageMobject("logos/logo_su.png").scale(0.4)
        if black_and_white == 1:
            logo_inr = ImageMobject("logos/inr_logo_grisbleu.png").scale(0.4)
        else:
            logo_inr = ImageMobject("logos/inr_logo_blanc.png").scale(0.4)

        logo_cnrs.move_to([-3,-2.8,0])
        logo_su.move_to([0,-2.8,0])
        logo_inr.move_to([3,-2.8,0])

        logos = Group(logo_cnrs,logo_inr,logo_su)

        ## ANIM

        ## == SLIDE ==
        self.next_section('INTRO',PresentationSectionType.NORMAL)
        self.play(
            Write(title_intro),
            #FadeIn(logo_canum),
        )
        self.wait(0.5)
        self.play(
            FadeIn(logos),
            FadeIn(infos),
        )

        self.wait(0.5)
        self.next_section('INTRO.1',PresentationSectionType.SUB_SKIP)
        self.play(
            FadeOut(infos),
            FadeOut(logos),
            #FadeOut(logo_emrsim),
            FadeOut(pres_subtitle),
        )

        self.wait(0.1)

# ==============================================
# SUMMARY SCENE
# Explain what will be talked about
# ==============================================

class B_Summary(Scene):
    def construct(self):

        # ===============
        # COLOR MANAGMENT
        # ===============

        Tex.set_default(color = FRONT_COLOR,font_size = 30)
        MathTex.set_default(color = FRONT_COLOR,font_size = 30)
        Mobject.set_default(color = FRONT_COLOR)

        # ===============
        # GRID FOR CONSTRUCTION PURPUSE ONLY
        # ===============

        L1 = Line(start=[- 7.1, 0., 0.], end=[7.1, 0., 0.],stroke_opacity =0.2)
        for i in range(-3,4):
            L1 = VGroup(L1,Line(start=[- 7.1, i, 0.], end=[7.1, i, 0.],stroke_opacity =0.1))

        L2 = Line(start=[0., -4., 0.], end=[0., 4., 0.],stroke_opacity =0.2)
        for i in range(-6,7):
            L2 = VGroup(L2,Line(start=[i, -4., 0.], end=[i, 4., 0.],stroke_opacity =0.1))

        if grid == 1 :
            self.add(L1,L2)

        # ===============
        # REPEAT
        # ===============

        pres_title = Tex("Time parallelisation for data assimilation",font_size=48)
        pres_subtitle = Tex("Paraexp and Luenberger observer",font_size=30)
        title_intro = VGroup(pres_title,pres_subtitle).arrange(DOWN).move_to([0,1.5,0])
        self.add(pres_title)

        step_one   = Tex(r"$\rightarrow$"," Present a sequential data assimilation : the Luenberger observer").shift(UP)
        step_two   = Tex(r"$\rightarrow$"," Explain the parallel in time scheme used : Paraexp").align_to(step_one,LEFT)
        step_three = Tex(r"$\rightarrow$"," Expose our PinT method for sequential data assimilation").align_to(step_two,LEFT).shift(DOWN)
        steps      = VGroup(step_one,step_two,step_three).scale(1.2).shift(0.5*DOWN)

        ## ANIM

        ## == SLIDE == (AUTO)
        self.next_section('SUMMARY',PresentationSectionType.SKIP)
        self.play(pres_title.animate.to_edge(UP).scale(40/48))
        underline = Line(6*LEFT, 6*RIGHT,color=FRONT_COLOR).next_to(pres_title, DOWN, buff=MED_SMALL_BUFF)
        self.play(Create(underline))
        self.wait(0.1)

        ## == SLIDE ==
        self.next_section('SUMMARY.1',PresentationSectionType.SUB_NORMAL)
        self.play(Write(step_one))
        self.play(Write(step_two))
        self.play(Write(step_three))
        self.wait(0.5)

        ## == SLIDE ==
        self.next_section('SUMMARY.2',PresentationSectionType.SUB_SKIP)
        self.play(FadeOut(VGroup(underline,pres_title)),FadeOut(step_one),FadeOut(step_two),FadeOut(step_three,))
        self.wait(0.2)

# ==============================================
# ASSIMILATION SCENE
# Present the Luenberger observer
# ==============================================

class C_Assimilation_2_1(Scene):
    def construct(self):

        # ===============
        # COLOR MANAGMENT
        # ===============

        Tex.set_default(color = FRONT_COLOR,font_size = 30)
        MathTex.set_default(color = FRONT_COLOR,font_size = 30)
        Mobject.set_default(color = FRONT_COLOR)

        # ===============
        # GRID FOR CONSTRUCTION PURPUSE ONLY
        # ===============

        L1 = Line(start=[- 7.1, 0., 0.], end=[7.1, 0., 0.],stroke_opacity =0.2)
        for i in range(-3,4):
            L1 = VGroup(L1,Line(start=[- 7.1, i, 0.], end=[7.1, i, 0.],stroke_opacity =0.1))

        L2 = Line(start=[0., -4., 0.], end=[0., 4., 0.],stroke_opacity =0.2)
        for i in range(-6,7):
            L2 = VGroup(L2,Line(start=[i, -4., 0.], end=[i, 4., 0.],stroke_opacity =0.1))

        if grid == 1 :
            self.add(L1,L2)

        # ===============
        # TITLE
        # ===============

        title = Title("Data assimilation : Luenberger observer \& dynamical systems",font_size=40)

        # ===============
        # STATE SYSTEM
        # ===============

        state_tt    = Tex("state dynamical system : ",font_size = 30).move_to([-3.5,2.3,0])

        state_eq_1  = MathTex("\dot{x}","=A","x(t)"," + B u(t)",font_size = 30)
        state_eq_1.set_color_by_tex('x', STATE_COLOR)

        state_eq_2  = MathTex("y(t) = C","x(t)",font_size = 30)
        state_eq_2.set_color_by_tex('x', STATE_COLOR).align_to(state_eq_1,LEFT).shift(0.5*DOWN)

        state_eq_3  = MathTex("x(0)","=","x_{0}",", \quad t \geq 0",font_size = 30)
        state_eq_3.set_color_by_tex('x', STATE_COLOR).align_to(state_eq_1,LEFT).shift(DOWN)

        state_eq    = VGroup(VGroup(state_eq_1,state_eq_2,state_eq_3)).move_to([-3.5,1.25,0])
        brace1      = Brace(state_eq,LEFT)

        state_blist = VGroup(
            Tex(r"$\rightarrow$ ",r"$x(t)$",r" : \textit{state}",r" vector").set_color_by_tex('x', STATE_COLOR),
            Tex(r"$\rightarrow$ ",r"$y(t)$ : \textit{output} vector"),
            Tex(r"$\rightarrow$ ",r"$A \in \mathcal{M}_{m \times m}(\mathbb{R})$,\\     $B \in \mathcal{M}_{m \times p}(\mathbb{R})$,\\    $C \in \mathcal{M}_{q \times m}(\mathbb{R})$"),
            Tex(r"$\rightarrow$ ",r"$x_0$",r" is ",r"unknown").set_color_by_tex('x', STATE_COLOR).set_color_by_tex('unk', DEMARK_COLOR),
        ).arrange_in_grid(cols=1,col_alignments="l",buff=0.1).move_to([-3.5,-1,0])

        # ===============
        # OBSERVER SYSTEM
        # ===============

        observer_tt = Tex("observer system : ",font_size = 30).move_to([3.5,2.3,0])

        L_tex = MathTex(r"L",font_size = 30)

        obs_eq_1  = MathTex("\dot{\hat{x}}(t)","=A","\hat{x}(t)","+B u(t)+L[y(t)-\hat{y}(t)]",font_size = 30)
        obs_eq_1.set_color_by_tex('x', OBS_COLOR)

        obs_eq_1  = VGroup(
        MathTex("\dot{\hat{x}}(t)","=A","\hat{x}(t)","+B u(t)+").set_color_by_tex('x', OBS_COLOR),
        L_tex,
        MathTex("[y(t)-\hat{y}(t)]"),
        ).arrange(buff=0.05)


        obs_eq_2  = MathTex("\hat{y}(t)=C","\hat{x}(t)",font_size = 30)
        obs_eq_2.set_color_by_tex('x', OBS_COLOR).align_to(obs_eq_1,LEFT).shift(0.5*DOWN)

        obs_eq_3  = MathTex("\hat{x}(0)","=","\hat{x}_{0}",", \quad t \geq 0",font_size = 30)
        obs_eq_3.set_color_by_tex('x', OBS_COLOR).align_to(obs_eq_1,LEFT).shift(DOWN)

        obs_eq    = VGroup(VGroup(obs_eq_1,obs_eq_2,obs_eq_3)).move_to([3.5,1.25,0])
        brace2    = Brace(obs_eq,LEFT)

        obs_blist = VGroup(
            Tex(r"$\rightarrow$ ",r"$\hat{x}(t)$",r" : \textit{observer}",r" vector").set_color_by_tex('x', OBS_COLOR),
            Tex(r"$\rightarrow$ ",r"$L \in \mathcal{M}_{m \times q}(\mathbb{R})$"),
            Tex(r"$\rightarrow$ ",r"$\hat{x}_0$",r" chosen as we want").set_color_by_tex('x', OBS_COLOR),
        ).arrange_in_grid(cols=1,col_alignments="l",buff=0.1).move_to([3.5,-1,0])

        # ===============
        # ERROR EQUATION
        # ===============

        error_1 = MathTex("\dot{x}(t)","-","\dot{\hat{x}}","(t)","=","(A-LC)","(","x(","t",")","-\hat{x}","(","t",")",")",
            font_size = 35,
        ).move_to([0,-2.6,0])

        error_2 = MathTex("x(t)","-","\hat{x}","(t)","=","\mathrm{e}^{","(A-LC)","t}","(","x(","0",")","-\hat{x}","(","0",")",")",
            font_size = 35,
        ).move_to([0,-2.6,0])

        error_3 = MathTex("\epsilon(t)","=","\mathrm{e}^{","(A-LC)","t}","(","x(","0",")","-\hat{x}","(","0",")",")",
            font_size = 35,
        ).move_to([0,-2.6,0])

        error_3_i = MathTex("\epsilon(t)","=","\mathrm{e}^{","(A-LC)","t}","(","x","(0)","-\hat{x}","(0)",")",
            font_size = 35,
        ).move_to([0,-2.6,0])

        error_4 = MathTex("\lVert","\epsilon(t)","\lVert","=","\lVert","\mathrm{e}^{","(A-LC)","t}","\epsilon","(0)","\lVert",
            font_size = 35,
        ).move_to([0,-2.6,0])

        error_5 = MathTex("\lVert","\epsilon(t)","\lVert",
            "=","\lVert","\mathrm{e}^{","(A-LC)","t}","\epsilon","(0)","\lVert",
            "\leq","\lVert x(0)-\hat{x}(0) \lVert \cdot \kappa(X) \cdot \mathrm{e}^{-\mu t}",
            font_size = 30,
        ).move_to([0,-2.6,0]).set_color_by_tex("x",DEMARK_COLOR)

        explain_error_5 = VGroup(
            Tex(r"$\rightarrow$ ",r"$\mu = \min\{|\Lambda|\}$"),
            Tex(r"$\rightarrow$ ",r"$X =$ e.v. of $A-LC$"),
        ).arrange_in_grid(cols=1,col_alignments="l").move_to([5.2,-2.8,0])

        box_error = SurroundingRectangle(error_2, color = DEMARK_COLOR, buff = 0.2, corner_radius = 0.2)

        ## ANIM

        ## == SLIDE == (SKIP)
        self.next_section('ASSIMILATION_1',PresentationSectionType.NORMAL)

        self.play(Write(title))
        self.wait(0.2)

        ## == SLIDE ==
        self.next_section('ASSIMILATION_1.1',PresentationSectionType.SUB_NORMAL)

        self.play(Write(state_tt),Write(state_eq),Create(brace1))
        self.play(Write(state_blist))
        self.wait(0.2)

        ## == SLIDE ==
        self.next_section('ASSIMILATION_1.2',PresentationSectionType.SUB_NORMAL)

        self.play(Write(observer_tt),Write(obs_eq),Create(brace2))
        self.play(Write(obs_blist))
        self.wait(0.2)

        ## == SLIDE ==
        self.next_section('ASSIMILATION_1.3',PresentationSectionType.SUB_NORMAL)

        self.play(Write(error_1))
        self.wait(0.2)

        ## == SLIDE ==
        self.next_section('ASSIMILATION_1.4',PresentationSectionType.SUB_NORMAL)

        self.play(TransformMatchingTex(error_1,error_2))
        self.play(TransformMatchingTex(error_2,error_3))
        self.play(ShowPassingFlash(box_error, run_time = 2, time_width = 1))
        self.wait(0.2)

        ## == SLIDE ==
        self.next_section('ASSIMILATION_1.5',PresentationSectionType.SUB_SKIP)

        self.play(FadeOut(VGroup(obs_blist,state_blist)))
        self.wait(0.5)

        # ===============
        # CHOICE OF L AND ERROR
        # ===============

        L_tex2 = L_tex.copy()
        sub_question = [Tex("How do we choose "),Tex(" ?")]

        question = VGroup(
            sub_question[0],L_tex2,sub_question[1],
        ).arrange(buff=0.1).align_to(brace1,LEFT).scale(35/30).shift([-0.5,-0,0])
        underline_question = Line(question.get_left(),question.get_right(),buff=0).next_to(question,DOWN,buff=SMALL_BUFF)

        st_tex     = Tex("so that :  ").align_to([-6,0,0],LEFT).shift(1*DOWN)
        objectif   = MathTex("\hat{x}(t)","\longrightarrow","x(t)").align_to(st_tex.get_right(),LEFT).shift(1*DOWN+0.1*RIGHT).set_color_by_tex("hat",OBS_COLOR).set_color_by_tex("x(",STATE_COLOR)
        objectif_2 = MathTex("\lVert\epsilon(t)\lVert","\longrightarrow","0").align_to(objectif,LEFT).shift((1+0.4)*DOWN)
        objectif_3 = MathTex("\mathfrak{Re}(\Lambda = \sigma","(A-LC)",")","< 0").align_to(objectif_2,LEFT).shift((1+0.8)*DOWN)

        footnote1 = VGroup(
            Tex("[1] Kautsky, Nichols, Van Dooren. ",font_size=20),
            Tex("'Robust pole assignment in linear state feedback.' (1985)",font_size=20)
        ).arrange(RIGHT, buff= 0.05).to_corner(DL)#.shift(0.35*DOWN)

        footnote2 = VGroup(
            Tex("[2] Liu. 'Locally distributed control and damping ",font_size=20),
            Tex("for the conservative systems.' (1987)",font_size=20),
        ).arrange(RIGHT, buff= 0.05).to_corner(DL).shift(0.35*DOWN)

        p1   = np.array([-1.5,-1,0])
        p2   = np.array([0,-1,0])
        p3_1 = np.array([0,-0.25,0])
        p3_2 = np.array([0,-1.75,0])
        l_ar = np.array([1.5,0,0])

        arrow_1  = VGroup(
            Line(p1,p2),
            Line(p2,p3_1),
            Arrow(p3_1,p3_1+l_ar,buff=0,stroke_width=3,max_tip_length_to_length_ratio=0.1)
        )
        arrow_2  = VGroup(
            Line(p2,p3_2),
            Arrow(p3_2,p3_2+l_ar,buff=0,stroke_width=3,max_tip_length_to_length_ratio=0.1)
        )

        L_place   = Tex(r"ODE : $L=\texttt{place(}\Lambda,A,C\texttt{)}$").align_to(arrow_1.get_right(),LEFT).match_y(Dot(p3_1)).shift(0.1*RIGHT)
        L_place_2 = Tex(r"'pole placement procedure'",font_size=27).move_to(L_place.get_center()).shift(0.4*DOWN)
        L_edp     = Tex(r"dsicretized PDE : $L = \gamma C^T$  ($\gamma \in \mathbb{R}$)").align_to(arrow_1.get_right(),LEFT).match_y(Dot(p3_2)).shift(0.1*RIGHT)

        ## ANIM

        ## == SLIDE ==
        self.next_section('ASSIMILATION_2',PresentationSectionType.NORMAL)

        self.play(FocusOn(L_tex))
        self.play(ReplacementTransform(L_tex.copy(),L_tex2))
        self.play(Write(VGroup(sub_question[0],sub_question[1],underline_question)))
        self.wait(1)

        ## == SLIDE ==
        self.next_section('ASSIMILATION_2.1',PresentationSectionType.SUB_NORMAL)

        self.play(Write(VGroup(st_tex,objectif)))
        self.play(Write(objectif_2))
        self.play(Write(objectif_3))
        self.wait(1)

        ## == SLIDE ==
        self.next_section('ASSIMILATION_2.2',PresentationSectionType.SUB_NORMAL)

        self.play(Create(arrow_1))
        self.play(Write(L_place),Write(L_place_2))
        self.play(FadeIn(footnote1))
        self.wait(1)
        ## == SLIDE ==
        self.next_section('ASSIMILATION_2.3',PresentationSectionType.SUB_NORMAL)

        self.play(Create(arrow_2))
        self.play(Write(L_edp))
        self.play(FadeIn(footnote2))
        self.wait(1)

        ## == SLIDE ==
        self.next_section('ASSIMILATION_2.4',PresentationSectionType.SUB_NORMAL)

        self.play(TransformMatchingTex(error_3,error_4))
        self.play(TransformMatchingTex(error_4,error_5))
        self.wait()
        self.play(Write(explain_error_5))
        self.wait(1)

        ## == SLIDE == (CLEANING)
        self.next_section('ASSIMILATION_2.5',PresentationSectionType.SUB_SKIP)
        self.play(FadeOut(VGroup(
            L_edp,L_place,L_place_2,
            arrow_1,arrow_2,
            objectif,objectif_2,objectif_3,
            st_tex,
            sub_question[0],sub_question[1],underline_question,
            L_tex2, error_5,
            footnote1,footnote2,
            explain_error_5,
            state_tt,
            observer_tt,
        )))
        self.play(VGroup(state_eq,brace1).animate.shift(3.75*DOWN),VGroup(obs_eq,brace2).animate.shift(3.75*DOWN))
        self.wait()

class C_Assimilation_2_2(Scene):
    def construct(self):

        # ===============
        # COLOR MANAGMENT
        # ===============

        Tex.set_default(color = FRONT_COLOR,font_size = 30)
        MathTex.set_default(color = FRONT_COLOR,font_size = 30)
        Mobject.set_default(color = FRONT_COLOR)

        # ===============
        # GRID FOR CONSTRUCTION PURPUSE ONLY
        # ===============

        L1 = Line(start=[- 7.1, 0., 0.], end=[7.1, 0., 0.],stroke_opacity =0.2)
        for i in range(-3,4):
            L1 = VGroup(L1,Line(start=[- 7.1, i, 0.], end=[7.1, i, 0.],stroke_opacity =0.1))

        L2 = Line(start=[0., -4., 0.], end=[0., 4., 0.],stroke_opacity =0.2)
        for i in range(-6,7):
            L2 = VGroup(L2,Line(start=[i, -4., 0.], end=[i, 4., 0.],stroke_opacity =0.1))

        if grid == 1 :
            self.add(L1,L2)

        # ===============
        # TITLE
        # ===============

        title = Title("Data assimilation : Luenberger observer \& dynamical systems",font_size=40)

        # ===============
        # STATE & OBS EQ
        # ===============

        state_eq_1  = MathTex("\dot{x}","=A","x(t)"," + B u(t)",font_size = 30)
        state_eq_1.set_color_by_tex('x', STATE_COLOR)

        state_eq_2  = MathTex("y(t) = C","x(t)",font_size = 30)
        state_eq_2.set_color_by_tex('x', STATE_COLOR).align_to(state_eq_1,LEFT).shift(0.5*DOWN)

        state_eq_3  = MathTex("x(0)","=","x_{0}",", \quad t \geq 0",font_size = 30)
        state_eq_3.set_color_by_tex('x', STATE_COLOR).align_to(state_eq_1,LEFT).shift(DOWN)

        state_eq    = VGroup(VGroup(state_eq_1,state_eq_2,state_eq_3)).move_to([-3.5,1.25,0])
        brace1      = Brace(state_eq,LEFT)

        L_tex = MathTex(r"L",font_size = 30)

        obs_eq_1  = MathTex("\dot{\hat{x}}(t)","=A","\hat{x}(t)","+B u(t)+L[y(t)-\hat{y}(t)]",font_size = 30)
        obs_eq_1.set_color_by_tex('x', OBS_COLOR)

        obs_eq_1  = VGroup(
        MathTex("\dot{\hat{x}}(t)","=A","\hat{x}(t)","+B u(t)+").set_color_by_tex('x', OBS_COLOR),
        L_tex,
        MathTex("[y(t)-\hat{y}(t)]"),
        ).arrange(buff=0.05)

        obs_eq_2  = MathTex("\hat{y}(t)=C","\hat{x}(t)",font_size = 30)
        obs_eq_2.set_color_by_tex('x', OBS_COLOR).align_to(obs_eq_1,LEFT).shift(0.5*DOWN)

        obs_eq_3  = MathTex("\hat{x}(0)","=","\hat{x}_{0}",", \quad t \geq 0",font_size = 30)
        obs_eq_3.set_color_by_tex('x', OBS_COLOR).align_to(obs_eq_1,LEFT).shift(DOWN)

        obs_eq    = VGroup(VGroup(obs_eq_1,obs_eq_2,obs_eq_3)).move_to([3.5,1.25,0])
        brace2    = Brace(obs_eq,LEFT)

        error_5 = MathTex("\lVert","\epsilon(t)","\lVert",
            "=","\lVert","\mathrm{e}^{","(A-LC)","t}","\epsilon","(0)","\lVert",
            "\leq","\lVert x(0)-\hat{x}(0) \lVert \cdot \kappa(X) \cdot \mathrm{e}^{-\mu t}",
            font_size = 35,
        ).move_to([0,-3,0]).set_color_by_tex("x",DEMARK_COLOR)

        footnote3 = VGroup(
            Tex("[3] Yu, Pei, Xu. 'Estimation of velocity potential of ",font_size=20),
            Tex("water waves using a Luenberger-like observer.' (2020)",font_size=20),
        ).arrange(RIGHT, buff= 0.05).to_corner(DL).shift(0.35*DOWN)

        self.add(title)
        self.add(VGroup(state_eq,brace1).shift(3.75*DOWN),VGroup(obs_eq,brace2).shift(3.75*DOWN))

        # ===============
        # LWWE EXAPLE
        # ===============

        axes_state_obs = Axes(x_range = [-0.1,1,1], y_range = [-0.15,0.15,0.15],
        x_length = 8, y_length = 4,
        tips = False,
        y_axis_config = {"include_numbers": True, "font_size": 25, "exclude_origin_tick" : False},
        x_axis_config = {"include_numbers": True, "font_size": 30, "exclude_origin_tick" : True},
        ).shift(0.5*UP)

        x_lab_state_obs = axes_state_obs.get_x_axis_label("(x-x_0)/L").scale(1).shift(0.5*LEFT+0.5*UP)
        y_lab_state_obs = axes_state_obs.get_y_axis_label("\eta(x)", edge=LEFT, direction=LEFT, buff=0.2).scale(1).shift(0.1*RIGHT)
        lab_state_obs = VGroup(x_lab_state_obs, y_lab_state_obs)

        ## RECOVERING MATLAB ANIMATION DATA :

        U_s    = np.genfromtxt('U_s.csv',delimiter=',')
        Uobs_s = np.genfromtxt('Uobs_s.csv',delimiter=',')
        T_end  = 10
        Nx     = np.int64(U_s.shape[0]/2)
        Nt     = np.int64(U_s.shape[1])
        tspan  = np.linspace(0,Nt-1,Nt)*T_end/Nt
        xspan  = np.linspace(0,1+(1/Nx),Nx)

        Eta_s     = U_s[0:Nx,:]
        Phi0_s    = U_s[Nx:,:]
        Etaobs_s  = Uobs_s[0:Nx,:]
        Phi0obs_s = Uobs_s[Nx:,:]
        Err_s     = np.linalg.norm(Uobs_s-U_s,axis=0)/np.linalg.norm(U_s,axis=0)
        mu        = 2.35
        Err_th    = 5*np.exp(-tspan*mu)

        time_t = ValueTracker(0)

        def graph_state_fun():
            return axes_state_obs.plot_line_graph(xspan, Eta_s[:,np.int64(time_t.get_value())],add_vertex_dots=False,line_color=STATE_COLOR)

        def graph_obs_fun():
            return axes_state_obs.plot_line_graph(xspan, Etaobs_s[:,np.int64(time_t.get_value())],add_vertex_dots=False,line_color=OBS_COLOR)

        graph_state = always_redraw(graph_state_fun)
        graph_obs   = always_redraw(graph_obs_fun)

        ## ANIM

        ## == SLIDE ==
        self.next_section('ASSIMILATION_3.0',PresentationSectionType.SUB_NORMAL)

        self.play(DrawBorderThenFill(axes_state_obs),Write(lab_state_obs))
        self.play(Create(graph_state),Create(graph_obs),FadeIn(footnote3))
        self.wait(1)

        ## == SLIDE ==
        self.next_section('ASSIMILATION_3.1',PresentationSectionType.SUB_NORMAL)

        self.play(time_t.animate.set_value(Nt-1),rate_func = rate_functions.linear,run_time = 10)
        self.wait(1)

        # ===============
        # ERROR GRAPH
        # ===============

        axes_error = Axes(x_range = [0,T_end,2], y_range = [-12,1,2],
        x_length = 5, y_length = 4.2,
        tips = False,
        axis_config={"include_numbers": True, "font_size": 25},
        y_axis_config={"scaling": LogBase(custom_labels=True)},
        ).add_coordinates()

        axes_error.move_to([3.5,0,0])

        x_lab_error = axes_error.get_x_axis_label("t")
        y_lab_error = axes_error.get_y_axis_label("\lVert \epsilon(t) \lVert=\lVert x(t) - \hat{x}(t) \lVert", buff=0.05).scale(0.8).shift(0.4*DOWN+0.2*RIGHT)
        lab_error = VGroup(x_lab_error, y_lab_error)

        def graph_err_fun():
            return axes_error.plot_line_graph(tspan[0:1+np.int64(time_t.get_value())], Err_s[0:1+np.int64(time_t.get_value())],add_vertex_dots=False,line_color=FRONT_COLOR)

        graph_err = always_redraw(graph_err_fun)
        graph_th  = axes_error.plot_line_graph(tspan[0:150], Err_th[0:150],add_vertex_dots=False,line_color=DEMARK_COLOR)

        error_lab_graph = MathTex("C \mathrm{e}^{-\mu t}",color = DEMARK_COLOR,font_size = 28).move_to([4,1.3,0])

        ## == SLIDE ==
        self.next_section('ASSIMILATION_3.2',PresentationSectionType.SUB_NORMAL)

        self.play(
            FadeOut(VGroup(state_eq,brace1)),
            FadeOut(VGroup(obs_eq,brace2)),
        )
        self.play(
            VGroup(axes_state_obs,lab_state_obs).animate.shift(3.5*LEFT + 0.5*DOWN).scale(5/8),
            DrawBorderThenFill(axes_error),Write(lab_error), Write(error_5),
            time_t.animate.set_value(0)
        )
        self.wait(1)

        ## == SLIDE ==
        self.next_section('ASSIMILATION_3.3',PresentationSectionType.SUB_NORMAL)

        self.add(graph_err)
        self.play(time_t.animate.set_value(Nt-2),rate_func = rate_functions.linear,run_time = 8)
        self.wait(1)

        ## == SLIDE ==
        self.next_section('ASSIMILATION_3.4',PresentationSectionType.SUB_NORMAL)

        self.play(Create(graph_th),Write(error_lab_graph))
        self.wait(1)

        ## == SLIDE == (CLEANING)
        self.next_section('ASSIMILATION_3.5',PresentationSectionType.SUB_SKIP)
        self.play(
            Unwrite(error_5),
            Unwrite(error_lab_graph),
            Uncreate(graph_th),
            Uncreate(graph_err),
            FadeOut(axes_error),FadeOut(lab_error),
            Uncreate(graph_state),
            FadeOut(axes_state_obs),FadeOut(lab_state_obs),
            Uncreate(graph_obs),
            Unwrite(title),
            FadeOut(footnote3)
        )
        self.wait(1)

# ==============================================
# PARALLEL SCENE
# Present the PinT algorithm : Paraexp
# ==============================================

class D_Parallel(Scene):
    def construct(self):

        # ===============
        # COLOR MANAGMENT
        # ===============

        Tex.set_default(color = FRONT_COLOR,font_size = 30)
        MathTex.set_default(color = FRONT_COLOR,font_size = 30)
        Mobject.set_default(color = FRONT_COLOR)

        # ===============
        # GRID FOR CONSTRUCTION PURPUSE ONLY
        # ===============

        L1 = Line(start=[- 7.1, 0., 0.], end=[7.1, 0., 0.],stroke_opacity =0.2)
        for i in range(-3,4):
            L1 = VGroup(L1,Line(start=[- 7.1, i, 0.], end=[7.1, i, 0.],stroke_opacity =0.1))

        L2 = Line(start=[0., -4., 0.], end=[0., 4., 0.],stroke_opacity =0.2)
        for i in range(-6,7):
            L2 = VGroup(L2,Line(start=[i, -4., 0.], end=[i, 4., 0.],stroke_opacity =0.1))

        if grid == 1 :
            self.add(L1,L2)

        # ===============
        # TITLE
        # ===============

        title = Title("Time parallelization : the Paraexp algorithm",font_size=40)

        # ===============
        # PARAEXP
        # ===============

        system_1  = MathTex("\dot{x}(t) = M x(t) + g(t), \quad t \in[0, T]")
        system_2  = MathTex("x(0) = x_{0}").align_to(system_1,LEFT).shift(0.5*DOWN)
        brace_sys = Brace(VGroup(system_1,system_2),LEFT)
        system    = VGroup(brace_sys,system_1,system_2)

        setting_sub = [Tex(r"$\rightarrow M \in \mathcal{M}_{m \times m} (\mathbb{C})$"),Tex(r"$\rightarrow x(t), g(t) \in \mathbb{C}^m$")]
        setting_sub[1].align_to(setting_sub[0],LEFT).shift(0.5*DOWN)
        setting = VGroup(setting_sub[0],setting_sub[1]).move_to([5,2,0])

        w_tex_2 = Tex(r"$w(t)$",color = GREEN)
        v_tex_2 = Tex(r"$v(t)$",color = BROWN)

        w_tex_22 = Tex(r"$w_j(t)$",color = GREEN)
        v_tex_22 = Tex(r"$v_j(t)$",color = BROWN)


        hom_system_1_sub = MathTex("\dot{w}(t)"," = M ").set_color_by_tex("w",GREEN)
        hom_system_1_sub2 = MathTex("\dot{w}_j(t)"," = M ").set_color_by_tex("w",GREEN)
        hom_system_1 = VGroup(hom_system_1_sub,w_tex_2).arrange(buff=0.05)
        hom_system_2 = MathTex("w(0)"," = x_{0}").set_color_by_tex("w",GREEN).align_to(hom_system_1,LEFT).shift(0.5*DOWN)
        hom_system_22 = MathTex("w_j(t_{j-1})"," = ","v_j(t_j)").set_color_by_tex("w",GREEN).set_color_by_tex("v",BROWN).align_to(hom_system_1,LEFT).shift(0.5*DOWN)
        brace_hom    = Brace(VGroup(hom_system_1,hom_system_2),LEFT)
        hom_system   = VGroup(brace_hom,hom_system_1,hom_system_2)

        inhom_system_1_sub = [MathTex("\dot{v}(t)"," = M ").set_color_by_tex("v",BROWN),MathTex(" + g(t)")]
        inhom_system_1_sub2 = [MathTex("\dot{v}_j(t)"," = M ").set_color_by_tex("v",BROWN),MathTex(" + g(t)")]
        inhom_system_1 = VGroup(inhom_system_1_sub[0],v_tex_2,inhom_system_1_sub[1]).arrange(buff=0.05)
        inhom_system_2 = MathTex("v(0)"," = 0").set_color_by_tex("v",BROWN).align_to(inhom_system_1,LEFT).shift(0.5*DOWN)
        inhom_system_22 = MathTex("v_j(t_{j-1})"," = 0").set_color_by_tex("v",BROWN).align_to(inhom_system_1,LEFT).shift(0.5*DOWN)
        brace_inhom    = Brace(VGroup(inhom_system_1,inhom_system_2),LEFT)
        inhom_system   = VGroup(brace_inhom,inhom_system_1,inhom_system_2)

        w_tex = w_tex_2.copy()
        v_tex = v_tex_2.copy()

        w_tex_1 = Tex(r"$\sum_{j=1}^{p}$",r"$w_j$",r"$(t)$",color = GREEN)
        v_tex_1 = Tex(r"$\sum_{j=1}^{p}$",r"$v_j$",r"$(t)$",color = BROWN)

        eq_1_sub = [MathTex("x(t) = "),MathTex(" + ")]
        eq_2     = VGroup(eq_1_sub[0],v_tex_1,eq_1_sub[1],w_tex).arrange(buff=0.05).move_to([0,1,0])
        eq_3     = VGroup(eq_1_sub[0],v_tex_1,eq_1_sub[1],w_tex_1).arrange(buff=0.05).move_to([0,1,0])

        eq_1     = VGroup(eq_1_sub[0],v_tex,eq_1_sub[1],w_tex).arrange(buff=0.05).move_to([0,1,0])

        system.move_to([0,2,0])
        hom_system.move_to([2,0,0])
        inhom_system.move_to([-2,0,0])

        inhom_system_1_sub2[0].move_to(inhom_system_1_sub[0].get_center()).shift(0.05*LEFT)
        inhom_system_22.move_to(inhom_system_2.get_center()).align_to(inhom_system_1_sub2[0],LEFT)

        hom_system_1_sub2.move_to(hom_system_1_sub.get_center()).shift(0.05*LEFT)
        hom_system_22.move_to(hom_system_2.get_center()).align_to(hom_system_1_sub2,LEFT)

        w_tex_22.move_to(w_tex_2.get_center())
        v_tex_22.move_to(v_tex_2.get_center())

        inhom_compute = VGroup(
            Tex("Euler", font_size = 25, color = BROWN),
            Tex("Runge-Kutta", font_size = 25, color = BROWN),
        ).arrange(DOWN).move_to([-5.3,0,0])

        arrow_inhom = Arrow(inhom_system,[-4.65,0,0],buff=0.15,stroke_width=3,max_tip_length_to_length_ratio=0.1)

        box_hom_system = SurroundingRectangle(hom_system, color = DEMARK_COLOR, buff = 0.2, corner_radius = 0.2)

        exp_system = MathTex("\Rightarrow","w(t)"," = \mathrm{e}^{(tM)}","w(0)").set_color_by_tex("w(t)",GREEN).set_color_by_tex("w(0)",GREEN).move_to([5,0,0])

        box_exp_system = SurroundingRectangle(exp_system, color = DEMARK_COLOR, buff = 0.2, corner_radius = 0.2)

        exp_compute = VGroup(
            Tex("Rational Krylov", font_size = 25, color = GREEN),
            Tex("Chebyshev polynomials", font_size = 25, color = GREEN)
        ).arrange(DOWN).move_to([5,-1.8,0])

        footnote4 = VGroup(
            Tex("[4] Gander, Güttel.",font_size=20),
            Tex(" 'Paraexp : a parallel integrator for ",font_size=20),
            Tex(" linear initial-value problems.' (2013)",font_size=20),
        ).arrange(RIGHT, buff=0.05).to_corner(DL).shift(0.35*DOWN)

        arrow_exp = Arrow([5,-0.2,0],exp_compute,buff=0.2,stroke_width=3,max_tip_length_to_length_ratio=0.1)

        box_exp_compute = SurroundingRectangle(VGroup(exp_compute,exp_system), color = DEMARK_COLOR, buff = 0.2, corner_radius = 0.2)

        ## ANIM

        ### == SLIDE ==
        self.next_section('PARALLEL_1',PresentationSectionType.SKIP)
        self.play(Write(title))
        self.wait(1)

        ### == SLIDE ==
        self.next_section('PARALLEL_1.1',PresentationSectionType.SUB_NORMAL)
        self.play(Write(VGroup(system_1,system_2)),Create(brace_sys))
        self.play(Write(setting))
        self.wait(1)

        ### == SLIDE ==
        self.next_section('PARALLEL_1.2',PresentationSectionType.SUB_NORMAL)
        self.play(Write(eq_1))
        self.wait(1)

        ### == SLIDE ==
        self.next_section('PARALLEL_1.3',PresentationSectionType.SUB_NORMAL)
        self.play(ReplacementTransform(v_tex.copy(),v_tex_2))
        self.play(ReplacementTransform(w_tex.copy(),w_tex_2))
        self.play(
            Write(VGroup(hom_system_1_sub,hom_system_2)),
            Write(VGroup(inhom_system_1_sub[0],inhom_system_1_sub[1],inhom_system_2)),
            Create(brace_hom),Create(brace_inhom),
        )
        self.wait(1)

        ### == SLIDE ==
        self.next_section('PARALLEL_1.4',PresentationSectionType.SUB_NORMAL)
        self.play(Create(arrow_inhom))
        self.play(Write(inhom_compute))
        self.wait(1)

        ### == SLIDE ==
        self.next_section('PARALLEL_1.5',PresentationSectionType.SUB_NORMAL)
        self.play(Create(box_hom_system))
        self.wait(1)

        ### == SLIDE ==
        self.next_section('PARALLEL_1.6',PresentationSectionType.SUB_NORMAL)
        self.play(Write(exp_system))
        self.wait(1)
        self.play(ReplacementTransform(box_hom_system,box_exp_system))
        self.wait(1)

        ### == SLIDE ==
        self.next_section('PARALLEL_1.7',PresentationSectionType.SUB_NORMAL)
        self.play(Create(arrow_exp))
        self.play(Write(exp_compute),FadeIn(footnote4))
        self.wait(1)
        self.play(ReplacementTransform(box_exp_system,box_exp_compute))
        self.wait(1)


        type_1_tex = Tex("'Type 1'",r" on $[t_{j-1},t_{j}]$").set_color_by_tex("ype",BROWN).move_to([-2,-1,0])
        type_2_tex = Tex("'Type 2'",r" on $[t_{j-1},T]$").set_color_by_tex("ype",GREEN).move_to([2,-1,0])

        dict_values = {1 : Tex(r"$0 = t_0$"), 2 : Tex(r"$t_1$"), 3 : Tex(r"$t_2$"), 4 : Tex(r"$t_3$"), 5 : Tex(r"$t_4 = T$")}
        axes_paraexp = Axes(x_range = [1,5,1], y_range = [0,1,2],
        x_length = 6, y_length = 1,
        tips = False,
        axis_config = {"include_numbers": False, "font_size": 25, "exclude_origin_tick" : True},
        y_axis_config = {"stroke_opacity" : 0}
        ).move_to([0,-2.5,0])

        axes_paraexp.get_axes()[0].add_labels(dict_values),

        graph_type_1 = [axes_paraexp.plot(lambda x: 1/2*(x-1) + 1/9 * np.sin(2*x*PI), x_range=[1, 2], color = BROWN),
            axes_paraexp.plot(lambda x: 1/2*(x-2) + 1/10 * np.sin(3*x*PI), x_range=[2, 3], color = BROWN),
            axes_paraexp.plot(lambda x: 1/2*(x-3) + 1/15 * np.sin(x*PI), x_range=[3, 4], color = BROWN),
            axes_paraexp.plot(lambda x: 1/2*(x-4) + 1/20 * np.sin(4*x*PI), x_range=[4, 5], color = BROWN)]

        graph_type_2 = [axes_paraexp.plot(lambda x: ((x-1)/5)**2 + 3/4, x_range=[1, 5], color = GREEN),
            axes_paraexp.plot(lambda x: ((x-1)/5)**2 + 2/4.35, x_range=[2, 5], color = GREEN),
            axes_paraexp.plot(lambda x: ((x-2)/6)**2 + 2/4.35, x_range=[3, 5], color = GREEN),
            axes_paraexp.plot(lambda x: ((x-4)/7)**2 + 1/2, x_range=[4, 5], color = GREEN)]

        initial_point = VGroup(
            MathTex("x_0").set_color_by_tex("x",GREEN).move_to([-3.3,-2,0]),
            Tex(r"$\times$").set_color_by_tex("times",GREEN).move_to([-3,-2.2,0])
        )

        p_computer_tex = Tex(r"$p = 4$ computers :").move_to([-5.3,-2,0])

        ## ANIM

        ### == SLIDE ==
        self.next_section('PARALLEL_1.8',PresentationSectionType.SUB_NORMAL)
        self.play(Uncreate(box_exp_compute))
        self.wait()
        self.play(Write(p_computer_tex))
        self.wait()
        self.play(DrawBorderThenFill(axes_paraexp))
        self.wait(1)

        ### == SLIDE ==
        self.next_section('PARALLEL_1.9',PresentationSectionType.SUB_NORMAL)
        self.play(
            Write(type_1_tex),
            TransformMatchingTex(eq_1,eq_2),eq_1_sub[0].animate.shift(0.9*LEFT),
            TransformMatchingTex(inhom_system_1_sub[0],inhom_system_1_sub2[0]),
            TransformMatchingTex(inhom_system_2,inhom_system_22),
            inhom_system_1_sub[1].animate.shift(0.1*RIGHT),
            TransformMatchingTex(v_tex_2,v_tex_22)
        )
        self.wait(0.5)
        self.play(
            Create(graph_type_1[0]),
            Create(graph_type_1[1]),
            Create(graph_type_1[2]),
            Create(graph_type_1[3]),
        )
        self.wait(1)

        ### == SLIDE ==
        self.next_section('PARALLEL_1.10',PresentationSectionType.SUB_NORMAL)
        self.play(
            Write(type_2_tex),
            TransformMatchingTex(eq_2,eq_3),
            TransformMatchingTex(hom_system_1_sub,hom_system_1_sub2),
            TransformMatchingTex(hom_system_2,hom_system_22),
            TransformMatchingTex(w_tex_2,w_tex_22),
            )
        self.wait(0.5)
        self.play(
            Write(initial_point),
            Create(graph_type_2[0]),
            Create(graph_type_2[1]),
            Create(graph_type_2[2]),
            Create(graph_type_2[3]),
        )
        self.wait(1)

        ### == SLIDE == (CLEANING)
        self.next_section('PARALLEL_1.11',PresentationSectionType.SUB_SKIP)
        self.play(
            FadeOut(type_1_tex),FadeOut(type_2_tex),
            Unwrite(initial_point),Uncreate(VGroup(*graph_type_2)),Uncreate(VGroup(*graph_type_1)),
            FadeOut(axes_paraexp),FadeOut(p_computer_tex),
            FadeOut(VGroup(exp_compute,arrow_exp,footnote4,exp_system)),
            FadeOut(VGroup(inhom_compute,arrow_inhom)),
            #FadeOut(VGroup(hom_system,inhom_system)),
            FadeOut(VGroup(inhom_system_1_sub2[0],inhom_system_1_sub[1],inhom_system_22,v_tex_22,hom_system_1_sub2,hom_system_22,w_tex_22,brace_hom,brace_inhom)),
            FadeOut(VGroup(system_1,system_2)),FadeOut(brace_sys),
            FadeOut(setting),FadeOut(eq_3),
            Unwrite(title),
        )
        self.wait()

# ==============================================
# COUPLING SCENE
# Present the strategy used for applying
# PinT to sequential data assimilation procedure
# ==============================================

class E_Coupling(Scene):
    def construct(self):

        # ===============
        # COLOR MANAGMENT
        # ===============

        Tex.set_default(color = FRONT_COLOR,font_size = 30)
        MathTex.set_default(color = FRONT_COLOR,font_size = 30)
        Mobject.set_default(color = FRONT_COLOR)

        # ===============
        # GRID FOR CONSTRUCTION PURPUSE ONLY
        # ===============

        L1 = Line(start=[- 7.1, 0., 0.], end=[7.1, 0., 0.],stroke_opacity =0.2)
        for i in range(-3,4):
            L1 = VGroup(L1,Line(start=[- 7.1, i, 0.], end=[7.1, i, 0.],stroke_opacity =0.1))

        L2 = Line(start=[0., -4., 0.], end=[0., 4., 0.],stroke_opacity =0.2)
        for i in range(-6,7):
            L2 = VGroup(L2,Line(start=[i, -4., 0.], end=[i, 4., 0.],stroke_opacity =0.1))

        if grid == 1 :
            self.add(L1,L2)

        # ===============
        # TITLE
        # ===============

        title = Title("Coupling PinT \& Data assimilation",font_size=40)

        # ===============
        # OBJECTIVES
        # ===============

        objective_tex_1 = Tex("Objective : ","Apply ","P","arralel-","in","-","T","ime"," to ","data assimilation").shift(2*UP)
        objective_tex_2 = Tex("Objective : ","P","arralel ","in"," ","T","ime","(","data assimilation",")").shift(2*UP)
        objective_tex_3 = Tex("Objective : ","P","in","T","(","data assimilation",")").shift(2*UP).scale(35/30)

        technicality_tex_1 = Tex(
            r"$\rightarrow$ ","PinT algorithms are on a ","bounded"," time interval, data assimilation is on an ","unbounded"," time interval"
        ).set_color_by_tex('bound', DEMARK_COLOR).scale(32/30).shift(0.5*UP)
        technicality_tex_2 = Tex(
            r"$\rightarrow$ ","To optimize PinT, we want to start with a coarse approximation and ",r"refine it over time"
        ).scale(32/30).align_to(technicality_tex_1,LEFT).shift(1*DOWN).set_color_by_tex('refine', DEMARK_COLOR)
        technicality_tex_3 = Tex(
            r"$\rightarrow$ ","We want to ",r"preserve",r" the property of the data assimilation scheme : in our case ",r"the convergence rate $\mu$"
        ).scale(32/30).align_to(technicality_tex_1,LEFT).shift(2.5*DOWN).set_color_by_tex('\mu', DEMARK_COLOR).set_color_by_tex('preserve', DEMARK_COLOR)

        ## ANIM

        ### == SLIDE ==
        self.next_section('COUPLING_1',PresentationSectionType.SKIP)
        self.play(Write(title))
        self.wait()

        ## == SLIDE ==
        self.next_section('COUPLING_1.1',PresentationSectionType.SUB_SKIP)
        self.play(Write(objective_tex_1))
        self.wait(1)
        ## == SLIDE ==
        self.next_section('COUPLING_1.2',PresentationSectionType.SUB_SKIP)
        self.play(TransformMatchingTex(objective_tex_1,objective_tex_2))
        self.wait(0.1)
        self.play(TransformMatchingTex(objective_tex_2,objective_tex_3))
        self.wait(1)
        ## == SLIDE ==
        self.next_section('COUPLING_1.3',PresentationSectionType.SUB_NORMAL)
        self.play(Write(technicality_tex_1))
        self.play(Write(technicality_tex_2))
        self.play(Write(technicality_tex_3))
        self.wait(1)
        # CLEANING SLIDE
        self.next_section('COUPLING_1.4',PresentationSectionType.SUB_SKIP)
        self.play(
            FadeOut(technicality_tex_2),
            FadeOut(technicality_tex_3),
            FadeOut(objective_tex_3),
            technicality_tex_1.animate.shift(1.8*UP),
        )
        self.wait(1)

        # ===============
        # BOUNDED & UNBONDED SOLUTION (IDEA)
        # ===============

        strategy_sub_tex = [
            Tex(r"1) Divide the unbonded interval into 'windows' of size ",r"$T$",r" : $W_\ell = (T_{\ell-1},T_\ell), \ell \leq 0$"),
            Tex(r"2) Apply time parallelization scheme on each 'window'"),
            Tex(r"3) Estimate the error at the end of each 'window' to go (or not) onto the next one"),
        ]
        strategy = VGroup(*strategy_sub_tex).arrange(DOWN, buff=0.5).shift(0.5*DOWN)

        ## ANIM

        ## == SLIDE ==
        self.next_section('COUPLING_2',PresentationSectionType.NORMAL)
        self.play(Write(strategy_sub_tex[0]))
        self.play(Write(strategy_sub_tex[1]))
        self.play(Write(strategy_sub_tex[2]))
        self.wait(1)
        ## == SLIDE ==
        self.next_section('COUPLING_2.1',PresentationSectionType.SUB_SKIP)
        self.play(FadeOut(strategy))
        self.wait(0.5)

        # ===============
        # BOUNDED & UNBONDED SOLUTION (GRAPH)
        # ===============

        bounded_unbounded_tex = Tex("PinT on unbounded time intervals ?").move_to([-4,2,0])

        dict_values = {
            0 : Tex(r"$0=T_0$"),
            1 : Tex(r"$T_1$"),
            2 : Tex(r"$T_2$"),
            3 : Tex(r"$T_3$"),
            4 : Tex(r"$T_4$")
        }

        axes_PinT = Axes(
            x_range = [-0.1,4.1,1],
            y_range = [-0.2,1.2,2],
            x_length = 10*(4.2/4),
            y_length = 4,
            tips = False,
            x_axis_config = {"include_numbers": False, "font_size": 25},
            y_axis_config = {"include_numbers": False, "font_size": 25},
        ).shift(DOWN)

        axes_PinT.get_axes()[0].add_labels(dict_values)

        def f_func(t): return( (1/20) * np.sin(8*(t**(4/3))) )
        def g_func(t): return( (1/12) * ( (t-2)**3 + (t-3)**2 ) )
        def h_func(t): return( (1/2) * np.exp(-1.5*(t-2.5)**2) )
        def i_func(t): return( f_func(t) + g_func(t) + h_func(t) )
        def j_func(t): return( i_func(t) + np.exp(-2*t) )
        def k_func(t): return( i_func(t) + np.exp(-2*t) * (t+1) )

        graph_state      = axes_PinT.plot(lambda t: i_func(t), x_range=[0, 4], color = STATE_COLOR)
        graph_state_dash = DashedVMobject(graph_state, num_dashes = 50, dashed_ratio = 1/2)
        state_init       = MathTex("x_0",color = STATE_COLOR,font_size=30).move_to([-5.3,-2.1,0])

        state_lab_tex = Tex(r"$x$").set_color(STATE_COLOR).move_to([-4,-2,0])

        graph_obs      = axes_PinT.plot(lambda t: j_func(t), x_range=[0, 3.2], color = OBS_COLOR)
        obs_init       = MathTex("\hat{x}_0",color = OBS_COLOR,font_size=30).move_to([-5.3,0.6,0])

        obs_lab_tex = Tex(r"$\hat{x}$").set_color(OBS_COLOR).move_to([-4,-0.8,0])

        obs_precision_tex = Tex(r"$\hat{x}$",r" computed with max. precision ($\Delta_t \ll 0$)").set_color_by_tex('hat',OBS_COLOR).to_corner(DL).shift(0.3*DOWN)

        dot_final_obs  = Dot([3,-1.3,0],color = OBS_COLOR)
        stop_obs_sub   = [DashedLine(start = dot_final_obs, end = [3,-3,0],color = OBS_COLOR),
            MathTex("T_f",font_size=30,color = OBS_COLOR).move_to([3,-3.3,0])]
        stop_obs       = VGroup(*stop_obs_sub)

        graph_obs_para_sub = [axes_PinT.plot(lambda t: k_func(t), x_range=[k/4, (k+1)/4], color = DEMARK_COLOR) for k in range(0,16)]
        graph_obs_para = VGroup(*graph_obs_para_sub)

        obs_para_lab_tex = Tex(r"$\hat{x}_{\lVert}$").set_color(DEMARK_COLOR).move_to([-4,0.5,0]).scale(35/30)

        obs_para_precision_tex = Tex(r"$\hat{x}_{\lVert}$ : ",r"$\hat{x}_{\lVert}^{T1}$",r" : with \textit{some} precision ($\Delta_t < 0$), ",r"$\hat{x}_{\lVert}^{T2}$",r" exact (expm)").set_color_by_tex('T1',BROWN).set_color_by_tex('T2',GREEN).set_color_by_tex('\lVert}$',DEMARK_COLOR).to_corner(DL).shift(0.4*DOWN+0.3*LEFT).scale(28/30)

        separator = VGroup(
            DashedLine(start = [-5,-3,0], end = [-5,1,0],stroke_opacity =0.4),
            DashedLine(start = [-2.5,-3,0], end = [-2.5,1,0],stroke_opacity =0.4)
        )
        fill_intervals = [Rectangle(width = (2.5/4.0), height=4.0, color = FRONT_COLOR, fill_opacity = 0.1 ,stroke_opacity = 0).move_to([-5+(2.5/8),-1,0]),
            Rectangle(width = (2.5/4.0), height=4.0, color = GRAY, fill_opacity = 0.1 ,stroke_opacity = 0).move_to([-5+3*(2.5/8),-1,0]),
            Rectangle(width = (2.5/4.0), height=4.0, color = FRONT_COLOR, fill_opacity = 0.1 ,stroke_opacity = 0).move_to([-5+5*(2.5/8),-1,0]),
            Rectangle(width = (2.5/4.0), height=4.0, color = GRAY, fill_opacity = 0.1 ,stroke_opacity = 0).move_to([-5+7*(2.5/8),-1,0])]

        intervals = VGroup(*fill_intervals)

        #brace = Brace(intervals,UP)
        brace = DoubleArrow(start = intervals.get_left(), end = intervals.get_right(),stroke_width=3,max_tip_length_to_length_ratio=0.05,buff=0).shift(2.2*UP)
        window_tex_1 = MathTex("W_","1", font_size= 25).next_to(brace,UP).shift(0.2*DOWN)
        window_tex_2 = MathTex("W_","2", font_size= 25).next_to(brace,UP).shift(0.2*DOWN + 2.5*RIGHT)
        window_tex_3 = MathTex("W_","3", font_size= 25).next_to(brace,UP).shift(0.2*DOWN + 2*2.5*RIGHT)
        window_tex_4 = MathTex("W_","4", font_size= 25).next_to(brace,UP).shift(0.2*DOWN + 3*2.5*RIGHT)
        Window = VGroup(brace,window_tex_1)

        dot_final_para  = Dot([5,-0.2,0],color = DEMARK_COLOR)
        stop_para_sub   = [DashedLine(start = dot_final_para, end = [5,-3,0],color = DEMARK_COLOR),
            MathTex("T_{f\lVert}",font_size=30,color = DEMARK_COLOR).move_to([5,-3.3,0])]
        stop_para       = VGroup(*stop_para_sub)

        stopping_criteria_obs_tex = Tex(r"stop :  ",r"$\lVert \epsilon(t) \lVert < \texttt{tol}$",font_size=22).move_to([2.8,-3.7,0]).set_color_by_tex('eps',OBS_COLOR)
        stopping_criteria_para_tex = Tex(r"$\lVert \epsilon_{\lVert}(T_\ell) \lVert < \texttt{tol}$",font_size=22).move_to([5,-3.7,0]).set_color(DEMARK_COLOR)

        ## ANIM

        ## == SLIDE ==
        self.next_section('COUPLING_3',PresentationSectionType.NORMAL)

        self.play(DrawBorderThenFill(axes_PinT))
        self.play(Write(state_init))
        self.play(Create(graph_state,rate_func = rate_functions.linear, run_time = 3), Write(state_lab_tex))
        self.play(FadeTransform(graph_state,graph_state_dash),)
        self.wait(1)

        ### == SLIDE ==
        self.next_section('COUPLING_3.1',PresentationSectionType.SUB_NORMAL)

        self.play(Write(obs_init))
        self.play(Create(graph_obs, rate_func=rate_functions.linear, run_time = 3), Write(obs_lab_tex), Write(obs_precision_tex))
        self.play(Create(dot_final_obs))
        self.play(Flash(dot_final_obs,color = DEMARK_COLOR),Create(stop_obs),Write(stopping_criteria_obs_tex))
        self.wait(2)

        ## == SLIDE ==
        self.next_section('COUPLING_3.2',PresentationSectionType.SUB_SKIP)

        self.play(graph_state_dash.animate.fade(0.3))
        self.play(graph_obs.animate.fade(0.3))
        self.wait(0.5)

        ## == SLIDE ==
        self.next_section('COUPLING_3.3',PresentationSectionType.SUB_NORMAL)

        self.play(Create(separator),Create(intervals),Create(Window),run_time=3)
        self.play(Indicate(fill_intervals[0],color=DEMARK_COLOR))
        self.play(Indicate(fill_intervals[1],color=DEMARK_COLOR))
        self.play(Indicate(fill_intervals[2],color=DEMARK_COLOR))
        self.play(Indicate(fill_intervals[3],color=DEMARK_COLOR))
        self.wait(1)

        ## == SLIDE ==
        self.next_section('COUPLING_3.4',PresentationSectionType.SUB_NORMAL)

        self.play(*[Create(graph_obs_para[s], rate_func=rate_functions.linear) for s in range(0,4)])
        self.play(Write(obs_para_lab_tex),ReplacementTransform(obs_precision_tex,obs_para_precision_tex))
        self.wait(1)

        ## == SLIDE ==
        self.next_section('COUPLING_3.5',PresentationSectionType.SUB_SKIP)

        self.play(
            separator.animate.shift(2.5*RIGHT),
            intervals.animate.shift(2.5*RIGHT),
            brace.animate.shift(2.5*RIGHT),
            TransformMatchingTex(window_tex_1,window_tex_2)
        )
        self.wait(1)

        ## == SLIDE ==
        self.next_section('COUPLING_3.6',PresentationSectionType.SUB_NORMAL)

        self.play(*[Create(graph_obs_para[s], rate_func=rate_functions.linear) for s in range(4,8)])
        self.wait(1)

        ## == SLIDE ==
        self.next_section('COUPLING_3.7',PresentationSectionType.SUB_SKIP)

        self.play(
            separator.animate.shift(2.5*RIGHT),
            intervals.animate.shift(2.5*RIGHT),
            brace.animate.shift(2.5*RIGHT),
            TransformMatchingTex(window_tex_2,window_tex_3)
        )
        self.wait(0.5)
        self.play(*[Create(graph_obs_para[s], rate_func=rate_functions.linear) for s in range(8,12)])
        self.wait(0.5)

        ## == SLIDE ==
        self.next_section('COUPLING_3.8',PresentationSectionType.SUB_NORMAL)

        self.play(
            separator.animate.shift(2.5*RIGHT),
            intervals.animate.shift(2.5*RIGHT),
            brace.animate.shift(2.5*RIGHT),
            TransformMatchingTex(window_tex_3,window_tex_4)
        )
        self.wait(0.5)
        self.play(*[Create(graph_obs_para[s], rate_func=rate_functions.linear) for s in range(12,16)])
        self.play(Create(dot_final_para),)
        self.play(Flash(dot_final_para,color = DEMARK_COLOR),Create(stop_para),Write(stopping_criteria_para_tex))
        self.wait(1)
        self.play(
            Uncreate(separator),
            Uncreate(intervals),
            Uncreate(VGroup(brace,window_tex_4)),
        )
        self.wait(1)

        ## == SLIDE ==
        self.next_section('COUPLING_3.9',PresentationSectionType.SUB_SKIP)

        self.play(
            Uncreate(graph_state_dash),Uncreate(graph_obs),Uncreate(graph_obs_para),
            Uncreate(state_init),Uncreate(obs_init),
            Uncreate(dot_final_obs),Uncreate(stop_obs),
            Uncreate(dot_final_para),Uncreate(stop_para),
            FadeOut(axes_PinT),FadeOut(technicality_tex_1),
            FadeOut(stopping_criteria_obs_tex),FadeOut(stopping_criteria_para_tex),
            FadeOut(state_lab_tex),FadeOut(obs_lab_tex),
            FadeOut(obs_precision_tex),FadeOut(obs_para_lab_tex),FadeOut(obs_para_precision_tex),
        )
        self.wait(1)

        # ===============
        # PRESERVING PROPERTY (I)
        # ===============

        technicality_tex_2 = Tex(
            r"$\rightarrow$ ",r"To optimize PinT, we want to start with a coarse approximation and ",r"refine it over time",r", while ",r"conserving the convergence rate $\mu$"
        ).scale(32/30).align_to(technicality_tex_1,LEFT).shift(1*DOWN).set_color_by_tex('refine', DEMARK_COLOR).set_color_by_tex('mu', DEMARK_COLOR)

        technicality_tex_2.move_to(technicality_tex_1.get_center())

        error_reminder_tex = Tex(r"$\lVert \epsilon(T_\ell)\lVert \approx C\mathrm{e}^{-\mu T_\ell} $").move_to([4.5,0.7,0])

        box_error_reminder = SurroundingRectangle(error_reminder_tex, color = DEMARK_COLOR, buff = 0.2, corner_radius = 0.2)

        error_sys_sub_tex = [
            Tex(r"$\hat{x}(T_\ell) = $",r"$\hat{x}^{T1}(T_\ell)$",r"$ + $",r"$\hat{x}^{T2}(T_\ell)$").shift(4.7*RIGHT + 1*DOWN).set_color_by_tex('T1',BROWN).set_color_by_tex('T2',GREEN),
            Tex(r"$\hat{x}_{\lVert} (T_\ell) = $",r"${\hat{x}_{\lVert}}^{T1}(T_\ell)$",r"$ + $",r"${\hat{x}_{\lVert}}^{T2}(T_\ell)$").shift(4.6*RIGHT + 1.8*DOWN).set_color_by_tex('T1',BROWN).set_color_by_tex('T2',GREEN)
        ]
        error_sys_sub_tex[1].align_to(error_sys_sub_tex[0],LEFT)
        error_sys_tex = VGroup(*error_sys_sub_tex)
        error_sys     = VGroup(Brace(error_sys_tex,LEFT),error_sys_tex)

        separator_field = Line(start = [2.1,1.5,0], end = [2.1,-3.4,0])

        error_para_1_tex = Tex(r"$\lVert $",r"$\hat{x}(T_\ell) $",r"$ - $",r"$\hat{x}_{\lVert}(T_\ell)$",r"$ \lVert$").set_color_by_tex('\hat{x}_',DEMARK_COLOR).set_color_by_tex('$\hat{x}(',OBS_COLOR).set_color_by_tex('$x',STATE_COLOR)

        error_sub_1_tex = [
            Tex(r"$\lVert \epsilon_{\lVert}(T_\ell)\lVert$",r"$=$",r"$\lVert $",r"$\hat{x}_{\lVert}(T_\ell)$",r"$ - $",r"$x(T_\ell)$",r"$ \lVert$"
            ).set_color_by_tex('\hat{x}_',DEMARK_COLOR).set_color_by_tex('$x',STATE_COLOR).shift(1*UP + 2.5*LEFT),
            Tex(r"$\lVert \epsilon_{\lVert}(T_\ell)\lVert$",r"$=$",r"$\lVert $",r"$\hat{x}_{\lVert}(T_\ell)$",r"$ - $",r"$x(T_\ell)$",r"$ \lVert$",
                r"$\leq$",r"$\lVert$",r"$x(T_\ell)$",r"$ - $",r"$\hat{x}(T_\ell)$",r"$\lVert$",r"$+$",r"$\lVert $",r"$\hat{x}(T_\ell) $",r"$ - $",r"$\hat{x}_{\lVert}(T_\ell)$",r"$ \lVert$"
            ).set_color_by_tex('\hat{x}_',DEMARK_COLOR).set_color_by_tex('$\hat{x}(',OBS_COLOR).set_color_by_tex('$x',STATE_COLOR).shift(1*UP + 2.5*LEFT),
            VGroup(
                Tex(r"$\lVert \epsilon_{\lVert}(T_\ell)\lVert$",r"$=$",r"$\lVert $",r"$\hat{x}_{\lVert}(T_\ell)$",r"$ - $",r"$x(T_\ell)$",r"$ \lVert$",
                r"$\leq$",r"$\lVert$",r"$\epsilon(T_\ell)$",r"$\lVert$",r"$+$").set_color_by_tex('\hat{x}_',DEMARK_COLOR).set_color_by_tex('$\hat{x}(',OBS_COLOR).set_color_by_tex('$x',STATE_COLOR),error_para_1_tex
            ).arrange(buff=0.05).shift(1*UP + 2.5*LEFT),
        ]

        box_error_2 = SurroundingRectangle(error_sub_1_tex[2], color = DEMARK_COLOR, buff = 0.2, corner_radius = 0.2)

        error_sub_2_tex_1 = Tex(r"$\epsilon_{\lVert}$").move_to([-3.2,0.2,0])

        error_sub_2_tex_2  = VGroup(
            Tex(r"$= $",r"$\hat{x}_{\lVert}$",r"$ - $",r"$x$").set_color_by_tex('\hat{x}_',DEMARK_COLOR).set_color_by_tex('$\hat{x}(',OBS_COLOR).set_color_by_tex('$x',STATE_COLOR),
            Tex(r"$= $",r"${\hat{x}_{\lVert}}^{T1}$",r"$ + $",r"${\hat{x}_{\lVert}}^{T2}$",r"$ - $",r"$x$").set_color_by_tex('\hat{x}_',DEMARK_COLOR).set_color_by_tex('$\hat{x}^',OBS_COLOR).set_color_by_tex('$x',STATE_COLOR),
            Tex(r"$= $",r"${\hat{x}_{\lVert}}^{T1}$",r"$ + $",r"${\hat{x}_{\lVert}}^{T2}$",r"$ - $",r"$\hat{x}^{T1}$",r"$ + $",r"$\hat{x}^{T1}$",r"$ - $",r"$x$").set_color_by_tex('\hat{x}_',DEMARK_COLOR).set_color_by_tex('$\hat{x}^',OBS_COLOR).set_color_by_tex('$x',STATE_COLOR),
            Tex(r"$= $",r"${\hat{x}_{\lVert}}^{T1}$",r"$ - $",r"$\hat{x}^{T1}$",r"$ + $",r"${\hat{x}_{\lVert}}^{T2}$",r"$ + $",r"$\hat{x}^{T1}$",r"$ - $",r"$x$").set_color_by_tex('\hat{x}_',DEMARK_COLOR).set_color_by_tex('$\hat{x}^',OBS_COLOR).set_color_by_tex('$x',STATE_COLOR),
            Tex(r"$= $",r"${\hat{x}_{\lVert}}^{T1}$",r"$ - $",r"$\hat{x}^{T1}$",r"$ + $",r"$\hat{x}$",r"$ - $",r"$x$").set_color_by_tex('\hat{x}_',DEMARK_COLOR).set_color_by_tex('$\hat{x}$',OBS_COLOR).set_color_by_tex('$x',STATE_COLOR).set_color_by_tex('$\hat{x}^',OBS_COLOR)
        ).arrange_in_grid(cols=1,col_alignments="l").align_to(error_sub_2_tex_1.get_corner([1,1,0]),[-1,0.9,0]).shift(0.1*RIGHT)

        error_para_3_tex = error_para_1_tex.copy()

        error_sub_3_tex  = VGroup(
            error_para_3_tex,Tex(r"$=$",r"$\lVert $",r"${\hat{x}_{\lVert}}^{T1}(T_{\ell})$",r"$ - $",r"$\hat{x}^{T1}(T_{\ell})$",r"$ \lVert$").set_color_by_tex('\hat{x}_',DEMARK_COLOR).set_color_by_tex('$\hat{x}^',OBS_COLOR).set_color_by_tex('$x',STATE_COLOR)
        ).arrange(buff = 0.05).move_to([-2.5,-3.2,0])

        box_error_3 = SurroundingRectangle(error_sub_3_tex, color = DEMARK_COLOR, buff = 0.2, corner_radius = 0.2)

        ## ANIM

        ## == SLIDE ==
        self.next_section('COUPLING_4',PresentationSectionType.SKIP)

        self.play(Write(technicality_tex_2),Create(separator_field))
        self.play(Write(error_reminder_tex))
        self.wait()

        ## == SLIDE ==
        self.next_section('COUPLING_4.1',PresentationSectionType.SUB_NORMAL)

        self.play(Write(error_sub_1_tex[0]))
        self.play(TransformMatchingTex(error_sub_1_tex[0],error_sub_1_tex[1]))
        self.wait(1)
        ## == SLIDE ==
        self.next_section('COUPLING_4.1',PresentationSectionType.SUB_SKIP)

        self.play(TransformMatchingTex(error_sub_1_tex[1],error_sub_1_tex[2]))
        self.wait()
        self.play(Write(error_sys))
        self.wait()

        ## == SLIDE ==
        self.next_section('COUPLING_4.2',PresentationSectionType.SUB_SKIP)

        self.play(Write(error_sub_2_tex_1))
        self.play(Write(error_sub_2_tex_2[0]))
        self.play(TransformMatchingTex(error_sub_2_tex_2[0].copy(),error_sub_2_tex_2[1]))
        self.play(TransformMatchingTex(error_sub_2_tex_2[1].copy(),error_sub_2_tex_2[2]))
        self.play(TransformMatchingTex(error_sub_2_tex_2[2].copy(),error_sub_2_tex_2[3]))
        self.play(TransformMatchingTex(error_sub_2_tex_2[3].copy(),error_sub_2_tex_2[4]))
        self.wait(1)

        ## == SLIDE ==
        self.next_section('COUPLING_4.3',PresentationSectionType.SUB_NORMAL)

        self.play(ReplacementTransform(error_para_1_tex.copy(),error_para_3_tex))
        self.wait()
        self.play(Write(error_sub_3_tex[1]))
        self.wait(1)

        ## == SLIDE ==
        self.next_section('COUPLING_4.4',PresentationSectionType.SUB_NORMAL)

        self.play(Create(box_error_2),Create(box_error_3),Create(box_error_reminder))
        self.wait(1)

        ## == SLIDE == (CLEANING)
        self.next_section('COUPLING_4.5',PresentationSectionType.SUB_SKIP)

        self.play(
            FadeOut(error_sys),
            FadeOut(VGroup(error_sub_2_tex_1,error_sub_2_tex_2)),
            Uncreate(separator_field),
            FadeOut(box_error_2),
            FadeOut(box_error_3),
            FadeOut(box_error_reminder),
        )
        self.play(VGroup(error_reminder_tex,error_sub_1_tex[2],error_sub_3_tex).animate.arrange(DOWN, buff = 0.5).shift(0.5*UP))
        self.wait(1)

        # ===============
        # PRESERVING PROPERTY (II)
        # ===============

        preserving_tex = Tex(r"We must have ",r"$\lVert $",r"${\hat{x}_{\lVert}}^{T1}(T_{\ell})$",r"$ - $",r"$\hat{x}^{T1}(T_{\ell})$",r"$ \lVert \approx C_{\lVert}\mathrm{e}^{-\mu T_\ell}$").set_color_by_tex('\hat{x}_',DEMARK_COLOR).set_color_by_tex('$\hat{x}^',OBS_COLOR).set_color_by_tex('$x',STATE_COLOR).shift(1.5*DOWN)

        rate_tex = Tex(r"If RK4 : ",r"$(\Delta_t)_{\ell+1} \leq \left(((\Delta_t)_{\ell})^4 \mathrm{e}^{-\mu T}\right)^{1/4}, \quad \forall \ell \leq 1$").shift(2.5*DOWN)

        box_preserving = SurroundingRectangle(VGroup(preserving_tex,rate_tex), color = DEMARK_COLOR, buff = 0.2, corner_radius = 0.2)

        ## ANIM

        ## == SLIDE ==
        self.next_section('COUPLING_5',PresentationSectionType.NORMAL)

        self.play(Write(preserving_tex))
        self.wait(1)
        self.play(Write(rate_tex))
        self.play(Create(box_preserving))
        self.wait(1)

        ## == SLIDE == (CLEANING)
        self.next_section('COUPLING_5.1',PresentationSectionType.SUB_SKIP)

        self.play(
            Unwrite(title),
            FadeOut(VGroup(error_reminder_tex,error_sub_1_tex[2],error_sub_3_tex)),
            Unwrite(rate_tex),
            Unwrite(preserving_tex),
            Uncreate(box_preserving),
            Unwrite(technicality_tex_2)
        )
        self.wait(1)

# ==============================================
# RESULTS SCENE
# Present the results of Paraexp applied to a
# Luenberger observer with a 2D wave equation
# ==============================================

class F_Results(Scene):
    def construct(self):

        # ===============
        # COLOR MANAGMENT
        # ===============

        Tex.set_default(color = FRONT_COLOR,font_size = 30)
        MathTex.set_default(color = FRONT_COLOR,font_size = 30)
        Mobject.set_default(color = FRONT_COLOR)

        # ===============
        # GRID FOR CONSTRUCTION PURPUSE ONLY
        # ===============

        L1 = Line(start=[- 7.1, 0., 0.], end=[7.1, 0., 0.],stroke_opacity =0.2)
        for i in range(-3,4):
            L1 = VGroup(L1,Line(start=[- 7.1, i, 0.], end=[7.1, i, 0.],stroke_opacity =0.1))

        L2 = Line(start=[0., -4., 0.], end=[0., 4., 0.],stroke_opacity =0.2)
        for i in range(-6,7):
            L2 = VGroup(L2,Line(start=[i, -4., 0.], end=[i, 4., 0.],stroke_opacity =0.1))

        if grid == 1 :
            self.add(L1,L2)

        # ===============
        # TITLE_1 : WAVE
        # ===============

        title_1 = Title("Results : a wave equation",font_size=40)

        # ===============
        # RESULTS WAVE
        # ===============

        wave_tex = Tex(r'2D Wave eq., on $\Omega = [0,2\pi]^2$, $N_x = 9$, obs. space : $\omega$').shift(2.3*UP + 3.35*LEFT).scale(28/30)
        wave_ul = Underline(wave_tex)

        eff_tex = Tex(r"Efficiency = $\frac{\textit{cputime(non-parallel)}}{\textit{\# computers } \times \textit{ cputime(parallel)}}$").shift(2.3*UP + 3.7*RIGHT).scale(28/30)

        # RESULTS
        #T_list = np.array([0.05, 0.1, 0.5, 1, 2, 5, 10, 15])
        T_list = 10**np.arange(-1.5,1.3+0.4,0.4)
        Efficiency_p4_s08 = np.array([0.6201, 0.8199, 0.9114, 0.9454, 0.9113, 0.8923, 0.7098, 0.2376])
        Efficiency_p4_s05 = np.array([0.7080, 0.8413, 0.9461, 0.9504, 0.9843, 0.9644, 0.7733, 0.5146])
        Efficiency_p4_s03 = np.array([0.7197, 0.8606, 0.9366, 0.9675, 0.9779, 0.9359, 1.0031, 1.0117])

        Efficiency_p8_s08 = np.array([0.5757, 0.7740, 0.8737, 0.9340, 0.9035, 0.8844, 0.7186, 0.2420])
        Efficiency_p8_s05 = np.array([0.5849, 0.7800, 0.8904, 0.9369, 0.9949, 0.9664, 0.7774, 0.5201])
        Efficiency_p8_s03 = np.array([0.6047, 0.7829, 0.8909, 0.9551, 0.9644, 0.9535, 1.0059, 1.0092])

        Efficiency_p16_s08 = np.array([0.4080, 0.6358, 0.7788, 0.8715, 0.8849, 0.8711, 0.7058, 0.2362])
        Efficiency_p16_s05 = np.array([0.4087, 0.6309, 0.7898, 0.8789, 0.9600, 0.9471, 0.7560, 0.5056])
        Efficiency_p16_s03 = np.array([0.4334, 0.6478, 0.8034, 0.8979, 0.9342, 0.9112, 0.9870, 0.9973])

        # AXES
        axes_results_p4 = Axes(
            #x_range = [-1,16,5],
            x_range = [-1.5,1.3,0.5],
            y_range = [-0.05,1,0.2],
            x_length = 3.5,
            y_length = 3.5,
            tips = False,
            #x_axis_config = {"include_numbers": True, "font_size": 20},
            x_axis_config = {"include_numbers": False, "font_size": 20, "scaling": LogBase(custom_labels=True), "include_ticks" :True},
            y_axis_config = {"include_numbers": True, "font_size": 20},
        )

        dict_values = {0.1 : Tex(r"$10^{-1}$"), 1 : Tex(r"$10^{0}$"), 10 : Tex(r"$10^{1}$")}
        axes_results_p4.get_axes()[0].add_labels(dict_values),

        x_lab_results_p4 = axes_results_p4.get_x_axis_label("T = |W_\ell|").scale(0.7).shift(0.4*LEFT+0.7*DOWN)
        y_lab_results_p4 = axes_results_p4.get_y_axis_label("Eff").scale(0.7).shift(0.4*LEFT)
        lab_results_p4   = VGroup(x_lab_results_p4,y_lab_results_p4)

        axes_results_p8  = axes_results_p4.copy()
        lab_results_p8   = lab_results_p4.copy()
        axes_results_p16 = axes_results_p4.copy()
        lab_results_p16  = lab_results_p4.copy()

        axes_results_p4.shift(4.5*LEFT)
        lab_results_p4.shift(4.5*LEFT)
        axes_results_p16.shift(4.5*RIGHT)
        lab_results_p16.shift(4.5*RIGHT)

        VGroup(axes_results_p4,lab_results_p4,axes_results_p8,lab_results_p8,axes_results_p16,lab_results_p16).shift(1*DOWN)

        h = (3.5-0.05)/4

        red_zone_p4  = Rectangle(width = 3.5, height=(3.5-0.05)/4, color = RED, fill_opacity = 0.2 ,stroke_opacity = 0).move_to(axes_results_p4.get_center()).shift(1.07*DOWN+0.25*RIGHT)
        red_zone_p8  = Rectangle(width = 3.5, height=(3.5-0.05)/8, color = RED, fill_opacity = 0.2 ,stroke_opacity = 0).move_to(axes_results_p8.get_center()).shift((1.07+h/4)*DOWN+0.25*RIGHT)
        red_zone_p16 = Rectangle(width = 3.5, height=(3.5-0.05)/16, color = RED, fill_opacity = 0.2 ,stroke_opacity = 0).move_to(axes_results_p16.get_center()).shift((1.11+h/3)*DOWN+0.25*RIGHT)

        axes_titles = VGroup(
            Tex(r'computers = 4').shift(4.5*LEFT),
            Tex(r'computers = 8'),
            Tex(r'computers = 16').shift(4.5*RIGHT),
        ).shift(3.2*DOWN)

        footnote5 = VGroup(
            Tex("[5] Bardos, Lebau, Rauch. 'Sharp sufficient conditions for the observation",font_size=20),
            Tex(", control, and stabilization of waves from the boundary.' (1992)",font_size=20),
        ).arrange(RIGHT, buff= 0.05).to_corner(DL).shift(0.35*DOWN)

        # RESULTS LEGEND
        line_dot_s08 = VGroup(Line([-0.75,0,0],[0.75,0,0], color = BLUE),Dot( stroke_width=3, fill_color=BLUE))
        legend_s08 = VGroup(line_dot_s08, Tex(r': $|\omega|=0.85|\Omega|$',font_size=25)).arrange(buff = 0.1)

        line_dot_s05 = VGroup(Line([-0.75,0,0],[0.75,0,0], color = RED),Dot( stroke_width=3, fill_color=RED))
        legend_s05 = VGroup(line_dot_s05, Tex(r': $|\omega|=0.5|\Omega|$',font_size=25)).arrange(buff = 0.1)

        line_dot_s03 = VGroup(Line([-0.75,0,0],[0.75,0,0], color = GREEN),Dot( stroke_width=3, fill_color=GREEN))
        legend_s03 = VGroup(line_dot_s03, Tex(r': $|\omega|=0.35|\Omega|$',font_size=25)).arrange(buff = 0.1)

        legend_group = VGroup(legend_s08,legend_s05,legend_s03).arrange(buff=1).shift(1.5*UP)

        # RESULTS GRAPH
        ### Results p=4

        results_p4_s08 = axes_results_p4.plot_line_graph(T_list,Efficiency_p4_s08,
            line_color=BLUE,
            vertex_dot_style=dict(stroke_width=3,  fill_color=BLUE)
        )
        results_p4_s05 = axes_results_p4.plot_line_graph(T_list,Efficiency_p4_s05,
            line_color=RED,
            vertex_dot_style=dict(stroke_width=3,  fill_color=RED)
        )
        results_p4_s03 = axes_results_p4.plot_line_graph(T_list,Efficiency_p4_s03,
            line_color=GREEN,
            vertex_dot_style=dict(stroke_width=3,  fill_color=GREEN)
        )

        ### Results p=8

        results_p8_s08 = axes_results_p8.plot_line_graph(T_list,Efficiency_p8_s08,
            line_color=BLUE,
            vertex_dot_style=dict(stroke_width=3,  fill_color=BLUE)
        )
        results_p8_s05 = axes_results_p8.plot_line_graph(T_list,Efficiency_p8_s05,
            line_color=RED,
            vertex_dot_style=dict(stroke_width=3,  fill_color=RED)
        )
        results_p8_s03 = axes_results_p8.plot_line_graph(T_list,Efficiency_p8_s03,
            line_color=GREEN,
            vertex_dot_style=dict(stroke_width=3,  fill_color=GREEN)
        )

        ### Results p=16

        results_p16_s08 = axes_results_p16.plot_line_graph(T_list,Efficiency_p16_s08,
            line_color=BLUE,
            vertex_dot_style=dict(stroke_width=3,  fill_color=BLUE)
        )
        results_p16_s05 = axes_results_p16.plot_line_graph(T_list,Efficiency_p16_s05,
            line_color=RED,
            vertex_dot_style=dict(stroke_width=3,  fill_color=RED)
        )
        results_p16_s03 = axes_results_p16.plot_line_graph(T_list,Efficiency_p16_s03,
            line_color=GREEN,
            vertex_dot_style=dict(stroke_width=3,  fill_color=GREEN)
        )

        ## ANIM

        ## == SLIDE ==
        self.next_section('RESULTS',PresentationSectionType.SKIP)

        self.play(Write(title_1))
        self.wait(1)

        ## == SLIDE ==
        self.next_section('RESULTS_1.1',PresentationSectionType.SUB_NORMAL)

        self.play(
            FadeIn(wave_tex),FadeIn(wave_ul),FadeIn(footnote5),
            DrawBorderThenFill(axes_results_p4),Write(lab_results_p4),
            DrawBorderThenFill(axes_results_p8),Write(lab_results_p8),
            DrawBorderThenFill(axes_results_p16),Write(lab_results_p16),
        )
        self.play(Write(axes_titles),Write(eff_tex))
        self.wait()
        self.play(Create(red_zone_p4),Create(red_zone_p8),Create(red_zone_p16))
        self.wait(1)

        ## == SLIDE ==
        self.next_section('RESULTS_1.2',PresentationSectionType.SUB_NORMAL)

        self.play(Create(legend_s08[0]),Write(legend_s08[1]),Create(results_p4_s08,run_time = 2))
        self.wait(1)

        ## == SLIDE ==
        self.next_section('RESULTS_1.3',PresentationSectionType.SUB_NORMAL)

        self.play(Create(legend_s05[0]),Write(legend_s05[1]),Create(results_p4_s05,run_time = 2))
        self.wait(1)

        ## == SLIDE ==
        self.next_section('RESULTS_1.4',PresentationSectionType.SUB_NORMAL)

        self.play(Create(legend_s03[0]),Write(legend_s03[1]),Create(results_p4_s03,run_time = 2))
        self.wait(1)

        ## == SLIDE ==
        self.next_section('RESULTS_1.5',PresentationSectionType.SUB_NORMAL)

        self.play(Create(results_p8_s08,run_time = 2),Create(results_p16_s08,run_time = 2))
        self.play(Create(results_p8_s05,run_time = 2),Create(results_p16_s05,run_time = 2))
        self.play(Create(results_p8_s03,run_time = 2),Create(results_p16_s03,run_time = 2))
        self.wait(1)

        ## == SLIDE ==
        self.next_section('RESULTS_1.6',PresentationSectionType.SUB_SKIP)

        self.play(
            FadeOut(VGroup(results_p16_s08,results_p16_s05,results_p16_s03)),
            FadeOut(VGroup(results_p8_s08,results_p8_s05,results_p8_s03)),
            FadeOut(VGroup(results_p4_s08,results_p4_s05,results_p4_s03)),
            #FadeOut(VGroup(axes_results_p4,axes_results_p8,axes_results_p16,lab_results_p4,lab_results_p8,lab_results_p16)),
            FadeOut(footnote5),
            Uncreate(legend_s08[0]),Unwrite(legend_s08[1]),
            Uncreate(legend_s05[0]),Unwrite(legend_s05[1]),
            Uncreate(legend_s03[0]),Unwrite(legend_s03[1]),
            #Unwrite(axes_titles),
            #Uncreate(red_zone_p4),Uncreate(red_zone_p8),Uncreate(red_zone_p16),
            FadeOut(wave_ul),FadeOut(wave_tex),
            #Unwrite(eff_tex)
        )

        # ===============
        # TITLE_2 LWWE
        # ===============

        title_2 = Title("Results : linear water waves equations",font_size=40)

        footnote3 = VGroup(
            Tex("[3] Yu, Pei, Xu. 'Estimation of velocity potential of ",font_size=20),
            Tex("water waves using a Luenberger-like observer.' (2020)",font_size=20),
        ).arrange(RIGHT, buff= 0.05).to_corner(DL).shift(0.35*DOWN)

        # ===============
        # RESULTS LWWE
        # ===============

        # RESULTS
        #T_list = np.array([0.05, 0.1, 0.5, 1, 2, 5, 10, 15])
        T_list = 10**np.arange(-2.,1.,0.4)

        Efficiency_p4_g15 = np.array([0.5425, 0.7502, 0.8524, 0.8805, 0.9354, 0.6847, 0.4591, 0.1519])
        Efficiency_p4_g8 = np.array([0.5499, 0.7438, 0.8596, 0.8976, 0.9563, 0.8263, 0.8384, 0.2797])
        Efficiency_p4_g3 = np.array([0.5810, 0.7676, 0.8684, 0.9356, 0.9481, 0.9412, 0.7373, 0.7437])

        Efficiency_p8_g15 = np.array([0.4203, 0.6453, 0.7701, 0.8433, 0.9158, 0.6798, 0.4615, 0.1545])
        Efficiency_p8_g8 = np.array([0.4367, 0.6628, 0.7938, 0.8875, 0.9698, 0.8515, 0.8679, 0.2897])
        Efficiency_p8_g3 = np.array([0.4084, 0.6131, 0.7626, 0.8812, 0.9121, 0.9345, 0.7318, 0.7337])

        Efficiency_p16_g15 = np.array([0.2663, 0.4604, 0.6054, 0.7359, 0.8393, 0.6581, 0.4576, 0.1524])
        Efficiency_p16_g8 = np.array([0.2622, 0.4488, 0.5809, 0.7248, 0.8726, 0.7719, 0.8071, 0.2707])
        Efficiency_p16_g3 = np.array([0.2819, 0.4885, 0.6306, 0.8095, 0.8935, 0.9639, 0.8487, 0.6476])

        # AXES
        axes_results_p4_2 = Axes(
            #x_range = [-1,16,5],
            x_range = [-2.,1.1,0.5],
            y_range = [-0.05,1,0.2],
            x_length = 3.5,
            y_length = 3.5,
            tips = False,
            #x_axis_config = {"include_numbers": True, "font_size": 20},
            x_axis_config = {"include_numbers": False, "font_size": 20, "scaling": LogBase(custom_labels=True), "include_ticks" :True},
            y_axis_config = {"include_numbers": True, "font_size": 20},
        )

        dict_values = {0.1 : Tex(r"$10^{-1}$"), 1 : Tex(r"$10^{0}$"), 10 : Tex(r"$10^{1}$")}
        axes_results_p4_2.get_axes()[0].add_labels(dict_values),

        x_lab_results_p4_2 = axes_results_p4_2.get_x_axis_label("T = |W_\ell|").scale(0.7).shift(0.4*LEFT+1*DOWN)
        y_lab_results_p4_2 = axes_results_p4_2.get_y_axis_label("Eff").scale(0.7).shift(0.4*LEFT)
        lab_results_p4_2   = VGroup(x_lab_results_p4_2,y_lab_results_p4_2)

        axes_results_p8_2  = axes_results_p4_2.copy()
        lab_results_p8_2   = lab_results_p4_2.copy()
        axes_results_p16_2 = axes_results_p4_2.copy()
        lab_results_p16_2  = lab_results_p4_2.copy()

        axes_results_p4_2.shift(4.5*LEFT)
        lab_results_p4_2.shift(4.5*LEFT)
        axes_results_p16_2.shift(4.5*RIGHT)
        lab_results_p16_2.shift(4.5*RIGHT)

        VGroup(axes_results_p4_2,lab_results_p4_2,axes_results_p8_2,lab_results_p8_2,axes_results_p16_2,lab_results_p16_2).shift(1*DOWN)

        # RESULTS LEGEND
        line_dot_g15 = VGroup(Line([-0.75,0,0],[0.75,0,0], color = BLUE),Dot( stroke_width=3, fill_color=BLUE))
        legend_g15 = VGroup(line_dot_g15, Tex(r': $\gamma = 15$',font_size=25)).arrange(buff = 0.1)

        line_dot_g8 = VGroup(Line([-0.75,0,0],[0.75,0,0], color = RED),Dot( stroke_width=3, fill_color=RED))
        legend_g8 = VGroup(line_dot_g8, Tex(r': $\gamma = 8$',font_size=25)).arrange(buff = 0.1)

        line_dot_g3 = VGroup(Line([-0.75,0,0],[0.75,0,0], color = GREEN),Dot( stroke_width=3, fill_color=GREEN))
        legend_g3 = VGroup(line_dot_g3, Tex(r': $\gamma = 3$',font_size=25)).arrange(buff = 0.1)

        legend_group = VGroup(legend_g15,legend_g8,legend_g3).arrange(buff=1).shift(1.5*UP)

        # RESULTS GRAPH
        ### Results p=4

        #axes_results_p4.get_axes()[0](x_range = [-2,1,0.4])

        results_p4_g15 = axes_results_p4_2.plot_line_graph(T_list,Efficiency_p4_g15,
            line_color=BLUE,
            vertex_dot_style=dict(stroke_width=3,  fill_color=BLUE)
        )
        results_p4_g8 = axes_results_p4_2.plot_line_graph(T_list,Efficiency_p4_g8,
            line_color=RED,
            vertex_dot_style=dict(stroke_width=3,  fill_color=RED)
        )
        results_p4_g3 = axes_results_p4_2.plot_line_graph(T_list,Efficiency_p4_g3,
            line_color=GREEN,
            vertex_dot_style=dict(stroke_width=3,  fill_color=GREEN)
        )

        ### Results p=8

        results_p8_g15 = axes_results_p8_2.plot_line_graph(T_list,Efficiency_p8_g15,
            line_color=BLUE,
            vertex_dot_style=dict(stroke_width=3,  fill_color=BLUE)
        )
        results_p8_g8 = axes_results_p8_2.plot_line_graph(T_list,Efficiency_p8_g8,
            line_color=RED,
            vertex_dot_style=dict(stroke_width=3,  fill_color=RED)
        )
        results_p8_g3 = axes_results_p8_2.plot_line_graph(T_list,Efficiency_p8_g3,
            line_color=GREEN,
            vertex_dot_style=dict(stroke_width=3,  fill_color=GREEN)
        )

        ### Results p=16

        results_p16_g15 = axes_results_p16_2.plot_line_graph(T_list,Efficiency_p16_g15,
            line_color=BLUE,
            vertex_dot_style=dict(stroke_width=3,  fill_color=BLUE)
        )
        results_p16_g8 = axes_results_p16_2.plot_line_graph(T_list,Efficiency_p16_g8,
            line_color=RED,
            vertex_dot_style=dict(stroke_width=3,  fill_color=RED)
        )
        results_p16_g3 = axes_results_p16_2.plot_line_graph(T_list,Efficiency_p16_g3,
            line_color=GREEN,
            vertex_dot_style=dict(stroke_width=3,  fill_color=GREEN)
        )

        ###

        lwwe_tex = Tex(r'LWWE, $N_x = 128$, $L=1$, $y(x,t) = \eta(x,t)$').shift(2.3*UP + 3.35*LEFT).scale(28/30)
        lwwe_ul = Underline(lwwe_tex)

        ## ANIM

        ## == SLIDE ==
        self.next_section('RESULTS_2',PresentationSectionType.NORMAL)

        self.play(ReplacementTransform(title_1,title_2),FadeIn(lwwe_tex),FadeIn(lwwe_ul),
        ReplacementTransform(axes_results_p4,axes_results_p4_2),ReplacementTransform(lab_results_p4,lab_results_p4_2),
        ReplacementTransform(axes_results_p8,axes_results_p8_2),ReplacementTransform(lab_results_p8,lab_results_p8_2),
        ReplacementTransform(axes_results_p16,axes_results_p16_2),ReplacementTransform(lab_results_p16,lab_results_p16_2),
        #FadeIn(VGroup(axes_results_p4_2,axes_results_p8_2,axes_results_p16_2,lab_results_p4_2,lab_results_p8_2,lab_results_p16_2)),
        #axes_titles.animate.shift(0.3*DOWN)
        )
        self.play(Write(footnote3))
        self.play(Create(results_p4_g15),Create(results_p8_g15),Create(results_p16_g15),Create(legend_g15[0]),Write(legend_g15[1]),run_time = 1)
        self.play(Create(results_p4_g8),Create(results_p8_g8),Create(results_p16_g8),Create(legend_g8[0]),Write(legend_g8[1]),run_time = 1)
        self.play(Create(results_p4_g3),Create(results_p8_g3),Create(results_p16_g3),Create(legend_g3[0]),Write(legend_g3[1]),run_time = 1)
        self.wait(1)

        ## == SLIDE ==
        self.next_section('RESULTS_1.6',PresentationSectionType.SUB_SKIP)

        self.play(
            FadeOut(VGroup(results_p16_g15,results_p16_g8,results_p16_g3)),
            FadeOut(VGroup(results_p8_g15,results_p8_g8,results_p8_g3)),
            FadeOut(VGroup(results_p4_g15,results_p4_g8,results_p4_g3)),
            FadeOut(VGroup(axes_results_p4_2,axes_results_p8_2,axes_results_p16_2,lab_results_p4_2,lab_results_p8_2,lab_results_p16_2)),
            #FadeOut(footnote5),
            Uncreate(legend_g15[0]),Unwrite(legend_g15[1]),
            Uncreate(legend_g8[0]),Unwrite(legend_g8[1]),
            Uncreate(legend_g3[0]),Unwrite(legend_g3[1]),
            Unwrite(axes_titles),
            Uncreate(red_zone_p4),Uncreate(red_zone_p8),Uncreate(red_zone_p16),
            Uncreate(lwwe_ul),Unwrite(lwwe_tex),
            Unwrite(eff_tex),
            FadeOut(footnote3),
        )

        # ===============
        # RESULTS FOLLOWING
        # ===============

        title_3 = Title("Results : following \& leads",font_size=40)

        limitation_1 = Tex(r"$\rightarrow$ ",r"Works similarly for heat equation (1D \& 2D)")

        limitation_2 = Tex(r"$\rightarrow$ ",r"Application to ",r"linear water wave equations",r" : (in progress with N. Desmars)").set_color_by_tex("LWT",DEMARK_COLOR)

        limitation_21 = [Tex(r"$\cdot$ ",r"Convergence of the observer ",r"only when surface fully observed",r" ($y(x,t) = \eta(x,t)$)").set_color_by_tex("only",DEMARK_COLOR),
            Tex(r"$\cdot$ ",r"Naive",r" description of the data assimilation setting").set_color_by_tex("Naive",DEMARK_COLOR),
            Tex(r"$\cdot$ ",r"Go to a ",r"probabilistic",r" setting ? ($y(x,t) = C \eta(x,t) + \varepsilon(x,t)$)").set_color_by_tex("proba",DEMARK_COLOR)
        ]

        limitations = VGroup(limitation_1,limitation_2,
            limitation_21[0],limitation_21[1],limitation_21[2],
        ).arrange_in_grid(cols=1, col_alignments="l").shift(0.8*RIGHT)

        VGroup(*limitation_21).shift(1*RIGHT + 0.3*DOWN)
        limitation_21[2]#.shift(0.1*RIGHT)
        limitations.shift(0.5*LEFT)

        ## ANIM

        ## == SLIDE ==
        self.next_section('RESULTS_2',PresentationSectionType.SKIP)

        self.play(ReplacementTransform(title_2,title_3))
        self.wait(1)

        ## == SLIDE ==
        self.next_section('RESULTS_2.1',PresentationSectionType.SUB_NORMAL)

        self.play(Write(limitations,run_time = 4))
        self.wait(1)

        ## == SLIDE ==
        self.next_section('RESULTS_2.2',PresentationSectionType.SUB_SKIP)

        self.play(
            Unwrite(title_3),
            FadeOut(limitations)
        )
        self.wait(1)

# ==============================================
# END SCENE
# Thanks and bibliography
# ==============================================

class G_End(Scene):
    def construct(self):

        # ===============
        # COLOR MANAGMENT
        # ===============

        Tex.set_default(color = FRONT_COLOR,font_size = DEFAULT_FONT_SIZE)
        MathTex.set_default(color = FRONT_COLOR,font_size = DEFAULT_FONT_SIZE)
        Mobject.set_default(color = FRONT_COLOR)

        # ===============
        # GRID FOR CONSTRUCTION PURPUSE ONLY
        # ===============

        L1 = Line(start=[- 7.1, 0., 0.], end=[7.1, 0., 0.],stroke_opacity =0.2)
        for i in range(-3,4):
            L1 = VGroup(L1,Line(start=[- 7.1, i, 0.], end=[7.1, i, 0.],stroke_opacity =0.1))

        L2 = Line(start=[0., -4., 0.], end=[0., 4., 0.],stroke_opacity =0.2)
        for i in range(-6,7):
            L2 = VGroup(L2,Line(start=[i, -4., 0.], end=[i, 4., 0.],stroke_opacity =0.1))

        if grid == 1 :
            self.add(L1,L2)

        # ===============
        # THANKS & BANNER
        # ===============

        Thanks = Tex("Thanks for your attention !",font_size=40).shift(0.3*UP)
        banner = ManimBanner(dark_theme = not(black_and_white)).scale(0.2)
        banner_tex = Tex("realised with :",font_size=30)
        group_banner = VGroup(banner_tex,banner).arrange(DOWN).shift(3*DOWN+5.5*RIGHT)


        # ===============
        # BIB
        # ===============

        ref_1 = VGroup(
            Tex("[1] Kautsky, Nichols, Van Dooren. ","'Robust pole assignment in linear state feedback.' (1985).",font_size=25)
        ).arrange(RIGHT, buff= 0.05)

        ref_2 = VGroup(
            Tex("[2] Haine, Ramdani. 'Observateurs itératifs, ","en horizon fini. Application à la reconstruction"," de données initiales pour des EDP d'évolution.' (2011).",font_size=25)
        ).arrange(RIGHT, buff= 0.05)

        ref_3 = VGroup(
            Tex("[3] Yu, Pei, Xu. 'Estimation of velocity potential of water waves using a Luenberger-like observer.' (2020).",font_size=25)
        ).arrange(RIGHT, buff= 0.05)

        ref_4 = VGroup(
            Tex("[4] Gander, Güttel."," 'Paraexp : a parallel integrator for "," linear initial-value problems.' (2013).",font_size=25),
        ).arrange(RIGHT, buff=0.05)

        ref_5 = VGroup(
            Tex("[5] Bardos, Lebau, Rauch. 'Sharp sufficient conditions for the observation, control, and stabilization of waves from the boundary.' (1992).",font_size=25),
        ).arrange(RIGHT, buff= 0.05)

        ref_6 = VGroup(
            Tex("[6] The Manim Community Developers. ","Manim – Mathematical Animation Framework (Version v0.15.2)."," https://www.manim.community/. (2022).",font_size=25)
        ).arrange(RIGHT, buff= 0.05)

        ## == SLIDE ==
        self.next_section('END',PresentationSectionType.SKIP)
        self.play(Write(Thanks))
        self.wait(2)

        ## == SLIDE ==
        self.next_section('END.1',PresentationSectionType.SUB_NORMAL)
        self.play(Thanks.animate.shift(2.7*UP))
        self.play(Write(VGroup(ref_1,ref_2,ref_3,ref_4,ref_5,ref_6).arrange_in_grid(cols=1, col_alignments="l")))
        self.play(Write(banner))
        self.play(banner.expand(direction="center"))
        self.wait(1)

        ## == SLIDE ==
        self.next_section('END.1',PresentationSectionType.SUB_NORMAL)
        self.play(Unwrite(banner),Unwrite(Thanks),FadeOut(VGroup(ref_1,ref_2,ref_3,ref_4,ref_5,ref_6)))
        self.wait(1)

# ==============================================
# PDF SLIDES SCENE
# Thanks and bibliography
# ==============================================

class H_PDF_Slides(Scene):
    def construct(self):

        # ===============
        # COLOR MANAGMENT
        # ===============

        Tex.set_default(color = FRONT_COLOR,font_size = DEFAULT_FONT_SIZE)
        MathTex.set_default(color = FRONT_COLOR,font_size = DEFAULT_FONT_SIZE)
        Mobject.set_default(color = FRONT_COLOR)

        # ===============
        # GRID FOR CONSTRUCTION PURPUSE ONLY
        # ===============

        L1 = Line(start=[- 7.1, 0., 0.], end=[7.1, 0., 0.],stroke_opacity =0.2)
        for i in range(-3,4):
            L1 = VGroup(L1,Line(start=[- 7.1, i, 0.], end=[7.1, i, 0.],stroke_opacity =0.1))

        L2 = Line(start=[0., -4., 0.], end=[0., 4., 0.],stroke_opacity =0.2)
        for i in range(-6,7):
            L2 = VGroup(L2,Line(start=[i, -4., 0.], end=[i, 4., 0.],stroke_opacity =0.1))

        if grid == 1 :
            self.add(L1,L2)

        # ===============
        # SLIDE LIST
        # ===============

        slides = [
            ImageMobject("end_slides/thumb_0000.jpg"),
            ImageMobject("end_slides/thumb_0003.jpg"),
            ImageMobject("end_slides/thumb_0008.jpg"),
            ImageMobject("end_slides/thumb_0009.jpg"),
            ImageMobject("end_slides/thumb_0015.jpg"),
            ImageMobject("end_slides/thumb_0017.jpg"),
            ImageMobject("end_slides/thumb_0021.jpg"),
            ImageMobject("end_slides/thumb_0033.jpg"),
            ImageMobject("end_slides/thumb_0038.jpg"),
            ImageMobject("end_slides/thumb_0040.jpg"),
            ImageMobject("end_slides/thumb_0045.jpg"),
            ImageMobject("end_slides/thumb_0046.jpg"),
            ImageMobject("end_slides/thumb_0048.jpg"),
            ImageMobject("end_slides/thumb_0049.jpg"),
            ImageMobject("end_slides/thumb_0050.jpg"),
            ImageMobject("end_slides/thumb_0057.jpg"),
            ImageMobject("end_slides/thumb_0059.jpg"),
            ImageMobject("end_slides/thumb_0066.jpg"),
            ImageMobject("end_slides/thumb_0068.jpg"),
            ImageMobject("end_slides/thumb_0071.jpg"),
            ImageMobject("end_slides/thumb_0074.jpg"),
            ImageMobject("end_slides/Annex.png"),
        ]

        ## == SLIDE ==
        self.next_section('SLIDES',PresentationSectionType.NORMAL)
        self.add(slides[0]),
        self.wait(0.1)
        self.next_section('SLIDES.f',PresentationSectionType.SUB_SKIP)
        self.remove(slides[0]),

        ## == SLIDE ==
        self.next_section('SLIDES.1',PresentationSectionType.SUB_NORMAL)
        self.add(slides[1]),
        self.wait(0.1)
        self.next_section('SLIDES.1f',PresentationSectionType.SUB_SKIP)
        self.remove(slides[1]),

        ## == SLIDE ==
        self.next_section('SLIDES.2',PresentationSectionType.SUB_NORMAL)
        self.add(slides[2]),
        self.wait(0.1)
        self.next_section('SLIDES.2f',PresentationSectionType.SUB_SKIP)
        self.remove(slides[2]),

        ## == SLIDE ==
        self.next_section('SLIDES.3',PresentationSectionType.SUB_NORMAL)
        self.add(slides[3]),
        self.wait(0.1)
        self.next_section('SLIDES.3f',PresentationSectionType.SUB_SKIP)
        self.remove(slides[3]),

        ## == SLIDE ==
        self.next_section('SLIDES.4',PresentationSectionType.SUB_NORMAL)
        self.add(slides[4]),
        self.wait(0.1)
        self.next_section('SLIDES.4f',PresentationSectionType.SUB_SKIP)
        self.remove(slides[4]),

        ## == SLIDE ==
        self.next_section('SLIDES.5',PresentationSectionType.SUB_NORMAL)
        self.add(slides[5]),
        self.wait(0.1)
        self.next_section('SLIDES.5f',PresentationSectionType.SUB_SKIP)
        self.remove(slides[5]),

        ## == SLIDE ==
        self.next_section('SLIDES.6',PresentationSectionType.SUB_NORMAL)
        self.add(slides[6]),
        self.wait(0.1)
        self.next_section('SLIDES.6f',PresentationSectionType.SUB_SKIP)
        self.remove(slides[6]),

        ## == SLIDE ==
        self.next_section('SLIDES.7',PresentationSectionType.SUB_NORMAL)
        self.add(slides[7]),
        self.wait(0.1)
        self.next_section('SLIDES.7f',PresentationSectionType.SUB_SKIP)
        self.remove(slides[7]),

        ## == SLIDE ==
        self.next_section('SLIDES.8',PresentationSectionType.SUB_NORMAL)
        self.add(slides[8]),
        self.wait(0.1)
        self.next_section('SLIDES.8f',PresentationSectionType.SUB_SKIP)
        self.remove(slides[8]),

        ## == SLIDE ==
        self.next_section('SLIDES.9',PresentationSectionType.SUB_NORMAL)
        self.add(slides[9]),
        self.wait(0.1)
        self.next_section('SLIDES.9f',PresentationSectionType.SUB_SKIP)
        self.remove(slides[9]),

        ## == SLIDE ==
        self.next_section('SLIDES.10',PresentationSectionType.SUB_NORMAL)
        self.add(slides[10]),
        self.wait(0.1)
        self.next_section('SLIDES.10f',PresentationSectionType.SUB_SKIP)
        self.remove(slides[10]),

        ## == SLIDE ==
        self.next_section('SLIDES.11',PresentationSectionType.SUB_NORMAL)
        self.add(slides[11]),
        self.wait(0.1)
        self.next_section('SLIDES.11f',PresentationSectionType.SUB_SKIP)
        self.remove(slides[11]),

        ## == SLIDE ==
        self.next_section('SLIDES.12',PresentationSectionType.SUB_NORMAL)
        self.add(slides[12]),
        self.wait(0.1)
        self.next_section('SLIDES.12f',PresentationSectionType.SUB_SKIP)
        self.remove(slides[12]),

        ## == SLIDE ==
        self.next_section('SLIDES.13',PresentationSectionType.SUB_NORMAL)
        self.add(slides[13]),
        self.wait(0.1)
        self.next_section('SLIDES.13f',PresentationSectionType.SUB_SKIP)
        self.remove(slides[13]),

        ## == SLIDE ==
        self.next_section('SLIDES.14',PresentationSectionType.SUB_NORMAL)
        self.add(slides[14]),
        self.wait(0.1)
        self.next_section('SLIDES.14f',PresentationSectionType.SUB_SKIP)
        self.remove(slides[14]),

        ## == SLIDE ==
        self.next_section('SLIDES.15',PresentationSectionType.SUB_NORMAL)
        self.add(slides[15]),
        self.wait(0.1)
        self.next_section('SLIDES.15f',PresentationSectionType.SUB_SKIP)
        self.remove(slides[15]),

        ## == SLIDE ==
        self.next_section('SLIDES.16',PresentationSectionType.SUB_NORMAL)
        self.add(slides[16]),
        self.wait(0.1)
        self.next_section('SLIDES.16f',PresentationSectionType.SUB_SKIP)
        self.remove(slides[16]),

        ## == SLIDE ==
        self.next_section('SLIDES.17',PresentationSectionType.SUB_NORMAL)
        self.add(slides[17]),
        self.wait(0.1)
        self.next_section('SLIDES.17f',PresentationSectionType.SUB_SKIP)
        self.remove(slides[17]),

        ## == SLIDE ==
        self.next_section('SLIDES.18',PresentationSectionType.SUB_NORMAL)
        self.add(slides[18]),
        self.wait(0.1)
        self.next_section('SLIDES.18f',PresentationSectionType.SUB_SKIP)
        self.remove(slides[18]),
        ## == SLIDE ==
        self.next_section('SLIDES.19',PresentationSectionType.SUB_NORMAL)
        self.add(slides[19]),
        self.wait(0.1)
        self.next_section('SLIDES.19f',PresentationSectionType.SUB_SKIP)
        self.remove(slides[19]),
        ## == SLIDE ==
        self.next_section('SLIDES.20',PresentationSectionType.SUB_NORMAL)
        self.add(slides[20]),
        self.wait(0.1)
        self.next_section('SLIDES.20f',PresentationSectionType.SUB_SKIP)
        self.remove(slides[20]),
        ## == SLIDE ==
        self.next_section('SLIDES.21',PresentationSectionType.SUB_NORMAL)
        self.add(slides[21]),
        self.wait(0.1)
        self.next_section('SLIDES.21f',PresentationSectionType.SUB_SKIP)
        self.remove(slides[21]),

class I_Annexes(Scene):
    def construct(self):

        # ===============
        # COLOR MANAGMENT
        # ===============

        Tex.set_default(color = FRONT_COLOR,font_size = DEFAULT_FONT_SIZE)
        MathTex.set_default(color = FRONT_COLOR,font_size = DEFAULT_FONT_SIZE)
        Mobject.set_default(color = FRONT_COLOR)

        # ===============
        # GRID FOR CONSTRUCTION PURPUSE ONLY
        # ===============

        L1 = Line(start=[- 7.1, 0., 0.], end=[7.1, 0., 0.],stroke_opacity =0.2)
        for i in range(-3,4):
            L1 = VGroup(L1,Line(start=[- 7.1, i, 0.], end=[7.1, i, 0.],stroke_opacity =0.1))

        L2 = Line(start=[0., -4., 0.], end=[0., 4., 0.],stroke_opacity =0.2)
        for i in range(-6,7):
            L2 = VGroup(L2,Line(start=[i, -4., 0.], end=[i, 4., 0.],stroke_opacity =0.1))

        if grid == 1 :
            self.add(L1,L2)


        def draw_sattelite():

            LiDAR_tex = Tex("LiDAR").scale(50/30)
            Body = Square(color = FRONT_COLOR)
            Triangl = Triangle(color = FRONT_COLOR).rotate(30*DEGREES).next_to(Body,LEFT,buff=0.05)
            a = [-1.5,1,0]
            b = [-1.5,-1,0]
            semi_lune = ArcBetweenPoints(a, b, radius=-np.sqrt(2),fill_opacity=1)
            wing_1 = Rectangle(width=1.5, height=3*1.5, grid_xstep=1.5, grid_ystep=1.5, color = FRONT_COLOR).next_to(Body,UP)
            wing_2 = Rectangle(width=1.5, height=3*1.5, grid_xstep=1.5, grid_ystep=1.5, color = FRONT_COLOR).next_to(Body,DOWN)

            sattelite = VGroup(Body,Triangl,semi_lune,wing_1,wing_2).scale(0.5).rotate(60*DEGREES).shift(2*(UP + RIGHT)) #LiDAR_tex

            sea = FunctionGraph(
                lambda x: np.cos(x*2*np.pi/0.25) + 0.25*np.cos(x*2*np.pi/0.07-np.pi),
                color=BLUE,
                x_range=[0, 1]
            ).stretch_to_fit_width(7).stretch_to_fit_height(0.5).shift(2*DOWN + LEFT)

            ondes = VGroup(
                Arc(radius = 1, arc_center=Triangl.get_center(), start_angle=1.1*PI),
                Arc(radius = 2, arc_center=Triangl.get_center(), start_angle=1.1*PI),
                Arc(radius = 3, arc_center=Triangl.get_center(), start_angle=1.1*PI),
            )

            return(VGroup(sattelite,sea,ondes).set_stroke(width=2).move_to([0,0,0]))

        sattelite_drawing = draw_sattelite().scale(0.37).to_corner(DL).shift(1.2*RIGHT)

        lwwe_tex = Tex('Annex : linearised water wave equations',font_size=35).to_edge(UP).shift(0.2*UP)

        equation_system_tex = VGroup(
            Tex(r"$\Delta \Phi = 0$"),
            Tex(r"$\partial_t \Phi = -g\eta - \frac{1}{2}\left\vert\nabla \Phi \right\vert^2$"),
            Tex(r"$\partial_t \eta = \partial_z \Phi - \partial_x \Phi \partial_x \eta$"),
            Tex(r"$\partial_z \Phi = 0$"),
            Tex(r"in the fluid domain"),
            Tex(r"on $z = \eta(x,t)$"),
            Tex(r"on $z = \eta(x,t)$"),
            Tex(r"on $z = -h$"),
        ).arrange_in_grid(rows=4,cols=2,col_alignments="ll",buff=(1,0.25),flow_order="dr")

        equation_system_2_tex = VGroup(
            Tex(r"$\partial_t \Phi (x,z,t) + g\eta(x,t) = 0$"),
            Tex(r"$\partial_t \eta(x,t) - \partial_z \Phi(x,z,t) = 0$"),
            Tex(r"on $z = 0$"),
            Tex(r"on $z = 0$")
        ).arrange_in_grid(rows=2,cols=2,col_alignments="ll",buff=(1,0.25),flow_order="dr")

        definition_1_tex = VGroup(
            Tex(r"$U(x,t)$",r"$ = [$",r"$\Phi(x,0,t)$",r"$,$",r"$ \eta(x,t)$",r"$]^T$").set_color_by_tex('x,',STATE_COLOR),
            Tex(r"$\hat{U}(x,t)$",r"$ = [$",r"$\hat{\Phi}(x,0,t)$",r"$, $",r"$\hat{\eta}(x,t)$",r"$]^T$").set_color_by_tex('x,',OBS_COLOR),
        ).arrange_in_grid(rows=2,col_alignments="ll",buff=(1,0.25),flow_order="dr")

        state_system_tex = VGroup(
            Tex(r"$\partial_t $",r"$U(x,t)$",r"$ = A $",r"$U(x,t)$").set_color_by_tex('x',STATE_COLOR),
            Tex(r"$y(x,t)$",r"$ = $",r"$\eta(x,t)$").set_color_by_tex('x',STATE_COLOR),
            Tex(r"$U_0(x)$",r"$ = $",r"$U(x,0)$").set_color_by_tex('x',STATE_COLOR),
        ).arrange_in_grid(rows=3,col_alignments="ll",buff=(1,0.25),flow_order="dr")

        obs_system_tex = VGroup(
            Tex(r"$\partial_t $",r"$\hat{U}(x,t)$",r"$ = A $",r"$\hat{U}(x,t)$",r"$ + L[$",r"$y(x,t)$",r"$ - $",r"$\hat{y}(x,t)$",r"$]$").set_color_by_tex('x',STATE_COLOR).set_color_by_tex('hat',OBS_COLOR),
            Tex(r"$\hat{y}(x,t)$",r"$ = $",r"$\hat{\eta}(x,t)$").set_color_by_tex('x,',OBS_COLOR),
            Tex(r"$U_0(x)$",r"$ = $",r"$U(x,0)$").set_color_by_tex('x,',OBS_COLOR),
        ).arrange_in_grid(rows=3,col_alignments="ll",buff=(1,0.25),flow_order="dr")

        matrix_A = Matrix([[0, "- g I_d"], ["\\partial_z(\\cdot)", 0]],left_bracket="(",right_bracket=")",h_buff=2,element_alignment_corner=UR)
        ent      = matrix_A.get_entries()
        A_tex    = Tex(r"$A = $")

        Matrice = VGroup(A_tex,matrix_A).arrange(buff=0.1)

        system_tex = VGroup(Brace(equation_system_tex,direction=LEFT),equation_system_tex).scale(0.6).to_corner(UL).shift(0.6*DOWN)
        system_2_tex = VGroup(Brace(equation_system_2_tex,direction=LEFT),equation_system_2_tex).scale(0.6).next_to(system_tex,DOWN,buff = 1).align_to(system_tex,LEFT)

        definition_1_tex.scale(0.6).to_corner(UR).shift(0.6*DOWN)
        Matrice.scale(0.6).next_to(definition_1_tex,DOWN,buff = 0.5).shift(1.1*LEFT)
        ent[0].shift(0.15*LEFT)
        ent[3].shift(0.18*LEFT)
        state_system_tex = VGroup(Brace(state_system_tex,direction=LEFT),state_system_tex).scale(0.6).next_to(Matrice,DOWN,buff = 0.5)
        obs_system_tex = VGroup(Brace(obs_system_tex,direction=LEFT),obs_system_tex).scale(0.6).next_to(state_system_tex,DOWN,buff = 0.5)

        state_system_tex.align_to(obs_system_tex,LEFT)

        VGroup(definition_1_tex,state_system_tex,obs_system_tex).shift(1*LEFT)
        ## ANIM

        self.add(sattelite_drawing,lwwe_tex)
        self.add(system_tex,system_2_tex)
        self.add(state_system_tex,definition_1_tex,obs_system_tex)
        self.add(Matrice)



# ==============================================
# BIBLIOGRAPHY
# ==============================================
#
# present in the presentation :
#
# [1] Kautsky, Nichols, Van Dooren. 'Robust pole assignment in linear state feedback.' (1985).
# [2] Liu. 'Locally distributed control and damping for the conservative systems.' (1987).
# [3] Yu, Pei, Xu. 'Estimation of velocity potential of water waves using a Luenberger-like observer.' (2020).
# [4] Gander, Güttel. 'Paraexp : a parallel integrator for linear initial-value problems.' (2013).
# [5] Bardos, Lebau, Rauch. 'Sharp sufficient conditions for the observation, control, and stabilization of waves from the boundary.' (1992).
# [6] The Manim Community Developers. Manim – Mathematical Animation Framework (Version v0.15.2). https://www.manim.community/. (2022).
#
# ==============================================
# ABSTRACT
# ==============================================
#
# Assimilation and identification problems related to hyperbolic systems arise in many fields of applications,
# e.g. weather forecasting, seismology or reconstruction of ocean surface [2, 8, 1, 7]. Despite the growing importance
# of computational issues in these fields, to the best of our knowledge, time parallelization of the assimilation
# procedures has never been investigated either from a practical or from a mathematical point of view. On the other hand,
# the use of such parallelization techniques for optimal control problems is now well documented. The processing
# of data arriving as a continuous stream adds a new level of difficulty, both for the assimilation method, which
# can no longer be based on adjoint computation, and for time parallelization, which usually applies to simulations on bounded,
# predefined time intervals. The problem of adjoint-free assimilation is usually dealt with by observers,
# also called nudging techniques [3], but other methods based on probabilities can also be use [5]. Adapting parallelization
# techniques in time is the core of this presentation.
#
# Our aim is to present a coupling between a time parallelization method and an observer, in order to accelerate the
# data assimilation procedure over unbounded time intervals. We will mainly focus on the algorithm ParaExp [4] for the first part,
# and the Luenberger observer [6] for the second one. We will present both problems individually, and then our solution
# for applying the ParaExp algorithm onto the Luenberger observer over and unbounded time interval. We will then illustrate
# the performance of this technique with some numerical examples over systems governed by evolution partial differential
# equations (PDEs), specifically parabolic and hyperbolic problems. Finally, we aim to apply those parallelization methods
# to data-assimilation problems over a system arising from Linear Wave Theory (LWT).
#
# [1] Reconstruction of Ocean Surfaces From Randomly Distributed Measurements Using a Grid-Based Method,
#     vol. Volume 6 : Ocean Engineering of International Conference on Offshore Mechanics and Arctic Engineering, 2021.
#     doi :10.1115/OMAE2021-62409. V006T06A059.
# [2] M. Asch, M. Bocquet, M. Nodet. Data assimilation : methods, algorithms, and applications.
#     Funamentals of Algorithms. SIAM, 2016.
# [3] D. Auroux, J. Blum, G. Ruggiero. Data assimilation for geophysical fluids : the Diffusive Back and Forth Nudging,
#     vol. 15 of INdAM Series, pp. 139–174. Springer, 2016.
# [4] M. J. Gander, S. Güttel. Paraexp : A parallel integrator for linear initial-value problems.
#     SIAM Journal on Scientific Computing, 35(2), C123–C142, 2013. doi :10.1137/110856137.
# [5] J. M. Lewis, S. Lakshmivarahan, S. Dhall. Dynamic data assimilation : a least squares approach,
#     vol. 13. Cambridge University Press, 2006.
# [6] D. Luenberger. An introduction to observers.
#     Automatic Control, IEEE Transactions on, 16, 596 – 602, 1972. doi :10.1109/TAC.1971.1099826.
# [7] A. Simpson, M. Haller, D. Walker, P. Lynett, D. Honegger. Wave-by-wave forecasting via assimi- lation of marine radar data.
#     Journal of Atmospheric and Oceanic Technology, 37(7), 1269 – 1288, 2020. doi :10.1175/JTECH-D-19-0127.1.
# [8] C. K. Wikle. Atmospheric modeling, data assimilation, and predictability.
#     Technometrics, 47(4), 521–521, 2005. doi :10.1198/tech.2005.s326.
