---
layout: post
title: Low noise current source
image: /images/2016-04-21/BfieldCoils.JPG
category: general
tags: blog
use_math: true
---

{% assign image_link ="images/2016-04-23/" %}


There are 2 primary noise sources we deal with when using an optical qubit, fluctuations in the frequency of the addressing laser and level shifts due to external magnetic field fluctuations. Our experiments rely on constant level shift produced by a DC magnetic field we apply with a pair of helmholtz coils around our chamber, along with smaller cancellation coils which serve to cancel the earths magnetic field. These coils are wound such that we produce about 0.1-5Gauss / Amp at the ion position. Our optical transition has a linear zeeman shift of ~0.5-3MHz / Gauss. 

[insert figure ]

To easily resolve these zeeman levels we apply a field of ~5-6Gauss to (about 10x the earths magnetic field). Requiring about 1A of current through our Helmholtz pair. Now that these levels are frequency resolved, we'd like to address a particular transition, This requires that the frequency fluctuations of each level be ~O(linewidth = 3Hz). So our current source needs to produce ~1Amp of current with <10uA of fluctuation. Operation at the 1-10ppm stability level is difficult. Most experiments in our lab so far have used standard linear power supplies to source the current and then actively track the drifts in the current through measurements of the zeeman level shifts. This procedures works well on short time scales but does not have the bandwidth to cancel any fast time scale fluctuations on the current output, particularly the feedthrough of 60Hz through the power supplies transformer. These fast time scale fluctuations result in increased decoherence when addressing these transitions. 

Here I'll describe the layout and structure of a low noise bi-directional current source for such applications. 

<a href="{{image_link}}QuCCBRD.png">
<img src="{{image_link}}QUCCBRD.png" width="400px"/>
</a>

$$
  \begin{align}
    |\psi_1\rangle &= a|0\rangle + b|1\rangle \\\\
    |\psi_2\rangle &= c|0\rangle + d|1\rangle
  \end{align}
$$

  \begin{align}
    |\psi_1\rangle &= a|0\rangle + b|1\rangle \\\\
    |\psi_2\rangle &= c|0\rangle + d|1\rangle
  \end{align}