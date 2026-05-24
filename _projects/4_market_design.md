---
layout: page
title: Electricity Market Design
img: assets/img/research/Market_Design.png
importance: 4
category: Research Areas
related_publications: true
---

Electricity market design sits at the intersection of economics and engineering, and is critical to the net-zero transition. From an economics perspective, electricity markets determine the transactions and incentives that drive investment, efficiently allocate scarce capacity, and enable new business models. From an engineering perspective, they provide the coordination mechanisms that ensure physical power balance and network feasibility across locations and timescales.

Our research on market design aims to enable the large-scale integration of renewable generation and distributed demand-side flexibility. We bring an engineering and computational focus to these problems, rigorously addressing power network constraints, uncertainty, and the strategic behaviour of market participants. This is inherently multidisciplinary work, and we collaborate closely with researchers from economics, operations research, and social science. We aim to provide new market designs and evidence-backed analysis to system operators and policymakers that help navigate the complex trade-offs between system objectives. Prof. Morstyn is a member of NESO's Expert Panel on Balancing, Settlement, and Dispatch reforms, and was previously part of the Government's Review of Electricity Market Arrangements (REMA) Challenge Group.


<h2 class="category">Key Research Streams</h2>

<b>Market Design for Grid-Edge Flexibility:</b> 
The rollout of millions of flexible grid-edge devices, including electric vehicles, heat-pumps and home/community-scale batteries, motivates the design of new market mechanisms which can coordinate these privately-owned assets while respecting network constraints. We have developed a scalable decentralised architecture for local flexibility markets {% cite morstyn2018designing %}, and shown how uncertainty can be incorporated into local flexibility procurement {% cite essayeh2025optimising %}. We have also developed scalable optimisation approaches for flexibility aggregator revenue stacking across multi-scale markets {% cite paredes2023stacking %}. In {% cite  savelli2023energy %} we identified priority regions in Great Britain where the rollout of demand-side flexibility could offer high system value while simultaneously reducing economic deprivation.


<b>Peer-to-Peer (P2P) Energy Trading:</b> 
Our work first introduced networked matching theory as a mathematical framework for designing decentralised energy markets {%cite morstyn2018bilateral %}. Using this framework, a computationally scalable price-negotiation mechanism enables participants to reach a competitive equilibrium using only local decisions and P2P communication between trading partners. We have extended this work to also incorporate multi-product P2P trading {% cite morstyn2018multiclass %}, decentralised management of network constraints and uncertainty {% cite morstyn2019integrating %}, and integration with local flexibility markets {% cite khorasany2022framework %}. In {% cite morstyn2018using %}, we proposed the federated power plant concept, which enables virtual power plants to be formed bottom-up through P2P transactions. 

<b>Cooperative Game Theory for Energy Coalition Formation:</b> 
Cooperative game theory provides rigorous tools for designing fair and game-theoretically stable profit-sharing mechanisms. Our work proposed and developed cooperative game theory to support optimal energy management between prosumers with diverse energy resources sharing a local network {% cite han2018incentivizing %}. Computational complexity is the key challenge, which we have addressed through novel approaches based on stratified sampling {% cite han2021estimation %} and clustering {% cite han2020scaling %}.

<b>Blockchain Smart Contracts:</b> 
--Distributed ledger technologies offer programmable, trustless settlement infrastructure for energy transactions. We have proposed on-demand flexibility markets via smart contracts to reduce balancing costs in Great Britain (Khalid, Savelli & Morstyn, 2023), explored decentralised autonomous organisation structures for financing, governing, and disbursing revenues of battery storage systems (Savelli, Morstyn et al., 2022), and developed a blueprint for energy system design in the era of central bank digital currencies (Savelli, Hepburn & Morstyn, Technological Forecasting & Social Change 2024).

- On-demand energy flexibility market via smart contracts to help reduce balancing costs in Great Britain
- Towards a distributed autonomous organisation for financing, governing and disbursing revenues of a battery energy storage system
- A blueprint for energy systems in the era of central bank digital currencies


<b>Locational Contracts-for-Difference (CfDs) & CfD Auction Game Theory:</b> 
In {% cite savelli2022putting %} we worked with DESNZ to design an enhancement for the UK Contracts-for-Difference scheme to internalise locational costs associated with network congestion and reserve requirements. A separate stream of research with Dr Ajit Pillai and EDF developed game theoretic models for CfD auctions {% cite kell2023methodology %} and uncertainty-aware bidding strategies {% cite kell2022dealing %}.

<b>Making Resource Adequacy a Private Good:</b> 
--Conventional capacity mechanisms socialise the costs of reliability, creating incentives for free-riding and inefficient investment. We have examined proposals to make resource adequacy a private good — analysing the trade-offs between efficiency, equity, and implementability (Morstyn & Teytelboym, 2021), proposed an insurance paradigm for improving system resilience through distributed investment (Morstyn et al., 2022), and developed an insurance mechanism for electricity reliability differentiation under deep decarbonisation (Morstyn & Teytelboym, 2023).

- Making resource adequacy a private good: The good, the bad, and the ugly
- An insurance paradigm for improving power system resilience via distributed investment
- An insurance mechanism for electricity reliability differentiation under deep decarbonization
