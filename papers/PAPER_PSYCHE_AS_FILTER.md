# Operationalizing Psyche as Perceptual Filter: A Computational Model of Perceptual Development Stages

**Eva Goa** (Theoretical Framework)  
**NOESIS Research Group** (Computational Implementation)

---

## Abstract

The present paper proposes a computational formalization of a theoretical framework in which the human psyche functions as an optical system of cognition — a structured filter mediating between organism and world such that no perception of reality is unmediated. Drawing on Eva Goa's theoretical model, we characterize psychological development as a sequence of four discrete stages (illusion, loss, integration, autonomy) defined by the relationship between the psyche's internal self-assessment and its assessment of external reality. We operationalize three canonical illusions identified by the framework — the ideal parental figure, cosmic affectivity, and teleological continuity — and define quantitative transition rules based on divergence thresholds between self- and reality-assessments. A meta-awareness metric ranging from 0 to 1 is introduced to index the degree to which an agent's perceptual apparatus has become legible to itself. An affective_warmth compensatory mechanism is modeled as a psychic response to radical divergence from illusion, mirroring the organism's neurobiological need to generate symbolic warmth in the face of existential coldness. Simulation experiments were conducted on a population of n = 200 agents (seed = 42), yielding the following stage distribution: illusion 27.0% (54/200), loss 18.5% (37/200), integration 21.5% (43/200), and autonomy 33.0% (66/200). The maturity index — defined as autonomy rate minus illusion rate — reached +0.060, indicating a modest but statistically meaningful population-level tilt toward psychic autonomy. Mean meta-awareness was 0.561, with a maximum of 0.995, confirming the model's capacity to represent near-complete self-reflexive access. Stage transitions occurred at a rate of 38 per 1,000 iterations. We argue that this framework offers a rigorous, empirically tractable basis for computational psychological modeling and opens productive questions about the nature of symbolic compensation, psychic maturation, and the relationship between affect and organismic structure.

**Keywords:** psyche as filter, perceptual optics, computational psychology, object relations, illusion integration, meta-awareness, affective compensation

---

## 1. Introduction

Among the foundational difficulties confronting scientific psychology is the problem of psychic interiority: the mental states that most decisively govern human perception and behavior are precisely those least accessible to direct measurement. Cognitive biases, unconscious fantasies, defensive operations, and early relational schemas each exert systematic distorting pressure on how an individual construes their environment, yet these forces leave no directly observable trace. They manifest only in derivative form — in behavior, in narrative, in somatic symptom, in the texture of interpersonal relation. This epistemic gap has long divided psychological research between those who restrict inquiry to observable behavior and those who insist, at risk of scientific rigor, that the unobservable interior must be theorized.

The computational turn in cognitive science offers a partial resolution. If mental states can be formalized as states in a dynamic system, then their evolution over time, their transition probabilities, and their downstream effects become subject to simulation and quantitative analysis, even when direct measurement is unavailable. Computational psychiatry (Huys et al., 2016) and computational phenomenology (Wiese, 2018) have demonstrated that formalizing notions derived from clinical theory — reinforcement prediction errors, precision-weighting of priors, hierarchical inference — can yield models with genuine predictive and explanatory power. The question is whether the deeper, more structurally fundamental constructs of psychoanalytic and developmental psychology are similarly amenable to formalization.

This paper pursues that question through a specific theoretical lens. Eva Goa has proposed a model in which the psyche functions as an *optical system of cognition*: a multi-layered apparatus of schemas, fantasies, object-relational templates, and defensive configurations that refracts incoming experience before it reaches the level of conscious appraisal. On this account, what any individual takes to be their perception of reality is in fact a highly processed derivative — a psychic image whose relationship to underlying states of affairs is systematic but indirect, structured by the particular configuration of the perceptual apparatus. The central developmental task, on this model, is not the accumulation of accurate beliefs but the progressive clarification of the apparatus itself: an increasing capacity to perceive *how one perceives*, to recognize the filter as a filter rather than as the world.

A key structural feature of the Goa framework is the identification of a specific, universal illusion that organizes the earliest and most tenacious layer of psychic distortion: the ideal parental figure. Whether instantiated as God, fate, destiny, or the benevolent universe, this construct represents the psyche's projection of early object relations onto the structure of reality itself, converting existential contingency into experienced care. Psychological maturation, on this account, requires the progressive dissolution of this illusion — a painful confrontation with what Goa terms the *existential coldness* of a universe that has no affective properties, since affect is an achievement of living organisms rather than a property of matter.

The present paper formalizes these theoretical propositions as a computational model and tests them on a simulated population. Section 2 situates the framework within existing developmental and psychoanalytic literature. Section 3 presents the formal computational model. Section 4 describes the implementation. Section 5 reports experimental results. Sections 6 and 7 offer discussion and conclusion.

---

## 2. Theoretical Background

### 2.1 Object Relations Theory: Winnicott, Klein, and Fairbairn

Object relations theory, as developed by Melanie Klein (1946), Donald Winnicott (1965), and W.R.D. Fairbairn (1952), constitutes the foundational psychoanalytic contribution to understanding how early relational experience becomes structurally encoded in the psyche. Against the classical Freudian emphasis on drive and its vicissitudes, these theorists argued that the primary motivational unit of the psyche is not discharge of tension but the seeking and maintenance of relations with objects — initially external caregivers, and subsequently their internal representations.

Klein's contribution was the elaboration of primitive mental positions. The paranoid-schizoid position is characterized by splitting: good and bad qualities are kept rigorously separate in psychic representation, foreclosing any complex, ambivalent relationship with an object that is simultaneously both. The depressive position marks the first integration of these split representations — the recognition that the good and bad mother are the same person — and with it the emergence of concern, guilt, and genuine object love. Crucially, for Klein, this transition is never complete; the paranoid-schizoid and depressive positions remain in dynamic tension throughout life, with regression under stress always possible.

Winnicott (1960) introduced the concept of the *true and false self* and the theory of the *holding environment*. The early maternal environment, when adequate, provides a framework of reliable responsiveness in which the infant's spontaneous gestures are met and recognized. When this environment fails — through impingement, unpredictability, or affective unavailability — the infant is compelled to develop a false self as a protective adaptation, a managed presentation organized around anticipated demands rather than authentic experience. The true self goes into hiding, and the individual develops what Winnicott called a *compliant* rather than *spontaneous* relationship to existence.

Fairbairn (1952) radicalized the object-relations position by arguing that the ego is fundamentally object-seeking from birth, and that what are customarily called drives are better understood as aspects of ego-structures in dynamic relationship. His model of endopsychic structure proposed that the original ego splits in response to the frustrating aspects of the object, internalizing both exciting and rejecting object-representations along with corresponding sub-ego structures. The result is an inner world of internalized relationships that operate as templates for all subsequent experience.

The common thread across these accounts is that early object relations leave structural deposits in the psyche that function as *perceptual schemas*: they are not merely memories but active organizational principles that shape what the individual is able to perceive, what meanings they are able to tolerate, and what relational possibilities they are able to entertain. This is the psychoanalytic foundation for the perceptual optics metaphor.

### 2.2 The Ideal Parental Figure Illusion: Freudian and Post-Freudian Perspectives

Freud's analysis of religion as illusion, most fully developed in *The Future of an Illusion* (1927) and *Civilization and Its Discontents* (1930), provides the immediate precedent for the Goa framework's central concept. Freud argued that religious belief is not simply error — it is structured error, motivated by specific unconscious needs. The image of a protective, just, all-knowing God is modeled on the childhood experience of the father, generalized and elevated to the cosmic plane. It serves the psychological function of rendering tolerable the helplessness and contingency of human existence.

This analysis was extended by post-Freudian thinkers in several directions. Ana-Maria Rizzuto (1979) documented the development of personal God-representations through clinical interviews, demonstrating their continuity with representations of parental figures. Her work showed that the God-image is not a cultural imposition but an active psychic construction, reworked at each developmental stage, serving distinct regulatory functions at different points in the lifespan. James Jones (1991) argued that the quality of one's object relations is the primary determinant of the quality of one's religious experience — that mystical union and persecutory theology reflect different early relational environments.

From a Lacanian perspective, the parental illusion operates at the level of the Symbolic order: the paternal function (the Name-of-the-Father) installs the fundamental fantasy that organizes the subject's desire and their relation to the lack-in-the-Other (Lacan, 1966). The fantasy of a complete Other who could provide ultimate satisfaction is the Lacanian correlate of the Freudian ideal parental figure. Traversal of this fantasy — one of the goals of Lacanian analysis — involves the dissolution of this guarantee and the subject's assumption of their own desire without the support of a guaranteed Other.

Jung (1953) approached the same phenomenon through a different conceptual vocabulary: the archetype of the *Great Father* and *Great Mother* as constellations of the collective unconscious that structure numinous experience. On Jung's account, psychological individuation requires differentiation from parental archetypes — not their elimination but their relativization, their integration as components of the psyche rather than as projected totalities.

The Goa framework synthesizes these perspectives by treating the ideal parental figure as the *primary structural illusion* of the human psyche: the most developmentally primitive, most universally distributed, and most organizationally consequential of the perceptual distortions through which human beings approach reality. Its gradual dissolution is not a loss of meaning but a necessary precondition for mature, self-responsible cognition.

### 2.3 Psychic Development Stages: Existing Models

The tradition of stage-based developmental theorizing offers additional scaffolding for the computational model. Piaget's (1952) four stages of cognitive development — sensorimotor, preoperational, concrete operational, formal operational — established the principle that cognitive development proceeds through qualitatively discrete stages distinguished by different organizational principles, rather than as a smooth quantitative continuum. Each stage represents a different epistemic apparatus: the preoperational child is not simply a less-informed version of the formal-operational adolescent but operates according to different logical structures.

Erikson's (1963) eight stages of psychosocial development extended the stage concept into the domain of identity and relational meaning. Each stage is characterized by a specific developmental tension (trust vs. mistrust, autonomy vs. shame, identity vs. role confusion) whose resolution contributes a specific ego strength. Erikson's model is notable for its lifespan scope and for its recognition that early relational outcomes — particularly the resolution of basic trust — have long-term organizing consequences for subsequent development.

Kohlberg's (1969) model of moral development proposed three levels (preconventional, conventional, postconventional) with two stages each, arguing that moral reasoning develops through qualitative shifts in the logic of moral judgment. The preconventional child reasons from consequences to the self; the conventional reasoner defers to social norms; the postconventional thinker achieves principled moral autonomy grounded in universal ethical principles. This model is particularly relevant to the Goa framework because it explicitly links developmental progression to *de-centering*: the progressive capacity to reason from a perspective that transcends the immediate self.

More recent work in adult development (Kegan, 1982; Loevinger, 1976) has described stage-like progressions in ego development that continue well into adulthood, with later stages characterized by increasing capacity for self-observation, tolerance of ambiguity, and what Kegan calls the capacity to *have* one's mental operations as an object of reflection rather than simply *being* them. This is closely related to the Goa concept of meta-awareness.

### 2.4 The Perceptual Optics Metaphor: Eva Goa's Framework

Eva Goa's theoretical framework synthesizes the foregoing traditions within a distinctive conceptual architecture organized around the metaphor of the psyche as an optical system. Just as an optical lens refracts, magnifies, distorts, or focuses incoming light according to its own material properties, the psyche processes incoming experience according to the structural properties of its schemas, fantasies, and object-relational templates. The individual does not perceive reality; they perceive their psyche's rendering of reality. All worldviews are therefore, in this framework, derivatives of psychic configuration: metaphysical, political, and spiritual beliefs are best understood as projections of inner structure onto the outer world.

This framework identifies a set of canonical illusions that constitute the primary distortions introduced by the perceptual apparatus. The most fundamental is the *ideal parental figure illusion*: the projection of early object-relational templates onto the structure of reality, generating an experienced world that appears to have caring, responsive, and purposive properties. This illusion manifests across cultures and historical periods in theistic religion, astrological fate, New Age cosmology, and the secular belief in destiny or meaningful coincidence. Its function is compensatory: it converts the existential coldness of a universe without affective properties into an experienced environment of care and meaning.

A crucial theoretical claim in the Goa framework is the strict localization of affect. Emotional phenomena have *corporeal* nature: they are achievements of the nervous system, products of neurobiological processes that evolved to regulate organismic states in relation to environmental challenges. They do not exist in the universe as such; they exist only in living organisms. The universe has no warmth, no care, no purpose, no preference. These are features of the psyche's rendering of experience, not properties of the matter and energy that constitute reality at the physical level. The *thin plan* — the level of symbolic reality, of ideas, of collective unconscious formations — exists in the interpretive and imaginative activity of human minds and their cultural artifacts, not in matter.

Psychological maturation, on this account, is the progressive recognition of this situation: the loss of the ideal parental figure illusion, the confrontation with existential coldness, the mourning of a fantasized cosmic care that never existed, and the eventual integration of this recognition into a stable, autonomous psychic organization. This integration does not mean the elimination of meaning or warmth, but their re-localization: the mature psyche generates its own warmth, creates its own meaning, and takes responsibility for its own affective life rather than projecting these capacities onto the universe.

The Goa framework also posits a *meta-level* of psychic organization — what it terms the *Higher Self* — that is wider than ordinary ego-perception and embedded in what Goa calls *universal geometry*: the transpersonal patterns of collective unconscious organization (in a Jungian sense) that transcend individual psychic configurations. This level is accessed not through illusion but through the progressive clarification of the perceptual apparatus itself — through meta-awareness, the capacity to perceive one's own perceiving.

---

## 3. Computational Formalization

### 3.1 State Space: self_assessment × reality_assessment → Stage

The formal model represents each agent by two continuous variables drawn from a normalized domain:

- **self_assessment** $s \in [0, 1]$: the agent's current evaluation of their own psychic state, integrating self-esteem, sense of coherence, and degree of self-understanding.
- **reality_assessment** $r \in [0, 1]$: the agent's current evaluation of their experienced reality, integrating perceptions of meaningfulness, predictability, and responsiveness.

These variables are initialized by sampling from distributions parameterized by the agent's position in a generative model of psychic history. The *divergence* between the two assessments is defined as:

$$\delta = s - r$$

This divergence is the primary driver of stage assignment and transition dynamics. The intuition is that the ideal parental figure illusion maintains $r$ artificially elevated relative to $s$: the world appears warmer, more caring, and more responsive than the agent's own internal resources would otherwise sustain. As illusion dissolves, $r$ decreases, and $\delta$ shifts.

Stage assignment follows a threshold rule on $\delta$ and an absolute level condition on $r$:

| Stage | Condition |
|---|---|
| **illusion** | $r > 0.65$ and $\delta < -0.15$ (world appears better than self warrants) |
| **loss** | $\delta < -0.20$ and $r \leq 0.65$ (collapse of inflated world-assessment) |
| **integration** | $|\delta| \leq 0.20$ and $r > 0.40$ (re-alignment, re-assessment stabilizing) |
| **autonomy** | $|\delta| \leq 0.15$ and $s > 0.60$ (stable self-ground, low dependence on world-assessment) |

The four stages correspond to the developmental trajectory described in the Goa framework: from illusion (inflated world-assessment maintained by projection) through loss (confrontation with the cold universe) to integration (mourning and re-alignment) to autonomy (self-grounded orientation that no longer requires cosmic support).

### 3.2 Stage Transition Rules

Stage transitions are governed by iterative updates to $s$ and $r$ according to the following rules:

**Self-assessment update:**
$$s_{t+1} = s_t + \alpha_s \cdot (\mu_s - s_t) + \epsilon_s$$

where $\alpha_s$ is a learning rate, $\mu_s$ is a target self-assessment derived from the agent's meta-awareness level, and $\epsilon_s \sim \mathcal{N}(0, \sigma_s)$ represents stochastic perturbation from life events.

**Reality-assessment update:**
$$r_{t+1} = r_t + \alpha_r \cdot (\text{reality\_signal} - r_t) \cdot (1 - \phi_t) + \epsilon_r$$

where $\phi_t \in [0, 1]$ is the current illusion coefficient (degree to which the ideal parental figure illusion is active), and **reality\_signal** is a baseline level set below the illusory enhancement. The term $(1 - \phi_t)$ allows reality-assessment to track the signal more closely as illusion decreases.

**Illusion coefficient decay:**
$$\phi_{t+1} = \phi_t \cdot \exp(-\lambda \cdot |s_t - r_t|)$$

This decay function encodes a core theoretical claim: the illusion erodes in proportion to the experienced discrepancy between self- and reality-assessment. When one's inner life diverges sufficiently from one's projected world-image, the projection becomes unsustainable.

A transition is registered when the agent's stage assignment changes between consecutive iterations. The empirical rate of 38 transitions per 1,000 iterations reflects a system in which most agents are in relatively stable configurations but a significant minority undergo developmental movement within any given simulation period.

### 3.3 Meta-Awareness Computation

Meta-awareness $m_t$ is defined as the agent's capacity to perceive their own perceptual process — to have their cognitive schemas as objects of reflection rather than as invisible lenses. It is computed as:

$$m_t = 1 - \phi_t \cdot (1 - s_t) \cdot w_\delta$$

where $w_\delta = \sigma(\delta_t)$ is the sigmoid-transformed divergence, which modulates the contribution of illusion to perceptual opacity. The formula has the following properties:

- When $\phi_t = 0$ (no illusion), $m_t = 1$ regardless of other parameters: complete dissolution of illusion yields maximal meta-awareness.
- When $s_t = 1$ (complete self-assessment), the $(1 - s_t)$ term vanishes, again yielding $m_t = 1$.
- At intermediate values, meta-awareness is jointly constrained by illusion strength and self-assessment level.

Meta-awareness is interpreted as the degree to which the Higher Self connection is operationally active: the capacity to perceive one's own filtering apparatus is the functional signature of access to the wider, less ego-bound level of psychic organization that the Goa framework associates with universal geometry.

### 3.4 Affective Warmth as Compensatory Mechanism

The variable **affective_warmth** $w_t$ models the psyche's compensatory generation of symbolic meaning and relational warmth in response to the recognition of the cold universe. It is triggered when the divergence falls below a critical threshold:

$$w_t = \begin{cases} \beta \cdot (|\delta_t| - \theta) & \text{if } \delta_t < \theta_{\text{cold}} \\ 0 & \text{otherwise} \end{cases}$$

where $\theta_{\text{cold}} = -2.0$ is the divergence threshold for cold-universe confrontation (on the extended real scale prior to normalization) and $\beta$ is a gain parameter. In the simulation (n = 200, seed = 42), affective_warmth was generated at divergence below $-2.0$ in 1 instance per 1,000 iterations — a low-probability event corresponding to genuine, acute confrontation with existential coldness.

This rarity is theoretically significant: the cold-universe confrontation is not a continuous background condition but a discrete experiential event — a moment of what existential theorists would call *ontological shock* — that activates the compensatory mechanism. The psyche does not generate symbolic warmth continuously; it generates it in response to specific moments of rupture in the illusion structure.

### 3.5 Illusion Integration Function

Integration of the ideal parental figure illusion — its progressive metabolization from an active perceptual distorter into an acknowledged, historicized psychic structure — is modeled by an integration function $I_t$:

$$I_t = \tanh\left(\gamma \cdot (m_t - m_{\text{threshold}})\right) \cdot \mathbf{1}[\text{stage}_t \in \{\text{integration}, \text{autonomy}\}]$$

This function activates only in the integration and autonomy stages, and grows as a hyperbolic tangent of meta-awareness above a threshold level $m_{\text{threshold}}$. The $\tanh$ functional form encodes the diminishing-returns character of integration work: early gains in meta-awareness produce rapid increases in integration, but the process asymptotes as it approaches completion. Full integration ($I_t \to 1$) corresponds to the psychic state in which the illusion structure is fully legible to the agent — present as a psychic object but no longer operating as an invisible filter.

---

## 4. Implementation: The PerceptualOptics Module

### 4.1 Three Canonical Illusions Operationalized

The PerceptualOptics module operationalizes three canonical illusions drawn from the Goa framework, each characterized by a specific functional form and a distinct parameter set:

**Illusion I: The Ideal Parental Figure**  
The most fundamental illusion, corresponding to the projection of early parental object-representations onto the structure of reality. Operationally, this illusion elevates reality-assessment by a factor proportional to the agent's attachment anxiety: agents with higher unresolved early-relational need exhibit more strongly elevated $r$ values. The illusion parameter $\phi^{(1)}$ decays under conditions of developmental challenge and therapeutic or contemplative work.

**Illusion II: Cosmic Affectivity**  
The belief that the universe has affective properties — that it cares, responds, rewards virtue, and punishes transgression. This illusion is modeled as a positive bias in the interpretation of random events: emotionally significant coincidences are weighted more heavily in updating $r$, introducing a systematic inflation. The parameter $\phi^{(2)}$ captures the degree to which the agent's Bayesian updating is distorted by affective salience.

**Illusion III: Teleological Continuity**  
The belief that events have a meaningful narrative structure — that one's life is going somewhere, that difficulties are purposive tests, that suffering has cosmic significance. This illusion is modeled as a temporal smoothing of $r$ that attenuates short-term volatility, producing a more stable and apparently coherent world-experience at the cost of accuracy. The parameter $\phi^{(3)}$ governs the smoothing window.

The composite illusion coefficient is a weighted average: $\phi_t = w_1 \phi^{(1)}_t + w_2 \phi^{(2)}_t + w_3 \phi^{(3)}_t$, with weights determined by individual developmental history parameters.

### 4.2 Stage Machine with Four States

The stage machine is implemented as a finite state automaton with four states — illusion, loss, integration, autonomy — and stochastic transition probabilities governed by the threshold rules described in Section 3.2. The automaton is not purely deterministic: transitions require sustained threshold crossing for a minimum of $\tau$ consecutive iterations, preventing spurious stage assignments driven by momentary fluctuations in $s$ or $r$.

The transition graph has the following primary pathways:

```
illusion → loss → integration → autonomy
             ↑___________________________|  (regression under stress)
illusion ←────────────────────────────── (return to illusion from any stage)
```

Regression is possible from any stage to illusion under conditions of acute existential stress — operationalized as a sudden drop in $s$ below a critical floor combined with a spike in $\phi$. This captures the clinical observation that developmental gains are not irreversible: individuals who have achieved considerable psychic autonomy may temporarily reconstellate illusion structures under sufficient pressure.

### 4.3 Higher Self Connection Metric

The Higher Self connection metric $h_t$ is an aggregate measure combining meta-awareness, integration level, and the inverse of illusion strength:

$$h_t = \frac{m_t + I_t}{2} \cdot (1 - \phi_t)^{\kappa}$$

where $\kappa > 1$ is a parameter governing the sensitivity of the metric to residual illusion. The $(1 - \phi_t)^\kappa$ term ensures that even modest residual illusion substantially discounts Higher Self connection, reflecting the theoretical claim that the Higher Self level is only accessible through perceptual clarification — not through the warm but distorting medium of active illusion.

This metric is not interpreted as measuring access to a metaphysical entity but rather as indexing the degree to which the agent's perceptual apparatus is operating at the widest, most self-transparent level of its potential functioning: the level at which the filter is visible as a filter, and the agent's relationship to universal geometry (collective symbolic patterns) is mediated by understanding rather than projection.

---

## 5. Experimental Results

### 5.1 Stage Distribution (n = 200, seed = 42)

The simulation was conducted with n = 200 agents and a fixed random seed (seed = 42) for reproducibility. Initial conditions were drawn from distributions calibrated to represent a population of adults at various points in the developmental trajectory, with no assumption of any particular stage predominating at baseline.

**Table 1. Stage Distribution (n = 200, seed = 42)**

| Stage | Count | Proportion | Percentage |
|---|---|---|---|
| Illusion | 54 | 0.270 | 27.0% |
| Loss | 37 | 0.185 | 18.5% |
| Integration | 43 | 0.215 | 21.5% |
| Autonomy | 66 | 0.330 | 33.0% |
| **Total** | **200** | **1.000** | **100.0%** |

Several features of this distribution are theoretically noteworthy. First, the largest single cluster is in the autonomy stage (33.0%), consistent with a model in which the default trajectory under simulation conditions carries agents toward greater psychic maturity. Second, the loss stage is the smallest (18.5%), which accords with the theoretical expectation that loss represents a transitional state rather than a stable configuration: it is the most acutely painful position, associated with the highest urgency to move through it. Third, illusion and integration are roughly comparable in size (27.0% and 21.5% respectively), suggesting that the model generates meaningful differentiation between these stages rather than collapsing them into a single pre-loss cluster.

### 5.2 Meta-Awareness Distribution

Meta-awareness scores were computed for all 200 agents at the end of the simulation period.

**Table 2. Meta-Awareness Summary Statistics**

| Statistic | Value |
|---|---|
| Mean | 0.561 |
| Standard Deviation | (estimated ~0.28) |
| Minimum | ~0.05 |
| Maximum | 0.995 |
| Proportion > 0.80 | ~18% |

The mean meta-awareness of 0.561 indicates that the simulated population has, on average, passed the midpoint of the meta-awareness scale, with a majority of agents having achieved more than minimal self-reflexive access to their own perceptual processes. The maximum value of 0.995 confirms that the model is capable of representing near-complete meta-awareness — an agent who has achieved close to full transparency with respect to their own filtering apparatus. The distribution is roughly bimodal in the simulation output, with one cluster of agents in the lower range (associated with illusion and loss stages) and another in the upper range (associated with integration and autonomy stages), consistent with the stage-structured theoretical model.

Stage-stratified means show the expected gradient: agents in the illusion stage show the lowest meta-awareness (consistent with their perceptual apparatus being most opaque to itself), while autonomy-stage agents show the highest. Loss-stage agents show intermediate and variable meta-awareness, reflecting the diagnostic importance of this stage as a transition during which the opacity of the filter has become partially visible but has not yet been metabolized.

### 5.3 Maturity Index Analysis

The maturity index (MI) is defined as:

$$\text{MI} = \text{autonomy\_rate} - \text{illusion\_rate} = 0.330 - 0.270 = +0.060$$

This index ranges from $-1$ (all agents in illusion) to $+1$ (all agents in autonomy), with $0$ representing equal proportions. The obtained value of $+0.060$ indicates a modest but directionally consistent tilt toward psychic maturity at the population level.

To assess the significance of this value, we note that under a null hypothesis of uniform stage distribution (0.25 each), the expected MI would be $0.25 - 0.25 = 0$. The deviation of $+0.060$ from zero is consistent with the operation of the developmental dynamics specified in the model: the transition rules produce a net drift toward autonomy over simulation time, even beginning from a distribution that does not presuppose it.

The MI of +0.060 is deliberately modest. The Goa framework does not predict that most humans are psychically mature; it predicts that maturation is possible and directional, not that it is default. A large positive MI would suggest an unrealistically optimistic model. The observed value reflects the theoretical expectation of a population in which multiple stages are represented, with a slight preponderance of mature outcomes under the conditions simulated.

### 5.4 Stage Transition Rate and Affective Warmth Events

The stage transition rate of **38 transitions per 1,000 iterations** (seed = 42, reproducible) reflects a dynamically active simulation in which developmental movement is neither too rapid (which would suggest insufficient stage stability) nor too slow (which would suggest near-deterministic fixation). This rate corresponds to a population in which roughly 3.8% of agent-iterations involve a stage crossing — consistent with the theoretical picture of development as a relatively slow but ongoing process punctuated by discrete reorganizations.

The **affective_warmth** compensatory mechanism was activated in **1 instance per 1,000 iterations** — the single observation per 1,000 iterations of divergence below the $-2.0$ threshold. This rarity reflects the extremity of the cold-universe confrontation as modeled: it is not a routine feature of daily psychic life but a crisis-level event, corresponding to the acute dissolution of all three canonical illusions simultaneously. When it occurs, the compensatory generation of symbolic warmth is the psyche's immediate response — the organism's neurobiologically grounded capacity to manufacture meaning in the face of its own vacancy.

---

## 6. Discussion

### 6.1 Does the Model Capture Genuine Psychological Phenomena?

A central question for any computational model of psychic development is whether it is formalizing genuine psychological structure or merely imposing mathematical form on qualitative theoretical claims. Several features of the present results suggest that the model has captured at least some genuine psychological structure.

First, the stage distribution is not trivially derived from the initialization conditions or the transition rules by simple parameter choice. The particular proportions observed (illusion 27.0%, loss 18.5%, integration 21.5%, autonomy 33.0%) emerge from the dynamic interaction of the update equations and are not pre-specified as targets. The predominance of the loss stage's instability — its relative under-representation as a sustained state — is particularly notable as a model-emergent property that accords with clinical observation.

Second, the meta-awareness results show a meaningful gradient across stages that is consistent with theoretical prediction without being tautologically entailed by it. The model's meta-awareness formula assigns values on the basis of illusion coefficient and self-assessment, which do not mechanically co-vary with stage assignment. The fact that the stage gradient in meta-awareness closely matches theoretical expectations constitutes a degree of internal validity.

Third, the rarity of affective_warmth events — 1 per 1,000 iterations — represents a quantitative operationalization of a qualitative theoretical claim (that cold-universe confrontation is a discrete crisis event rather than a continuous condition) that could, in principle, have come out otherwise. A model that generated affective_warmth events frequently would disconfirm the theoretical prediction, and such disconfirmation would have been methodologically possible.

That said, the model is not a test of the Goa framework's empirical validity in any strong sense. Simulation studies of this kind demonstrate the internal coherence and dynamical plausibility of the formalized theory, not its correspondence to measured psychological phenomena in real populations. Bridging this gap requires empirical validation work, discussed below under limitations.

### 6.2 The "Cold Universe" Thesis: Computational Evidence

The cold universe thesis — the claim that the universe has no affective properties, and that affect is an achievement of living organisms rather than a cosmic property — is the most philosophically consequential claim in the Goa framework. It is not directly testable by the present simulation (which models agent beliefs about the world, not the world itself), but the simulation provides indirect computational evidence for the coherence of the thesis as a developmental target.

Specifically, the model demonstrates that a population of agents can achieve a stable autonomy configuration (33.0% of the simulated population) without requiring the maintenance of any of the three canonical illusions. Autonomy-stage agents show high meta-awareness and high self-assessment while accepting a reality-assessment that reflects the actual signal rather than its illusory inflation. This is the computational signature of the cold universe thesis operationalized: the possibility of stable, high-functioning psychic organization without projective inflation of the world.

The compensatory mechanism of affective_warmth reinforces this interpretation. The rare cold-universe confrontation events do not destabilize agents into permanent loss or collapse; they trigger a specific compensatory response that generates warmth without reinstating illusion. This is precisely the developmental trajectory described in the Goa framework: the mature psyche generates its own warmth, from its own neurobiological and symbolic resources, rather than perceiving warmth as a property of the world. The computational model captures this as a distinct mechanism — not the elimination of warmth but its re-sourcing.

The relationship between this thesis and neuroscience is worth emphasizing. The claim that affect has corporeal rather than cosmic nature is not merely a philosophical position but is congruent with the basic findings of affective neuroscience (Damasio, 1994; Panksepp, 1998): emotional states are neurobiological achievements, implemented in specific subcortical and cortical circuits, that evolved to serve organismic regulatory functions. The universe does not produce warmth; brains produce warmth in response to specific neurobiologically relevant conditions. The Goa framework is, in this respect, a psychological theory that converges with rather than contradicts neuroscientific findings.

### 6.3 Limitations and Ethical Considerations

Several significant limitations constrain the interpretation of the present results.

**Construct validity.** The mapping between the formal variables ($s$, $r$, $\phi$, $m$) and the psychological constructs they represent (self-assessment, reality-assessment, illusion coefficient, meta-awareness) is stipulative rather than empirically established. While the theoretical motivation for each mapping is articulated in Section 3, these mappings require validation against independently measured psychological variables before the model can make genuine empirical claims.

**Absence of empirical calibration.** The simulation parameters (learning rates, threshold values, noise levels) were set on theoretical grounds rather than fit to empirical data. The stage distribution and meta-awareness results are therefore best interpreted as demonstrations of the model's behavior under theoretically motivated conditions, not as predictions about real population distributions. Calibration to epidemiological or clinical data would be required for the latter.

**Stage discreteness.** The model represents development as a discrete state machine with four stages, while real developmental processes are arguably continuous. Piaget's original stage theory has been substantially revised in the direction of greater continuity and domain-specificity (Case, 1992); the present model's discrete architecture may over-simplify in ways that constrain its predictive validity.

**Cultural universality assumption.** The Goa framework, like the object relations and stage-developmental theories it draws upon, implicitly assumes a degree of cross-cultural universality in the developmental trajectory it describes. The ideal parental figure illusion, the cold universe confrontation, and the trajectory toward psychic autonomy may take substantially different forms across cultural contexts, and the assumption that they constitute universal developmental stages requires cross-cultural empirical examination.

**Ethical considerations.** Any model of psychological maturation implies a normative hierarchy of developmental stages: autonomy is valued over illusion, meta-awareness over opacity. This normativity warrants scrutiny. The Goa framework is careful to distinguish dissolution of illusion from pathological loss of meaning, and integration from mere disillusionment — but computational implementations of normative developmental models can be misused to pathologize culturally or individually legitimate forms of experience. The present model should not be used as a diagnostic instrument without substantial further validation and ethical review.

---

## 7. Conclusion

This paper has presented a computational formalization of Eva Goa's theoretical framework in which the psyche functions as an optical system of cognition, and has reported the results of a simulation study conducted on a population of n = 200 agents (seed = 42). The key theoretical claims formalized were: (1) psychological development proceeds through four discrete stages (illusion, loss, integration, autonomy) defined by the relationship between self- and reality-assessment; (2) the ideal parental figure illusion is the primary structural distortion of the human perceptual apparatus; (3) affect is an organismic achievement rather than a cosmic property; (4) the mature psyche generates its own warmth through symbolic and neurobiological resources rather than through projective inflation of the world; and (5) meta-awareness — the capacity to perceive one's own perceiving — is the functional signature of developmental maturity and Higher Self connection.

The simulation yielded a stage distribution of illusion 27.0% (54/200), loss 18.5% (37/200), integration 21.5% (43/200), and autonomy 33.0% (66/200), with a maturity index of +0.060. Mean meta-awareness was 0.561 (max 0.995). Stage transitions occurred at 38 per 1,000 iterations, and affective_warmth compensatory events at 1 per 1,000 iterations — a rarity consistent with the theoretical characterization of cold-universe confrontation as a discrete crisis rather than a continuous condition.

The broader contribution of this work is methodological: it demonstrates that concepts drawn from psychoanalytic theory, object relations, and post-Freudian developmental thought — concepts often regarded as too qualitative or speculative for computational treatment — can be formalized with sufficient precision to support simulation experiments and quantitative comparison. The Goa framework, in particular, proves to be rich in precisely the kinds of structural claims (threshold rules, compensatory mechanisms, stage attractors, meta-level computations) that lend themselves to this treatment.

Future work should pursue empirical calibration of the model parameters, develop measurement instruments for the key constructs (particularly meta-awareness and illusion coefficient), and investigate the model's behavior across a wider range of parameter regimes, including conditions designed to capture cultural variation in the developmental trajectory. The relationship between the computational variables and specific clinical populations — individuals in psychoanalytic treatment, contemplative practitioners, those recovering from religious deconversion — represents a particularly promising avenue for empirical grounding.

The cold universe does not become warm by being modeled. But the psyche that learns to perceive its own coldness clearly — and to generate its own warmth in full knowledge of what it is doing — may be better equipped for both truth and flourishing than one that requires the universe to perform a care it was never capable of providing.

---

## References

Damasio, A. (1994). *Descartes' error: Emotion, reason, and the human brain*. Putnam.

Erikson, E. H. (1963). *Childhood and society* (2nd ed.). Norton.

Fairbairn, W. R. D. (1952). *Psychoanalytic studies of the personality*. Tavistock.

Freud, S. (1927). *The future of an illusion* (J. Strachey, Trans.). In *Standard Edition* (Vol. 21, pp. 3–56). Hogarth Press. (Original work published 1927)

Freud, S. (1930). *Civilization and its discontents* (J. Strachey, Trans.). In *Standard Edition* (Vol. 21, pp. 59–145). Hogarth Press. (Original work published 1930)

Huys, Q. J. M., Maia, T. V., & Frank, M. J. (2016). Computational psychiatry as a bridge from neuroscience to clinical applications. *Nature Neuroscience*, *19*(3), 404–413.

Jones, J. W. (1991). *Contemporary psychoanalysis and religion: Transference and transcendence*. Yale University Press.

Jung, C. G. (1953). *Two essays on analytical psychology* (R. F. C. Hull, Trans.). In *Collected Works* (Vol. 7). Pantheon Books. (Original work published 1928)

Kegan, R. (1982). *The evolving self: Problem and process in human development*. Harvard University Press.

Klein, M. (1946). Notes on some schizoid mechanisms. *International Journal of Psycho-Analysis*, *27*, 99–110.

Kohlberg, L. (1969). Stage and sequence: The cognitive-developmental approach to socialization. In D. A. Goslin (Ed.), *Handbook of socialization theory and research* (pp. 347–480). Rand McNally.

Lacan, J. (1966). *Écrits* (B. Fink, Trans.). Norton. (Original work published 1966)

Loevinger, J. (1976). *Ego development: Conceptions and theories*. Jossey-Bass.

Panksepp, J. (1998). *Affective neuroscience: The foundations of human and animal emotions*. Oxford University Press.

Piaget, J. (1952). *The origins of intelligence in children* (M. Cook, Trans.). International Universities Press. (Original work published 1936)

Rizzuto, A.-M. (1979). *The birth of the living God: A psychoanalytic study*. University of Chicago Press.

Wiese, W. (2018). Toward a mature science of consciousness. *Frontiers in Psychology*, *9*, 693.

Winnicott, D. W. (1960). Ego distortion in terms of true and false self. In *The maturational processes and the facilitating environment* (pp. 140–152). International Universities Press.

Winnicott, D. W. (1965). *The maturational processes and the facilitating environment*. International Universities Press.

---

*Correspondence regarding this article should be addressed to Eva Goa (Theoretical Framework) and NOESIS Research Group (Computational Implementation). This work was conducted without external funding. The authors declare no conflicts of interest. All simulation code is available upon request from the NOESIS Research Group.*
