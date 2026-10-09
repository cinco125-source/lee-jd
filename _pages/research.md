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
    <div class="theme-papers">Representative work<ul><li><a href="/publications/#lee2025groundeffect">Sparse online GP-based robust NDI with ground effect (AST 2025)</a></li><li><a href="/publications/#lee2025sindympc">SINDy-based MPC for collision avoidance (IET CTA 2025)</a></li><li><a href="/publications/#kim2024gpderiv">GP-based state derivative estimator for INDI (AST 2024)</a></li><li><a href="/publications/#jo2026ijcas">RL-based error-gated σ-modification adaptive autopilot (IJCAS, accepted)</a></li><li><a href="/publications/#kim2025pursuit">Guided exploration RL for 3D pursuit-evasion (IJCAS 2025)</a></li></ul></div>
  </div>
</div>

<div class="theme-block">
  <img src="/assets/img/publication_preview/lee2026taes.jpg" alt="SINDy-based fault detection and diagnosis for eVTOL">
  <div>
    <h3>2 · Fault diagnosis &amp; fault-tolerant control</h3>
    <p>For multirotors, eVTOL, and UAM, I develop methods that <strong>detect, isolate, and accommodate</strong> actuator and sensor faults in real time. This includes data-driven fault diagnosis with SINDy and Koopman-operator models, kernel-based fault detection, and fault-tolerant control allocation for over-actuated airframes.</p>
    <div class="theme-papers">Representative work<ul><li><a href="/publications/#lee2026taes">Data-driven FDD for eVTOL using SINDy (IEEE TAES 2026)</a></li><li><a href="/publications/#lee2026uamfdi">Sensor and actuator FDI for UAM (IEEE Sensors J. 2026)</a></li><li><a href="/publications/#lee2024koopmanfdi">Koopman-based FDI for multirotors (JIRS 2024)</a></li><li><a href="/publications/#lee2024koopman">Deep Koopman fault diagnosis with weighted-window EDMD (IJCAS 2024)</a></li><li><a href="/publications/#yoon2025dodeca">Fault-tolerant control allocation for a coaxial dodecacopter (CEP 2025)</a></li></ul></div>
  </div>
</div>

<div class="theme-block">
  <img src="/assets/img/publication_preview/kim2026fgouwb.jpg" alt="Adaptive sliding window factor graph optimization">
  <div>
    <h3>3 · GNSS-denied navigation</h3>
    <p>When satellite navigation is jammed or unavailable, I estimate vehicle position with <strong>factor graph optimization</strong>, combining INS with UWB, terrain, and <strong>quantum magnetometer</strong> measurements of the magnetic anomaly field. This work connects estimation theory to quantum sensing hardware for passive navigation.</p>
    <div class="theme-papers">Representative work<ul><li><a href="/publications/#kim2026fgouwb">Adaptive sliding window FGO with multi-tag UWB/INS (AST 2026)</a></li><li><a href="/publications/#lee2026fgomagnav">FGO-based magnetic navigation with a quantum magnetometer (IPNT 2026)</a></li></ul></div>
  </div>
</div>

## Future directions

<div class="theme-block">
  <img src="/assets/img/research/digital_twin.jpg" alt="Hybrid physics-residual digital twin with a virtual moment sensor">
  <div>
    <h3>4 · Digital twin &amp; integrated validation</h3>
    <p>I build digital twins that are updated with flight data, together with <strong>hardware-in-the-loop</strong> test benches and custom <strong>redundant flight control computers</strong>, so that an algorithm can move from simulation to flight with the same software. Platforms range from quadrotors to a full-scale hoverbike.</p>
  </div>
</div>

<div class="theme-block">
  <img src="/assets/img/research/certifiable_ai_fc.jpg" alt="Handling-quality-guaranteed learning-based flight control">
  <div>
    <h3>5 · Certifiable AI flight control</h3>
    <p>Learning-based controllers need to satisfy the same requirements as conventional ones before they can fly in certified aircraft. I study <strong>handling-qualities requirements</strong> (e.g., MIL-STD-1797, ADS-33) as design constraints, <strong>run-time assurance</strong> that switches between AI and classical controllers, and requirement-driven reinforcement learning.</p>
  </div>
</div>

Videos of these experiments are on the [home page](/#research-highlights).

For the full record, see my [publications](/publications/) and [CV](/cv/).
