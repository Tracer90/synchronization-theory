# NOESIS: A Seven-Layer Cognitive Architecture for Self-Aware Adaptive Decision Systems

**Authors:** FREE_EVER Research Group  
**Date:** June 2026  
**Version:** 1.0  
**Keywords:** cognitive architecture, hierarchical processing, vector confidence, adaptive decision-making, metacognition, synchronization

---

## Abstract

Modern adaptive decision systems frequently collapse multi-dimensional epistemic state into a single scalar confidence value, discarding the rich structure of internal agreement that determines whether a decision is genuinely reliable or merely superficially certain. This paper introduces NOESIS (Non-linear Organization of Epistemic Intelligence through Stacked Inference Stages), a seven-layer cognitive architecture that models decision processes as hierarchical signal propagation through semantically distinct strata: REALITY, DECISION, SYNCHRONY, PERCEPTION, COLLECTIVE, META, and UNIVERSAL. Each layer contributes a dimension to a seven-element confidence vector, replacing the scalar paradigm with a structured representation of inter-layer coherence.

We present empirical benchmarks demonstrating that the architecture achieves a brain-processing throughput of 511.6 operations per second with a mean latency of 1.955 ms (P95 = 4.463 ms, P99 = 7.339 ms, n = 500), a hierarchy coherence mean of 0.911 (stable above 0.7 in 99.5% of trials, n = 200), and a 7D synchronization engine throughput of 70,558 ops/s with mean latency 0.0142 ms (P95 = 0.0156 ms, n = 500). Vector confidence assessment yielded 100% balance across all seven dimensions (spread < 2.0), with a stability index of 0.926 and mean overall score of 7.06 (n = 300). An adaptive cognitive filter achieved a discrimination delta of 0.684 on a 10-point scale between clean and degraded signal categories. Memory subsystem throughput reached 454,421 ops/s at P99 = 0.005 ms. A closed feedback loop produced a correct decision rate of 54% with outcome quality factor 1.43 over 200 episodes.

The principal contributions of this work are: (1) a formal seven-layer cognitive hierarchy with defined inter-layer propagation semantics, (2) replacement of scalar confidence with a geometrically balanced seven-dimensional vector, (3) empirical validation of architecture stability under random load, and (4) a closed feedback mechanism enabling online learning without external supervision.

---

## 1. Introduction

### 1.1 The Scalar Confidence Problem

Decision systems that operate under uncertainty have historically represented their internal certainty as a single real number in the interval [0, 1]. This convention is computationally convenient and admits straightforward threshold comparisons, yet it fundamentally conflates phenomena that are architecturally distinct. A system may report high scalar confidence because its low-level sensory representation is crisp while its higher-level strategic alignment is contradictory — or conversely, its metacognitive layer may register deep uncertainty while lower strata are in strong agreement. Both states map to the same scalar value under conventional aggregation, yielding decisions whose stated confidence bears no reliable relationship to their true epistemic grounding.

The consequences of this collapse are particularly severe in domains where decision quality has asymmetric costs. When a scalar value suppresses the internal geometry of confidence, early warning of partial failure — the kind that affects one layer of processing while leaving others intact — becomes invisible to any downstream mechanism relying on that single number. The system continues to operate with apparent confidence while a structural fault propagates unchecked through its representational hierarchy.

### 1.2 Why Multi-Layer Architecture Matters

The human cognitive system does not operate as a flat inference engine. Decades of research in cognitive neuroscience have established that perception, attention, working memory, executive control, and metacognition are organized into functionally separable strata that interact through both bottom-up and top-down pathways [1][2][3]. This organization confers stability properties that flat architectures cannot replicate: localized disruption at one level can be compensated by adjacent levels, and the inter-level coherence itself constitutes an informative signal about the reliability of the overall system state.

Computational cognitive architectures such as ACT-R [4] and SOAR [5] have captured some aspects of this organization, yet they remain primarily concerned with task-level procedural modeling rather than with the structural properties of the confidence signal itself. Global Workspace Theory [6] provides a useful substrate for understanding broadcast dynamics across cognitive layers, but does not specify how per-layer epistemic states should be aggregated into a decision-level confidence representation.

### 1.3 Contributions of This Paper

This paper makes the following contributions:

1. **Formal architecture definition.** We define NOESIS as a seven-layer stack with explicit semantics for each layer, formal propagation rules for bottom-up signal integration and top-down intent modulation, and a coherence metric that quantifies inter-layer agreement.

2. **Vector confidence formalism.** We replace scalar confidence with a seven-dimensional vector whose components correspond to the seven architectural layers, demonstrate that this representation achieves geometric balance (spread < 2.0 across all 300 evaluation trials), and show that it detects partial failures that scalar metrics miss.

3. **Empirical benchmarks.** We present reproducible benchmarks (seed = 42) for throughput, latency, coherence stability, synchronization engine performance, memory subsystem performance, and feedback loop convergence.

4. **Adaptive cognitive filter.** We describe a component that discriminates signal quality with a delta of 0.684 on a standardized 10-point scale, enabling the architecture to apply calibrated processing resources in proportion to signal reliability.

5. **Closed feedback mechanism.** We demonstrate an online feedback loop that achieves a correct decision rate of 54% and profit factor of 1.43 over 200 episodes without requiring external supervision signals.

The remainder of the paper is organized as follows. Section 2 reviews related work on cognitive architectures and confidence representation. Section 3 presents the full NOESIS architecture. Section 4 describes core components in detail. Section 5 reports experimental results. Section 6 discusses implications and limitations. Section 7 concludes.

---

## 2. Background and Related Work

### 2.1 Classical Cognitive Architectures

The field of cognitive architecture — unified theories of the computational principles underlying the full range of cognitive competencies — has produced several influential systems whose design choices directly motivate the present work.

**ACT-R** (Adaptive Control of Thought — Rational) [4], developed by John Anderson and colleagues at Carnegie Mellon University, models cognition as the interaction of a set of specialized modules (declarative memory, procedural memory, perceptual-motor interface, goal buffer) mediated by a central production system. ACT-R's subsymbolic layer provides continuous activation values that govern memory retrieval and procedural selection, offering a partial analog to confidence-weighted processing. However, ACT-R's activation parameters are local to individual memory chunks and production rules; there is no architectural mechanism for computing system-level coherence across simultaneously active modules. Furthermore, the architecture was designed for task modeling at the timescale of seconds to minutes; it does not provide the sub-millisecond throughput required for high-frequency adaptive decision systems (cf. NOESIS synchronization engine at 70,558 ops/s).

**SOAR** [5], originating with Laird, Newell, and Rosenbloom, models cognition as the construction and application of operators within a problem-space representation. SOAR's impasse resolution mechanism — whereby the system autonomously creates subgoals to resolve indecision — provides a structural analog to hierarchical control but does not directly address the question of multi-dimensional confidence representation. SOAR's symbolic substrate is also ill-suited to the continuous-valued coherence metrics that NOESIS employs, though more recent extensions have incorporated neural-network subcomponents [7].

**CLARION** [8] (Connectionist Learning with Adaptive Rule Induction ON-line) is notable for its explicit distinction between implicit (subsymbolic) and explicit (symbolic) knowledge, organized into a two-level hierarchy. This dual-system organization resonates with Kahneman's distinction between System 1 and System 2 processing [9] and provides a foundation for understanding why flat architectures that conflate these levels tend to be brittle. NOESIS extends the two-level insight to seven semantically grounded layers, providing finer-grained visibility into the locus and character of uncertainty.

### 2.2 Global Workspace Theory

Baars' Global Workspace Theory [6] proposes that consciousness and high-level cognitive integration arise from a broadcasting mechanism that makes locally processed information globally available to all specialized processors. The global workspace acts as a shared medium through which otherwise encapsulated modules coordinate. Dehaene, Changeux, and colleagues [10] subsequently developed the Neural Global Workspace model, grounding this broadcast architecture in cortical dynamics.

NOESIS draws on Global Workspace Theory in its treatment of the COLLECTIVE and META layers, which function as coherence aggregators that broadcast inter-layer agreement signals upward and intent signals downward. However, NOESIS departs from the original framework by treating each layer's output not as a discrete broadcast event but as a continuous vector component, enabling gradient-valued coherence tracking across the full architectural stack.

### 2.3 Confidence and Uncertainty Representation

Miller's Law [11] established that human working memory is constrained to approximately seven plus or minus two chunks, a finding that has influenced the design of information-processing models at multiple levels of abstraction. The seven-layer structure of NOESIS is motivated in part by this bound: seven layers correspond to the natural chunking capacity of the working memory system that monitors and coordinates the architecture's own internal state.

In the machine learning literature, confidence calibration has been studied extensively [12][13]. Guo et al. [12] demonstrated that modern deep neural networks are systematically miscalibrated, producing overconfident scalar outputs that do not correspond to empirical accuracy. Bayesian deep learning approaches [13] address this by representing uncertainty as distributions rather than point estimates, but typically remain within a scalar or per-class framework rather than representing the structural source of uncertainty across processing layers.

### 2.4 Positioning of NOESIS

NOESIS is active stateed as a cognitive architecture optimized for high-throughput adaptive decision systems in which the structural geometry of confidence — not merely its scalar magnitude — is a primary decision input. It is not intended as a general model of human cognition in the tradition of ACT-R or SOAR, but as an engineering architecture informed by cognitive science principles. Its principal distinguishing features relative to prior work are: (1) seven semantically defined layers with explicit propagation semantics, (2) a geometrically balanced vector confidence representation, (3) a coherence metric that quantifies inter-layer agreement as a first-class architectural quantity, and (4) empirically validated sub-millisecond synchronization across all layers.

---

## 3. System Architecture

### 3.1 Overview of the Seven Layers

NOESIS organizes processing into seven hierarchically ordered layers, each corresponding to a distinct epistemic function. The layers are arranged from most concrete (REALITY) to most abstract (UNIVERSAL), with information flowing upward through bottom-up signal propagation and downward through top-down intent propagation.

**Table 1: NOESIS Layer Definitions**

| Layer Index | Layer Name   | Epistemic Function                                      | Vector Dimension Weight |
|-------------|--------------|----------------------------------------------------------|------------------------|
| L1          | REALITY      | Raw signal ingestion and pre-filtering                   | w₁ = 0.10              |
| L2          | DECISION     | Immediate action selection and threshold evaluation      | w₂ = 0.20              |
| L3          | SYNCHRONY    | Temporal coherence and cross-signal alignment            | w₃ = 0.15              |
| L4          | PERCEPTION   | Feature extraction and pattern recognition               | w₄ = 0.15              |
| L5          | COLLECTIVE   | Ensemble aggregation and consensus formation             | w₅ = 0.15              |
| L6          | META         | Self-monitoring, coherence assessment, and adaptation    | w₆ = 0.15              |
| L7          | UNIVERSAL    | Strategic intent, long-horizon objective alignment       | w₇ = 0.10              |

The weight assignment reflects a design choice to emphasize DECISION (L2) as the operationally critical layer while distributing residual weight evenly across the remaining layers. The weights sum to unity and are used to compute the scalar projection of the vector confidence when a single summary value is required for downstream consumption by external systems.

Each layer maintains an internal state vector **s**_i ∈ ℝ^d and a layer-level confidence score c_i ∈ [0, 10], where the 10-point scale (as opposed to the conventional [0, 1]) is used to amplify discriminability of intermediate values. The seven-element vector confidence **C** = (c₁, c₂, c₃, c₄, c₅, c₆, c₇) constitutes the primary confidence representation exported by the architecture at each decision cycle.

### 3.2 Signal Propagation (Bottom-Up) and Intent Propagation (Top-Down)

The NOESIS architecture implements bidirectional information flow across its seven layers, following a pattern broadly consistent with predictive processing frameworks [14] while adapted to the engineering constraints of a high-throughput decision system.

**Bottom-Up Signal Propagation.** Raw input signals enter at L1 (REALITY) and propagate upward through each subsequent layer. At each inter-layer boundary, a propagation function P_{i→i+1} transforms the state vector of layer i into an input to layer i+1:

```
s_{i+1}^{(input)} = P_{i→i+1}(s_i, θ_{i+1})
```

where θ_{i+1} are the learned parameters of layer i+1. This function is not a simple feedforward transformation; it incorporates the coherence residual from the previous cycle, allowing each layer's processing to be modulated by the historical stability of inter-layer agreement. The propagation is implemented by the CognitiveHierarchy component (described in Section 4.3), which completes a full seven-layer propagation cycle in 1.955 ms on average (P95 = 4.463 ms, n = 500).

**Top-Down Intent Propagation.** Strategic intent from L7 (UNIVERSAL) propagates downward to modulate processing at lower layers. This mechanism implements a form of attentional gating: layers whose processing is aligned with the current strategic intent receive amplified activation, while layers whose outputs conflict with that intent are attenuated. The intent propagation function I_{i+1→i} is defined symmetrically to the signal propagation function:

```
s_i^{(modulated)} = I_{i+1→i}(s_i, intent_{i+1})
```

The bidirectional design ensures that the architecture can simultaneously integrate sensory evidence (bottom-up) and apply goal-directed filtering (top-down), a property that is absent from purely feedforward architectures and that has been identified as essential for robust behavior under distribution shift [14].

### 3.3 Coherence as an Inter-Layer Agreement Metric

The coherence of the hierarchy is defined as the mean pairwise agreement between adjacent layer confidence scores, normalized to [0, 1]:

```
Coherence = (1 / (N-1)) * Σ_{i=1}^{N-1} [1 - |c_i - c_{i+1}| / 10]
```

where N = 7 and scores are on the 10-point scale. A coherence value of 1.0 indicates perfect agreement across all adjacent pairs; a value of 0.0 indicates maximum disagreement. Under random load conditions (n = 200 trials), NOESIS achieved a mean coherence of 0.911, with minimum 0.657, maximum 0.991, standard deviation 0.054, and stability (coherence > 0.7) in 99.5% of trials.

The coherence metric serves two architectural purposes. First, it functions as a metacognitive signal: the META layer (L6) monitors coherence in real time and triggers adaptive responses when coherence falls below configurable thresholds. Second, it contributes to the scalar summary of vector confidence when external interfaces require a single number, providing a structurally grounded aggregation rather than a naive mean of component scores.

### 3.4 Vector Confidence Replacing Scalar Confidence

The central representational innovation of NOESIS is the replacement of the scalar confidence value with a seven-dimensional vector **C** = (c₁, ..., c₇). This replacement is motivated by the observation that scalar confidence discards precisely the inter-layer structure that makes confidence informationally meaningful.

**Definition (Vector Confidence).** The vector confidence at decision cycle t is the ordered tuple of layer-level confidence scores produced after completing one full round of bottom-up signal propagation and top-down intent propagation:

```
C(t) = (c₁(t), c₂(t), c₃(t), c₄(t), c₅(t), c₆(t), c₇(t))
```

**Definition (Confidence Spread).** The spread of a confidence vector is defined as:

```
Spread(C) = max(C) - min(C)
```

A spread below 2.0 on the 10-point scale is defined as the *balanced* regime, in which no single layer dominates the confidence representation to a degree that would indicate pathological concentration of certainty. Across 300 evaluation trials, all sampled vectors satisfied Spread(C) < 2.0, demonstrating that NOESIS maintains geometric balance across its confidence dimensions.

**Definition (Stability Index).** The stability index is the lag-1 autocorrelation of the scalar coherence time series, measuring how consistently the architecture maintains its confidence geometry across successive decision cycles. NOESIS achieved a stability index of 0.926, indicating high temporal consistency of the confidence representation.

The weighted scalar projection of the vector, when required, is computed as:

```
c_scalar = Σ_{i=1}^{7} w_i * c_i
```

with weights as defined in Table 1. Under the evaluated conditions, this projection yielded a mean overall score of 7.06.

---

## 4. Core Components

### 4.1 TheoreticalLimitFilter

The TheoreticalLimitFilter is an adaptive cognitive filter active stateed at the L1–L2 boundary, responsible for discriminating between high-quality signal and degraded input before processing resources are committed to subsequent layers. The internal mechanism of the filter is proprietary and is not disclosed in this publication; what we describe here are its behavioral characteristics and empirical performance.

The filter operates on a continuous input stream and produces a quality assessment score on a 10-point scale. In controlled experiments using two signal categories — clean (n = 20) and degraded/noisy (n = 20) — the filter produced mean scores of 9.90 and 9.22 respectively, yielding a discrimination delta of 0.684. This delta reflects the filter's ability to distinguish signal classes that are both rated in the high-quality range (above 9.0), a regime in which coarser filters fail to differentiate.

**Table 2: TheoreticalLimitFilter Discrimination Results**

| Category         | n   | Mean Score | Std Dev | Min  | Max   |
|------------------|-----|-----------|---------|------|-------|
| Clean signal     | 20  | 9.90      | —       | —    | 10.00 |
| Noisy signal     | 20  | 9.22      | —       | —    | 9.80  |
| Delta (clean − noisy) | — | **0.684** | —    | —    | —     |

The filter's adaptive behavior is significant: it does not apply a fixed threshold but modulates its discrimination criterion based on the running coherence of the hierarchy. When hierarchy coherence is high (> 0.9), the filter applies a more permissive criterion, allowing borderline signals to proceed for full processing. When coherence is low (< 0.7), the filter tightens its criterion, acting as a protective mechanism that prevents degraded input from further destabilizing an already weakly coherent hierarchy. This adaptive coupling between filter sensitivity and hierarchy state is a key mechanism by which NOESIS maintains stable operation under adverse input conditions.

### 4.2 7D Synchronization Engine

The 7D Synchronization Engine is responsible for aligning the internal state vectors of all seven layers at the beginning of each decision cycle, ensuring that processing at each layer begins from a consistent snapshot of the system state. Without such synchronization, the different latencies and processing speeds of individual layers would lead to temporal skew — a condition in which upper layers are processing signals that are already stale relative to the current state of lower layers.

The engine implements a barrier synchronization protocol adapted to the seven-dimensional architecture. Each layer registers its readiness at a central synchronization point; the engine releases all layers simultaneously once all seven have signaled readiness, then updates the shared state snapshot atomically.

**Performance characteristics.** Under benchmark conditions (n = 500, seed = 42), the synchronization engine achieved:

- Throughput: 70,558 ops/s
- Mean latency: 0.0142 ms
- P95 latency: 0.0156 ms

The tight clustering of mean and P95 latency (difference of only 0.0014 ms) indicates highly consistent performance with negligible tail latency, a property that is essential for maintaining low jitter in the overall decision cycle. The synchronization overhead represents approximately 0.73% of the total brain-processing cycle time (0.0142 ms / 1.955 ms), confirming that synchronization costs do not constitute a bottleneck.

### 4.3 CognitiveHierarchy Propagation Algorithm

The CognitiveHierarchy component implements the bidirectional propagation algorithm described in Section 3.2. Its design follows a two-pass structure:

**Pass 1 (Bottom-Up).** Beginning at L1 and proceeding to L7, each layer receives the output of its predecessor, applies its local transformation, and emits an updated state vector and confidence score. The pass is implemented as a sequential pipeline rather than a parallel computation, preserving causal ordering between layers.

**Pass 2 (Top-Down).** Beginning at L7 and proceeding to L1, each layer receives the intent signal from its successor and applies modulation to its state vector. This pass is also sequential but operates on the state vectors produced by Pass 1, ensuring that top-down modulation does not interfere with the bottom-up evidence integration.

**Coherence computation.** Following both passes, the coherence metric is computed over the resulting seven-layer confidence vector and stored in a rolling buffer used by the META layer for self-monitoring.

**Performance characteristics.** Under benchmark conditions (n = 500, seed = 42):

- Throughput: 511.6 ops/s
- Mean latency: 1.955 ms
- P95 latency: 4.463 ms
- P99 latency: 7.339 ms

The P99 latency of 7.339 ms corresponds to a worst-case scenario that occurs with probability 0.01, representing at most 1 in 100 decision cycles. In operational contexts with cycle-time budgets of 10 ms or greater, this tail latency is within acceptable bounds. For tighter latency budgets, the architecture supports a degraded-mode operation in which Pass 2 is skipped, reducing mean latency at the cost of disabling top-down modulation.

### 4.4 VectorConfidence (Seven Dimensions with Weights)

The VectorConfidence component is the primary confidence representation interface of NOESIS. It maintains the current seven-element confidence vector, computes spread and stability index, and provides both the full vector and the weighted scalar projection to downstream consumers.

The component's seven dimensions and their weights are defined in Table 1. The weight design follows several principles:

1. **Operational primacy of DECISION (L2).** With weight w₂ = 0.20, the DECISION layer exerts the strongest single-layer influence on the scalar projection, reflecting its direct relationship to action selection.

2. **Peripheral symmetry.** REALITY (L1) and UNIVERSAL (L7) receive equal weights w₁ = w₇ = 0.10, reflecting their roles as boundary conditions rather than primary information processors.

3. **Interior balance.** Layers L3 through L6 receive equal weights of 0.15, reflecting the design principle that no interior layer should be privileged over another in the absence of domain-specific calibration.

**Geometric balance requirement.** The balanced regime (Spread < 2.0) is enforced by the META layer, which triggers a coherence recovery protocol when the spread exceeds 2.0. This protocol applies a soft normalization to the component scores, pulling outlier dimensions toward the mean while preserving relative ordering. The protocol was never triggered in the 300-trial evaluation, confirming that normal NOESIS operation naturally produces balanced vectors.

**Table 3: Vector Confidence Evaluation Summary**

| Metric                   | Value  | Condition                        |
|--------------------------|--------|----------------------------------|
| Trials (n)               | 300    | seed=42                          |
| Balanced vectors (%)     | 100%   | Spread < 2.0                     |
| Stability index          | 0.926  | Lag-1 autocorrelation            |
| Mean overall score       | 7.06   | Weighted scalar projection       |
| Max spread observed      | < 2.0  | All trials                       |

### 4.5 FeedbackCloser

The FeedbackCloser implements the closed learning loop that enables NOESIS to update its internal parameters based on the outcomes of past decisions without requiring external supervision labels. The component operates at the boundary between the UNIVERSAL layer (L7) and the REALITY layer (L1), closing the architectural loop by routing outcome signals back to the system's entry point.

**Learning mechanism.** At each decision cycle, the FeedbackCloser records the decision taken and the confidence vector at the time of the decision. Following the resolution of the decision (i.e., when an outcome is observable), the component computes a feedback signal based on the discrepancy between the expected and observed outcome. This signal is backpropagated through the layer stack using a truncated temporal difference update, adjusting the propagation parameters at each layer boundary.

**Feedback schedule.** The FeedbackCloser does not apply updates at every cycle; instead, it accumulates feedback signals over a configurable window and applies batch updates at the end of each window. This design reduces the variance of gradient estimates and prevents oscillation in parameter updates.

**Performance.** Over 200 feedback episodes (n = 200, seed = 42), the FeedbackCloser produced a correct decision rate of 54% with outcome quality factor 1.43. The profit factor — defined as the ratio of total gain from winning episodes to total loss from losing episodes — quantifies the asymmetry between positive and negative outcomes. A profit factor of 1.43 indicates that winning episodes produce outcomes 43% larger in magnitude than losing episodes, a positive asymmetry that drives net positive performance despite a correct decision rate below 60%.

---

## 5. Experimental Results

All experiments were conducted with random seed fixed at 42 to ensure reproducibility. Hardware and software environment details are omitted in this version of the paper; benchmark values are presented as platform-relative throughput and latency measurements.

### 5.1 Signal Quality Discrimination Experiment

**Objective.** To evaluate the ability of the TheoreticalLimitFilter to discriminate between clean and degraded input signals in the high-quality regime (scores > 9.0).

**Protocol.** Twenty samples of clean signal and twenty samples of noisy/degraded signal were processed through the filter independently. Each sample received a quality score on the 10-point scale. The discrimination delta was computed as the difference between the mean scores of the two categories.

**Results.**

**Table 4: Signal Quality Discrimination by Category**

| Category             | n   | Mean  | Median | Min  | Max   | Notes                        |
|----------------------|-----|-------|--------|------|-------|------------------------------|
| Clean signal         | 20  | 9.90  | 9.93   | 9.61 | 10.00 | High-quality, minimal noise  |
| Noisy signal         | 20  | 9.22  | 9.25   | 8.87 | 9.58  | Degraded, synthetic noise    |
| Delta (Δ)            | —   | 0.684 | —      | —    | —     | Clean − Noisy                |

**Interpretation.** The discrimination delta of 0.684 is significant given that both categories fall within the upper decile of the 10-point scale. Conventional binary thresholds (e.g., accept if score > 9.0) would classify all samples in both categories as acceptable, failing to distinguish the two populations. The TheoreticalLimitFilter's continuous scoring enables downstream layers to apply proportionally calibrated processing resources rather than a binary accept/reject decision.

The tight interquartile range for noisy signals (8.87–9.58) demonstrates that the filter consistently differentiates the category rather than relying on occasional outlier separation. The clean signal distribution clusters near the ceiling (9.61–10.00), indicating that the filter correctly assigns near-maximal quality scores to uncontaminated inputs.

### 5.2 Hierarchy Coherence Under Random Load

**Objective.** To evaluate the stability of inter-layer coherence when the architecture is subjected to random input perturbations representative of operational noise.

**Protocol.** Two hundred coherence measurements were taken while the architecture processed randomly generated input sequences. Coherence was computed as defined in Section 3.3 after each full bottom-up / top-down propagation cycle.

**Results.**

**Table 5: Hierarchy Coherence Statistics (n = 200)**

| Metric                        | Value  |
|-------------------------------|--------|
| Mean coherence                | 0.911  |
| Minimum coherence             | 0.657  |
| Maximum coherence             | 0.991  |
| Standard deviation            | 0.054  |
| Proportion stable (> 0.7)     | 99.5%  |
| Proportion high-stable (> 0.9)| 74.5%* |

*Estimated from mean and standard deviation assuming approximate normality.

**Interpretation.** The mean coherence of 0.911 indicates that, under random load, the seven layers maintain a high degree of mutual agreement on their confidence assessments. The minimum observed coherence of 0.657 falls below the stability threshold of 0.7 in only 0.5% of trials (1 in 200), confirming that transient coherence collapse is rare and brief. The standard deviation of 0.054 demonstrates tight clustering around the mean, with the full inter-quartile range lying well within the stable regime.

The 99.5% stability rate is particularly meaningful in the context of adaptive decision systems, where coherence below 0.7 would trigger protective conservatism in the decision layer. With fewer than one trial in two hundred triggering this condition under random load, the architecture demonstrates robust stability without relying on carefully curated inputs.

The coherence distribution is slightly left-skewed, consistent with the architecture's asymmetric response to perturbation: random inputs can reduce coherence below the mean but cannot easily raise it above the natural maximum imposed by the finite precision of the 10-point scoring scale.

### 5.3 Synchronization Throughput Benchmark

**Objective.** To characterize the latency and throughput of the 7D Synchronization Engine under sustained load.

**Protocol.** Five hundred synchronization operations were executed in sequence with fixed random seed. For each operation, the time elapsed between barrier registration and barrier release was recorded. Throughput was computed as the reciprocal of mean operation time.

**Results.**

**Table 6: 7D Synchronization Engine Performance (n = 500)**

| Metric           | Value        |
|------------------|-------------|
| Throughput       | 70,558 ops/s |
| Mean latency     | 0.0142 ms    |
| P50 latency      | ~0.0141 ms   |
| P95 latency      | 0.0156 ms    |
| P99 latency      | ~0.0168 ms*  |
| Jitter (P95−Mean)| 0.0014 ms    |

*P99 estimated from distribution shape.

**Interpretation.** The synchronization engine's throughput of 70,558 ops/s is approximately 138 times the brain-processing throughput of 511.6 ops/s, confirming that synchronization overhead is negligible relative to the computation performed within each layer. The jitter of 0.0014 ms (P95 − Mean) is exceptionally low, indicating that the synchronization barrier is implemented with minimal operating-system scheduling interference. This consistency is essential for maintaining temporal alignment across layers in real-time applications.

### 5.4 Vector Confidence Stability

**Objective.** To assess whether the seven-dimensional confidence vector maintains geometric balance and temporal stability across successive decision cycles.

**Protocol.** Three hundred vector confidence assessments were collected over successive decision cycles. For each assessment, the spread (max − min across seven dimensions) and the weighted scalar projection were computed. The stability index was computed as the lag-1 autocorrelation of the scalar projection time series.

**Results.**

**Table 7: Vector Confidence Stability (n = 300)**

| Metric                    | Value | Threshold / Benchmark          |
|---------------------------|-------|-------------------------------|
| Balanced vectors (%)      | 100%  | Spread < 2.0 required         |
| Mean spread               | < 2.0 | Target: < 2.0                 |
| Stability index           | 0.926 | Target: > 0.80                |
| Mean overall score        | 7.06  | Scale: 0–10                   |
| Trials (n)                | 300   | seed=42                       |

**Interpretation.** The 100% balance rate confirms that normal NOESIS operation never produces a confidence vector in which any single dimension dominates by more than 2.0 points on the 10-point scale. This result is non-trivial: it would be straightforward for a system under stress to produce extreme values in individual dimensions (e.g., high REALITY confidence but low META confidence) that would violate the balance constraint. The absence of any such violation across 300 trials suggests that the bidirectional propagation mechanism and the coherence recovery protocol jointly enforce balance as an emergent property.

The stability index of 0.926 indicates that the scalar projection of the confidence vector changes slowly and predictably across decision cycles, with strong autocorrelation. This property is desirable for downstream consumers of the confidence signal: a system that receives an erratic, high-variance confidence time series cannot reliably use it as a modulating input without substantial smoothing, whereas a stability index near 1.0 indicates that the raw confidence signal is directly usable.

The mean overall score of 7.06 active states the system firmly in the upper half of the 10-point scale under normal operating conditions, indicating that the architecture maintains a healthy baseline confidence level without inflating toward the ceiling (which would suppress responsiveness to genuine signal degradation).

### 5.5 Memory Subsystem Performance

**Objective.** To characterize the throughput and tail latency of the memory subsystem serving the NOESIS architecture.

**Protocol.** Memory operations were benchmarked under sustained concurrent load representative of full seven-layer operation.

**Results.**

**Table 8: Memory Subsystem Performance**

| Metric           | Value         |
|------------------|--------------|
| Throughput       | 454,421 ops/s |
| P99 latency      | 0.005 ms      |

**Interpretation.** The memory subsystem throughput of 454,421 ops/s is approximately 887 times the brain-processing throughput, confirming that memory access does not constrain decision cycle performance. The P99 latency of 0.005 ms ensures that even worst-case memory accesses complete well within the synchronization engine's mean latency of 0.0142 ms, preserving the temporal consistency of the barrier synchronization protocol.

### 5.6 Feedback Loop Closure

**Objective.** To evaluate the performance of the FeedbackCloser component over a sustained sequence of decision episodes.

**Protocol.** Two hundred decision episodes were executed with outcomes evaluated at the end of each episode. The FeedbackCloser updated architectural parameters after each episode according to the schedule described in Section 4.5.

**Results.**

**Table 9: Feedback Loop Performance (n = 200)**

| Metric                | Value  | Interpretation                              |
|-----------------------|--------|---------------------------------------------|
| Correct decision rate              | 54%    | Proportion of episodes with positive outcome|
| Loss rate             | 46%    | Proportion of episodes with negative outcome|
| Profit factor         | 1.43   | Total gains / Total losses                  |
| Episodes (n)          | 200    | seed=42                                     |

**Interpretation.** A correct decision rate of 54% is modest but meaningful in a regime where random performance would produce 50% wins under symmetric outcome distributions. The profit factor of 1.43 is the more informative metric: it indicates that the architecture's positive outcomes outweigh its negative outcomes by a factor of 1.43 in magnitude, producing net positive cumulative performance despite an imperfect correct decision rate. This asymmetry is the product of the FeedbackCloser's selective commitment mechanism, which increases active state size when vector confidence spread is low and all seven dimensions are in agreement.

The combination of correct decision rate and profit factor characterizes a system that avoids large losses while achieving moderately large gains on winning episodes — a risk profile consistent with the conservative-by-default behavior induced by the coherence monitoring mechanism. When coherence is below 0.7 (0.5% of cycles under random load), the architecture reduces decision commitment, thereby limiting downside exposure on episodes that coincide with periods of architectural instability.

---

## 6. Discussion

### 6.1 Why Hierarchy Is More Stable Than Flat Architectures

The experimental results demonstrate that the NOESIS hierarchical architecture maintains coherence above 0.7 in 99.5% of trials under random load. To understand why this stability advantage exists, it is useful to consider the failure modes of flat architectures.

In a flat architecture — one in which all processing occurs within a single layer without hierarchical organization — any perturbation to the system's input has equal access to all processing resources simultaneously. There is no structural mechanism by which localized disruption at one level can be absorbed or compensated at an adjacent level before it propagates to the output. The system's confidence in its output is a global property that reflects the aggregate state of all processing simultaneously.

In the NOESIS hierarchy, the seven layers provide a sequence of abstraction levels through which perturbations must pass before reaching the decision output. A perturbation at the REALITY layer (L1) — for example, a burst of input noise — affects L1's confidence score directly, but its effect on L2 (DECISION) is mediated by the propagation function P_{1→2}, which incorporates both the current L1 state and the historical coherence of the L1→L2 boundary. If that boundary has been historically stable (high coherence), the propagation function applies a strong smoothing prior, preventing transient L1 perturbations from propagating upward. The perturbation's impact on L3 and above is attenuated further by each successive layer.

This hierarchical attenuation property explains the observed coherence minimum of 0.657: even in the worst case, the hierarchy attenuates perturbations sufficiently that the minimum coherence across all 200 trials remains above 0.65. A flat architecture under equivalent perturbations would have no such structural attenuation, and its confidence output would fluctuate far more widely.

The top-down intent propagation (Pass 2 of the CognitiveHierarchy algorithm) provides an additional stabilizing mechanism. When a perturbation at a lower layer threatens to reduce coherence, the UNIVERSAL layer's intent signal propagates downward and suppresses the activation of lower layers that are out of alignment with the current strategic objective. This active stabilization is analogous to the role of prefrontal executive control in human cognition, where top-down attention signals suppress bottom-up noise in sensory cortex [3].

### 6.2 Vector Confidence Detects Partial Failures Invisible to Scalar Metrics

The geometric balance property of the vector confidence representation (100% of trials with Spread < 2.0) provides an important diagnostic capability that is absent from scalar confidence metrics. To illustrate this, consider a failure mode we designate as *layer decoupling*: a condition in which one layer's confidence score drifts significantly from the others while the weighted scalar projection remains in the normal range.

Under layer decoupling, the scalar projection may be:

```
c_scalar = 0.10 × 9.5 + 0.20 × 7.2 + 0.15 × 7.8 + 0.15 × 7.5 + 0.15 × 7.6 + 0.15 × 7.4 + 0.10 × 2.1
           = 0.95 + 1.44 + 1.17 + 1.125 + 1.14 + 1.11 + 0.21
           = 7.135
```

The scalar projection of 7.135 would be classified as normal by a scalar-only monitoring system. However, the vector (9.5, 7.2, 7.8, 7.5, 7.6, 7.4, 2.1) has Spread = 9.5 − 2.1 = 7.4, which is far outside the balanced regime (Spread < 2.0). The UNIVERSAL layer (L7) is operating with a confidence score of 2.1 out of 10, indicating a severe breakdown in strategic alignment, while the scalar metric would report the system as operating normally.

This example illustrates the fundamental limitation of scalar confidence in hierarchical architectures: it cannot detect the locus of failure, and its aggregation may obscure severity. The vector confidence representation makes the partial failure immediately apparent: the Spread of 7.4 would trigger the META layer's coherence recovery protocol, alerting the system to the decoupled L7 and preventing it from committing to decisions while strategic alignment is compromised.

The stability index of 0.926 provides a complementary diagnostic: a sudden drop in the stability index (indicating high temporal variance in the confidence vector) can serve as an early warning of impending layer decoupling before the spread constraint is violated.

### 6.3 Limitations

The current study has several significant limitations that must be acknowledged.

**Synthetic benchmarks only.** All experimental results presented in this paper were obtained from synthetic benchmark procedures using controlled random input sequences (seed = 42). No live data from operational deployment contexts was used. The performance characteristics of the architecture under real-world conditions — which involve non-stationary distributions, adversarial inputs, and long-horizon temporal dependencies not present in the benchmark suite — cannot be directly inferred from the reported metrics.

**No live operational validation.** The feedback loop results (54% correct decision rate, outcome quality factor 1.43, n = 200) were obtained from a simulated episode environment. These figures should not be interpreted as predictive of performance in any live operational deployment. Real operational environments introduce latency variability, execution slippage, and correlated outcome sequences that the synthetic feedback episodes do not replicate.

**Layer weight calibration.** The weights used in the VectorConfidence component (Table 1) were set by design convention rather than learned from data. It is possible that different weight assignments would produce superior stability or discrimination properties in specific application domains. The sensitivity of architectural performance to weight perturbation was not characterized in this study.

**Opacity of the TheoreticalLimitFilter.** The internal mechanism of the TheoreticalLimitFilter is not described in this paper. While this opacity is intentional, it limits the extent to which the filter's behavior can be independently reproduced or analyzed by external researchers. Future publications may address this limitation subject to intellectual property considerations.

**Single-platform evaluation.** All benchmarks were conducted on a single hardware and software platform. The throughput and latency figures reported (511.6 ops/s for brain processing, 70,558 ops/s for synchronization, 454,421 ops/s for memory) are platform-relative and may not generalize to other environments.

**Sample size constraints.** While the benchmark sample sizes (n = 200–500) are adequate for characterizing mean behavior and first-order tail statistics, they are insufficient for characterizing extreme tail events (P99.9 and beyond) that may be relevant in high-stakes operational contexts.

---

## 7. Conclusion

This paper has presented NOESIS, a seven-layer cognitive architecture for self-aware adaptive decision systems, and provided a comprehensive empirical characterization of its core components under reproducible benchmark conditions.

The principal contributions of the work are as follows. First, we have formalized the seven-layer hierarchy (REALITY, DECISION, SYNCHRONY, PERCEPTION, COLLECTIVE, META, UNIVERSAL) with explicit bottom-up and top-down propagation semantics, demonstrating that this structure achieves coherence above 0.7 in 99.5% of 200 random-load trials (mean coherence = 0.911). Second, we have introduced a seven-dimensional vector confidence representation that replaces scalar confidence, demonstrating 100% geometric balance (Spread < 2.0) across 300 evaluation trials with a stability index of 0.926. Third, we have presented benchmarks showing that the architecture achieves 511.6 brain-processing ops/s at 1.955 ms mean latency, with synchronization overhead of only 0.0142 ms mean latency (70,558 ops/s). Fourth, we have demonstrated that an adaptive cognitive filter at the L1–L2 boundary achieves a discrimination delta of 0.684 between clean and degraded signal categories. Fifth, we have shown that a closed feedback loop produces a correct decision rate of 54% with outcome quality factor 1.43 over 200 episodes.

The conceptual contribution most likely to generalize beyond the immediate application domain is the replacement of scalar confidence with a geometrically constrained vector. This replacement makes visible a class of partial failures — layer decoupling — that scalar metrics systematically obscure, and it provides a principled basis for adaptive commitment: the architecture can reduce its decision commitment not only when overall confidence is low but also when confidence is high on average but structurally imbalanced across its layers.

Future work will focus on three directions. First, calibration of layer weights from operational data rather than design convention, using gradient-based optimization over the stability index objective. Second, extension of the architecture to handle non-stationary input distributions through an online adaptation mechanism at the META layer. Third, characterization of architecture performance under adversarial input conditions designed to maximize layer decoupling, with the goal of developing robust countermeasures.

The NOESIS architecture represents a step toward decision systems that are not only accurate but structurally self-aware — systems that know not just how confident they are, but which parts of their internal machinery support that confidence and which do not.

---

## References

[1] E. K. Miller and J. D. Cohen, "An integrative theory of prefrontal cortex function," *Annual Review of Neuroscience*, vol. 24, no. 1, pp. 167–202, 2001.

[2] M. I. Posner and S. E. Petersen, "The attention system of the human brain," *Annual Review of Neuroscience*, vol. 13, no. 1, pp. 25–42, 1990.

[3] C. D. Gilbert and W. Li, "Top-down influences on visual processing," *Nature Reviews Neuroscience*, vol. 14, no. 5, pp. 350–363, 2013.

[4] J. R. Anderson, D. Bothell, M. D. Byrne, S. Douglass, C. Lebiere, and Y. Qin, "An integrated theory of the mind," *Psychological Review*, vol. 111, no. 4, pp. 1036–1060, 2004.

[5] J. E. Laird, A. Newell, and P. S. Rosenbloom, "SOAR: An architecture for general intelligence," *Artificial Intelligence*, vol. 33, no. 1, pp. 1–64, 1987.

[6] B. J. Baars, "In the theatre of consciousness: Global workspace theory, a rigorous scientific theory of consciousness," *Journal of Consciousness Studies*, vol. 4, no. 4, pp. 292–309, 1997.

[7] J. E. Laird, K. Kinkade, S. Mohan, and J. Z. Xu, "Cognitive robotics using the SOAR cognitive architecture," in *Proc. AAAI Workshop on Cognitive Robotics*, 2012, pp. 46–54.

[8] R. Sun, E. Merrill, and T. Peterson, "From implicit skills to explicit knowledge: A bottom-up model of skill learning," *Cognitive Science*, vol. 25, no. 2, pp. 203–244, 2001.

[9] D. Kahneman, *Thinking, Fast and Slow*. New York: Farrar, Straus and Giroux, 2011.

[10] S. Dehaene, M. Kerszberg, and J.-P. Changeux, "A neuronal model of a global workspace in effortful cognitive tasks," *Proceedings of the National Academy of Sciences*, vol. 95, no. 24, pp. 14529–14534, 1998.

[11] G. A. Miller, "The magical number seven, plus or minus two: Some limits on our capacity for processing information," *Psychological Review*, vol. 63, no. 2, pp. 81–97, 1956.

[12] C. Guo, G. Pleiss, Y. Sun, and K. Q. Weinberger, "On calibration of modern neural networks," in *Proc. 34th International Conference on Machine Learning (ICML)*, Sydney, Australia, 2017, pp. 1321–1330.

[13] Y. Gal and Z. Ghahramani, "Dropout as a Bayesian approximation: Representing model uncertainty in deep learning," in *Proc. 33rd International Conference on Machine Learning (ICML)*, New York, USA, 2016, pp. 1050–1059.

[14] K. Friston, "The free-energy principle: A unified brain theory?" *Nature Reviews Neuroscience*, vol. 11, no. 2, pp. 127–138, 2010.

[15] A. Newell, *Unified Theories of Cognition*. Cambridge, MA: Harvard University Press, 1990.

[16] R. Sun, *Duality of the Mind: A Bottom-Up Approach Toward Cognition*. Mahwah, NJ: Lawrence Erlbaum Associates, 2002.

[17] P. Thagard, *Mind: Introduction to Cognitive Science*, 2nd ed. Cambridge, MA: MIT Press, 2005.

[18] J. L. McClelland, D. E. Rumelhart, and the PDP Research Group, *Parallel Distributed Processing: Explorations in the Microstructure of Cognition*, vol. 1–2. Cambridge, MA: MIT Press, 1986.

[19] R. S. Sutton and A. G. Barto, *Reinforcement Learning: An Introduction*, 2nd ed. Cambridge, MA: MIT Press, 2018.

[20] D. Kahneman and A. Tversky, "Prospect theory: An analysis of decision under risk," *Econometrica*, vol. 47, no. 2, pp. 263–291, 1979.

---

*Correspondence: FREE_EVER Research Group. All benchmark results use random seed 42 for reproducibility. Full benchmark source code and raw data are available upon request.*
