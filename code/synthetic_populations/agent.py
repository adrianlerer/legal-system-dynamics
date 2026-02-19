"""
Agent class for synthetic populations in legal system dynamics.

Implements Dennett's intentionality levels (0-3) and heterogeneous belief updating.
"""

import numpy as np
from typing import Dict, List, Optional, Tuple
from enum import Enum


class IntentionalityLevel(Enum):
    """Dennett's intentionality hierarchy"""
    LEVEL_0 = 0  # Reactive (thermostat)
    LEVEL_1 = 1  # Goal-directed, no beliefs about beliefs (corporations)
    LEVEL_2 = 2  # Strategic, 1-level recursion (legislators, lawyers)
    LEVEL_3 = 3  # Reflective, 2+ levels recursion (judges, academics)


class AgentType(Enum):
    """Types of institutional actors"""
    CITIZEN = "citizen"
    JUDGE = "judge"
    LEGISLATOR = "legislator"
    BUREAUCRAT = "bureaucrat"
    CORPORATION = "corporation"


class Agent:
    """
    Agent in synthetic population for legal system modeling.
    
    Attributes:
        agent_id (int): Unique identifier
        agent_type (AgentType): Institutional role
        intentionality_level (IntentionalityLevel): Dennett level
        beliefs (Dict[str, float]): Beliefs about norms (0-1, liberty vs control)
        group_identity (Optional[str]): Group membership (for HBU effects)
        party_loyalty (float): Partisan alignment (0-1)
        position_layer (int): Nested institutional layer (1-4)
    """
    
    def __init__(
        self,
        agent_id: int,
        agent_type: AgentType = AgentType.CITIZEN,
        intentionality_level: Optional[IntentionalityLevel] = None,
        initial_beliefs: Optional[Dict[str, float]] = None,
        group_identity: Optional[str] = None,
        party_loyalty: float = 0.5,
        position_layer: int = 4
    ):
        self.agent_id = agent_id
        self.agent_type = agent_type
        
        # Set default intentionality based on type if not specified
        if intentionality_level is None:
            intentionality_level = self._default_intentionality(agent_type)
        self.intentionality_level = intentionality_level
        
        # Initialize beliefs (default: neutral 0.5 = no preference)
        self.beliefs = initial_beliefs or {"liberty": 0.5, "control": 0.5}
        
        # Social/institutional attributes
        self.group_identity = group_identity
        self.party_loyalty = party_loyalty
        self.position_layer = position_layer
        
        # Meta-beliefs (only for Level 2+)
        self.meta_beliefs: Dict[int, Dict[str, float]] = {}
        if self.intentionality_level.value >= 2:
            self._initialize_meta_beliefs()
    
    def _default_intentionality(self, agent_type: AgentType) -> IntentionalityLevel:
        """Default intentionality level by agent type"""
        defaults = {
            AgentType.CITIZEN: IntentionalityLevel.LEVEL_1,
            AgentType.CORPORATION: IntentionalityLevel.LEVEL_1,
            AgentType.BUREAUCRAT: IntentionalityLevel.LEVEL_2,
            AgentType.LEGISLATOR: IntentionalityLevel.LEVEL_2,
            AgentType.JUDGE: IntentionalityLevel.LEVEL_3,
        }
        return defaults.get(agent_type, IntentionalityLevel.LEVEL_1)
    
    def _initialize_meta_beliefs(self):
        """Initialize beliefs about others' beliefs (Level 2+)"""
        # Start with assumption others share own beliefs
        self.meta_beliefs[1] = self.beliefs.copy()
    
    def update_belief(
        self,
        norm: str,
        evidence: float,
        update_rule: str = "bayesian"
    ) -> None:
        """
        Update belief about a norm given evidence.
        
        Args:
            norm: Norm identifier (e.g., "liberty", "control")
            evidence: Evidence strength (0-1, favor liberty or control)
            update_rule: "bayesian", "hbu" (Heteronomous Bayesian Updating), 
                        "confirmation_bias"
        """
        if norm not in self.beliefs:
            self.beliefs[norm] = 0.5  # Initialize if new norm
        
        prior = self.beliefs[norm]
        
        if update_rule == "bayesian":
            posterior = self._bayesian_update(prior, evidence)
        elif update_rule == "hbu":
            posterior = self._hbu_update(prior, evidence)
        elif update_rule == "confirmation_bias":
            posterior = self._confirmation_bias_update(prior, evidence)
        else:
            raise ValueError(f"Unknown update rule: {update_rule}")
        
        self.beliefs[norm] = np.clip(posterior, 0.0, 1.0)
        
        # Update meta-beliefs if Level 2+
        if self.intentionality_level.value >= 2:
            self._update_meta_beliefs(norm, posterior)
    
    def _bayesian_update(self, prior: float, evidence: float) -> float:
        """Standard Bayesian belief updating"""
        # Simple Bayesian: posterior = (prior * likelihood) / evidence
        # Simplified: weight evidence by strength
        alpha = 0.3  # Learning rate
        return prior + alpha * (evidence - prior)
    
    def _hbu_update(self, prior: float, evidence: float) -> float:
        """
        Heteronomous Bayesian Updating (HBU).
        
        Group identity increases weight of confirming evidence,
        decreases weight of contradicting evidence.
        """
        if self.group_identity is None:
            return self._bayesian_update(prior, evidence)
        
        # HBU effect: 39% boost to confirming evidence (from Confer et al. 2025)
        hbu_factor = 1.39 if abs(evidence - prior) < 0.3 else 0.71
        
        alpha = 0.3 * hbu_factor
        return prior + alpha * (evidence - prior)
    
    def _confirmation_bias_update(self, prior: float, evidence: float) -> float:
        """Confirmation bias: only update if evidence confirms"""
        if abs(evidence - prior) < 0.3:  # Confirming evidence
            return self._bayesian_update(prior, evidence)
        else:  # Contradicting evidence: update weakly or not at all
            return prior + 0.1 * (evidence - prior)
    
    def _update_meta_beliefs(self, norm: str, new_belief: float) -> None:
        """Update beliefs about others' beliefs"""
        # Simple model: assume others' beliefs converge toward own
        if 1 in self.meta_beliefs:
            self.meta_beliefs[1][norm] = 0.7 * self.meta_beliefs[1].get(norm, 0.5) + 0.3 * new_belief
    
    def decide(
        self,
        options: List[str],
        context: Optional[Dict] = None
    ) -> Tuple[str, float]:
        """
        Make decision among options based on beliefs.
        
        Args:
            options: List of choices (e.g., ["support_reform", "oppose_reform"])
            context: Additional context (e.g., {"pressure": 0.8, "crisis": True})
        
        Returns:
            (chosen_option, confidence)
        """
        if self.intentionality_level == IntentionalityLevel.LEVEL_0:
            # Reactive: choose randomly weighted by beliefs
            return self._reactive_decision(options)
        elif self.intentionality_level == IntentionalityLevel.LEVEL_1:
            # Goal-directed: choose option maximizing belief alignment
            return self._goal_directed_decision(options)
        elif self.intentionality_level == IntentionalityLevel.LEVEL_2:
            # Strategic: consider others' likely responses
            return self._strategic_decision(options, context)
        else:  # LEVEL_3
            # Reflective: hypothetical reasoning, truth-tracking
            return self._reflective_decision(options, context)
    
    def _reactive_decision(self, options: List[str]) -> Tuple[str, float]:
        """Level 0: Reactive decision (random weighted)"""
        weights = [np.random.random() for _ in options]
        total = sum(weights)
        probabilities = [w/total for w in weights]
        choice = np.random.choice(options, p=probabilities)
        confidence = max(probabilities)
        return choice, confidence
    
    def _goal_directed_decision(self, options: List[str]) -> Tuple[str, float]:
        """Level 1: Goal-directed (maximize belief alignment)"""
        # Simple: choose option most aligned with dominant belief
        dominant_belief = max(self.beliefs, key=self.beliefs.get)
        
        # Map options to beliefs (simplified heuristic)
        if "support" in options[0].lower() or "reform" in options[0].lower():
            choice = options[0] if self.beliefs.get("liberty", 0.5) > 0.5 else options[1] if len(options) > 1 else options[0]
        else:
            choice = np.random.choice(options)
        
        confidence = self.beliefs.get(dominant_belief, 0.5)
        return choice, confidence
    
    def _strategic_decision(self, options: List[str], context: Optional[Dict]) -> Tuple[str, float]:
        """Level 2: Strategic (consider others' responses)"""
        # Consider meta-beliefs: what do others believe?
        if 1 in self.meta_beliefs:
            others_dominant = max(self.meta_beliefs[1], key=self.meta_beliefs[1].get)
            own_dominant = max(self.beliefs, key=self.beliefs.get)
            
            # If aligned with others, high confidence; if not, adjust
            if others_dominant == own_dominant:
                choice = self._goal_directed_decision(options)[0]
                confidence = 0.8
            else:
                # Strategic compromise
                choice = np.random.choice(options)
                confidence = 0.5
        else:
            return self._goal_directed_decision(options)
        
        # Factor in party loyalty if relevant
        if context and "party_position" in context:
            if self.party_loyalty > 0.7:
                choice = context["party_position"]
                confidence = self.party_loyalty
        
        return choice, confidence
    
    def _reflective_decision(self, options: List[str], context: Optional[Dict]) -> Tuple[str, float]:
        """Level 3: Reflective (hypothetical reasoning, truth-tracking)"""
        # Most sophisticated: evaluate counterfactuals
        scores = []
        for option in options:
            score = self._evaluate_option_reflectively(option, context)
            scores.append(score)
        
        best_idx = np.argmax(scores)
        choice = options[best_idx]
        confidence = scores[best_idx] / sum(scores) if sum(scores) > 0 else 0.5
        
        return choice, confidence
    
    def _evaluate_option_reflectively(self, option: str, context: Optional[Dict]) -> float:
        """Evaluate option using hypothetical reasoning"""
        score = 0.5  # Base score
        
        # Consider alignment with beliefs
        for belief, value in self.beliefs.items():
            if belief in option.lower():
                score += value * 0.3
        
        # Consider context if available
        if context:
            if context.get("crisis", False):
                # In crisis, prefer swift action (control)
                score += 0.2 if "control" in option.lower() else -0.1
            if context.get("pressure", 0) > 0.7:
                # High pressure: more likely to reform
                score += 0.2 if "reform" in option.lower() else -0.1
        
        # Normalization
        return max(0.0, min(1.0, score))
    
    def can_form_common_knowledge_with(self, other: 'Agent') -> bool:
        """
        Check if common knowledge is possible with another agent.
        
        Common knowledge requires both agents at Level 2+.
        Intentional span ≥2 blocks CK.
        """
        if self.intentionality_level.value < 2 or other.intentionality_level.value < 2:
            return False
        
        span = abs(self.intentionality_level.value - other.intentionality_level.value)
        return span < 2  # Span ≥2 blocks CK
    
    def __repr__(self) -> str:
        return (f"Agent(id={self.agent_id}, type={self.agent_type.value}, "
                f"level={self.intentionality_level.value}, "
                f"beliefs={self.beliefs})")
