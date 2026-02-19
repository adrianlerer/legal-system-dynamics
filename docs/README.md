# Documentation

Comprehensive documentation for the Legal System Dynamics framework.

## Documentation Structure

```
docs/
├── README.md (this file)
├── theory/
│   ├── constitutional_hysteresis.md
│   ├── phenotypic_nesting.md
│   ├── common_knowledge_impossibility.md
│   ├── legal_rituals.md
│   └── evolutionary_separation_of_powers.md
├── methods/
│   ├── cli_calculation.md
│   ├── synthetic_populations.md
│   ├── hysteresis_detection.md
│   ├── belief_updating.md
│   └── statistical_tests.md
├── tutorials/
│   ├── quickstart.md
│   ├── adding_cli_data.md
│   ├── running_experiments.md
│   └── creating_visualizations.md
├── api/
│   ├── agent.md
│   ├── population.md
│   ├── experiments.md
│   └── analysis.md
└── examples/
    ├── case_study_argentina.md
    ├── case_study_hungary.md
    └── case_study_usa.md
```

## Quick Links

### Theory

- **[Constitutional Hysteresis](theory/constitutional_hysteresis.md)**: Path-dependent memory in legal systems
- **[Phenotypic Nesting Theory](theory/phenotypic_nesting.md)**: Four-layer model of institutional change
- **[Common Knowledge Impossibility](theory/common_knowledge_impossibility.md)**: Heterogeneous intentionality prevents coordination
- **[Legal Rituals](theory/legal_rituals.md)**: Procedural formalism as common-knowledge machinery
- **[Evolutionary Separation of Powers](theory/evolutionary_separation_of_powers.md)**: ESoP framework

### Methods

- **[CLI Calculation](methods/cli_calculation.md)**: Computing Constitutional Lock-in Index
- **[Synthetic Populations](methods/synthetic_populations.md)**: Agent-based modeling
- **[Hysteresis Detection](methods/hysteresis_detection.md)**: Identifying path dependence
- **[Belief Updating](methods/belief_updating.md)**: Heteronomous Bayesian Updating (HBU)
- **[Statistical Tests](methods/statistical_tests.md)**: Validation procedures

### Tutorials

- **[Quickstart](../QUICKSTART.md)**: Get started in 5 minutes
- **[Adding CLI Data](tutorials/adding_cli_data.md)**: Contribute data for new jurisdictions
- **[Running Experiments](tutorials/running_experiments.md)**: Reproduce paper figures
- **[Creating Visualizations](tutorials/creating_visualizations.md)**: Custom plots and dashboards

### API Reference

- **[Agent Class](api/agent.md)**: Individual institutional actors
- **[Population Class](api/population.md)**: Synthetic societies
- **[Experiments Module](api/experiments.md)**: Simulation protocols
- **[Analysis Module](api/analysis.md)**: Empirical data processing

### Examples

- **[Argentina Case Study](examples/case_study_argentina.md)**: 23 labor reforms, CLI = 0.87
- **[Hungary Case Study](examples/case_study_hungary.md)**: Orbán era, constitutional compliance theater
- **[USA Case Study](examples/case_study_usa.md)**: Post-9/11 executive power expansion

## Key Concepts

### Constitutional Lock-in Index (CLI)

$$\text{CLI} = 1 - \frac{\text{Reforms Sustained}}{\text{Reforms Attempted}}$$

- **Range**: [0, 1]
- **Interpretation**: 
  - 0.0–0.30: Fluid systems (Denmark, Netherlands, New Zealand)
  - 0.30–0.50: Optimal flexibility (Chile, Canada, Germany)
  - 0.50–0.70: Moderate rigidity (France, Spain, Italy)
  - 0.70–1.0: High rigidity (USA, Argentina, Russia, Hungary)

**Predictive Power**:
- CLI >0.70 → 92% reform failure rate
- CLI <0.40 → 85% reform success rate

### Hysteresis Loop

![Hysteresis Loop](../results/experiment_01/hysteresis_loops.png)

**Components**:
1. **Increasing branch**: Support rate vs reform pressure (ascending)
2. **Decreasing branch**: Support rate vs reform pressure (descending)
3. **Loop area**: Quantifies path dependence (larger area = more rigidity)

**Temporal Hierarchy**:
$$T_{reversion} = \sqrt{T_{micro} \times T_{macro}}$$

Where:
- $T_{micro}$: Individual belief update timescale (~days)
- $T_{macro}$: Institutional change timescale (~decades)
- $T_{reversion}$: Reform reversal timescale (~months to years)

**Empirical Finding**: $T_{reversion} \approx 18$ months for constitutional reforms

### Phenotypic Nesting

Four nested layers of legal systems:

1. **Constitutional Text** (decades)
   - Formal documents
   - Amendment procedures
   - Explicit separation of powers

2. **Doctrine** (years)
   - Judicial interpretations
   - Legal scholarship
   - Professional norms

3. **Bureaucracy** (months)
   - Administrative procedures
   - Enforcement capacity
   - Implementation protocols

4. **Culture** (centuries)
   - Societal expectations
   - Compliance habits
   - Common knowledge about norms

**Nesting Failure**: Reforms succeed only when liberty-memes aligned across ALL layers.

### Heterogeneous Intentionality

**Dennett's Levels**:
- **Level 0**: Reactive (thermostat) — no beliefs
- **Level 1**: Goal-directed (corporations) — beliefs, no meta-beliefs
- **Level 2**: Strategic (legislators, lawyers) — beliefs about beliefs (1-level recursion)
- **Level 3**: Reflective (judges, academics) — beliefs about beliefs about beliefs (2+ levels)

**Impossibility Theorem**: Common knowledge impossible when actors span ≥2 intentionality levels.

**Consequence**: Separation of powers degrades when corporations (L1) interact with judiciary (L3).

### Heteronomous Bayesian Updating (HBU)

Standard Bayesian updating:
$$P(H|E) = \frac{P(E|H) \cdot P(H)}{P(E)}$$

HBU modification for group identity:
$$P(H|E, G) = \frac{P(E|H) \cdot P(H) \cdot \alpha_G(E)}{P(E)}$$

Where $\alpha_G(E)$ is group-identity weight:
- $\alpha_G > 1$ if evidence confirms in-group beliefs
- $\alpha_G < 1$ if evidence contradicts in-group beliefs

**Empirical calibration**: $\alpha_G \approx 1.39$ for professional identity (39% bias toward confirming evidence)

## Building Documentation Locally

```bash
# Install Sphinx
pip install sphinx sphinx-rtd-theme

# Build HTML docs
cd docs/
make html

# View docs
open _build/html/index.html
```

## Contributing to Documentation

See [CONTRIBUTING.md](../CONTRIBUTING.md) for:
- Documentation style guide
- Adding new pages
- Translation to Spanish

### Documentation Priorities

**Phase 1 (March 2026)**:
- [x] README structure
- [ ] Theory pages (5 papers)
- [ ] CLI calculation guide
- [ ] Quickstart tutorial

**Phase 2 (April 2026)**:
- [ ] API reference (auto-generated from docstrings)
- [ ] Methods documentation
- [ ] Case study examples

**Phase 3 (May 2026)**:
- [ ] Interactive notebooks
- [ ] Video tutorials
- [ ] Spanish translation

## External Resources

- **Papers**: [papers/](../papers/)
- **Notebooks**: [notebooks/](../notebooks/)
- **Data**: [data/](../data/)
- **Code**: [code/](../code/)

## Contact

For documentation questions:
- **Email**: adrian@lerer.com.ar
- **Issues**: https://github.com/adrianlerer/legal-system-dynamics/issues

---

**Good documentation makes evolutionary constitutional theory accessible to all.** 📚
