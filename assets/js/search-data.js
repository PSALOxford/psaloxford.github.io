// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-power-systems-architecture-lab",
    title: "Power Systems Architecture Lab",
    section: "Navigation",
    handler: () => {
      window.location.href = "/";
    },
  },{id: "nav-research",
          title: "Research",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/projects/";
          },
        },{id: "nav-code-amp-data",
          title: "Code &amp; Data",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/code-and-data/";
          },
        },{id: "nav-publications",
          title: "Publications",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/publications/";
          },
        },{id: "nav-people",
          title: "People",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/people/";
          },
        },{id: "nav-work-with-us",
          title: "Work With Us",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/work-with-us/";
          },
        },{id: "nav-join-us",
          title: "Join Us",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/join/";
          },
        },{id: "nav-contact",
          title: "Contact",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/contact/";
          },
        },{id: "projects-flexedge-data-driven-cloud-to-edge-computing-for-scalable-near-real-time-local-flexibility-markets",
          title: 'FleXEdge: Data-Driven Cloud-to-Edge Computing for Scalable Near Real-Time Local Flexibility Markets',
          description: "",
          section: "Current Projects",handler: () => {
              window.location.href = "/projects/10_flexedge/";
            },},{id: "projects-ionate-knowledge-transfer-partnership-ai-powered-control-for-hybrid-intelligent-transformers",
          title: 'IONATE Knowledge Transfer Partnership: AI-Powered Control for Hybrid Intelligent Transformers',
          description: "",
          section: "Current Projects",handler: () => {
              window.location.href = "/projects/11_ionate/";
            },},{id: "projects-oxford-martin-programme-on-circular-battery-economies",
          title: 'Oxford Martin Programme on Circular Battery Economies',
          description: "",
          section: "Current Projects",handler: () => {
              window.location.href = "/projects/12_circular_battery/";
            },},{id: "projects-power-systems-modelling",
          title: 'Power Systems Modelling',
          description: "",
          section: "Research Areas",handler: () => {
              window.location.href = "/projects/1_systems_modelling/";
            },},{id: "projects-power-systems-control",
          title: 'Power Systems Control',
          description: "",
          section: "Research Areas",handler: () => {
              window.location.href = "/projects/2_systems_control/";
            },},{id: "projects-power-systems-planning",
          title: 'Power Systems Planning',
          description: "",
          section: "Research Areas",handler: () => {
              window.location.href = "/projects/3_systems_planning/";
            },},{id: "projects-electricity-market-design",
          title: 'Electricity Market Design',
          description: "",
          section: "Research Areas",handler: () => {
              window.location.href = "/projects/4_market_design/";
            },},{id: "projects-energyrev-market-design-for-scaling-up-local-clean-energy-systems",
          title: 'EnergyREV: Market Design for Scaling Up Local Clean Energy Systems',
          description: "",
          section: "Completed Projects",handler: () => {
              window.location.href = "/projects/5_energyrev/";
            },},{id: "projects-digest-data-driven-exploration-of-the-carbon-emissions-impact-of-grid-energy-storage",
          title: 'DIGEST: Data-Driven Exploration of the Carbon Emissions Impact of Grid Energy Storage',
          description: "",
          section: "Completed Projects",handler: () => {
              window.location.href = "/projects/6_digest/";
            },},{id: "projects-benchmarking-quantum-advantage",
          title: 'Benchmarking Quantum Advantage',
          description: "",
          section: "Completed Projects",handler: () => {
              window.location.href = "/projects/7_quantum_benchmarking/";
            },},{id: "projects-the-blaise-pascal-quantum-challenge-2025-1st-prize",
          title: 'The Blaise Pascal Quantum Challenge 2025: 1st Prize',
          description: "",
          section: "Completed Projects",handler: () => {
              window.location.href = "/projects/8_blaise_pascal/";
            },},{id: "projects-aria-sageflex-safeguarded-ai-agents-for-grid-edge-flexibility",
          title: 'ARIA SAGEflex: Safeguarded AI Agents for Grid-Edge Flexibility',
          description: "",
          section: "Current Projects",handler: () => {
              window.location.href = "/projects/9_sageflex/";
            },},{
        id: 'social-email',
        title: 'email',
        section: 'Socials',
        handler: () => {
          window.open("mailto:%74%68%6F%6D%61%73.%6D%6F%72%73%74%79%6E@%65%6E%67.%6F%78.%61%63.%75%6B", "_blank");
        },
      },{
        id: 'social-github',
        title: 'GitHub',
        section: 'Socials',
        handler: () => {
          window.open("https://github.com/PSALOxford", "_blank");
        },
      },{
        id: 'social-linkedin',
        title: 'LinkedIn',
        section: 'Socials',
        handler: () => {
          window.open("https://www.linkedin.com/in/thomas-morstyn-27b26144", "_blank");
        },
      },{
        id: 'social-researchgate',
        title: 'ResearchGate',
        section: 'Socials',
        handler: () => {
          window.open("https://www.researchgate.net/profile/Thomas-Morstyn/", "_blank");
        },
      },{
        id: 'social-scholar',
        title: 'Google Scholar',
        section: 'Socials',
        handler: () => {
          window.open("https://scholar.google.com/citations?user=nvzgGIcAAAAJ", "_blank");
        },
      },{
      id: 'light-theme',
      title: 'Change theme to light',
      description: 'Change the theme of the site to Light',
      section: 'Theme',
      handler: () => {
        setThemeSetting("light");
      },
    },
    {
      id: 'dark-theme',
      title: 'Change theme to dark',
      description: 'Change the theme of the site to Dark',
      section: 'Theme',
      handler: () => {
        setThemeSetting("dark");
      },
    },
    {
      id: 'system-theme',
      title: 'Use system default theme',
      description: 'Change the theme of the site to System Default',
      section: 'Theme',
      handler: () => {
        setThemeSetting("system");
      },
    },];
