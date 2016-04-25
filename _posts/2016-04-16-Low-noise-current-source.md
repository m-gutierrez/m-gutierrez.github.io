---
layout: post
title: Low noise current source
image: /images/2016-04-21/BfieldCoils.JPG
category: general
tags: blog
---

{% assign image_link ="/images/2016-04-23/" %}


There are 2 primary noise sources we deal with when using an optical qubit, fluctuations in the frequency of the addressing laser and level shifts due to external magnetic field fluctuations. Our experiments rely on constant level shift produced by a DC magnetic field we apply with a pair of helmholtz coils around our chamber, along with smaller cancellation coils which serve to cancel the earths magnetic field. These coils are wound such that we produce about 0.1-5Gauss / Amp at the ion position. Our optical transition has a linear zeeman shift of ~0.5-3MHz / Gauss. 

[insert figure ]

To easily resolve these zeeman levels we apply a field of ~5-6Gauss (about 10x the earths magnetic field). Requiring about 1A of current through our Helmholtz pair. Now that these levels are frequency resolved, we'd like to address a particular transition, This requires that the frequency fluctuations of each level be ~O(linewidth = 3Hz). So our current source needs to produce ~1Amp of current with <10$$\mu A$$ of fluctuation. Operation at the 1-10ppm stability level is difficult. Most experiments in our lab so far have used standard linear power supplies to source the current and then actively track the drifts in the current through measurements of the zeeman level shifts. This procedures works well on short time scales but does not have the bandwidth to cancel any fast time scale fluctuations on the current output, particularly the feedthrough of 60Hz through the power supplies transformer. These fast time scale fluctuations result in increased decoherence when addressing these transitions. 

Here I'll describe the layout and structure of a low noise bi-directional current source for such applications. 

<a href="{{image_link}}QuCCBRD.png">
<img src="{{image_link}}QuCCBRD.png" width="400px"/>
</a>


  \begin{align}
    |\psi_1\rangle &= a|0\rangle + b|1\rangle \\\
    |\psi_2\rangle &= c|0\rangle + d|1\rangle
  \end{align}


The circuit consists of 6 blocks. 

1. Power filtering
2. Current regulation 
3. reference voltage
4. Digital current set
5. Digital logic buffers
6. Temperature stabilization


Most of these circuits are adapted or taken directly from various app-notes or papers on current regulation. I'll try my best to link to those that were the biggest influence.
	
<h2>Power filtering</h2>

<a href="{{image_link}}PowerFilterSCH.png">
<img src="{{image_link}}PowerFilterSCH.png" width="400px"/>
</a>

The power filter section consists of high-current capable pi-filters, with frequency cut offs of \$ f = \frac{ 1} {2\pi \sqrt{LC}} = 2.3kHz \$. The inductor for this filter is a 47$\mu H$ coilcraft SER1390-473 power inductor. Chosen for its high saturation current, and low series resistance, for this device we expect a maximum current of 2-3A. The capacitor is a 100$\mu F$ tantalum capacitor in a 2917 package, which provides about 0.5$\Omega$ of series resistance, enough to nearly critically damp the LC circuit preventing oscillations, $Q = \frac{1}{R} \sqrt{ \frac{ L }{C} } \approx 1$. In addition, to the common mode pi-filter there is also a differential pi-filter with a cut-off frequency of ~2.0$kHz$.

The filter cut off frequency was chosen to match the ripple suppression roll off of the following linear regulators, 78XX and 79XX, which provide >60db of ripple suppression for frequencies <2$kHz$ 
<a href="{{image_link}}RippleRejection.png">
<img src="{{image_link}}RippleRejection.png" width="200px"/>
</a>

The combined pi-filter with the regulator 78XX/79XX provide noise and ripple rejection of >60db from DC-100$kHz$ where the capacitors begin to roll off. 
<a href="{{image_link}}TantalumCapRollOff.png">
<img src="{{image_link}}TantalumCapRollOff.png" width="200px"/>
</a>


<h2> Current regulation</h2>

The heart of this circuit is its current regulation. There seems to be a long standing bench mark for low-noise current sources, which is the <a href="http://scitation.aip.org/content/aip/journal/rsi/64/8/10.1063/1.1143949">Libbrecht-Hall design</a>. Which is targeted at laser-diode current sourcing. This design has remained more or less unchanged with a few more recent publications mainly focused on component choices.  

+ <a href="http://arxiv.org/abs/1604.00374"> Noise reduction of a Libbrecht--Hall style current driver </a>
+ <a href="http://arxiv.org/abs/0805.0015"> An Ultra-High Stability, Low-Noise Laser Current Driver with Digital Control</a>

In these circuits the current is stabilized by the voltage across a sense resistor. This sense resistor and an in series MOSTFET produce a voltage divider from the regulated voltage output. By dynamically tuning the MOSFET resistance via the gate pin the voltage across the sense resistor can be stabilized. Choosing appropriate value for the sense resistor and voltage drop across produces a current which flows through the MOSFET and through the diode to ground. 


This design utilizes the minimum number of components to provide a adjustable and stable current across a connected load. Low-to-medium power MOSFETs can have bandwidths in the 10s of $MHz$ making the p-only feedback controller all that is necessary for stabilization. And the voltages involved in current stabilization all reference Vreg. With the top end of the divider connected to Vreg and the bottom of the sense resistor stabilized to a Vreg-Vref*$\alpha$ where $\alpha$ is given by the divider out of the reference LM399.

There are a few down sides to this design, One concern I have with this circuit is that ground and Vreg and treated very asymmetrically, this could make the diode susceptible to common mode noise. Another point of note is that the circuit supplies only uni-directional current, not ideal for magnetic field generation or degaussing. 

The design presented here consists instead of a direct voltage stabilization across a sense resistor using a high power op-amp. While the addition of a more complex (and slower) active component may increase the noise floor of the current output it also adds the possibility to supply bipolar current. 

<a href="{{image_link}}CurrentRegulation.png">
<img src="{{image_link}}CurrentRegulation.png" width="400px"/>
</a>

This circuit follows these designs

+ <a href="http://scitation.aip.org/content/aapt/journal/ajp/82/8/10.1119/1.4867376"> Kangara1, Hachtel1, Steck et. al.</a>
+ <a href="http://george.ph.utexas.edu/~meyrath/informal/"> Todd Meyrath</a>
+ <a href="http://artofelectronics.net/"> Horowitz and hill, pg 898, 3rd ed. </a> 

here a pair of power op-amps (OPA544) are used to produce a differential current to the load, and an instrumentation amplifier INA128 is used to measure the voltage difference across a sense resistor whose difference with a digital setpoint is feedback to the OPA544 pair. 
In this case the component drift of the OPA544 and gain resistors, and the limited bandwidth of the OPA544 make it necessary to implement a full PID control. This is especially necessary to optimally reduce the noise floor of the load current. These values will be determined for particular inductive loads but an example of choosing these components can be seen in the Horowitz and Hill reference. 

The INA128 provides low input offset voltages, very small drift coefficients, and a very high common mode rejection ratio (CMRR) of >120db

The birdge circuit of the two OPA544 is taken from the OPA2544 data sheet. Two OPA544's are used instead of the single OPA2544 to better distribute heat dissipation. 


<h2> voltage reference </h2>

<a href="{{image_link}}VoltageReference.png">
<img src="{{image_link}}VoltageReference.png" width="400px"/>
</a>

The voltage reference section is pretty basic. A single LM399H providing a 6.95V reference above ground. This is followed by a 10$Hz$ RC filter to limit the integrated NSD to just ~2$\mu V$. 

<h2> Digital set point </h2>

<a href="{{image_link}}DAC.png">
<img src="{{image_link}}DAC.png" width="400px"/>
</a>

The digital set point is provided by an ad5791, a 20bit precision DAC, with buffered reference inputs given by the filtered LM399H and the board ground. A differential output is then generated using the AD5791's internal feedback resistor and a following op-amp AD8676. This uses the AD5791's internal matched resistor to match its 3.2$k \Omega$ output resistor. A 50pF capacitor is placed on its output, in conjunection with its 3.2$k\Omega$ output resistance forms a 1$MHz$ RC filter, which reduces / eliminates glitches when DAC values are changed.

4 control pins are routed to the cards buffer stage. LDAC, SYNC, SCLK, and SDIN. SYNC, SCLK, and SDIN are the minimum necessary to update the device. LDAC is routed in addition to these in order to sync updates between multiple cards. RESET and CLR are tied high, as specified in the datasheet.

<h2> digital logic buffer </h2>

Each card in the QuACK system has a backplane buffer stage. This serves 3 purposes; Firstly, to isolate the FPGA / computer ground and voltage noise from the analog circuits on the card and secondly, to convert the GTLP logic levels used on the backplane to the 3.3V TTL signals used on the card and lastly, to re-clock / re-align data coming from the backplane, allowing clock speeds in excess of 100MHz to be used for communication. 

On this particular card very few of these components are necessary, since only 4 input signals are needed. A Do not place (DNP) tag has been placed on all of the un-used isolators. The GTLP chips while unnecessary are still nice to have as they provide a consistent input impedance across the backplane. 

<h2> temperature stabilization </h2>

Lastly, Their is a far amount of heat generated on this board. And while we've chosen components to minimize the effects of temperature drifts, we'll still need to do better to allow up to 5deg of room temperature and board temperature changes. 
To improve this situation a temperature stabilized heat shield will be placed around the current set and stabilization components. This region is enclosed with a dotted line on the board. This isolates the high-power heat dissipating components from the low power, current stabilization components. We expect <1degC temperature fluctuations within the shield. 

Stabilization is done using a <a href="http://www.teamwavelength.com/products/product.php?part=54">wavelength electronics WHY5640</a>. Combined with a water-jetted aluminum shield and a peilter element.
Both the temperature set point, and thermistor are located within the shield near the voltage reference.


{% highlight ruby linenos %}
def show
  @widget = Widget(params[:id])
  respond_to do |format|
    format.html # show.html.erb
    format.json { render json: @widget }
  end
end
{% endhighlight %}
