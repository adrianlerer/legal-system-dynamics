# Data Directory

## Overview

This directory contains empirical data supporting the computational models and theoretical claims in the Legal System Dynamics framework.

## Structure

```
data/
├── raw/              # Original, unprocessed data
│   └── README.md
├── processed/        # Cleaned, analysis-ready datasets
│   └── cli_scores.csv
└── README.md         # This file
```

## Datasets

### Constitutional Lock-in Index (CLI) Scores

**File**: `processed/cli_scores.csv`

**Description**: Constitutional Lock-in Index scores for 20+ jurisdictions (expanding to 193), measuring institutional path dependence and resistance to reform.

**Columns**:
- `country`: Jurisdiction name
- `cli_score`: Constitutional Lock-in Index (0-1 scale, higher = more rigid)
- `n_reforms_attempted`: Number of constitutional reform attempts (1990-2025)
- `n_reforms_sustained`: Number of reforms that persisted >5 years
- `gdp_per_capita`: GDP per capita (World Bank, constant 2015 USD)
- `regime_type`: Democracy score (V-Dem polyarchy index, 0-1)
- `legal_family`: Legal tradition (common_law, civil_law, mixed, islamic, customary)

**CLI Calculation**:
```
CLI = 1 - (n_reforms_sustained / n_reforms_attempted)
```

**Data Sources**:
- Constitutional texts: [Constitute Project](https://www.constituteproject.org/)
- Reform attempts: Manual coding from national archives, academic papers
- GDP data: World Bank World Development Indicators
- Regime type: V-Dem Institute Democracy Indices
- Legal family: JuriGlobe - World Legal Systems

**Citation**:
```bibtex
@data{lerer2026_cli_dataset,
  author = {Lerer, Ignacio Adrián},
  title = {Constitutional Lock-in Index (CLI) Dataset},
  year = {2026},
  publisher = {GitHub},
  url = {https://github.com/adrianlerer/legal-system-dynamics}
}
```

## Adding New Jurisdictions

To contribute CLI data for additional countries:

1. Code reform attempts from constitutional history
2. Determine which reforms sustained >5 years
3. Calculate CLI score
4. Add row to `processed/cli_scores.csv`
5. Submit Pull Request with sources documented

**Template**:
```csv
country,cli_score,n_reforms_attempted,n_reforms_sustained,gdp_per_capita,regime_type,legal_family
YourCountry,0.XX,XX,XX,XXXXX,0.XX,civil_law
```

## Data Quality Standards

- **Reform coding**: At least 2 independent coders, inter-rater reliability >0.80
- **Sustained reforms**: Must persist unchanged for >5 years
- **GDP/regime data**: Use most recent available year (2023-2024)
- **Sources**: Primary sources (official gazettes, constitutional texts) preferred

## License

All data in this directory is released under **CC0 1.0 Universal (Public Domain)**. You can copy, modify, and distribute without attribution (though citation is appreciated).
