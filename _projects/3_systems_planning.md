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

<b>Multi-level Optimisation for Market-Aware Network Investment Planning :</b> investment decisions must anticipate the outcomes of market operation. Multi-level lexicographic  optimisation enables us to model how network investment decisions and cost recovery mechanisms are impacted by wholesale and local market design and operation (Xia, Savelli & Morstyn, Applied Energy 2025). 

<b>Optimisation Under Uncertainty:</b>
Data-driven distributionally robust optimisation enables decisions that are provably robust against true system uncertainty. However, computational complexity is the major barrier for practical implementation. We have developed  a convex inner-approximation which provides 100x speedups without compromising safety and performance {% cite zhou2024strengthened %}. In, {% cite zhou2025fica %} this approache was extended to problems with decision-coupled uncertainty. Important applications include unit commitment, automatic generation control (AGC) participation factor optimisation and transmission network planning {% cite xia2025bilevel%}.

<b>Smart Local Energy System Design:</b>
Designing smart local energy systems requires jointly optimising generation, storage, network reinforcement, and distributed flexibility. We have developed MILP-based optimal sizing strategies integrating EV and heat pump flexibility into planning decisions, demonstrated for the Perth West smart city project (Essayeh & Morstyn, Applied Energy 2023). For climate resilience, networked microgrids can maintain operation under severe wildfire conditions using geospatial fire risk modelling integrated into optimal power flow (Yang, Sparrow, Ashtine, Wallom & Morstyn, Applied Energy 2022). Beyond technical optimisation, we have proposed the concept of "smart energy neighbourhoods" which harness existing social relationships to foster community cooperation towards shared energy objectives (Savelli & Morstyn, Energy Research & Social Science 2021). 

<b>Quantum Computing for Power System Optimisation:</b>
Power system planning problems are combinatorial in nature and computationally intractable at scale with classical methods. We proposed and demonstrated quantum annealing for combinatorial optimal power flow, formulating network upgrade, generation placement, and EV flexibility decisions as a quadratic unconstrained binary optimisation problem solvable on D-Wave hardware (Morstyn, IEEE Transactions on Smart Grid 2023). A comprehensive review in Joule identified wide-ranging opportunities for quantum-accelerated optimisation across net-zero power system planning and operation (Morstyn & Wang, Joule 2024), with follow-on work demonstrating quantum scaling advantage for energy coalition formation with 100+ agents (Mohseni, Morstyn et al., Quantum Science & Technology 2025) and graph-learning-enhanced QAOA for PMU placement (Jiang et al., Quantum Machine Intelligence 2026). Professor Morstyn co-chairs the IEEE PES Task Force on Quantum Computing for Power System Operations.


