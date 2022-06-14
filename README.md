# CANUM 20 (2022) presentation

presentation for the 2022 CANUM 20 Congres : https://canum2020.math.cnrs.fr/accueil/

Lucas Perrin - INRIA Paris - LJLL

lucas.perrin@inria.fr / lucas.perrin@dauphine.eu

June 2022

This presentation was done using Manim :
The Manim Community Developers. (2022). Manim – Mathematical Animation Framework (Version v0.15.2) [Computer software]. https://www.manim.community/

### BIBLIOGRAPHY

present in the presentation :

[1] Kautsky, Nichols, Van Dooren. 'Robust pole assignment in linear state feedback.' (1985).

[2] Liu. 'Locally distributed control and damping for the conservative systems.' (1987).

[3] Yu, Pei, Xu. 'Estimation of velocity potential of water waves using a Luenberger-like observer.' (2020).

[4] Gander, Güttel. 'Paraexp : a parallel integrator for linear initial-value problems.' (2013).

[5] Bardos, Lebau, Rauch. 'Sharp sufficient conditions for the observation, control, and stabilization of waves from the boundary.' (1992).

[6] The Manim Community Developers. Manim – Mathematical Animation Framework (Version v0.15.2). https://www.manim.community/. (2022).


### ABSTRACT

Assimilation and identification problems related to hyperbolic systems arise in many fields of applications,
e.g. weather forecasting, seismology or reconstruction of ocean surface [2, 8, 1, 7]. Despite the growing importance
of computational issues in these fields, to the best of our knowledge, time parallelization of the assimilation
procedures has never been investigated either from a practical or from a mathematical point of view. On the other hand,
the use of such parallelization techniques for optimal control problems is now well documented. The processing
of data arriving as a continuous stream adds a new level of difficulty, both for the assimilation method, which
can no longer be based on adjoint computation, and for time parallelization, which usually applies to simulations on bounded,
predefined time intervals. The problem of adjoint-free assimilation is usually dealt with by observers,
also called nudging techniques [3], but other methods based on probabilities can also be use [5]. Adapting parallelization
techniques in time is the core of this presentation.

Our aim is to present a coupling between a time parallelization method and an observer, in order to accelerate the
data assimilation procedure over unbounded time intervals. We will mainly focus on the algorithm ParaExp [4] for the first part,
and the Luenberger observer [6] for the second one. We will present both problems individually, and then our solution
for applying the ParaExp algorithm onto the Luenberger observer over and unbounded time interval. We will then illustrate
the performance of this technique with some numerical examples over systems governed by evolution partial differential
equations (PDEs), specifically parabolic and hyperbolic problems. Finally, we aim to apply those parallelization methods
to data-assimilation problems over a system arising from Linear Wave Theory (LWT).

[1] Reconstruction of Ocean Surfaces From Randomly Distributed Measurements Using a Grid-Based Method,
    vol. Volume 6 : Ocean Engineering of International Conference on Offshore Mechanics and Arctic Engineering, 2021.
    doi :10.1115/OMAE2021-62409. V006T06A059.

[2] M. Asch, M. Bocquet, M. Nodet. Data assimilation : methods, algorithms, and applications.
    Funamentals of Algorithms. SIAM, 2016.

[3] D. Auroux, J. Blum, G. Ruggiero. Data assimilation for geophysical fluids : the Diffusive Back and Forth Nudging,
    vol. 15 of INdAM Series, pp. 139–174. Springer, 2016.

[4] M. J. Gander, S. Güttel. Paraexp : A parallel integrator for linear initial-value problems.
    SIAM Journal on Scientific Computing, 35(2), C123–C142, 2013. doi :10.1137/110856137.

[5] J. M. Lewis, S. Lakshmivarahan, S. Dhall. Dynamic data assimilation : a least squares approach,
    vol. 13. Cambridge University Press, 2006.

[6] D. Luenberger. An introduction to observers.
    Automatic Control, IEEE Transactions on, 16, 596 – 602, 1972. doi :10.1109/TAC.1971.1099826.

[7] A. Simpson, M. Haller, D. Walker, P. Lynett, D. Honegger. Wave-by-wave forecasting via assimi- lation of marine radar data.
    Journal of Atmospheric and Oceanic Technology, 37(7), 1269 – 1288, 2020. doi :10.1175/JTECH-D-19-0127.1.

[8] C. K. Wikle. Atmospheric modeling, data assimilation, and predictability.
    Technometrics, 47(4), 521–521, 2005. doi :10.1198/tech.2005.s326.
