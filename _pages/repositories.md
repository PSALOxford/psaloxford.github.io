---
layout: page
permalink: /code-and-data/
nav_title: Code & Data
title: Code & Data
description:
nav: true
nav_order: 4
---

{% if site.data.repositories.github_users %}

## GitHub users

<div class="repositories d-flex flex-wrap flex-md-row flex-column justify-content-between align-items-center">
  {% for user in site.data.repositories.github_users %}
    {% include repository/repo_user.liquid username=user %}
  {% endfor %}
</div>

---

{% if site.repo_trophies.enabled %}
{% for user in site.data.repositories.github_users %}
{% if site.data.repositories.github_users.size > 1 %}

  <h4>{{ user }}</h4>
  {% endif %}
  <div class="repositories d-flex flex-wrap flex-md-row flex-column justify-content-between align-items-center">
  {% include repository/repo_trophies.liquid username=user %}
  </div>

---

{% endfor %}
{% endif %}
{% endif %}

<div class="projects">

<h2 class="category">Featured</h2>

<div class="row row-cols-1 row-cols-md-4">

  <div class="col">
    <a href="https://github.com/PSALOxford/OPLEM" target="_blank">
      <div class="card h-100 hoverable">
        <img src="{{ '/assets/img/code/essayeh2024oplem.png' | relative_url }}" alt="OPLEM: Open Platform for Local Energy Markets" class="card-img-top card-img-contain">
        <div class="card-body">
          <h5 class="card-title">OPLEM: Open Platform for Local Energy Markets</h5>
        </div>
      </div>
    </a>
  </div>
  <div class="col">
    <a href="https://github.com/EPGOxford/OPEN" target="_blank">
      <div class="card h-100 hoverable">
        <img src="{{ '/assets/img/code/OPEN.png' | relative_url }}" alt="OPEN: An Open-Source Platform for Developing Smart Local Energy System Applications" class="card-img-top card-img-contain">
        <div class="card-body">
          <h5 class="card-title">OPEN: Open Platform for Smart Local Energy Networks</h5>
        </div>
      </div>
    </a>
  </div>
  <div class="col">
    <a href="https://github.com/floracharbo/hedge" target="_blank">
      <div class="card h-100 hoverable">
        <img src="{{ '/assets/img/code/charbonnier2024home.png' | relative_url }}" alt="HEDGE: Home Energy Data Generator" class="card-img-top card-img-contain">
        <div class="card-body">
          <h5 class="card-title">HEDGE: Home Energy Data Generator</h5>
        </div>
      </div>
    </a>
  </div>
  <div class="col">
    <a href="https://github.com/PSALOxford/EnhancedCfD" target="_blank">
      <div class="card h-100 hoverable">
        <img src="{{ '/assets/img/code/Modelling.png' | relative_url }}" alt="High Fidelity Data for Great Britain's Transmission Network with Balancing Mechanism" class="card-img-top">
        <div class="card-body">
          <h5 class="card-title">High Fidelity Data for Great Britain's Transmission Network and Balancing Mechanism</h5>
        </div>
      </div>
    </a>
  </div>
  <div class="col">
    <a href="https://github.com/PSALOxford/UKM-PS-info-public" target="_blank">
      <div class="card h-100 hoverable">
        <img src="{{ '/assets/img/code/zhou2024datasets.png' | relative_url }}" alt="Great Britain Primary Distribution Substations and Linked Household Heating Data" class="card-img-top card-img-contain">
        <div class="card-body">
          <h5 class="card-title">Great Britain Primary Distribution Substations and Linked Household Heating Data</h5>
        </div>
      </div>
    </a>
  </div>

</div>



<h2 class="category">Notebooks</h2>

<div class="row row-cols-1 row-cols-md-4">
  <div class="col">
    <a href="https://colab.research.google.com/drive/1fkMINZtjUmjEtjBaS7jgH59GsjYsT0ov?usp=sharing" target="_blank">
      <div class="card h-100 hoverable">
        <img src="{{ '/assets/img/code/data_centre_colab.png' | relative_url }}" alt="Data Centre Colab Notebook" class="card-img-top card-img-contain">
        <div class="card-body">
          <h5 class="card-title">Data centre power flexibility and cost across grid services</h5>
        </div>
      </div>
    </a>
  </div>  <div class="col">
    <a href="https://github.com/PSALOxford/intro_pandapower/blob/main/intro-pandapower-solution.ipynb" target="_blank">
      <div class="card h-100 hoverable">
        <img src="{{ '/assets/img/code/into_pp_mvnet.png' | relative_url }}" alt="Introduction to Pandapower" class="card-img-top card-img-contain">
        <div class="card-body">
          <h5 class="card-title">Introduction to Pandapower</h5>
        </div>
      </div>
    </a>
  </div>
</div>

{% if site.data.repositories.github_repos %}

<h2 class="category">GitHub Repositories</h2>

<div class="repositories d-flex flex-wrap flex-md-row flex-column justify-content-between align-items-center">
  {% for repo in site.data.repositories.github_repos %}
    {% include repository/repo.liquid repository=repo %}
  {% endfor %}
</div>
{% endif %}


</div>
