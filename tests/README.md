# Tests

Unit tests for Legal System Dynamics components.

## Running Tests

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest --cov=code tests/

# Run specific test file
pytest tests/test_agent.py -v

# Run specific test
pytest tests/test_agent.py::test_agent_initialization -v
```

## Test Structure

```
tests/
├── README.md (this file)
├── test_agent.py                    # Agent class tests
├── test_population.py               # Population dynamics tests
├── test_hysteresis.py              # Hysteresis detection tests
├── test_cli_calculation.py         # CLI computation tests
├── test_belief_updating.py         # HBU and Bayesian updating tests
├── test_nesting.py                 # Phenotypic nesting tests
├── test_experiments.py             # Experiment reproducibility tests
└── conftest.py                     # Pytest fixtures
```

## Test Coverage Goals

| Component | Current | Target |
|-----------|---------|--------|
| Agent class | 0% | 90% |
| Population | 0% | 85% |
| Hysteresis | 0% | 90% |
| CLI calculation | 0% | 95% |
| Experiments | 0% | 75% |

## Writing Tests

### Example: Testing Agent Initialization

```python
# tests/test_agent.py
import pytest
from code.synthetic_populations.agent import Agent, AgentType, IntentionalityLevel

def test_agent_initialization():
    """Test basic agent creation"""
    agent = Agent(
        agent_id=1,
        agent_type=AgentType.JUDGE,
        intentionality_level=IntentionalityLevel.LEVEL_3
    )
    
    assert agent.agent_id == 1
    assert agent.agent_type == AgentType.JUDGE
    assert agent.intentionality_level == IntentionalityLevel.LEVEL_3

def test_agent_belief_bounds():
    """Test beliefs stay in [0, 1] range"""
    agent = Agent(agent_id=1, initial_beliefs={'liberty': 0.5})
    
    # Should clip to 1.0
    agent.beliefs['liberty'] = 1.5
    agent._enforce_belief_bounds()
    assert agent.beliefs['liberty'] == 1.0
    
    # Should clip to 0.0
    agent.beliefs['liberty'] = -0.5
    agent._enforce_belief_bounds()
    assert agent.beliefs['liberty'] == 0.0
```

### Example: Testing CLI Calculation

```python
# tests/test_cli_calculation.py
import pytest
from code.empirical_analysis.cli import calculate_cli

def test_cli_perfect_rigidity():
    """Test CLI = 1.0 when no reforms sustained"""
    cli = calculate_cli(n_attempted=10, n_sustained=0)
    assert cli == 1.0

def test_cli_perfect_fluidity():
    """Test CLI = 0.0 when all reforms sustained"""
    cli = calculate_cli(n_attempted=10, n_sustained=10)
    assert cli == 0.0

def test_cli_moderate():
    """Test CLI calculation for moderate rigidity"""
    cli = calculate_cli(n_attempted=20, n_sustained=10)
    assert cli == pytest.approx(0.5, abs=1e-9)
```

### Example: Testing Reproducibility

```python
# tests/test_experiments.py
import pytest
import numpy as np
from code.experiments.exp01_hysteresis_loops import run_experiment

def test_exp01_reproducibility():
    """Test Experiment 1 produces consistent results"""
    np.random.seed(42)
    results_1 = run_experiment(n_agents=100, n_steps=200)
    
    np.random.seed(42)
    results_2 = run_experiment(n_agents=100, n_steps=200)
    
    np.testing.assert_array_equal(results_1['support_rate'], results_2['support_rate'])

def test_exp01_hysteresis_detection():
    """Test Experiment 1 detects hysteresis"""
    results = run_experiment(n_agents=200, n_steps=500)
    
    # Check loop area > 0 (indicator of hysteresis)
    assert results['loop_area'] > 0.0
    
    # Check asymmetry in increasing vs decreasing branches
    increasing = results['support_rate'][:250]
    decreasing = results['support_rate'][250:]
    assert not np.allclose(increasing, decreasing[::-1], atol=0.1)
```

## Test Fixtures

Shared test fixtures are defined in `conftest.py`:

```python
# tests/conftest.py
import pytest
import pandas as pd
from code.synthetic_populations.agent import Agent, AgentType, IntentionalityLevel

@pytest.fixture
def sample_cli_data():
    """Sample CLI dataset for testing"""
    return pd.DataFrame({
        'country': ['USA', 'Denmark', 'Argentina'],
        'cli_score': [0.89, 0.15, 0.87],
        'n_reforms_attempted': [18, 13, 23],
        'n_reforms_sustained': [2, 11, 3]
    })

@pytest.fixture
def sample_agent():
    """Sample agent for testing"""
    return Agent(
        agent_id=1,
        agent_type=AgentType.CITIZEN,
        intentionality_level=IntentionalityLevel.LEVEL_2,
        initial_beliefs={'liberty': 0.5}
    )

@pytest.fixture
def sample_population(sample_agent):
    """Sample population for testing"""
    from code.synthetic_populations.population import Population
    return Population(agents=[sample_agent] * 100)
```

## Continuous Integration

Tests run automatically on GitHub Actions:

```yaml
# .github/workflows/tests.yml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.9
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: pytest --cov=code tests/
```

## Test Priorities

### Phase 1 (March 2026)
- [x] Project structure
- [ ] Agent initialization tests
- [ ] CLI calculation tests
- [ ] Experiment 1 reproducibility

### Phase 2 (April 2026)
- [ ] Population dynamics tests
- [ ] Hysteresis detection tests
- [ ] Belief updating tests
- [ ] Nesting layer tests

### Phase 3 (May 2026)
- [ ] Integration tests
- [ ] Performance benchmarks
- [ ] Edge case coverage
- [ ] Full coverage >85%

## Contributing

See [CONTRIBUTING.md](../CONTRIBUTING.md) for:
- Test writing guidelines
- Coverage requirements
- CI/CD integration

---

**Test-driven development ensures reliability for evolutionary constitutional theory.** ✅
