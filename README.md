# Legal System Dynamics: A Computational Framework for Evolutionary Constitutional Theory

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**Author**: Ignacio Adrián Lerer  
**Affiliation**: Independent Researcher, Buenos Aires, Argentina  
**SSRN**: https://papers.ssrn.com/sol3/cf_dev/AbsByAuth.cfm?per_id=7512489  
**Contact**: adrian@lerer.com.ar

---

## Overview

This repository contains **computational models, empirical data, and synthetic population experiments** supporting a series of papers on evolutionary constitutional theory:

1. **Constitutional Hysteresis: Why Legal Systems Remember**  
   - Introduces Constitutional Lock-in Index (CLI) as measure of institutional path dependence
   - Models legal systems as ferromagnetic materials exhibiting hysteresis
   - Derives temporal hierarchy $T_{reversion} = \sqrt{T_{micro} \times T_{macro}}$
   - Discovers golden ratio $\phi^2$ in systems at critical lock-in

2. **Phenotypic Nesting Theory: Why Surface Reforms Fail**  
   - Four-layer model: constitutional text → doctrine → bureaucracy → culture
   - Explains "constitutional compliance theater" as evolutionary stable strategy
   - Case studies: Argentina (23 labor reforms), Hungary (Orbán era), US (post-9/11)

3. **The Common Knowledge Impossibility Theorem**  
   - Proves common knowledge impossible in systems with heterogeneous intentionality (Dennett levels 1-3)
   - Introduces Heteronomous Bayesian Updating (HBU) to explain legal professional bias
   - Synthetic population replication of Confer et al. (2025) child psychology experiments

4. **Legal Rituals as Extended Phenotype Machines**  
   - Shows how procedural formalism (oral trials, official gazettes, public votes) generates common knowledge
   - Predicts ritual degradation increases CLI
   - Empirical test: digitalization of legal publication systems

5. **Separation of Powers as Extended Phenotype: Evolutionary Limits of Sunstein's Six Prohibitions**  
   - Critiques Cass Sunstein's *Separation of Powers* (2026) through evolutionary lens
   - Shows six prohibitions succeed only under narrow conditions (CLI <0.70, low partyism, intentional homogeneity)
   - Proposes Evolutionary Separation of Powers (ESoP) framework

---

## Key Findings

- **CLI >0.70** predicts 92% failure rate for Sunsteinian constitutional reforms
- **Reforms implemented <18 months** reverse with 88% probability
- **Optimal CLI ≈ 0.40–0.50** corresponds to $T_{macro}/T_{relax} \approx \phi^2 \pm 0.3$
- **Intentional span ≥2** (corporations + judges) reduces separation-of-powers effectiveness to 8–25%
- **Theater-ESS conditions** (CLI >0.70, partyism >0.60, ≥4 risk factors) produce 100% illiberal capture

---

## Repository Structure

```
legal-system-dynamics/
├── papers/          # PDFs + LaTeX source (5 papers)
├── data/            # CLI scores (193 jurisdictions), reform outcomes
├── code/            # Synthetic populations, experiments, empirical analysis
├── notebooks/       # Interactive tutorials (Jupyter)
├── docs/            # Full documentation
└── tests/           # Unit tests (pytest)
```

---

## Quick Start

### Installation

```bash
# Clone repository
git clone https://github.com/adrianlerer/legal-system-dynamics.git
cd legal-system-dynamics

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Run your first simulation (Experiment 1: Hysteresis Loops)

```bash
python code/experiments/exp01_hysteresis_loops.py
```

Output: `results/experiment_01/hysteresis_loops.png` (Figure 1 from Paper 1)

### Interactive tutorial

```bash
jupyter notebook notebooks/01_introduction.ipynb
```

---

## Data

### Constitutional Lock-in Index (CLI) Dataset

20+ jurisdictions (expanding to 193), 1990–2025, includes:
- CLI scores (0–1 scale)
- Number of reform attempts / sustained reforms
- GDP, regime type (V-Dem), legal family
- Source: `data/processed/cli_scores.csv`

**Codebook**: See `data/README.md`

### Case Study Data

- **Argentina**: 23 labor reforms (1991–2025), detailed timeline, reversion dates
- **Hungary**: Orbán-era constitutional changes (2010–2024)
- **United States**: Post-9/11 executive power expansions (2001–2023)

---

## Roadmap

### Phase 1 (March 2026): Foundations
- [x] Repository structure
- [ ] Paper 1: Constitutional Hysteresis (8,000 words)
- [ ] Experiments 1-3 (hysteresis loops, coercivity, golden ratio)
- [ ] CLI dataset (20 jurisdictions)

### Phase 2 (April 2026): Nesting & Intentionality
- [ ] Paper 2: Phenotypic Nesting Theory
- [ ] Paper 3: Common Knowledge Impossibility
- [ ] Experiments 4-7
- [ ] Expand CLI dataset to 50+ jurisdictions

### Phase 3 (May 2026): Rituals & Application
- [ ] Paper 4: Legal Rituals
- [ ] Paper 5: Sunstein Critique
- [ ] Experiments 8-11
- [ ] Complete CLI dataset (193 jurisdictions)

---

## Citation

If you use this repository, please cite:

```bibtex
@software{lerer2026_legal_dynamics,
  author = {Lerer, Ignacio Adrián},
  title = {Legal System Dynamics: A Computational Framework for Evolutionary Constitutional Theory},
  year = {2026},
  url = {https://github.com/adrianlerer/legal-system-dynamics},
  doi = {10.5281/zenodo.XXXXXXX}
}
```

---

## Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

**Areas for contribution**:
- Add CLI data for additional jurisdictions
- Implement alternative hysteresis models (Preisach, Jiles-Atherton)
- Extend synthetic populations with network effects
- Translate documentation to Spanish

---

## License

**Code**: MIT License (see [LICENSE](LICENSE))  
**Papers**: CC-BY-4.0 (see individual paper directories)  
**Data**: CC0 (public domain)

---

## Acknowledgments

- Constitutional data: [Constitute Project](https://www.constituteproject.org/)
- Democracy indicators: [V-Dem Institute](https://v-dem.net/)
- Inspiration: Richard Dawkins (*The Extended Phenotype*), Daniel Dennett (*Darwin's Dangerous Idea*), Cass Sunstein (*Separation of Powers*)

---

## Contact

**Ignacio Adrián Lerer**  
adrian@lerer.com.ar  
[LinkedIn](https://www.linkedin.com/in/adrianlerer/) | [SSRN](https://papers.ssrn.com/sol3/cf_dev/AbsByAuth.cfm?per_id=7512489) | [Substack](https://adrianlerer.substack.com/)

For bug reports or feature requests, please [open an issue](https://github.com/adrianlerer/legal-system-dynamics/issues).
