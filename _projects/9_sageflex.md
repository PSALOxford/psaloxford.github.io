---
layout: page
title: "ARIA SAGEflex: Safeguarded AI Agents for Grid-Edge Flexibility"
importance: 1
category: Current Projects
img: assets/img/projects/SAGEflex.png
related_publications: true
---

The transition to net-zero carbon requires integrating millions of grid-edge devices (electric vehicles, heat pumps, batteries) into the Great Britain power system over the next decade. These devices can provide flexibility equivalent to multiple large power plants, but traditional centralised dispatch is infeasible due to computational and communication challenges.

The International Energy Agency’s 3DEN initiative estimates smart flexibility could reduce global network reinforcement costs by USD [$270bn to 2040](https://www.iea.org/reports/digitalisation-and-energy). Multi-Agent Reinforcement Learning (MARL) offers a scalable AI-based coordination solution. However, MARL lacks safety guarantees, preventing industrial adoption by system operators and flexibility aggregators.

At the same time, the Advanced Research + Invention Agency (ARIA) launched a programme to develop “gatekeeper” safe AI (Safeguarded AI), with a specific focus on demonstrating its economic value in real-world applications (TA3). This vision perfectly aligns with the need of power systems, which motivates this project.

The project objectives are:
 <ol>
    <li>Develop a curriculum of test problems varying in scale and complexity</li>
    <li>Develop a software platform for training, testing, benchmarking and scaling-up MARL-based solutions</li>
    <li>Extend the platform capable of ARIA’s gatekeeper AI workflow, and gain application-side requirements to guide the development of gatekeeper AI.</li>
 </ol>

 <div style="text-align: center; margin-top: 2rem;">
   <img src="{{ '/assets/img/projects/SAGEflex_wide.png' | relative_url }}" alt="PSAL Oxford logo" style="max-width: 800px; width: 100%;">
 </div>


<h2 class="category">Team</h2>

- [Thomas Morstyn](/people/#thomas-morstyn)
- [Yihong Zhou](/people/#yihong-zhou)

<h2 class="category">Key outputs</h2>
<ul>
    <li> Proposed gradient-based multi-agent proximal learning (GradMAP) for coordinating large populations of flexible grid-edge devices accounting for network constraints and uncertainty {% cite zhou2026gradmap %} </li>
    <li> Proposes the demonstrates the potential for AI data centres to delivery primary frequency response using reinforcement learning to control real-time power capping across GPU nodes {% cite zhou2026grid %} </li>
</ul>

