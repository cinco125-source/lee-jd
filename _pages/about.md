---
layout: about
title: about
permalink: /
subtitle: Postdoctoral Researcher (AITA InnoCORE), Ph.D. · <a href='https://www.kaist.ac.kr/en/'>Dept. of Aerospace Engineering, KAIST</a>

profile:
  align: right
  image: prof_pic.jpg
  image_circular: false
  more_info: >
    <p>N27 Building, Room 4117</p>
    <p>KAIST, 291 Daehak-ro, Yuseong-gu</p>
    <p>Daejeon 34141, Republic of Korea</p>
    <p>cinco125@gmail.com</p>

selected_papers: true
social: true

announcements:
  enabled: true
  scrollable: true
  limit: 5

latest_posts:
  enabled: false
  scrollable: true
  limit: 3
---

{% include lee_style.liquid %}

I am a postdoctoral researcher in the **AITA InnoCORE** program at the Department of Aerospace Engineering, **KAIST**. I received my Ph.D. from KAIST under Prof. Hyochoong Bang, and my dissertation received the **KAIST College of Engineering Outstanding Ph.D. Dissertation Award (2026)**.

I work on guidance, navigation, and control (GNC) for aerial vehicles, with a focus on keeping them safe when the model is wrong, a component fails, or GNSS is unavailable. My research has three parts:

- **AI-based guidance and control**: learning vehicle dynamics with Gaussian processes, SINDy, and reinforcement learning, and building adaptive and predictive controllers on top of them.
- **Fault diagnosis and fault-tolerant control**: detecting and isolating actuator and sensor faults in multirotors, eVTOL, and UAM, and reconfiguring the controller in flight.
- **GNSS-denied navigation**: factor graph optimization with quantum magnetometers and magnetic-anomaly maps for navigation without satellite signals.

I validate these methods on hardware, including custom flight control computers, hardware-in-the-loop simulation, and flight tests on platforms from quadrotors to a hoverbike. I received my B.S. from UNIST and my M.S. and Ph.D. from KAIST, and during graduate school I also worked as an AI research engineer at Hanyoung Nux (2021–2024).

I have published more than 20 SCI(E) journal articles, filed 4 patent applications, and received 10 paper awards. See the [research](/research/) and [publications](/publications/) pages, or my [CV](/cv/). Feel free to [reach out](mailto:cinco125@gmail.com).

### Research Highlights {#research-highlights}

<div class="hl-grid">
  <div class="hl-card">
    <div class="hl-media"><iframe src="https://www.youtube-nocookie.com/embed/pGmESKccsKI" title="Data-driven FTC for eVTOL: experiment" loading="lazy" allowfullscreen></iframe></div>
    <div class="hl-body"><div class="hl-tag">Fault Diagnosis &amp; FTC</div><div class="hl-title">Data-driven FTC for eVTOL: experiment</div><p class="hl-desc">Data-driven modeling and fault detection with an actuator fault injected in flight.</p></div>
  </div>
  <div class="hl-card">
    <div class="hl-media"><iframe src="https://www.youtube-nocookie.com/embed/k--g5ymM74U" title="Data-driven FTC for eVTOL: simulation" loading="lazy" allowfullscreen></iframe></div>
    <div class="hl-body"><div class="hl-tag">Fault Diagnosis &amp; FTC</div><div class="hl-title">Data-driven FTC for eVTOL: simulation</div><p class="hl-desc">Data-driven FDD and FTC in forward flight, compared with a baseline controller.</p></div>
  </div>
  <div class="hl-card">
    <div class="hl-media"><iframe src="https://www.youtube-nocookie.com/embed/ayYy44Vw-S8" title="Fault-tolerant control of a coaxial dodecacopter" loading="lazy" allowfullscreen></iframe></div>
    <div class="hl-body"><div class="hl-tag">Fault Diagnosis &amp; FTC</div><div class="hl-title">Fault-tolerant control allocation for a dodecacopter</div><p class="hl-desc">QP-based control allocation validated on a coaxial dodecacopter test jig.</p></div>
  </div>
  <div class="hl-card">
    <div class="hl-media"><iframe src="https://www.youtube-nocookie.com/embed/YEb-C0KXalY" title="SINDy-based MPC for multirotor collision avoidance" loading="lazy" allowfullscreen></iframe></div>
    <div class="hl-body"><div class="hl-tag">AI-based G&amp;C</div><div class="hl-title">SINDy-based MPC for collision avoidance</div><p class="hl-desc">Model predictive control on a dynamics model identified from flight data.</p></div>
  </div>
  <div class="hl-card">
    <div class="hl-media"><iframe src="https://www.youtube-nocookie.com/embed/SKZH87vOsHw" title="Hoverbike flight test" loading="lazy" allowfullscreen></iframe></div>
    <div class="hl-body"><div class="hl-tag">Digital Twin &amp; HILS</div><div class="hl-title">Hoverbike GNC integration</div><p class="hl-desc">GNC algorithm and hardware integration on a full-scale hoverbike.</p></div>
  </div>
  <div class="hl-card">
    <div class="hl-media"><iframe src="https://www.youtube-nocookie.com/embed/Uc1ALYmaBEE" title="Attitude control of a flexible spacecraft" loading="lazy" allowfullscreen></iframe></div>
    <div class="hl-body"><div class="hl-tag">Space Systems</div><div class="hl-title">Flexible spacecraft attitude control</div><p class="hl-desc">Adaptive prescribed performance control with vibration suppression.</p></div>
  </div>
</div>
