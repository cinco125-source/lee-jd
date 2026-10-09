---
layout: about
title: About
permalink: /
subtitle: Postdoctoral Researcher, AITA InnoCORE, <a href='https://www.kaist.ac.kr/en/'>Department of Aerospace Engineering, KAIST</a>

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

I validate these methods on hardware, including custom flight control computers, hardware-in-the-loop simulation, and flight tests on multirotor, eVTOL, and fixed-wing platforms. I received my B.S. from UNIST and my M.S. and Ph.D. from KAIST, and during graduate school I also worked as an AI research engineer at Hanyoung Nux (2021–2024).

I have published 23 SCI(E) journal articles (including accepted papers), filed 4 patent applications, and received 10 paper awards. See the [research](/research/) and [publications](/publications/) pages. Feel free to [reach out](mailto:cinco125@gmail.com).

### Research Highlights {#research-highlights}

<div class="hl-grid">
  <div class="hl-card">
    <div class="hl-media"><a href="https://www.youtube.com/watch?v=pGmESKccsKI" target="_blank" rel="noopener" aria-label="Data-driven FTC for eVTOL: experiment (YouTube)"><img src="https://i.ytimg.com/vi/pGmESKccsKI/hqdefault.jpg" alt="Data-driven FTC for eVTOL: experiment" loading="lazy"><span class="hl-play"></span></a></div>
    <div class="hl-body"><div class="hl-tag">Fault Diagnosis &amp; FTC</div><div class="hl-title">Data-driven FTC for eVTOL: experiment</div><p class="hl-desc">Data-driven modeling and fault detection with an actuator fault injected in flight.</p></div>
  </div>
  <div class="hl-card">
    <div class="hl-media"><video src="/assets/video/evtol_ftc_inner_motor.mp4" poster="/assets/img/outreach/evtol_ftc_poster.jpg" controls muted playsinline preload="none"></video></div>
    <div class="hl-body"><div class="hl-tag">Fault Diagnosis &amp; FTC</div><div class="hl-title">eVTOL fault-tolerant control: flight test</div><p class="hl-desc">Thrust reallocation across eight motors after an inner-motor failure. Also: <a href="/assets/video/evtol_ftc_outer_motor.mp4">outer-motor failure</a>.</p></div>
  </div>
  <div class="hl-card">
    <div class="hl-media"><a href="https://www.youtube.com/watch?v=ayYy44Vw-S8" target="_blank" rel="noopener" aria-label="Fault-tolerant control of a coaxial dodecacopter (YouTube)"><img src="https://i.ytimg.com/vi/ayYy44Vw-S8/hqdefault.jpg" alt="Fault-tolerant control of a coaxial dodecacopter" loading="lazy"><span class="hl-play"></span></a></div>
    <div class="hl-body"><div class="hl-tag">Fault Diagnosis &amp; FTC</div><div class="hl-title">Fault-tolerant control allocation for a dodecacopter</div><p class="hl-desc">QP-based control allocation validated on a coaxial dodecacopter test jig.</p></div>
  </div>
  <div class="hl-card">
    <div class="hl-media"><a href="https://www.youtube.com/watch?v=YEb-C0KXalY" target="_blank" rel="noopener" aria-label="SINDy-based MPC for multirotor collision avoidance (YouTube)"><img src="https://i.ytimg.com/vi/YEb-C0KXalY/hqdefault.jpg" alt="SINDy-based MPC for multirotor collision avoidance" loading="lazy"><span class="hl-play"></span></a></div>
    <div class="hl-body"><div class="hl-tag">AI-based G&amp;C</div><div class="hl-title">SINDy-based MPC for collision avoidance</div><p class="hl-desc">Model predictive control on a dynamics model identified from flight data.</p></div>
  </div>
  <div class="hl-card">
    <div class="hl-media"><a href="https://www.youtube.com/watch?v=SKZH87vOsHw" target="_blank" rel="noopener" aria-label="Hoverbike flight test (YouTube)"><img src="https://i.ytimg.com/vi/SKZH87vOsHw/hqdefault.jpg" alt="Hoverbike flight test" loading="lazy"><span class="hl-play"></span></a></div>
    <div class="hl-body"><div class="hl-tag">System Integration &amp; Flight Test</div><div class="hl-title">Hoverbike GNC integration and auto-landing</div><p class="hl-desc">GNC algorithm and hardware integration on a full-scale hoverbike, with auto-landing flight tests.</p></div>
  </div>
  <div class="hl-card">
    <div class="hl-media"><a href="https://www.youtube.com/watch?v=Uc1ALYmaBEE" target="_blank" rel="noopener" aria-label="Attitude control of a flexible spacecraft (YouTube)"><img src="https://i.ytimg.com/vi/Uc1ALYmaBEE/hqdefault.jpg" alt="Attitude control of a flexible spacecraft" loading="lazy"><span class="hl-play"></span></a></div>
    <div class="hl-body"><div class="hl-tag">Space Systems</div><div class="hl-title">Flexible spacecraft attitude control</div><p class="hl-desc">Adaptive prescribed performance control with vibration suppression.</p></div>
  </div>
</div>

<script>
  // Research Highlights: play YouTube videos inline instead of leaving the page
  document.querySelectorAll('.hl-media a[href*="youtube.com/watch"]').forEach(function (a) {
    a.addEventListener("click", function (e) {
      var id = new URL(a.href).searchParams.get("v");
      if (!id) return;
      e.preventDefault();
      var f = document.createElement("iframe");
      f.src = "https://www.youtube-nocookie.com/embed/" + id + "?autoplay=1&rel=0&modestbranding=1&playsinline=1";
      f.title = a.getAttribute("aria-label") || "Video";
      f.allow = "autoplay; encrypted-media; picture-in-picture; fullscreen";
      f.allowFullscreen = true;
      a.parentNode.replaceChild(f, a);
    });
  });
</script>
