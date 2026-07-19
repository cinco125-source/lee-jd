---
layout: page
permalink: /research/
title: research
description: What I work on, and why.
nav: true
nav_order: 2
---

My research sits between **data-driven methods and flight control** — building estimators and controllers that stay reliable under faults, uncertainty, and the loss of GPS, and carrying them onto real flight hardware. Four threads run through most of my work.

### 1 · Data-driven modeling &amp; control

I learn vehicle dynamics directly from data using **sparse identification of nonlinear dynamics (SINDy)**, the **Koopman operator**, and **Gaussian-process regression**, then build controllers on top: nonlinear disturbance observers, model-predictive control, and model-reference adaptive control. The goal is control design that adapts to the vehicle it actually flies on, rather than the model we assumed.

### 2 · Fault diagnosis &amp; fault-tolerant control

For multirotors, eVTOL, and urban air mobility, I develop methods to **detect, isolate, and accommodate** actuator and sensor faults in real time — including control allocation for over-actuated airframes and redundant, voting-based flight-control architectures. Much of this targets the reliability that certifiable air mobility will require.

### 3 · GNSS-denied navigation

When satellite navigation is jammed or unavailable, I estimate a vehicle's position by fusing **quantum magnetometers** and **magnetic-anomaly maps** through **factor graph optimization**, alongside INS/GNSS integration and multi-sensor navigation. This connects estimation theory to real quantum-sensing hardware for passive, GPS-independent positioning.

### 4 · GNC systems &amp; hardware integration

I care about closing the loop between algorithm and airframe: **triple-redundant flight-control computers**, hierarchical voting, **hardware-in-the-loop simulation**, and flight campaigns on platforms from quadrotors to hoverbikes. The algorithms have to survive contact with real hardware, not just simulation.

---

For the full record, see my [publications](/publications/) and [CV](/cv/).
