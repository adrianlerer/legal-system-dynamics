# Quick Start Guide

Get up and running with Legal System Dynamics in under 5 minutes.

## Prerequisites

- **Python 3.9+** (check with `python --version`)
- **Git** (check with `git --version`)
- **Jupyter** (optional, for notebooks)

## Step 1: Install

```bash
# Clone repository
git clone https://github.com/adrianlerer/legal-system-dynamics.git
cd legal-system-dynamics

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Step 2: Explore the CLI Dataset

```python
import pandas as pd

# Load Constitutional Lock-in Index data
cli_data = pd.read_csv('data/processed/cli_scores.csv')

# View high lock-in countries (rigid systems)
print(cli_data.nsmallest(5, 'cli_score'))
# Denmark (0.15), Netherlands (0.18), New Zealand (0.21), Chile (0.24), Canada (0.28)

# View low lock-in countries (fluid systems)
print(cli_data.nlargest(5, 'cli_score'))
# USA (0.89), Argentina (0.87), Mexico (0.81), Russia (0.78), Hungary (0.76)
```

**Key insight**: CLI >0.70 predicts 92% failure rate for constitutional reforms.

## Step 3: Run Your First Simulation

```bash
python code/experiments/exp01_hysteresis_loops.py
```

**Output**: 
- Figure saved to `results/experiment_01/hysteresis_loops.png`
- Shows constitutional hysteresis for three regime types
- Reproduces Figure 1 from Paper 1 ("Constitutional Hysteresis")

**What it does**:
- Simulates 200-agent synthetic populations
- Applies reform pressure cycles (0 → 1 → 0)
- Measures support rate at each step
- Reveals path-dependent memory effects

## Step 4: Create Your First Agent

```python
from code.synthetic_populations.agent import Agent, AgentType, IntentionalityLevel

# Create a judge with Level-3 intentionality (reflective)
judge = Agent(
    agent_id=1,
    agent_type=AgentType.JUDGE,
    intentionality_level=IntentionalityLevel.LEVEL_3,
    initial_beliefs={'liberty': 0.7},
    party_loyalty=0.3
)

# Create a corporation with Level-1 intentionality (goal-directed)
corp = Agent(
    agent_id=2,
    agent_type=AgentType.CORPORATION,
    intentionality_level=IntentionalityLevel.LEVEL_1,
    initial_beliefs={'control': 0.8},
    party_loyalty=0.0
)

# Simulate belief update (Heteronomous Bayesian Updating)
judge.update_belief('liberty', evidence=0.9, group_identity='legal_profession')
```

**Key concept**: Heterogeneous intentionality (Dennett Levels 1-3) prevents common knowledge, limiting separation-of-powers effectiveness.

## Step 5: Interactive Tutorial

```bash
jupyter notebook notebooks/01_introduction.ipynb
```

**Covers**:
1. CLI calculation and interpretation
2. Creating synthetic agents
3. Simulating simple reforms
4. Visualizing hysteresis loops

## What Next?

### Option A: Replicate Paper Findings

**Paper 1 – Constitutional Hysteresis**:
```bash
python code/experiments/exp01_hysteresis_loops.py
python code/experiments/exp02_coercivity_escalation.py  # Coming soon
python code/experiments/exp03_golden_ratio_emergence.py  # Coming soon
```

**Paper 2 – Phenotypic Nesting Theory**:
```bash
python code/experiments/exp04_nesting_layers.py  # Coming soon
python code/experiments/exp05_theater_ess.py  # Coming soon
```

### Option B: Explore Data

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load CLI data
df = pd.read_csv('data/processed/cli_scores.csv')

# Plot CLI vs regime type (V-Dem polyarchy score)
plt.scatter(df['regime_type'], df['cli_score'], alpha=0.6)
plt.xlabel('Regime Type (V-Dem)')
plt.ylabel('CLI Score')
plt.title('Constitutional Rigidity vs Democracy Level')
plt.show()

# Insight: No strong correlation (ρ = -0.24, p = 0.31)
# Democracies can be rigid (USA 0.89) or fluid (Denmark 0.15)
```

### Option C: Read the Papers

1. **Paper 1**: [Constitutional Hysteresis: Why Legal Systems Remember](papers/paper_01_hysteresis/)
2. **Paper 2**: [Phenotypic Nesting Theory: Why Surface Reforms Fail](papers/paper_02_nesting/)
3. **Paper 3**: [The Common Knowledge Impossibility Theorem](papers/paper_03_impossibility/)
4. **Paper 4**: [Legal Rituals as Extended Phenotype Machines](papers/paper_04_rituals/)
5. **Paper 5**: [Evolutionary Limits of Sunstein's Six Prohibitions](papers/paper_05_sunstein/)

## Key Concepts in 60 Seconds

### Constitutional Lock-in Index (CLI)
```
CLI = 1 - (Reforms Sustained / Reforms Attempted)
```
- **0.0**: All reforms succeed (fluid)
- **1.0**: All reforms fail (rigid)
- **Optimal**: 0.40–0.50 (critical flexibility)

### Hysteresis
Legal systems exhibit path-dependent memory:
- **Increasing pressure**: Reforms require threshold force
- **Decreasing pressure**: Support persists after pressure removal
- **Loop area**: Quantifies institutional inertia

### Phenotypic Nesting
Four layers of legal systems:
1. **Constitutional text** (decades)
2. **Doctrine** (years)
3. **Bureaucracy** (months)
4. **Culture** (centuries)

Reforms fail when memes aren't aligned across layers.

### Heterogeneous Intentionality
Actors have different cognitive levels (Dennett):
- **Level 1**: Corporations (goal-directed, no meta-beliefs)
- **Level 2**: Legislators (strategic, 1-level recursion)
- **Level 3**: Judges (reflective, 2+ levels recursion)

Common knowledge impossible → separation of powers degrades.

## Troubleshooting

### Import errors
```bash
# Ensure you're in the repo root
cd legal-system-dynamics
python -c "import sys; print(sys.path)"

# Add code/ to PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:$(pwd)/code"
```

### Missing dependencies
```bash
pip install -r requirements.txt --upgrade
```

### Data file not found
```bash
# Check data directory structure
ls -R data/

# Expected:
# data/processed/cli_scores.csv
# data/README.md
```

## Getting Help

- **Issues**: https://github.com/adrianlerer/legal-system-dynamics/issues
- **Email**: adrian@lerer.com.ar
- **Documentation**: See `docs/` directory

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on:
- Adding CLI data
- Implementing experiments
- Submitting pull requests

---

**Ready to explore evolutionary constitutional theory?** 🚀

Start with the [interactive notebook](notebooks/01_introduction.ipynb) or dive into [Paper 1](papers/paper_01_hysteresis/).
