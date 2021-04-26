---
title: 201 - Particle Detector  
---

**Contents**
* TOC
{:toc}

## What is the Detector for Particle Physics Experiment?
Detectors widely used in particle physics experiments extract signals in the
form of either photons or electrical current when particles pass through the detector material.
In addition, precise timing resolution is demanded especially for experiments in modern era
which is the characteristic different from others, for example,  some of key detectors
used in astrophysics having long timing gate, human eyes etc.
Capability of reproducing the event topology by means of hit position information
is also commonly required for the particle detectors.   <br>

Those detectors are classifiable from several perspective, and the following examples are some of the typical classification. <br>


## Classification of detectors by signals:          
### 1a) Producing photons as signal
  - Cherenkov detectors (RICH, ...)            
  - Counters (TOF, ...)   

### 1b) Producing electrical current as signal   
  - Silicon detectors (pixel/microstrip, ...)                   
  - Wire chambers (MWDC, ...), TPC
  - ...

<br>  

## Classification of detectors by measurement purposes:   
### 2a) Measurement of particle Momentum  
  - Silicon strip detectors
  - Drift chambers  

### 2b) Measurement of particle Vertex    
  - Silicon pixel detectors

### 2c) Measurement of particle Energy    
  - Calorimeters (ECal/HCal)

### 2d) Measurement of particle ID          
  - Drift chambers
  - TOFs
  - RICH
  - ...


<br>
**Above list/format is a first template (March 6th, 2021).   <br>



## Silicon Carbide
### 3a）Crystal structure of silicon carbide
One of the differences between silicon carbide and silicon: silicon carbide has a polycrystalline crystal structure, such as 3C, 4H, 6H.

<center>
<img src="/images/sic_hexagonal.png" width="500"/>
</center>

<center>
<font size=2 >
Figure 1. Crystal orientations in a hexagonal SiC polytype.(Reference:Synopsys.TCAD Sentaurus™ Tutorial.Sentaurus Device)
</font>
</center>

In hexagonal crystal structures, four Miller indices (a1, a2, a3, c) are commonly used to indicate directions.
However, it can be proved that there are the following relations between a1, a2 and a3: a1 + a2 + a3 = 0.
Therefore, it is simple and efficient to use only three Miller indices (a1, a2, and c) to indicate the direction, regardless of a3.
For example, the direction [11(-2)0] is simplified as as {1 1 0}.  <br>

### 3b) Layer structure of SiC
Both 4H-SiC and 6H-SiC lattices belong to hexagonal lattice structure, and the difference lies in the sequence of accumulation layers.For 4H-SiC, the deposit order is ABCB and for 6H-SiC, the deposit order is ABCACB.as shown in Figure 2.

<center>
<img src="/images/sd_sic_polytypes.png" width="500"/>
</center>

<center>
<font size=2 >
Figure 2. Layer structure of SiC (towards [0001] direction) with (left) tetrahedrally bonded carbon 
  atoms linked to three Si atoms within the bilayer and (right) shown together with the stacking sequences for 4H-SiC and 6H-SiC polytypes.(Reference:Synopsys.TCAD Sentaurus™ Tutorial.Sentaurus Device)
</font>
</center>

The direction of accumulation along the upward direction is the C-axis in the previous image, i.e. [0001] direction.

### 3c) Miscut angle
In the process of silicon carbide wafer production, the crystal growth is not completely along the normal direction of the wafer surface,
but there is an angle between the growth direction and the normal direction of the wafer surface.This Angle can be called a miscut Angle.
The miscut angle is usually in the range of 3.5 - 8.5°Field $$\vec{E_w}(\vec{x})$$ ..

<center>
<img src="/images/sp_sic_miscut.png" width="500"/>
</center>

<center>
<font size=2 >
Figure 3. Definition of miscut angle.
  (Reference:Synopsys.TCAD Sentaurus™ Tutorial.Sentaurus Device)
</font>
</center>


**Reference**<br>
[1] Synopsys.TCAD Sentaurus™ Tutorial.Sentaurus Device.v2018. <br>
[2] Synopsys.Sentaurus™ Device User Guide.June 2018.

## Several physical models related to silicon carbide
### 4a) Incomplete Ionization Model
* Dopant Incomplete Ionization <br>
In SiC materials, the impurity atoms are usually located in the deeper energy levels, so it is necessary to consider the degree of ionization of each impurity. <br>
<br>
For some impurity atoms, their ionization energy depends on the position (“h” or “k”) of the lattice they occupy.Table 1 shows the ionization energies of some common impurity atoms in different cell positions. Table 4a.1 shows the ionization energies of several common doped atoms occupying different lattice positions. <br>
<br>

<center>
<img src="/images/JC182-0.png" style="zoom:100%" />
</center>

<center>
<font size=2 >
Table 4a.1. Dopant ionization energies for 4H-SiC.
[1].
</font>
</center>
<br>
* Incomplete Ionization Model
The concentration of ionized impurity atoms in a semiconductor usually follows the Fermi-Dirac distribution: <br>

$$
N_{D}=\frac{N_{D,0}}{1+g_{D}exp(\frac{E_{F,n}-E_{D}}{kT})}
\tag{4a.1}
$$

$$
N_{A}=\frac{N_{A,0}}{1+g_{A}exp(\frac{E_{A}-E_{F,p}}{kT})}
\tag{4a.2}
$$

Another distribution function which is used to consider the incomplete ionization of impurity atoms  in SiC materials:<br>

$$
N_{D}=\frac{N_{D,0}}{1+G_{D}(T)exp(\frac{E_{F,n}-E_{C}}{kT})}
\tag{4a.3}
$$

$$
N_{A}=\frac{N_{A,0}}{1+G_{A}(T)exp(-\frac{E_{F,p}-E_{V}}{kT})}
\tag{4a.4}
$$

Rewrite Eq. 4a.1 and Eq. 4a.2 using carrier concentration as the variable

$$
N_{D}=\frac{N_{D,0}}{1+g_{D}/frac{n}{n_{I}}}
\tag{4a.5}
$$

$$
N_{A}=\frac{N_{A,0}}{1+g_{A}/frac{p}{p_{I}}}
\tag{4a.6}
$$
<br>
Here n1 and p1 are valid when the Boltzmann statistical distribution is used and there is no quantization model. If Ferm-Dirac statistics or quantitative models are used, then n1 and p1 need to be multiplied by the corresponding coefficients γn、γp.<br>
<font size="2">
(Quantization Models:)<br>
At present, some devices (such as MOSFET) have some characteristics of quantum mechanical length dimensions, so the wave of  carriers  can no longer be ignored.The quantitative model is designed to solve the problem of quantum effects.
</font><br /> 


The activation energy of the impurity atom is reduced by the total doping concentration of the impurity. <br>

$$
\DeltaE_{D}=\DeltaE_{D,0}-\alpha_{D}\cdotN_{tot}^{1/3}
$$

$$
\DeltaE_{A}=\DeltaE_{A,0}-\alpha_{A}\cdotN_{tot}^{1/3}
$$

<br>
where $N_{tot}=N_{A,0}+N_{D,0}$ . <br>

## 4H-SiC LGAD
4H-SiC LGAD refers to the design and production of LGAD(Low Gain Avalanche Detectors) in 4H-SiC semiconductor materials. <br>

$$x+y=z$$

### 5a) What is the LGAD & What is the usage
In high energy physics experiments, it is often necessary to determine the position and number of particles. How to detect particles effectively, and how to distinguish the two particles passing before and after in a very short time, has become an important problem in high energy experiments. <br>

The root of this problem lies in the design of the sensors. <br>

Usually the signal generated by a particle is very weak, in order to detect the particles, amplifying the signal was first been considered, but the gain should not be too large, otherwise the SNR will drop. Therefore, the detection target of the sensors is to output the signal with lower gain value (Gain ~10). <br>
Due to the requirement of fast time resolution, it is necessary to consider how to quickly collect the induced charge insider the detectors. <br>

LGAD is one of the detectors designed based on the above considerations. In short, LGAD is a front-end detector that quickly senses incident particles and outputs valid signals.
### 5b) Main Principle
#### (1) Structure

<center>
<img src="/images/PiN_LGAD_Schematic view.png" width="500"/>
</center>

<center>
<font size=2 >
Figure 5b.1.1. Schematic view of a traditional silicon sensor on the left and an LGAD on the right.
[1].
</font>
</center>

The structure of the LGAD is based on standard PIN diodes, where the charge doubling is caused by the gain layer. <br>

The following instructions are based on the device structure shown in the figure 5b.1.2 as below. The thickness of the N-type epitaxial layer of the LGAD (doping concentration of phosphorus is 1E13) is about 100 microns, and the thickness of the N-type substrate (doping concentration of phosphorus is 1E19) is about 350 microns. The doping of the N-type gain layer follows a Gaussian distribution (Gaussian peaks are described in the relevant section). <br>

Figure 5b.1.3 shows an enlarged view near the gain layer.

<center>
<img src="/images/4H-SiC LGAD.png" style="zoom:100%" />
</center>

<center>
<font size=2 >
Figure 5b.1.2. Schematic view of a 4H-SiC LGAD.
</font>
</center>


<center>
<img src="/images/enlarged view of gain layer.png" style="zoom:100%" />
</center>

<center>
<font size=2 >
Figure 5b.1.3. Enlarged view near the gain layer of the 4H-SiC LGAD.
</font>
</center>

#### (2) Working Conditions
The LGAD operates at an external reverse bias voltage that allows it to completely exhaust the device without breaking it down.The electric field at the junction increases significantly in the case of reverse bias, and the peak intensity of the electric field increases with the increase of the amplitude of reverse bias voltage. 

#### (3) The detectors were hit by a particle.
The figure shows what happens when a heavy ion hits the center of the LGAD. <br>

The epitaxial layer of the LGAD shown in the figure is about 100 microns and the substrate is about 350 microns.Heavy ions incident vertically from the center of the device.
The gradient of color from red to green in the image shows the gradient of carrier concentration due to heavy ion collision ionization. <br>

<center>
<img src="/images/Heavy ion incident.png" style="zoom:100%" />
</center>

<center>
<font size=2 >
Figure 5b.4.1. Schematic diagram of the ionized carrier concentration when the heavy ion incident.
</font>
</center>

Because the electric field at the PN junction increases significantly in the case of reverse bias.This allows an avalanche multiplier to be sent before the small number of electrons ionised by the incident particle collisions are absorbed by the electrodes, resulting in appreciable gains.



##### (3.1)  Radiation Models
The LGAD operates under a completely depleted external reverse bias, which produces a signal proportional to the energy deposited by the incident radiation. <br>
###### Gamma Radiation

###### Alpha Particles

###### Heavy Ions


##### (3.2) Avalanche impact ionization

#### (4) Charge Collection
When the epitaxial layer of LGAD is completely exhausted, the space charge in this space will generate an approximately uniform electric field, which can accelerate the effect of ionized particles, so that the particles can be quickly collected by the electrode plate. <br>


If the epitaxial layer of the device is not completely depleted and the depletion layer is correspondently thinned , the range of uniform electric field in the epitaxial layer must decrease along with it.This will cause the carrier can not be accelerated to enough speed, can not be absorbed in a short time. <br>


**Reference**<br>
[1] M. Ferrero et al.,Evolution of the design of ultra fast silicon detector to cope with high
irradiation fluences and fine segmentation,2020 JINST 15 C04027. <br>
[2] 












