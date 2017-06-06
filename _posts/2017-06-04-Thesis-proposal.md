---
layout: post
title: Thesis proposal
image: /img/galleries/g02/HOA_Oven_Cavity_THUMB.jpg
category: general
tags: exp

---

{% include addimg.html gal="gal2_Thesisproposal" name="HOA_Oven_Cavity" %}

# Introduction


Trapped ion experiments represent some of the most pristine quantum systems currently demonstrated. For a wide variety of elements groups have demonstrated complete control of both internal electronic states and external motional degrees of freedom, regularly producing initial states of both with >99% purity. This wide range of control has led and in turn been led by applications of quantum information processing, where precise and accurate manipulation of the quantum state is essential to perform practical algorithms. While proof of principle experiments have been demonstrated [1,2,3] scaling to systems with computing power beyond that of classical computers has remained out of reach and is an active area of research. The struggles in developing such a system are two-fold: firstly, universal gate fidelities have yet to reach fault tolerant thresholds required for small code sizes (10's of physical qubits), and secondly, experiments increasing the number of physical qubits suffer from a number of systematic effects further decreasing the achieved gate fidelities. However, beyond applications to quantum computing the performance achieved in these systems has led to steady improvements in sensing applications, such as atomic clocks [4], magnetometry [5], electrometry [6], and inertial sensors [7].

This thesis work progresses both quantum information processing and quantum enhanced sensing through the development of state-of-the-art classical control systems and novel techniques for improved quantum control. In particular we focus on developing techniques which reduce laser control and power overhead required for scaling-up ion trap systems while maximizing the number of parallel quantum logic gates, as well as protocols for phase-sensitive detection of perturbing forces. 




# Position-controlled composite quantum logic gates

{% include addimg.html gal="gal2_Thesisproposal" name="MotionalGates" %}


Quantum processors with hundreds or more qubits promise to deliver significant computational speedups over the best classical systems \cite{VanMeter2013}. The limits of physical coherence make large-scale parallelization of primitive quantum operations crucial for realizing a fault-tolerant device~\cite{Gottesman2014}. Trapped ions are one of the leading candidates for physical qubits due to their consistency---all ions are identical---and large ratio of coherence \cite{Ruster2016} to gate \cite{Mizrahi2014} times. Few-qubit ion systems can now demonstrate simple quantum algorithms~\cite{Monz2016, Debnath2016} as well as single- and multi-qubit operations within the fault-tolerant regime~\cite{Ballance2016, Harty2016,Linke2016,Blume-Kohout2016}.

However, current ion trap systems rely upon bulky free-space optical components and high-power radio-frequency laser modulators, both of which pose daunting technical difficulties~\cite{Haffner2008,Frohlich2007} to scaling to hundred- or thousand-qubit parallel systems \cite{Meter2006}. A major challenge moving forward is managing and optimizing physical resources required to implement high-performing quantum operations at scale. To this end, many proposed architectures identify key resources that offer clear and ready paths toward scaling up to an arbitrary number of qubits \cite{Brown2016, Harlander2012,Leibfried2007}.
    
One promising resource is fine voltage control of trap electrodes, which can be harnessed to displace the confining potential of single ions. Local targeted qubit operations have been proposed and performed using potential displacement in conjunction with static laser interaction zones~\cite{Harlander2012, Leibfried2007,Clercq2016,Nigmatullin2016} or magnetic field gradients~\cite{Warring2013, Weidt2016}. These schemes can greatly reduce complexity of optical addressing systems, and replace the numerous high-power laser modulators with low-power voltage generators which can be readily integrated on-chip with existing technology~\cite{Mehta2014}. However, quantum control techniques proposed thus far have focused on using local voltage changes to gate the interaction time by transporting ions to or through designated operation zones. This approach requires each ion to be transported over large distances ($>$100~$\mu$m), greatly limiting the speed and density of parallel operations. 

We propose an alternative approach using nanoscale ion movements parallel to the laser beam to implement local phase changes of the global beam. This scheme offers several significant advantages over previous works. First, the number of parallel ion movements per beam pass is limited only by the number of independently controlled electrodes, which is highly scalable. Second, movement operations are local and space efficient: ions remain within a single trapping zone and only undergo sub-micron displacements. Third, we demonstrate position-controlled composite sequences that enable arbitrary and ideal single-qubit operations on each ion in parallel, despite the large inhomogeneities that can arise in a global beam.


# Single ion matter-wave interferometry 

{% include addimg.html gal="gal2_Thesisproposal" name="MatterInterferometer" %}

Trapped ions have set record-level sensitivity for force detection~\cite{Biercuk2010} due to their small test-masses and precision control over both internal and external degrees of freedom. A variety of techniques have emerged in the last decade providing \NHz{z} (zepto - $10^{-21}$) - \NHz{y} (yocto = $10^{-24}$) sensitivities. Recently, a single-ion was used to detect forces as small as 5~yN using an injection-locked phonon laser~\cite{Kn??nz2010}. Noise measurements representing $\sim1$~\NHz{y} forces are routinely made through resolved sideband-spectroscopy~\cite{Maiwald2009} to characterize electric-field noise in surface trap devices. Doppler velocimetry has been applied in ensembles to achieve sensitivities of 170\NHz{y}~\cite{Biercuk2010}. These and the majority of techniques have made use of the high-quality factor of the trapped ion oscillator to detect resonant forces. However, technical noise and practical limitations prevent these systems from tuning their resonant frequency arbitrarily and are typically restricted to operate at frequencies in the 100~kHz - 10~MHz regime, preventing the extension of this precision to the low frequency (LF) DC-100~kHz or high frequency (RF) $>$10 MHz regime. A recent experiment utilized Doppler velocimetry to periodically probe a quadrupole transition locking in to off-resonant forces with a minimum detected force of 28~\NHz{z}~\cite{Shaniv2017}, and proposals for observing spontaneous symmetry breaking in Rabi, Jaynes-cumming and Jahn-teller models have estimated sub-\NHz{y} sensitivities \cite{Ivanov2016, Ivanov2015}.
    
Here we apply matter-wave interferometery protocols to allow linear force measurements. Such techniques have been used in ion systems for characterization of motional-states~\cite{Johnson2015}, study squeezing and continuous variable quantum computation~\cite{Lo2015} and recently proposed for implementing an ion Sagnac interferometer~\cite{Campbell2016}. This technique, like Doppler velocimetry and spontaneous symmetry breaking proposals, maps a coherent excitation from a driving force to the phase of the internal spin-states. Allowing a much simpler projective measurement over the more cumbersome number-state Fourier series measured in conventional sideband-spectroscopy methods. 



# Experiment control systems

Increasing experiment performance inevitably requires improving control hardware; moving more components in-loop and increasing feedback bandwidths. These experiments would not be possible without the hardware developed and constructed during the course of this thesis. Here the major components and their unique attributes are briefly described.

## vacuum systems
{% include addimg.html gal="gal2_Thesisproposal" name="TwinsExperiment" %}

The Twins experiment vacuum system was designed to accommodate a 100-pin CPGA mounted Paul trap, this is the standard package chosen by Sandia national laboratories for their fabricated devices. In addition optical access is key, as each of these chips provides dozens of trapping zones each can hold 10+ ions. To accommodate this requirements with catalog vacuum hardware a 6in kimball physics chamber was used with all electrical connections routed through a 6in flange housing two db-50 connectors and a 1-1/3'' in viewport. 5x 2 3/4'' viewports and 1x 6in viewport provides ample optical access for multi-zone multi-ion addressing. As well as high-NA imaging axes. 




## electronic systems
{% include addimg.html gal="gal2_Thesisproposal" name="QuACK" %}

Experiment sequences require nano-second timing resolution over time periods occasionally exceeding 1second and requires $\mu s$ modulation of analog signals within these time frames. The unique requirements in timing, frequency, and voltage resolution led us to develop a suite of custom hardware engineered to meet the experiment requirements and allow for flexible configuration and the ability to scale the system to arbitrary sizes. 

As an example of the device requirements, the parallel quantum logic gate implementation required the use of 7x DDS's to control laser-based operations, 48x DAC's to perform ion-movement across our trapping device, 5 TTL-out signals for triggering various locks and detection devices and 3 TTL-in signals for triggering and Photon counting from two PMT's. And this experiment required just two zones, single ions and multi-qubit operations.


## optics systems

{% include addimg.html gal="gal2_Thesisproposal" name="PCFdistr" %}

A large amount of optical hardware was developed for this work, including a number of laser systems, optical reference cavities, vapor cells, intensity locks, optical filtering and modulator systems. One of the most novel features in the twins setup is the use of a photonic crystal fiber to route all transition wavelengths along a single beam path. This significantly reduces the optical complexity around the experiment chamber and provides a fault-point for alignment corrections. We utilize an endlessly single-mode fiber to couple 405, 422, 461, 674, 1033, and 1092nm light using parabolic mirrors and broadband polarizers to produce identical beam trajectories and pure polarizations to the experiment.


# Outlook


# References

	[1] Monz, Thomas, et al. "Realization of a scalable Shor algorithm." Science 351.6277 (2016): 1068-1070.
	[2] Fallek, S. D., et al. "Transport implementation of the Bernstein–Vazirani algorithm with ion qubits." New Journal of Physics 18.8 (2016): 083030.
	[3] Debnath, S., et al. "Demonstration of a small programmable quantum computer with atomic qubits." Nature 536.7614 (2016): 63-66.
	[4] Rosenband, Till, et al. "Frequency ratio of Al+ and Hg+ single-ion optical clocks; metrology at the 17th decimal place." Science 319.5871 (2008): 1808-1812.
	[5] Shaniv, Ravid, and Roee Ozeri. "Quantum lock-in force sensing using optical clock Doppler velocimetry." Nature Communications 8 (2017).
	[6] Maiwald, Robert, et al. "Stylus ion trap for enhanced access and sensing." Nature Physics 5.8 (2009): 551-554.
	[7] Campbell, W. C., and P. Hamilton. "Rotation sensing with trapped ions." arXiv preprint arXiv:1609.00659 (2016).
