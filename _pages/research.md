---
layout: page
permalink: /research/
title: research
description: Advanced GNC technologies for future air mobility.
nav: true
nav_order: 2
---

{% include lee_style.liquid %}

My research develops guidance, navigation, and control (GNC) methods that keep aerial vehicles safe under model uncertainty, component faults, and loss of GNSS, and validates them on real flight hardware. It is organized into three fundamental areas and two future directions.

## Fundamentals

<div class="theme-block">
  <img src="/assets/img/publication_preview/lee2025groundeffect.jpg" alt="Sparse online GP-based nonlinear dynamic inversion">
  <div>
    <h3>1 · AI-based guidance &amp; control</h3>
    <p>I learn vehicle dynamics from data with <strong>Gaussian processes</strong>, <strong>SINDy</strong>, and <strong>reinforcement learning</strong>, and use the learned models inside adaptive, incremental, and model-predictive controllers. The aim is a controller that adapts to the vehicle it actually flies, including ground effect, payload changes, and aerodynamic uncertainty.</p>
    <div class="theme-papers">Representative work: SOGPR-based NDI (AST 2025), SINDy-based MPC (IET CTA 2025), GP-based INDI (AST 2024), RL-based σ-modification adaptive autopilot (IJCAS, accepted), RL pursuit-evasion (IJCAS 2025)</div>
  </div>
</div>

<div class="theme-block">
  <img src="/assets/img/publication_preview/lee2026taes.jpg" alt="SINDy-based fault detection and diagnosis for eVTOL">
  <div>
    <h3>2 · Fault diagnosis &amp; fault-tolerant control</h3>
    <p>For multirotors, eVTOL, and UAM, I develop methods that <strong>detect, isolate, and accommodate</strong> actuator and sensor faults in real time. This includes data-driven fault diagnosis with SINDy and Koopman-operator models, kernel-based fault detection, and fault-tolerant control allocation for over-actuated airframes.</p>
    <div class="theme-papers">Representative work: eVTOL FDD with SINDy (IEEE TAES 2026), UAM sensor/actuator FDI (IEEE Sensors 2026), Koopman-based FDI (JIRS 2024, IJCAS 2024), dodecacopter FTC allocation (CEP 2025)</div>
  </div>
</div>

<div class="theme-block">
  <img src="/assets/img/publication_preview/kim2026fgouwb.jpg" alt="Adaptive sliding window factor graph optimization">
  <div>
    <h3>3 · GNSS-denied navigation</h3>
    <p>When satellite navigation is jammed or unavailable, I estimate vehicle position with <strong>factor graph optimization</strong>, combining INS with UWB, terrain, and <strong>quantum magnetometer</strong> measurements of the magnetic anomaly field. This work connects estimation theory to quantum sensing hardware for passive navigation.</p>
    <div class="theme-papers">Representative work: adaptive sliding window FGO for UWB/INS (AST 2026), FGO-based magnetic navigation with a quantum magnetometer (IPNT 2026)</div>
  </div>
</div>

## Future directions

<div class="theme-block">
  <img src="/assets/img/outreach/hoverbike.jpg" alt="Full-scale hoverbike test vehicle">
  <div>
    <h3>4 · Digital twin &amp; integrated validation</h3>
    <p>I build digital twins that are updated with flight data, together with <strong>hardware-in-the-loop</strong> test benches and custom <strong>redundant flight control computers</strong>, so that an algorithm can move from simulation to flight with the same software. Platforms range from quadrotors to a full-scale hoverbike.</p>
  </div>
</div>

<div class="theme-block">
  <img src="/assets/img/publication_preview/jo2026ijcas.jpg" alt="Learning-based scheduler on top of a model-based autopilot">
  <div>
    <h3>5 · Certifiable AI flight control</h3>
    <p>Learning-based controllers need to satisfy the same requirements as conventional ones before they can fly in certified aircraft. I study <strong>handling-qualities requirements</strong> (e.g., MIL-STD-1797, ADS-33) as design constraints, <strong>run-time assurance</strong> that switches between AI and classical controllers, and requirement-driven reinforcement learning.</p>
  </div>
</div>

Videos of these experiments are on the [home page](/#research-highlights).

For the full record, see my [publications](/publications/) and [CV](/cv/).
