# Phase-Toroidal Engine: A Theoretical Framework for Vacuum-Mediated Propulsion via Coupled Topological Phase Transitions

**Pre-print** — July 2026  
**IP Protection:** Zenodo 10.5281/zenodo.21209447 (CC-BY-NC-ND 4.0)  
**Correspondence:** [via Telegram — see https://t.me/my_super_trader_v32_bot]

---

## Abstract

We present a theoretical framework for a novel class of propellantless propulsion — the Phase-Toroidal Engine (PTE) — which generates directed impulse by coupling toroidal field topology to controlled vacuum phase transitions. The engine exploits three mechanisms: (A) nested toroidal electromagnetic confinement producing a symmetry-breaking stress tensor along the torus axis; (B) scalar dilaton mode coupling that locally modulates the vacuum refractive index K, creating a metric gradient; and (C) controlled cycling through a critical topological phase transition in the vacuum state, yielding net impulse during the symmetry-breaking phase. We derive the governing effective Lagrangian, estimate thrust-to-power scaling, identify parametric stability conditions, and propose concrete experimental validation pathways. The framework naturally connects to recent empirical results: the 95.4 GeV dilaton resonance (CMS/ATLAS), toroidal spin ice Blume-Capel tricritical phase transitions (arXiv:2509.01522), and the topological vacuum energy modulator formalism. Six falsifiable predictions are identified, spanning Casimir force anomalies at golden-ratio resonance spacings, anomalous thrust from asymmetric RF cavities, neutron star spin-down anomalies, and gamma-ray signatures from vacuum phase transition decay. The PTE framework offers a testable bridge between quantum vacuum physics, condensed matter topology, and practical aerospace engineering.

**Keywords:** toroidal propulsion, quantum vacuum, phase transition, dilaton, metric engineering, Casimir effect, topological field theory

---

## 1. Introduction

The fundamental challenge of space propulsion remains the tyranny of the rocket equation: every kilogram of reaction mass must be accelerated along with the payload, creating an exponential mass penalty for delta-v. Propellantless propulsion — generating thrust without onboard reaction mass — has been a "holy grail" since the earliest days of astronautics.

Recent decades have seen serious theoretical proposals for propellantless systems, including the Woodward effect (transient mass fluctuations from Mach's principle), the Alcubierre metric (warp drive via exotic matter), and the EM drive controversy (asymmetric RF cavities). None have produced a theoretically consistent, experimentally reproducible, and physically conservative framework.

The Phase-Toroidal Engine (PTE) proposed here takes a different approach. Instead of invoking exotic matter with negative energy density, it exploits a known physical phenomenon — **topological phase transitions in the quantum vacuum** — and couples it to toroidal field geometry to produce directed impulse. The key insight is that the vacuum, like any medium, can undergo phase transitions under the influence of external fields, and that the symmetry-breaking dynamics of such transitions can be geometrically directed.

Recent work provides empirical grounding for this approach:
- The Toroidal Phase-Transition Model (TPTM) replaces gravitational singularities with rotating torus configurations [1]
- The Photonic-Conjugated Model (PCM) models massive particles as confined light in toroidal topologies [2]
- The Toroidal Torsion Field Theory (TTFT) derives fundamental constants from golden-ratio eigenmode hierarchies on toroidal manifolds [3]
- The 95.4 GeV dilaton resonance detected by CMS/ATLAS provides evidence for a scalar channel coupling to the trace anomaly [4]
- Blume-Capel tricritical phase transitions have been realized in toroidal spin ice arrays [5]

The PTE framework synthesizes these threads into an engineering-relevant propulsion architecture.

---

## 2. Theoretical Foundations

### 2.1 Toroidal Field Topology

Consider a toroidal volume with major radius R and minor radius r, parameterized by toroidal angle ϕ ∈ [0, 2π) and poloidal angle θ ∈ [0, 2π). The metric in standard toroidal coordinates (R, r, θ, ϕ) is:

$$ds^2 = -dt^2 + (R + r\cos\theta)^2 d\phi^2 + r^2 d\theta^2 + dr^2$$

Within this volume, we define a nested electromagnetic field configuration:

**Toroidal field** (winding the long way): $B_\phi = B_0 f(r/R)$

**Poloidal field** (winding the short way): $B_\theta = \varepsilon B_0 g(r/R)$

where ε is the asymmetry parameter and f,g are radial profile functions satisfying the Grad-Shafranov equilibrium:

$$\Delta^* \psi = -\mu_0 R^2 \frac{dP}{d\psi} - F\frac{dF}{d\psi}$$

where ψ is the poloidal flux function, P the plasma pressure, and F the toroidal field function.

The key geometric property is the **central null zone** — a region near the torus axis where the poloidal gradient of the combined field stress tensor is maximal while the total field pressure gradient vanishes:

$$\nabla \cdot \mathbf{T} \neq 0 \text{ (along symmetry axis)}$$
$$\nabla P_{\text{total}} = 0 \text{ (in null zone center)}$$

This creates an uncompensated stress along the torus symmetry axis — the foundation for directed impulse.

### 2.2 Vacuum Phase Transitions

The quantum vacuum is not empty but a dynamical medium with nontrivial topological structure. Following the Refractive Vacuum Gravity (RVG) formalism [4], we model the vacuum as a medium with refractive index K that responds to scalar fields coupled to the trace of the energy-momentum tensor:

$$K(x) = K_0 \exp(\alpha \phi(x) / M_{\text{Pl}})$$

where $\phi$ is a dilaton-like scalar field, $\alpha$ is a coupling constant, and $M_{\text{Pl}}$ is the Planck mass.

The vacuum effective action includes a phase transition term:

$$S_{\text{vac}} = \int d^4x \sqrt{-g} \left[ \frac{1}{2}(\partial\phi)^2 - V(\phi) + \frac{\phi}{4\Lambda} F_{\mu\nu}F^{\mu\nu} \right]$$

The potential V(ϕ) is assumed to have a tricritical point structure analogous to the Blume-Capel model [5]:

$$V(\phi) = a_2(T)\phi^2 + a_4\phi^4 + a_6\phi^6$$

where $a_2(T)$ changes sign at a critical temperature-like control parameter, producing a first-order phase transition below a tricritical point and second-order above it.

Biasing the system through an asymmetric toroidal field shifts the effective potential:

$$V_{\text{eff}}(\phi) = V(\phi) - \frac{1}{2}\xi \mathbf{B}^2\phi$$

where ξ is a coupling coefficient. The sign and magnitude of ξ depend on the field topology — and crucially, the toroidal asymmetry ε creates a **directional bias** in the phase transition dynamics.

### 2.3 Coupled Dynamics

The core mechanism couples the toroidal field topology to the vacuum phase transition:

1. **Pumping phase:** Nested toroidal fields reach critical energy density $U_{\text{crit}} = \xi^{-1} V'(\phi_0)$
2. **Transition phase:** Local vacuum undergoes topological phase transition (symmetry breaking), releasing energy $\Delta E = V(\phi_{\text{sym}}) - V(\phi_{\text{broken}})$
3. **Directional impulse:** The asymmetry ε directs the released energy along the torus symmetry axis

The effective Lagrangian for the coupled system:

$$\mathcal{L}_{\text{PTE}} = -\frac{1}{4}F_{\mu\nu}F^{\mu\nu} + \frac{1}{2}(\partial\phi)^2 - V(\phi) + \frac{\phi}{4\Lambda}F_{\mu\nu}F^{\mu\nu} + \epsilon^{\mu\nu\rho\sigma}A_\mu\partial_\nu\phi\partial_\rho A_\sigma$$

The last term is a topological coupling that — for toroidal boundary conditions — produces a net axial current:

$$J_{\text{axial}} = \int d^3x \, \nabla \times (\phi \mathbf{B}) \neq 0$$

---

## 3. Thrust Estimate

Starting from the energy-momentum tensor of the coupled system, the thrust per cycle is:

$$F_{\text{cycle}} \approx \eta \cdot \frac{\Delta V}{c} \cdot \frac{R}{r} \cdot \varepsilon$$

where:
- η is the conversion efficiency (estimated 0.1-1% for first-generation)
- ΔV is the vacuum energy released per phase transition
- R/r is the torus aspect ratio
- ε is the asymmetry parameter

The specific thrust (thrust per input power) scales as:

$$\frac{F}{P} \approx \frac{2\eta\varepsilon}{\omega R} \cdot \frac{R}{r}$$

For a laboratory-scale prototype (R ≈ 0.3 m, r ≈ 0.1 m, ω ≈ 10⁶ s⁻¹, ε ≈ 0.1, η ≈ 0.001):

$$\frac{F}{P} \approx 6.7 \times 10^{-6} \text{ N/W}$$

This is comparable to early ion thruster efficiencies. Optimization of parameters could yield 10-100× improvement.

---

## 4. Stability and Control

### 4.1 Parametric Stability Conditions

The coupled system exhibits three stability regimes:

| Regime | ε range | Behavior |
|--------|---------|----------|
| Subcritical | ε < ε_c | No phase transition, elastic response only |
| Critical | ε = ε_c ± δ | Controlled cycling, net impulse per cycle |
| Supercritical | ε > ε_c + δ | Runaway transition, loss of directional control |

The critical asymmetry is:

$$\varepsilon_c = \frac{V'(\phi_0)}{2\xi B_0^2} \cdot \frac{r}{R}$$

Control is maintained by modulating B₀ near the critical value, using the dilaton coupling to tune the phase boundary location.

### 4.2 Thermal Management

Each phase transition releases heat:

$$Q_{\text{cycle}} = \Delta V \approx V(\phi_0) - V(\phi_{\text{broken}})$$

For continuous operation at cycle frequency ω_c:

$$P_{\text{thermal}} = Q_{\text{cycle}} \cdot \omega_c$$

Thermal management requires active cooling. We estimate radiator mass scaling:

$$M_{\text{rad}} \approx \frac{P_{\text{thermal}}}{\sigma \epsilon_{\text{rad}} T^4}$$

---

## 5. Falsifiable Predictions

The PTE framework makes six testable predictions:

**P1: Casimir Force Anomalies**
At separations corresponding to toroidal resonance modes L_k = φ^k · L_0 (where φ ≈ 1.618 and L_0 = 2πr), the Casimir force deviates from the ideal parallel-plate value by >3%. This follows from the topological vacuum mode structure.

**P2: Anomalous Thrust from Asymmetric RF Cavities**
RF cavities with asymmetric toroidal dielectric inserts produce thrust at specific resonant frequencies where the dilaton coupling is maximal. Thrust scales as $F \propto Q \cdot \varepsilon \cdot P_{\text{RF}} / \omega$.

**P3: Gamma-Ray Signatures**
Vacuum phase transition decay produces monochromatic gamma-ray lines in the 10-30 GeV range, consistent with the excess reported by Totani (2025).

**P4: Neutron Star Spin-Down Anomalies**
In strong magnetic fields (\~10¹² G), toroidal vacuum drag produces anomalous spin-down torque not explained by magnetic dipole radiation alone.

**P5: Dilaton Resonance Modification**
The 95.4 GeV diphoton excess shows directional modulation correlated with the local galactic magnetic field geometry.

**P6: Apparent Mass Variation**
Objects within the toroidal null zone exhibit apparent mass variation proportional to the vacuum stiffness gradient, detectable via precision gravimetry.

---

## 6. Experimental Architecture

### 6.1 Laboratory Prototype

A minimal PTE prototype consists of:

1. **Toroidal RF cavity** with high-Q dielectric resonator (R/r ≈ 3)
2. **Asymmetric field gradient** produced by off-axis dielectric inserts (ε ≈ 0.05-0.2)
3. **Pulsed RF source** (1-10 kW, frequency tuned to cavity resonance)
4. **Precision thrust stand** (1 μN resolution, torsion balance)
5. **Cryogenic environment** (optional, to stabilize vacuum phase)

The cavity must support both TE and TM modes simultaneously, with poloidal/toroidal coupling mediated by the dielectric geometry.

### 6.2 Measurement Protocol

Proposed test sequence:
1. Measure thrust vs. RF power (test P2)
2. Measure thrust vs. asymmetry ε (test control model)
3. Measure thrust vs. aspect ratio R/r (test scaling law)
4. Null test: symmetric configuration (ε=0) should yield F=0
5. Null test: below-threshold power (B₀ < B_crit) should yield F=0

### 6.3 Key Risk Factors

- **Thermal effects** can produce spurious thrust via outgassing or asymmetric heating
- **RF interference** with thrust measurement electronics
- **Barometric pressure variations** affecting null measurements

Rigorous controls and vacuum operation (P < 10⁻⁶ torr) are essential.

---

## 7. Discussion

### 7.1 Connection to Observations

The PTE framework provides a natural language for several unexplained astrophysical phenomena:
- **Dark matter:** Topological defects from vacuum phase transitions act as effective mass
- **Dark energy:** Residual vacuum stiffness gradient produces cosmological acceleration
- **Matter-antimatter asymmetry:** Toroidal winding number chirality encodes preferred handedness

These correspondences are suggestive but not yet predictive — the coupling constants are currently fitted rather than derived from first principles.

### 7.2 Limitations

This work has several important limitations:
1. No complete quantum field theory derivation of the coupling constants
2. No numerical simulation of the phase transition dynamics
3. No experimental verification of the fundamental mechanism
4. The dilaton coupling to electromagnetism is assumed, not derived

Each limitation represents a priority for future work.

---

## 8. Conclusion

The Phase-Toroidal Engine offers a theoretically grounded path to propellantless propulsion that avoids the negative energy requirements of earlier proposals. By coupling toroidal field geometry to vacuum phase transition dynamics — both physically well-motivated and partially empirically supported — the PTE creates a directed impulse through topological symmetry breaking.

The framework makes six falsifiable predictions testable with existing or near-term experimental infrastructure. A laboratory prototype is within reach of modest university-scale funding.

---

## References

[1] Weinstock, J. (2026). *Toroidal Phase-Transition Model (TPTM)*. Zenodo 18138596.

[2] Caputo, R. N. (2025). *Photonic-Conjugated Model (PCM)*. Zenodo 17823666.

[3] Zero 4All (2025). *Toroidal Torsion Field Theory (TTFT)*. Zenodo 17533268.

[4] Hofseth, J. D. (2026). *Refractive Vacuum Gravity (RVG)*. Zenodo 18663961.

[5] Blume-Capel degrees of freedom in toroidal spin ice. arXiv:2509.01522 (2025).

[6] Totani, T. (2025). *20 GeV gamma-ray excess from the Galactic Center*.

[7] Woodward, V. (2026). *Toroidal Scale Dynamics (TSD)*. Zenodo 18357523.

[8] Hofseth, J. D. (2026). *Unified Field Scalar-Hydraulic Drive*. Zenodo 18652906.
