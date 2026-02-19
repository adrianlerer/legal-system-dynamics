# Contributing to Legal System Dynamics

Thank you for your interest in contributing to the Legal System Dynamics project! This document provides guidelines for contributing.

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/legal-system-dynamics.git
   cd legal-system-dynamics
   ```
3. **Create a branch** for your contribution:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Types of Contributions

### 1. Adding CLI Data

We welcome contributions of Constitutional Lock-in Index data for additional jurisdictions.

**Requirements**:
- Follow the format in `data/processed/cli_scores.csv`
- Include source documentation in `data/sources/COUNTRY_NAME.md`
- Provide calculation methodology
- Minimum 5-year observation period

**Example**:
```csv
country,cli_score,n_reforms_attempted,n_reforms_sustained,gdp_per_capita,regime_type,legal_family
Sweden,0.22,14,11,60239,0.91,civil_law
```

### 2. Implementing New Experiments

Contributions of new synthetic population experiments are encouraged.

**Structure**:
```python
# code/experiments/exp##_descriptive_name.py

"""
Brief description of experiment.

Reproduces: Figure X from Paper Y
"""

import numpy as np
from synthetic_populations.population import Population

def run_experiment(n_agents=1000, n_steps=500, **kwargs):
    """
    Main experiment function.
    
    Args:
        n_agents: Population size
        n_steps: Simulation steps
        **kwargs: Additional parameters
        
    Returns:
        dict: Results with keys 'data', 'figures', 'metrics'
    """
    # Your code here
    pass

if __name__ == "__main__":
    results = run_experiment()
    # Save results to results/experiment_##/
```

### 3. Extending Models

**Areas for extension**:
- Alternative hysteresis models (Preisach, Jiles-Atherton)
- Network effects in synthetic populations
- Multi-jurisdictional coupling
- Dynamic intentionality level transitions

**Requirements**:
- Add unit tests in `tests/`
- Document new parameters in docstrings
- Update relevant notebooks

### 4. Documentation

- Fix typos or unclear explanations
- Add examples to notebooks
- Translate documentation to Spanish
- Improve code comments

## Development Guidelines

### Code Style

We follow [PEP 8](https://peps.python.org/pep-0008/) with:
- **Line length**: 88 characters (Black formatter)
- **Quotes**: Double quotes for strings
- **Imports**: Grouped (standard library, third-party, local)

Run formatter before committing:
```bash
pip install black
black code/ tests/
```

### Testing

All new code must include tests:
```bash
# Run tests
pytest tests/

# Check coverage
pytest --cov=code tests/
```

### Commit Messages

Use conventional commits format:
```
type(scope): description

[optional body]
[optional footer]
```

**Types**: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

**Examples**:
- `feat(cli): add data for Nordic countries`
- `fix(agent): correct intentionality level initialization`
- `docs(readme): clarify CLI calculation methodology`

## Pull Request Process

1. **Update documentation** to reflect your changes
2. **Add tests** for new functionality
3. **Run the test suite** and ensure all tests pass
4. **Update CHANGELOG.md** if applicable
5. **Submit PR** with:
   - Clear title and description
   - Reference to related issue (if any)
   - Screenshots (for visualizations)

### PR Template

```markdown
## Description
Brief description of changes

## Motivation
Why is this change needed?

## Changes
- List key changes
- Include file paths

## Testing
- Describe how you tested
- Include test results

## Checklist
- [ ] Tests pass
- [ ] Documentation updated
- [ ] Code formatted (Black)
- [ ] CHANGELOG.md updated
```

## Code Review Process

1. At least one maintainer must review
2. All CI checks must pass
3. Discussion of design decisions is encouraged
4. Suggestions will be made for improvements

## Areas for Contribution

### High Priority

1. **CLI Data Expansion**
   - Target: 193 jurisdictions
   - Currently have: 20
   - Focus: Latin America, Africa, Asia

2. **Paper Replication**
   - Paper 1, Experiments 2-3 (coercivity, golden ratio)
   - Paper 2, Experiments 4-5 (nesting layers, theater-ESS)

3. **Unit Tests**
   - Agent class edge cases
   - Population dynamics validation
   - Hysteresis detection algorithms

### Medium Priority

1. **Network Effects**
   - Social influence in belief updating
   - Coalition formation
   - Institutional networks

2. **Visualization Tools**
   - Interactive dashboards (Plotly/Dash)
   - CLI map visualization
   - Phase space plots

3. **Documentation**
   - API reference (Sphinx)
   - Tutorial notebooks for Papers 2-5
   - Spanish translation

### Future Work

1. **Machine Learning Integration**
   - CLI prediction from constitutional text
   - Reform outcome classification
   - Hysteresis pattern recognition

2. **Agent-Based Extensions**
   - Geographic models
   - Multi-level selection mechanisms
   - Cultural transmission

## Questions?

- **Email**: adrian@lerer.com.ar
- **Issues**: https://github.com/adrianlerer/legal-system-dynamics/issues
- **Discussions**: https://github.com/adrianlerer/legal-system-dynamics/discussions

## License

By contributing, you agree that your contributions will be licensed under the MIT License (code) and CC-BY-4.0 (documentation).

---

Thank you for contributing to evolutionary constitutional theory! 🎉
