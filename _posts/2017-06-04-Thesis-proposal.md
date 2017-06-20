---
layout: post
title: Thesis proposal
image: /img/galleries/g02/HOA_Oven_Cavity_THUMB.jpg
category: general
tags: exp

---

{% include addimg.html gal="gal2_Thesisproposal" name="HOA_Oven_Cavity" %}


This post was generated using 

{% highlight python %}
pandoc -f latex -t markdown --no-wrap -o outfile.md infile.tex 
{% endhighlight %}

references can be found in the pdf - [thesis proposal]({{ site.url }}/assets/pdfs/quantum-control_mg.pdf)

# Quantum control for enhanced sensing and information processing with trapped ions

  Introduction 
==============

Trapped ion experiments represent some of the most pristine quantum systems currently demonstrated. For a wide variety of elements research groups have demonstrated complete control of both internal electronic states and external motional degrees of freedom, regularly producing initial states of both with $\>99$% purity. This wide range of control has led and in turn been led by applications of quantum information processing, where precise and accurate manipulation of the quantum state is essential to perform practical algorithms. While proof of principle experiments have been demonstrated @Monz2016 [@Nigmatullin2016; @Debnath2016] scaling to systems with computing power beyond that of classical computers has remained out of reach and is an active area of research. The struggles in developing such a system are two-fold: firstly, universal gate fidelities have yet to reach fault tolerant thresholds required for small code sizes (10’s of physical qubits), and secondly, experiments increasing the number of physical qubits suffer from a number of systematic effects further decreasing the achieved gate fidelities. However, beyond applications to quantum computing the performance achieved in these systems has led to steady improvements in sensing applications, such as atomic clocks @Rosenband2008, magnetometry @Shaniv2017, electrometry @Maiwald2009, and inertial sensors @Campbell2016.

This thesis work progresses both quantum information processing and quantum enhanced sensing through the development of state-of-the-art classical control systems and novel techniques for improved quantum control. In particular we focus on developing techniques which reduce laser control and power overhead required for scaling-up ion trap systems while maximizing the number of parallel quantum logic gates, as well as protocols for phase-sensitive detection of perturbing forces.

 Position-controlled composite quantum logic gates 
===================================================

Quantum processors with hundreds or more qubits promise to deliver significant computational speedups over the best classical systems @VanMeter2013. The limits of physical coherence make large-scale parallelization of primitive quantum operations crucial for realizing a fault-tolerant device @Gottesman2014. Trapped ions are one of the leading candidates for physical qubits due to their consistency—all ions are identical—and large ratio of coherence @Ruster2016 to gate @Mizrahi2014 times. Few-qubit ion systems can now demonstrate simple quantum algorithms @Monz2016 [@Debnath2016] as well as single- and multi-qubit operations within the fault-tolerant regime @Ballance2016 [@Harty2016; @Linke2016; @Blume-Kohout2016].

However, current ion trap systems rely upon bulky free-space optical components and high-power radio-frequency laser modulators, both of which pose daunting technical difficulties @Haffner2008 [@Frohlich2007] to scaling to hundred- or thousand-qubit parallel systems @Meter2006. A major challenge moving forward is managing and optimizing physical resources required to implement high-performing quantum operations at scale. To this end, many proposed architectures identify key resources that offer clear and ready paths toward scaling up to an arbitrary number of qubits @Brown2016 [@Harlander2012; @Leibfried2007].

One promising resource is fine voltage control of trap electrodes, which can be harnessed to displace the confining potential of single ions. Local targeted qubit operations have been proposed and performed using potential displacement in conjunction with static laser interaction zones @Harlander2012 [@Leibfried2007; @Clercq2016; @Nigmatullin2016] or magnetic field gradients @Warring2013 [@Weidt2016]. These schemes can greatly reduce complexity of optical addressing systems, and replace the numerous high-power laser modulators with low-power voltage generators which can be readily integrated on-chip with existing technology @Mehta2014. However, quantum control techniques proposed thus far have focused on using local voltage changes to gate the interaction time by transporting ions to or through designated operation zones. This approach requires each ion to be transported over large distances ($>$100 $\mu$m), greatly limiting the speed and density of parallel operations.

We propose and demonstrate an alternative approach using nanoscale ion movements parallel to the laser beam to implement local phase changes of the global beam. This scheme offers several significant advantages over previous works. First, the number of parallel ion movements per beam pass is limited only by the number of independently controlled electrodes, which is highly scalable. Second, movement operations are local and space efficient: ions remain within a single trapping zone and only undergo sub-micron displacements. Third, we demonstrate position-controlled composite sequences that enable arbitrary and ideal single-qubit operations on each ion in parallel, despite the large inhomogeneities that can arise in a global beam. Experiment configuration and sequence depicted in figure [fig:MotionalPhase] with data for parallel operations in two independently controlled trapping zones, showing $>99$% contrast. Further tomography experiments have been performed demonstrating position-controlled gate-fidelities equivalent to our standard laser-phase implemented operations with $99.990(4)$% process fidelity.

{% include addimg.html gal="gal2_Thesisproposal" name="PositionControlledGate" %}


 Single ion matter-wave interferometry 
=======================================

Trapped ions have set record-level sensitivity for force detection @Biercuk2010 due to their small test-masses and precision control over both internal and external degrees of freedom. A variety of techniques have emerged in the last decade providing <span> $\text{zN}/\sqrt{\text{Hz}}$ </span> (zepto - $10^{-21}$) - <span> $\text{yN}/\sqrt{\text{Hz}}$ </span> (yocto = $10^{-24}$) sensitivities. Recently, a single-ion was used to detect forces as small as 5 yN using an injection-locked phonon laser @Kn??nz2010. Noise measurements representing $\sim1$ <span> $\text{yN}/\sqrt{\text{Hz}}$ </span> forces are routinely made through resolved sideband-spectroscopy @Maiwald2009 to characterize electric-field noise in surface trap devices. Doppler velocimetry has been applied in ensembles to achieve sensitivities of 170<span> $\text{yN}/\sqrt{\text{Hz}}$ </span> @Biercuk2010. These and the majority of techniques have made use of the high-quality factor of the trapped ion oscillator to detect resonant forces. However, technical noise and practical limitations prevent these systems from tuning their resonant frequency arbitrarily and are typically restricted to operate at frequencies in the 100 kHz - 10 MHz regime, preventing the extension of this precision to the low frequency (LF) DC-100 kHz or high frequency (RF) $>$10 MHz regime. A recent experiment utilized Doppler velocimetry to periodically probe a quadrupole transition locking in to off-resonant forces with a minimum detected force of 28 <span> $\text{zN}/\sqrt{\text{Hz}}$ </span> @Shaniv2017, and proposals for observing spontaneous symmetry breaking in Rabi, Jaynes-cumming and Jahn-teller models have estimated sub-<span> $\text{yN}/\sqrt{\text{Hz}}$ </span> sensitivities @Ivanov2016 [@Ivanov2015].

Here we apply matter-wave interferometery protocols to allow linear force measurements. Such techniques have been used in ion systems for characterization of motional-states @Johnson2015, study squeezing and continuous variable quantum computation @Lo2015 and recently proposed for implementing an ion Sagnac interferometer @Campbell2016. This technique, like Doppler velocimetry and spontaneous symmetry breaking proposals, maps a coherent excitation from a driving force to the phase on the internal spin-states. Allowing a much simpler projective measurement over the more cumbersome number-state Fourier series measured in conventional sideband-spectroscopy methods.

The interferometry protocol consists of the following sequence, depicited in figure [fig:Interferometer] 
1 $|\psi_1 \rangle = R_x(\pi/2) | 0 \rangle $  Create super position of spin states, change basis
2  $|\psi_2 \rangle = BS(\gamma)| \psi_1 \rangle =  ( D(\gamma)\sigma_+ + D(-\gamma) \sigma_- ) | \psi_1 \rangle $ - Apply spin-motion enganglement
3  $|\psi_3 \rangle = U_{sense} |\psi_2 \rangle = D(\alpha_F) | \psi_2 \rangle$ - Free evolution, force phase accumulate.
4  $|\psi_4 \rangle = ( D(\gamma)\sigma_+ + D(-\gamma) \sigma_- ) | \psi_3 \rangle $ - undo spin-motion entanglement
5  $|\psi_5 \rangle = R_x(-\pi/2) | \psi_4 \rangle $ - change basis
6  ${ \langle \psi_5 \vert }P_0{ \vert  \psi_5  \rangle }$ - measure

After state preparation of the ${ \vert 0 \rangle }$ state the interferometer sequence begins with a ramsey pulse creating a super position of ${ \vert \pm \rangle } = ({ \vert 0 \rangle } \pm { \vert 1 \rangle })/\sqrt{2}$ states. Next a spin-motion entangling operation is implemented through the use of a bi-chromatic laser pulse at the motional sidebands, followed by a accumulation, sensing, period with a perturbing force generating a displacement operation of $D(\alpha_F)$. After this period, the spin-motion entanglement is un-done mapping the perturbing displacement onto the phase of the spin degree of freedom. Finally, a ramsey pulse maps the accumulated phase onto a population for the following projective measurement of the ${ \vert 0 \rangle }-$-state.

{% include addimg.html gal="gal2_Thesisproposal" name="MatterInterferometer" %}


 Experiment control systems 
============================

Increasing experiment performance inevitably requires improving control hardware; moving more components in-loop, increasing feedback bandwidths, improving sequence timing and synchronicity. These experiments would not be possible without the hardware developed and constructed during the course of this thesis. In this section the major components and their unique attributes are briefly described.

 vacuum systems 
----------------

The experiment vacuum system was designed to accommodate a 100-pin CPGA mounted microfabricated Paul trap, this is the standard package chosen by Sandia national laboratories for their fabricated devices. In addition, optical access is key, as each of these chips provides dozens of trapping zones each can hold 10+ ions. In particular for our device, the High-optical-access trap, a number of high-numerical aperture axes allow for single-ion imaging and addressing. To accommodate these requirements with catalog vacuum hardware, a 6” Kimball physics octagon chamber was chosen with all electrical connections routed through a Accuglass 6” flange housing two subd-50 connectors and a 1-1/3” in viewport. The remaining octagon-ports serve five 2-3/4” viewports and one 6” viewport prodiving ample optical access for multi-zone multi-ion addressing.

 electronic systems 
--------------------

{% include addimg.html gal="gal2_Thesisproposal" name="QuACK" %}

Experiment sequences require nano-second timing resolution over time periods occasionally exceeding 1second and requires $\mu s$ modulation of analog signals within these time frames. The unique requirements in timing, frequency, and voltage resolution led us to develop a suite of custom hardware engineered to meet the experiment requirements and allow for flexible configuration and the ability to scale the system to arbitrary sizes.

As an example of the device requirements, the position-controlled parallel quantum logic gate implementation required the use of seven DDS’s to control laser-based operations of the global qubit beam, addressed doppler cooling and readout beams, Forty-eight DAC’s to perform ion-movement across our trapping device, 5 TTL-out signals for triggering various locks and detection devices and 3 TTL-in signals for triggering and photon counting from two PMT’s. All for an experiment requiring just two zones, single ions and no multi-qubit operations.

 optic systems 
---------------

{% include addimg.html gal="gal2_Thesisproposal" name="PCFBeamDistr" %}


A large amount of optical hardware was developed for this work, including a number of laser systems, optical reference cavities, vapor cells, intensity locks, optical filtering and modulator systems. One of the most novel features implemented in this setup is the use of a photonic crystal fiber (PCF) to route all transition wavelengths along a single beam path. This significantly reduces the optical complexity around the experiment chamber and provides a single fault-point for alignment corrections on all critical beams. We utilize an endlessly single-mode PCF to couple 405, 422, 461, 674, 1033, and 1092nm light using parabolic mirrors and broadband polarizers to produce identical beam trajectories and pure polarizations to the experiment.

 Outlook 
=========

The techniques and hardware developed provides a strong foundation for future quantum information and metrology experiments with trapped ions. The position-controlled quantum logic gates in particular stand out as an area of great promise, not just in the simplification of quantum computing systems but more importantly for sensing applications. In this area trapped ion systems have typically been used as single-ion, single-trap devices, with an experiment housing just one trapping site and that trapping site containing a single ion. This architecture limits sensitivities to the quantum projection noise associated with a single-measurement. By combining the recently achievements incorporating integrated photonics @Mehta2015 into ion trap devices experiments can now tile any number of trapping sites onto a single device and utilizing the position-controlled quantum logic technique one can implement ideal control of each site without additional resource overhead. Providing significant improvements to the systems measurement bandwidth and thus the achievable sensitivities with trapped ions. This approach maintains the high-degree of control and low-systematics associated with single-ion systems while leveraging many simultaneous experiments currently only utilized by neutral atom experiments.


