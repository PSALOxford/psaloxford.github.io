---
layout: page
title: Power Systems Planning
img: assets/img/research/Planning.png
importance: 3
category: Research Areas
related_publications: true
---

Investment decisions in generation, transmission, and distribution infrastructure shape power system operation for decades. Getting these decisions right is increasingly difficult: the net-zero transition requires planning across a wider range of spatial and temporal scales, under greater uncertainty from variable renewables and flexible loads, and with growing interdependence between technical constraints, market incentives and government support schemes.

To address this, we develop robust decision-making support tools that reflect the true multi-scale, multi-actor complexity of infrastructure planning. To do this, we work to deeply understand the problems faced by decision-makers and develop solutions that are grounded in rigorous theory and take advantage of the latest advances in computational hardware and algorithms.

<h2 class="category">Key Research Streams</h2>

<b>Multi-level Optimisation for Market-Aware Network Investment Planning :</b> investment decisions must anticipate the outcomes of market operation. Multi-level lexicographic optimisation enables us to model how network investment decisions and cost recovery mechanisms are impacted by wholesale and local market design and operation {% cite xia2025integrating %}. We have also used this approach to address investment cost-recovery in distribution networks with a mix of fixed and nodal pricing {% cite savelli2021electricity %} and coupling between electricity, gas and carbon markets {% cite xia2025scalable %}.

<b>Optimisation Under Uncertainty:</b>
Data-driven distributionally robust optimisation enables decisions that are provably robust against true system uncertainty. However, computational complexity is the major barrier for practical implementation. We have developed a convex inner-approximation which provides 100x speedups without compromising safety and performance {% cite zhou2024strengthened %}. In, {% cite zhou2025fica %} this was extended to problems with decision-coupled uncertainty. Important applications include unit commitment, automatic generation control (AGC) participation factor optimisation and transmission network planning {% cite xia2025bilevel%}.

<b>Smart Local Energy System Design:</b>
The concept of ‘smart local energy systems’ brings together a diverse set of new approaches for integrating and coordinating new grid-edge technologies, including microgrids, active distribution networks, energy communities and multi-energy hubs. We worked with the Perth West smart city project to develop optimal design approaches incorporating local renewables, electric vehicle smart charging and heat pump flexibility {% cite essayeh2023optimal %}. Another stream of work has focused on how networked microgrids can help reduce transmission related wildfire risk without resorting to rolling blackouts {% cite yang2022resilient %}. We also developed the framework of "smart energy neighbourhoods" where community cooperation is harnessed to achieve shared local energy objectives {% cite savelli2021better %}.

<b>Quantum Computing for Power System Optimisation:</b>
Quantum computing offers a fundamentally new computational infrastructure with different capabilities and trade-offs, and is reaching a level of maturity where, for the first time, a practical advantage over classical computing is available for specific applications. Our research first proposed and demonstrated the use of annealing-based quantum computing to accelerate combinatorial optimal power flow problems {% cite morstyn2022annealing %}. We also collaborated with E.ON on quantum computing for energy coalition formation {% cite mohseni2026evidence%}, and with Prof. Yan Li on optimal phasor measurement unit (PMU) placement {% cite jiang2026qaoa %}. Our group's team at the 2025 “Blaise Pascal Quantum Challenge” hackathon won 1st place (€15,000 prize) extending our research to neutral atom devices. A forward-looking review in Joule presents our view of the future opportunities in this area {% cite morstyn2024opportunities %}.
