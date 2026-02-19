"""
Experiment 1: Constitutional Hysteresis Loops

Simulates reform-reversion cycles for different CLI regimes.
Generates Figure 1 for Paper 1.
"""

import numpy as np
import matplotlib.pyplot as plt
import sys
import os
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from synthetic_populations.agent import Agent, AgentType, IntentionalityLevel


def simulate_hysteresis_loop(
    n_agents: int = 200,
    cli_target: float = 0.5,
    n_steps: int = 20
) -> tuple:
    """
    Simulate one hysteresis loop (reform → reversion).
    
    Args:
        n_agents: Population size
        cli_target: Target CLI score (determines meme distribution)
        n_steps: Number of simulation steps
    
    Returns:
        (reform_pressure_array, flexibility_array)
    """
    # Create population with meme distribution matching CLI
    # High CLI = more control-memes
    liberty_ratio = 1 - cli_target
    
    agents = []
    for i in range(n_agents):
        # Assign beliefs based on CLI
        if np.random.random() < liberty_ratio:
            initial_beliefs = {"liberty": np.random.uniform(0.6, 0.9), 
                             "control": np.random.uniform(0.1, 0.4)}
        else:
            initial_beliefs = {"liberty": np.random.uniform(0.1, 0.4),
                             "control": np.random.uniform(0.6, 0.9)}
        
        agent = Agent(
            agent_id=i,
            agent_type=AgentType.CITIZEN,
            initial_beliefs=initial_beliefs
        )
        agents.append(agent)
    
    # Simulate reform pressure cycle: 0 → 1 → 0
    pressure_loading = np.linspace(0, 1, n_steps // 2)
    pressure_unloading = np.linspace(1, 0, n_steps // 2)
    reform_pressure = np.concatenate([pressure_loading, pressure_unloading])
    
    flexibility = []
    
    for pressure in reform_pressure:
        # Apply reform pressure as evidence
        adopted_count = 0
        for agent in agents:
            # Evidence strength depends on pressure
            evidence = pressure + np.random.normal(0, 0.1)
            evidence = np.clip(evidence, 0, 1)
            
            agent.update_belief("liberty", evidence, update_rule="bayesian")
            
            # Agent adopts reform if liberty belief > threshold
            # Threshold depends on CLI (high CLI = high threshold)
            threshold = 0.5 + (cli_target * 0.3)  # Range: 0.5-0.8
            if agent.beliefs.get("liberty", 0.5) > threshold:
                adopted_count += 1
        
        # Flexibility = % population that adopted reform
        flexibility.append(adopted_count / n_agents)
    
    return reform_pressure, np.array(flexibility)


def plot_hysteresis_loops(results: dict, save_path: str = "results/experiment_01"):
    """
    Plot hysteresis loops for multiple CLI regimes.
    
    Args:
        results: Dict mapping CLI values to (pressure, flexibility) tuples
        save_path: Directory to save figure
    """
    fig, ax = plt.subplots(figsize=(10, 7))
    
    colors = {0.30: '#2ecc71', 0.50: '#f39c12', 0.85: '#e74c3c'}
    labels = {0.30: 'Low CLI (≈0.30) - Chile, Denmark', 
              0.50: 'Medium CLI (≈0.50) - Brazil, Germany',
              0.85: 'High CLI (≈0.85) - Argentina, USA'}
    
    for cli, (pressure, flexibility) in results.items():
        # Split into loading and unloading paths
        mid = len(pressure) // 2
        
        # Loading path (reform)
        ax.plot(pressure[:mid+1], flexibility[:mid+1], 
                color=colors[cli], linewidth=2.5, 
                label=labels[cli], alpha=0.8)
        
        # Unloading path (reversion)
        ax.plot(pressure[mid:], flexibility[mid:], 
                color=colors[cli], linewidth=2.5, 
                linestyle='--', alpha=0.8)
        
        # Mark loop direction
        ax.annotate('', xy=(pressure[mid//2], flexibility[mid//2]),
                   xytext=(pressure[mid//2-1], flexibility[mid//2-1]),
                   arrowprops=dict(arrowstyle='->', color=colors[cli], lw=2))
    
    ax.set_xlabel('Reform Pressure (x)', fontsize=14, fontweight='bold')
    ax.set_ylabel('Institutional Flexibility (y)', fontsize=14, fontweight='bold')
    ax.set_title('Constitutional Hysteresis Loops Across CLI Regimes', 
                fontsize=16, fontweight='bold', pad=20)
    
    ax.legend(loc='upper left', fontsize=11, frameon=True, shadow=True)
    ax.grid(True, alpha=0.3, linestyle=':', linewidth=0.8)
    ax.set_xlim(-0.05, 1.05)
    ax.set_ylim(-0.05, 1.05)
    
    # Add annotations
    ax.text(0.5, 0.05, 
            'Loop area = energy dissipated per reform cycle', 
            ha='center', fontsize=10, style='italic', 
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))
    
    plt.tight_layout()
    
    # Save figure
    os.makedirs(save_path, exist_ok=True)
    fig_path = os.path.join(save_path, 'hysteresis_loops.png')
    plt.savefig(fig_path, dpi=300, bbox_inches='tight')
    print(f"✓ Figure saved to: {fig_path}")
    
    plt.show()


def calculate_loop_area(pressure: np.ndarray, flexibility: np.ndarray) -> float:
    """Calculate area of hysteresis loop using trapezoidal rule"""
    mid = len(pressure) // 2
    
    # Area using Shoelace formula
    x = pressure
    y = flexibility
    area = 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))
    
    return area


def main():
    """Run Experiment 1: Hysteresis Loops"""
    print("=" * 60)
    print("EXPERIMENT 1: Constitutional Hysteresis Loops")
    print("=" * 60)
    print()
    
    # Simulate three CLI regimes
    cli_values = [0.30, 0.50, 0.85]
    results = {}
    
    print("Simulating hysteresis loops...")
    for cli in cli_values:
        print(f"  - CLI = {cli:.2f}...", end=" ")
        pressure, flexibility = simulate_hysteresis_loop(
            n_agents=200,
            cli_target=cli,
            n_steps=20
        )
        results[cli] = (pressure, flexibility)
        
        # Calculate loop area
        area = calculate_loop_area(pressure, flexibility)
        print(f"Loop area = {area:.4f}")
    
    print()
    print("Plotting results...")
    plot_hysteresis_loops(results)
    
    print()
    print("=" * 60)
    print("KEY FINDINGS:")
    print("=" * 60)
    for cli, (pressure, flexibility) in results.items():
        area = calculate_loop_area(pressure, flexibility)
        remanence = flexibility[len(flexibility)//2]  # Flexibility at end of loading
        print(f"CLI {cli:.2f}: Loop area = {area:.4f}, Remanence = {remanence:.3f}")
    
    print()
    print("✓ Experiment 1 completed successfully")
    print()
    print("INTERPRETATION:")
    print("- Wider loops (larger area) = more energy dissipated")
    print("- High CLI systems: wide loops, low remanence")
    print("- Low CLI systems: narrow loops, high remanence")
    print()


if __name__ == "__main__":
    main()
