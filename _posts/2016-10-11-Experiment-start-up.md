---
layout: post
title: Experiment start up
image: /images/2016-10-05/HOA_OVEN.JPG
category: general
tags: blog

---

{% assign image_link ="/images/2016-10-05/" %}


There is always a lot to write down when starting up a new experiment. One of the things I usually forget are what needs to be running in order for software to function as planned. 


	1. MTservers
		* QuACK - Hansch
		* Power meter - Landau
		* Camera - Landau
		* wavemeter - molmer
	2. Main camera
		* Camera: /usr/local/ImageJ/mmimagej



Finally got 674 spectroscopy working. 

I can see large frequency changes during scans, 5min ish time scale. Looking around for the cause it looks like the power fluctuations to the cavity?


674 power input: 484uW
674 transmission: 32uW


674 power into the cavity varies between 400uW --> 900uW over ~5min time scale. 

damn... its like it is the AOM before the ULE port. This was changed recently to move the experiment AOM's from -200MHz, to +200MHz. This can be nearly completely eliminated by changing the AOM's input polarization by 90deg. Will monitor for an hour to confirm. hmm maybe not, was stable for about 30min, then fluctuations continued as before. I removed the waveplate and again it looked very stable for another 10-20min. The fluctuations seem to be in-sync with the AC. thats possibly the reasons for the 30min-ish stability. 
Going to check the power fluctuations directly after the AOM. 

 going to try changing the fiber. 



fluctuations now seem small enough to compensate by intensity stabilization on the AOM.


other improvements / changes. I saw a huge improvement in the prestabilization lock when trying to add an additional lock to the 2nd modulation port. When this port is configured as a secondary DC-mod input it is not isolated from the first DC-mod input. 