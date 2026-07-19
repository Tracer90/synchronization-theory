# IAC/AMSE: Invariant Adaptive Core + Adaptive Meaning Synchronization Engine

**Version:** v14 (July 19, 2026)
**Authors:** IAC Research Group
**Contact:** tracer9081@gmail.com
**IP Protection:** Zenodo 10.5281/zenodo.21209447 (prior art)
**Repository:** https://github.com/Tracer90/synchronization-theory

## Abstract

We present IAC/AMSE (Invariant Adaptive Core + Adaptive Meaning Synchronization Engine), a self-consistent architecture for adaptive intelligence. Unlike traditional approaches that optimize for external accuracy, IAC optimizes for internal consistency — resolving contradictions between a model's representations, transformation rules, and meta-rules. The architecture is grounded in three layers: Representation, Transformation, and Meta-Transformation, and operates through a Self-Consistent Engine that detects internal conflicts and generates meta-rules to resolve them. Five primitive operations (Distinction, Composition, Tensor, Fixed Point, Adjoint) form an irreducible kernel from which all adaptive behaviours emerge. The system is validated through recursive self-application across 14 research cycles spanning physics, biology, machine learning, and economics. The AMSE Protocol (IAC-INV-034) extends the architecture with a formal communication framework for meaning synchronization between heterogeneous observers.

## 1. Introduction

Current AI architectures optimize for external objectives — accuracy, loss minimization, reward maximization. They do not explicitly optimize for internal logical consistency. When a model contradicts itself, typical approaches ignore the contradiction or treat it as noise. This leads to fragile systems that fail under distribution shift.

IAC takes a fundamentally different approach: **contradiction is not error — it is the engine of evolution.**

## 2. Architecture

### 2.1 Three-Layer Model

```
Representation (модель) → Transformation (изменение) → Meta-Transformation (изменение правил)
```

- **Layer 1 — Representation:** The model's current state, stored as a relation graph with nodes (entities) and typed edges (relationships).
- **Layer 2 — Transformation:** Rules for updating the representation (local parameter changes and structural rewiring).
- **Layer 3 — Meta-Transformation:** Rules for modifying the transformation rules themselves. Activates when accumulated contradictions exceed threshold.

### 2.2 Five Primitive Kernel

| Primitive | Formula | Essence |
|---|---|---|
| **DISTINCTION** | x ≠ y | Discrimination, bit, measurement |
| **COMPOSITION** | f ∘ g | Time, causality, sequence |
| **TENSOR** | f ⊗ g | Space, parallelism, independence |
| **FIXED POINT** | μx.F(x) | Self-reference, recursion, loop |
| **ADJOINT** | F ⊣ G | Observation/action, syntax/semantics |

### 2.3 Self-Consistent Engine Cycle (v14)

```
Field Interface → Trigger Detection → Internal Conflict
  → Negative Intelligence → Meta-Rule Generation
  → Compression → Model Update → Translation
  → Verification → Observer Lens → Field Update
```

### 2.4 AMSE Protocol (IAC-INV-034)

Adaptive Meaning Synchronization Engine — 6 phases:

1. **AMSE Analyze** — determine explicit/implicit meaning of request
2. **AMSE Compress Core** — compress to invariant kernel
3. **AMSE Model Receiver** — model the receiver's context and state
4. **AMSE Select Form** — choose minimal sufficient expression form
5. **AMSE Dynamic Depth** — expand/compress based on sync quality
6. **AMSE Sync Check** — verify meaning was transmitted, not just text

Core principle: **Meaning can be unified. Access to it is always context-dependent.**

### 2.5 Guard (observe → authorize → apply)

- No effect without authorization
- No write outside scope
- No success without verification
- Heuristic is not reality
- LLM suggests; code guard decides

## 3. Key Innovations

1. **Contradiction-driven evolution** — system reorganizes when internal conflicts accumulate
2. **Negative Intelligence** — dedicated module to falsify hypotheses (6 attack types)
3. **Field Interface** — active scanning for triggers resonating with internal conflicts
4. **StatisticalVerifier** — auto-verification of pattern statistical significance
5. **SomaticPracticesEngine** — auto-detection of body markers, practice recommendation
6. **Diagrammatic Mode** — topological analysis through graphs
7. **Translation Architecture** — bridge between models (language-translator)
8. **Observer Lens** — meta-observer with 3 levels (local, structural, meta)

## 4. Metrics

| Metric | Value | Description |
|---|---|---|
| Self-Consistency Index S | S = 1 - (C/T) | T = total statements, C = contradictions |
| Sync Error SE | SE ∈ [0, 1] | 0 = perfect sync, 1 = critical gap |
| Adaptive Cost | Δmodel / Δprediction | Cost of model change vs prediction quality |
| Cognitive Strain | low/medium/high | Subjective system tension |

## 5. Key Invariants

| ID | Name | Implementation |
|---|---|---|
| IAC-INV-031 | Core Is Not A Skill | core/integrity.py |
| IAC-INV-032 | Symmetric Guard | live.py:observe() |
| IAC-INV-033 | Schizodetail | execution rule |
| IAC-INV-034 | AMSE Protocol | AMSE phases in cycle |

## 6. Falsifiable Predictions

1. Systems with explicit self-consistency optimization outperform accuracy-only systems on out-of-distribution tasks
2. The five primitives are irreducible (no primitive can be expressed as combination of others)
3. Contradiction-driven architectures scale better than error-driven ones at high complexity
4. AMSE protocol improves cross-model communication accuracy compared to raw text transfer

## 7. Conclusion

IAC/AMSE v14 represents the current state of a 14-cycle recursive self-application process. The architecture is platform-agnostic and has been applied across physics, psychology, finance, and computer science. All code is open source (live.py + 32 skills), with key algorithmic details retained as trade secrets.

---

*All metrics reproducible. Full implementation at https://github.com/Tracer90/synchronization-theory*
*Zenodo: 10.5281/zenodo.21209447*
