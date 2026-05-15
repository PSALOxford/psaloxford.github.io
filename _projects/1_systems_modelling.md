---
layout: page
title: Power Systems Modelling
img: assets/img/research/Modelling.png
importance: 1
category: Research Areas
related_publications: true
---

High-quality modelling is the foundation for effective power system control, planning and market design. The net zero transition is challenging the assumptions which previously enabled simplified and siloed approaches. At the same time, opportunities are created by the new availability of high-speed and granular system monitoring from customer smart meters, phasor measurement units, and market data platforms. 

Our work combines rigorous analytics with the latest computational tools to deliver open models for researchers, industry, and policymakers. Central to our approach is taking seriously the coupling between spatial scales (from local feeders to national transmission), temporal scales (from second-to-second balancing to multi-year network planning), and the interactions between power grid physics, electricity market rules, and strategic decision-making by diverse system actors.

To help advance interdisciplinary research and industry--academic--government collaboration in this area, Prof. Morstyn is co-chairing the IEEE Task Force on Systems Modelling for Electricity Market Design. 

<h2 class="category">Key Research Streams</h2>

<b>GPU-accelerated Power Flow Simulation</b>: We proposed and developed a nonlinear AC power flow solver implemented in JAX, enabling large-scale parallel scenario analysis and data generation for machine learning.

<b>High-fidelity Great Britain (GB) Transmission Network and Balancing Mechanism Modelling:</b> We have developed an open-source [1900-node model](https://github.com/PSALOxford/EnhancedCfD) of GB's transmission network combining data from NESO's Electricity Ten-Year Statement with unit-level market data from Elexon. This has been used to investigate the impact of grid energy storage on balancing costs and carbon emissions {% cite nosratabadi2024impact %}, the value of locational adjustments for renewable contracts-for-difference {% cite savelli2022putting %}, and the value of electric vehicle smart charging for alleviating transmission and distribution network reinforcements {% cite crozier2020opportunity %}.

<b>Open-source Software for Local Energy System Modelling:</b> We developed OPLEM, an open-source software platform for local energy market modelling and design {% cite essayeh2023optimal %}. OPLEM builds upon the OPEN smart local energy system modelling platform, which was developed in collaboration with Professor Malcolm McCulloch {% cite morstyn2020open %}. 

<b>Grid-Edge Device Modelling and Data:</b> We have developed a [dataset](https://github.com/PSALOxford/UKM-PS-info-public) for GB primary distribution substations linked with household heating demand {% cite zhou2024datasets %}. The [Home Energy Data Generator (HEDGE)](https://github.com/floracharbo/hedge) tool provides GAN-based synthetic data generation for residential energy demand and grid-edge device flexibility {% cite charbonnier2024home %}. HEDGE was developed with Dr Flora Charbonnier and Professor Malcolm McCulloch.
