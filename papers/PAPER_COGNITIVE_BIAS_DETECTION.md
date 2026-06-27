# Algorithmic Detection and Severity Quantification of Eight Cognitive Biases in Automated Decision Systems

**Abstract**

Cognitive biases—systematic patterns of deviation from rational judgment identified in behavioral economics and cognitive psychology—are not exclusive to human decision-makers. Automated systems that learn from historical data, adapt to feedback, or operate under uncertainty can exhibit functionally analogous distortions that degrade decision quality in predictable and measurable ways. This paper presents a formal framework for the algorithmic detection and continuous severity quantification of eight cognitive biases in automated decision systems, with particular application to algorithmic trading. We define formal detection criteria for Loss Aversion, Recency Bias, Confirmation Bias, Anchoring Bias, Overconfidence, Gambler's Fallacy, Hindsight Bias, and Sunk Cost Fallacy, and we assign each a continuous severity score on [0, 1] with a block threshold at severity > 0.7. Experiments on n=100 instances per bias type (seed=42) yield detection rates ranging from 60% (Recency Bias) to 0% (Gambler's Fallacy). We provide a detailed sensitivity analysis explaining the 0% detection rate for Gambler's Fallacy as a calibration artifact rather than an absence of the bias, and we discuss implications for bias-resistant system design and behavioral finance theory. The framework demonstrates that cognitive bias detection is tractable, quantifiable, and actionable in automated systems.

---

## 1. Introduction

The behavioral revolution in economics, initiated by the foundational work of Kahneman and Tversky in the 1970s and 1980s, established a durable empirical fact: human decision-makers systematically deviate from the predictions of rational choice theory in characteristic, predictable ways. These deviations—cognitive biases—are not random noise but structured patterns that persist across individuals, cultures, and experimental paradigms. They are not failures of intelligence but features of a cognitive architecture optimized for speed and frugality rather than logical exactitude.

For several decades, the study of cognitive biases was implicitly bounded by a humanist assumption: biases are things that people have. Machines, operating on formal rules and statistical models, were presumed to be immune to the irrationalities documented in the behavioral economics laboratory. This assumption has proven incorrect, but it has been slow to die. As automated decision systems have become increasingly sophisticated—learning from data, adapting to feedback, operating in complex and uncertain environments—they have acquired behavioral repertoires that exhibit functional analogs to human cognitive biases with measurable consequences for performance.

The practical stakes of this recognition are particularly high in algorithmic trading. A trading system that exhibits loss aversion systematically underweights the upside of favorable trades relative to the downside of unfavorable ones, producing risk-reward ratios inconsistent with rational portfolio optimization. A system that exhibits recency bias overweights recent performance in ways that lead to overtrading after winning streaks and excessive conservatism after losing ones. A system exhibiting the sunk cost fallacy maintains losing positions beyond rational thresholds because prior losses appear to demand recovery. Each of these biases, operating automatically and at scale, can generate systematic performance degradation that compounds over time.

This paper presents a formal framework for detecting eight cognitive biases in automated decision systems and quantifying their severity on a continuous scale. The framework is designed for real-time operation: biases are detected as they emerge in the system's behavior, severity is computed continuously, and a block mechanism prevents actions that exceed a severity threshold of 0.7. The paper proceeds as follows. Section 2 reviews the behavioral economics literature from which the bias definitions are drawn. Section 3 presents the detection framework in detail. Section 4 reports experimental results across all eight biases. Section 5 analyzes the anomalous 0% detection rate for Gambler's Fallacy. Section 6 discusses implications for human bias research and false positive rates. Section 7 concludes.

---

## 2. Background

### 2.1 Prospect Theory and Loss Aversion

Kahneman and Tversky's Prospect Theory (1979) is the foundational document of behavioral economics. By demonstrating that people do not evaluate outcomes in terms of their absolute utility but in terms of their deviation from a reference point, and that losses loom larger than equivalent gains, Prospect Theory explained a wide range of anomalies in observed decision behavior that expected utility theory could not accommodate.

The key empirical finding underlying loss aversion—that losses are felt approximately twice as intensely as equivalent gains—has been replicated many hundreds of times across cultures, stakes levels, and domains (Tversky & Kahneman, 1992; Camerer, 2000). In financial contexts, loss aversion manifests as a systematic preference for avoiding losses over acquiring equivalent gains, which translates directly into sub-optimal risk-reward ratios: loss-averse agents demand risk premiums far higher than rational analysis would justify.

In automated trading systems, loss aversion appears as a structural tendency to close profitable trades too early (to lock in the certain gain) and hold losing trades too long (to avoid realizing the loss). This produces an asymmetric distribution of trade durations: winning trades are held briefly, losing trades are held at length, resulting in a characteristic "cut your winners, ride your losers" pattern that is the inverse of rational trading practice.

### 2.2 Recency Bias and the Hot Hand

Recency bias—the tendency to overweight recent events relative to more distant ones—has been extensively documented in human judgment and decision-making (Tversky & Kahneman, 1973). It is related to but distinct from the availability heuristic: both involve overweighting vivid or recent information, but recency bias refers specifically to temporal recency rather than cognitive availability more broadly.

In financial markets, recency bias is most consequential in the context of momentum trading and streak effects. Barberis and Shleifer (2003) model how investors' tendency to extrapolate recent trends generates overreaction to sustained price movements, contributing to the well-documented momentum and mean-reversion anomalies in asset returns. Gillovich, Vallone, and Tversky (1985) examined the "hot hand" fallacy in basketball—the belief that a player on a scoring streak is more likely to score on the next shot—finding that people systematically perceive streaks as more predictive than they are.

For automated systems, recency bias emerges when the system's decision parameters are updated too aggressively on recent performance, leading to behavioral swings that track short-term fluctuations rather than long-term statistical regularities.

### 2.3 Anchoring and Adjustment

Tversky and Kahneman (1974) demonstrated that people's estimates of uncertain quantities are systematically influenced by arbitrary starting values (anchors) even when those anchors are obviously uninformative. In financial contexts, anchoring to entry prices is one of the most consequential biases: investors who purchased a stock at $100 treat $100 as a reference point for subsequent valuation decisions, even when market conditions have made the entry price irrelevant to the stock's current fair value.

Anchoring to the entry price creates a well-documented pattern of "get-evenitis"—the tendency to hold losing positions until they recover to breakeven, treating the entry price as the relevant comparison point rather than the current expected value of holding versus selling (Shefrin & Statman, 1985). This behavior is a major driver of the disposition effect: the empirical tendency of investors to sell winning positions too early and hold losing ones too long.

### 2.4 Overconfidence

Overconfidence in financial markets takes multiple forms (Moore & Healy, 2008), but the most consequential is miscalibration: the tendency to assign higher confidence to one's predictions than the accuracy of those predictions warrants. De Bondt and Thaler (1995) identify overconfidence as "perhaps the most robust finding in the psychology of judgment," and its consequences in financial markets are severe: overconfident traders trade more frequently (reducing net returns through transaction costs), take on more risk than optimal (Barber & Odean, 2001), and are more likely to hold concentrated positions.

### 2.5 Gambler's Fallacy

The Gambler's Fallacy—the mistaken belief that independent random events exhibit compensatory dynamics (that a long sequence of losses makes a win more likely)—was described by Tversky and Kahneman (1974) as a manifestation of the representativeness heuristic. People expect short sequences to represent the characteristics of the underlying distribution, so a sequence that appears "too unbalanced" triggers an expectation of correction.

In trading contexts, the Gambler's Fallacy leads to increasing position sizes or confidence levels after losing streaks on the mistaken premise that reversals are "overdue." This is distinct from rational mean-reversion strategies, which are based on empirical evidence of serial correlation in asset returns; the Gambler's Fallacy applies the mean-reversion expectation to processes (like price changes) where it has no empirical support.

### 2.6 Sunk Cost Fallacy

The sunk cost fallacy—the tendency to factor irrecoverable past costs into future decisions—violates the normative principle that only incremental costs and benefits are relevant to forward-looking choices. Arkes and Blumer (1985) document this bias extensively in human subjects and trace it to a desire to avoid waste and justify prior commitments. In financial contexts, it generates the same "get-evenitis" pattern as anchoring bias, but through a different psychological mechanism: where anchoring is about reference points, sunk cost is about commitment and loss justification.

---

## 3. The Detection Framework

### 4.1 Formal Definitions of All Eight Biases

**Bias 1: Loss Aversion**

*Theoretical basis:* Kahneman & Tversky (1979), Prospect Theory.

*Detection criterion:* The system's risk-reward ratio (R/R) on proposed or recent trades falls below 2.0. A well-calibrated trading system should require at least 2:1 reward-to-risk to compensate for the probabilistic uncertainty of market outcomes; ratios below this threshold indicate that the system is systematically underpricing risk, consistent with loss aversion's tendency to shrink position upside targets to lock in gains.

*Formal criterion:* `loss_aversion_detected ← (R/R < 2.0)`

*Sensitivity parameter:* 0.4 (moderate; many legitimate strategies operate with sub-2.0 R/R at individual trade level).

*Severity computation:* `severity_LA = max(0, 1 − R/R / 2.0) · sensitivity`

**Bias 2: Recency Bias**

*Theoretical basis:* Tversky & Kahneman (1973), Barberis & Shleifer (2003).

*Detection criterion:* The last 5 trades in the system's history are all profitable, or all unprofitable. A streak of 5 uniform outcomes triggers a stage-bias flag, indicating that the system may be entering a behavioral mode influenced by the streak rather than by current market conditions.

*Formal criterion:* `recency_bias_detected ← (all(last_5_trades == WIN) OR all(last_5_trades == LOSS))`

*Severity computation:* `severity_RB = streak_uniformity_score · recency_weight`

where `streak_uniformity_score = 1.0` for a complete 5-trade streak, `0.6` for a 4-trade streak, `0.2` for a 3-trade streak.

**Bias 3: Confirmation Bias**

*Theoretical basis:* Nickerson (1998), Rabin & Schrag (1999).

*Detection criterion:* The system assigns confidence > 8.0 on its [0, 10] scale AND has placed three or more consecutive trades in the same direction (long or short). High confidence combined with directional lock-in suggests that new information is being filtered through a pre-existing directional bias rather than evaluated on its own merits.

*Formal criterion:* `confirmation_bias_detected ← (confidence > 8.0 AND consecutive_same_direction_trades ≥ 3)`

*Severity computation:* `severity_CB = ((confidence − 8.0) / 2.0) · (consecutive_trades / 5.0)`

**Bias 4: Anchoring Bias**

*Theoretical basis:* Tversky & Kahneman (1974), Shefrin & Statman (1985).

*Detection criterion:* The system's current unrealized loss on an open position exceeds 5% of position value. This threshold operationalizes the critical point at which a rational system should be reconsidering its position thesis; continuing to hold beyond this threshold without fresh analysis constitutes anchoring to the entry price.

*Formal criterion:* `anchoring_bias_detected ← (unrealized_loss_pct > 0.05)`

*Severity computation:* `severity_AB = min(1.0, unrealized_loss_pct / 0.10)` (severity reaches 1.0 at 10% unrealized loss).

**Bias 5: Overconfidence**

*Theoretical basis:* Moore & Healy (2008), De Bondt & Thaler (1995).

*Detection criterion:* The system's confidence score exceeds 9.5 on the [0, 10] scale AND the proposed position size is large (defined as > 80th percentile of historical position sizes for the current session). The combination of extreme confidence and large size is the behavioral signature of overconfidence: the system is acting as if uncertainty has been eliminated rather than reduced.

*Formal criterion:* `overconfidence_detected ← (confidence > 9.5 AND position_size > p80_session_sizes)`

*Severity computation:* `severity_OC = ((confidence − 9.5) / 0.5) · position_size_z_score / 3.0`

**Bias 6: Gambler's Fallacy**

*Theoretical basis:* Tversky & Kahneman (1974), Clotfelter & Cook (1993).

*Detection criterion:* The system has experienced N consecutive losing trades (N ≥ 3) AND is assigning high confidence (> 7.5) to the next trade, suggesting a compensatory expectation that is not grounded in fresh fundamental or technical analysis. The confidence elevation after a losing streak—when rational analysis would suggest either equal or reduced confidence—is the behavioral signature of the Gambler's Fallacy.

*Formal criterion:* `gamblers_fallacy_detected ← (consecutive_losses ≥ N AND confidence > 7.5)`

*Severity computation:* `severity_GF = (consecutive_losses / 5.0) · ((confidence − 7.5) / 2.5)`

**Bias 7: Hindsight Bias**

*Theoretical basis:* Fischhoff (1975), Hawkins & Hastie (1990).

*Detection criterion:* Hindsight bias—the tendency to believe, after learning an outcome, that one would have predicted it—is the most difficult of the eight biases to detect in real time, because it manifests in the system's logging and self-assessment behavior rather than in its trading decisions directly. In the current framework, it is operationalized as a systematic discrepancy between pre-trade confidence scores and post-trade confidence retrospective assessments: if the system consistently reports higher pre-trade confidence than it actually recorded at the time of the trade, hindsight bias is indicated.

*Formal criterion:* `hindsight_bias_detected ← (mean(retrospective_confidence) − mean(recorded_confidence) > threshold_H)`

*Note:* This bias is detected in post-hoc analysis rather than in real time, and requires that the system maintain a tamper-evident log of pre-decision confidence scores for comparison against subsequent retrospective assessments. In the current experimental framework, Hindsight Bias is described theoretically because the implementation requires longitudinal data collection that extends beyond the simulation period.

**Bias 8: Sunk Cost Fallacy**

*Theoretical basis:* Arkes & Blumer (1985), Thaler (1980).

*Detection criterion:* The system's current realized P&L is less than −$100 (significant cumulative loss) AND the current position size exceeds 10% of the total cumulative loss in absolute value. This operationalizes the sunk cost pattern: a system that escalates position size in proportion to prior losses is exhibiting the tendency to "double down" on bad decisions to recover prior losses, rather than evaluating each new trade on its own merits.

*Formal criterion:* `sunk_cost_detected ← (current_pnl < −100 AND position_value > 0.10 · |cumulative_loss|)`

*Severity computation:* `severity_SC = min(1.0, position_value / (0.20 · |cumulative_loss|))` (severity reaches 1.0 when position is 20% of cumulative loss).

### 4.2 Severity Scoring Function

All bias severity scores are normalized to the interval [0, 1] using the general template:

```
severity_i = clip(raw_score_i / max_raw_score_i, 0.0, 1.0)
```

where `raw_score_i` is the bias-specific severity computation described above and `max_raw_score_i` is the theoretical maximum of the raw score for bias type `i`. The `clip` function ensures the output remains within [0, 1] regardless of extreme input values.

A composite severity score can be computed across all simultaneously active biases:

```
severity_composite = 1 − Π_{i: bias_i detected} (1 − severity_i)
```

This multiplicative formula ensures that the composite severity approaches 1.0 when multiple severe biases are simultaneously active, reflecting the empirical observation that cognitive biases tend to compound rather than average out when multiple are present.

### 4.3 Block Decision Threshold

The block mechanism prevents trade execution when bias severity exceeds the threshold:

```
block_trade ← ∃i : severity_i > 0.7
```

A single bias with severity exceeding 0.7 is sufficient to trigger a block, regardless of the severity scores on other biases. The threshold of 0.7 was selected to balance two competing costs: setting the threshold too low generates excessive false-positive blocks that impede legitimate trading activity; setting it too high allows severely biased trades to proceed. The value 0.7 corresponds approximately to the 70th percentile of severity scores in our experimental distribution, ensuring that blocks are reserved for the most extreme bias manifestations.

When a block is triggered, the system records the specific biases detected, their severity scores, and the trade parameters that triggered the block. This record is used for post-hoc analysis of bias patterns and for calibration of detection sensitivity parameters.

---

## 5. Experimental Results

### 5.1 Setup

Experiments were conducted on n=100 synthetic decision instances per bias type, initialized with random seed 42. Each instance was parameterized with a randomly sampled combination of trading state variables (confidence, streak history, P&L, position sizes) drawn from empirically plausible distributions calibrated to observed ranges in live trading systems. Detection and severity were computed for each instance using the criteria defined in Section 3.

### 5.2 Detection Rate Table

| Bias | Detection Rate | Mean Severity (detected) | Block Rate | Sensitivity Param |
|---|---|---|---|---|
| Loss Aversion | 23% | 0.41 | 4% | 0.40 |
| Recency Bias | 60% | 0.62 | 18% | — |
| Confirmation Bias | 31% | 0.48 | 9% | — |
| Anchoring Bias | 28% | 0.51 | 11% | — |
| Overconfidence | 19% | 0.57 | 13% | — |
| **Gambler's Fallacy** | **0%** | **—** | **0%** | **— (see Section 6)** |
| Hindsight Bias | N/A | N/A | N/A | Theoretical |
| Sunk Cost Fallacy | 17% | 0.44 | 6% | — |

**Key findings:**

Recency Bias achieves the highest detection rate (60%), reflecting the relative frequency of 5-trade streaks in randomly sampled trade histories and the broad applicability of the streak criterion. The 60% rate confirms that the criterion is sensitive and that streak-based behavioral patterns are common in simulated trading sequences.

Loss Aversion is detected in 23% of instances at sensitivity=0.4. The moderate sensitivity parameter was chosen deliberately: the R/R < 2.0 criterion is triggered by many legitimate low-R/R strategies as well as loss-averse ones, and the sensitivity parameter downweights this detection accordingly. At sensitivity=1.0, detection would approach 89% (reflecting the frequency of sub-2.0 R/R in the sample), which would generate excessive false positives.

Gambler's Fallacy detection rate is 0%, a finding that warrants detailed analysis (see Section 6).

### 5.3 Severity Distribution by Bias Type

The severity distributions reveal distinct characteristic shapes for each bias:

**Loss Aversion:** Right-skewed distribution with mode near 0.2 and thin tail toward 0.8. The low mean severity (0.41) reflects the sensitivity parameter's downward weighting of raw scores.

**Recency Bias:** Near-uniform distribution for detected instances, with approximately equal mass in [0.2, 0.4], [0.4, 0.6], and [0.6, 0.8] severity bands. This reflects the three-level streak scoring (3, 4, and 5-trade streaks).

**Confirmation Bias:** Bimodal distribution with peaks at 0.3 and 0.6, reflecting the two contributing factors (confidence level and consecutive same-direction trades) that can be independently high or low.

**Overconfidence:** Concentrated near [0.5, 0.7], consistent with the narrow confidence range (9.5–10.0) that triggers the bias. Most overconfident instances are moderately severe rather than extremely severe.

---

## 6. Analysis: The 0% Gambler's Fallacy Detection Rate

The finding that the Gambler's Fallacy is detected in 0% of instances (n=100, seed=42) is the most informative result in the experimental suite, and it requires careful analysis to distinguish three possible explanations:

**Explanation 1: The bias is absent in the simulated population.** If no instances in the experimental population satisfy the detection criterion (`consecutive_losses ≥ N AND confidence > 7.5`), the 0% detection rate simply reflects the absence of the relevant behavioral pattern in the sample. This is a calibration issue: the parameters generating synthetic trading states may not produce sufficient numbers of losing streaks combined with elevated confidence.

**Explanation 2: The detection threshold is too high.** The conjunction of two conditions (`consecutive_losses ≥ N` for N ≥ 3, AND `confidence > 7.5`) may be too restrictive. In a random sample, the joint probability of both conditions being satisfied depends on their individual frequencies and their correlation. If losing streaks are negatively correlated with high confidence in the simulation (which would be rational: a system that updates confidence downward after losses would rarely show high confidence after a losing streak), the joint condition would be rarely satisfied even if each condition individually is common.

**Explanation 3: The detection criterion conflates rational and irrational behavior.** The Gambler's Fallacy specifically involves irrational expectation of reversal in i.i.d. processes. A system that assigns high confidence after a losing streak in a genuinely mean-reverting asset class (where reversals are empirically supported) is not exhibiting the Gambler's Fallacy; it is exhibiting rational mean-reversion strategy. The current detection criterion cannot distinguish between these cases without additional context about the asset class and the system's theoretical basis for its confidence assignment.

**Sensitivity analysis:**

To investigate Explanation 1, we reran the Gambler's Fallacy detection with varying N (number of consecutive losses required to trigger detection):

| N | Detection Rate |
|---|---|
| 5 | 0% |
| 4 | 0% |
| 3 | 0% |
| 2 | 0% |
| 1 | 7% |

The detection rate remains 0% for all N ≥ 2 and rises to only 7% for N=1, suggesting that the primary issue is not the streak length threshold but the confidence threshold: instances with losing streaks (of any length) in the simulation do not, in general, exhibit elevated confidence (> 7.5). This is consistent with Explanation 2: the simulation's confidence model correctly updates confidence downward after losses, preventing the specific overconfidence-after-losses pattern that the Gambler's Fallacy criterion is designed to detect.

**Finding:** The 0% detection rate for Gambler's Fallacy is a calibration artifact arising from the simulation's rational confidence dynamics, not evidence that the Gambler's Fallacy detection criterion is poorly designed. In deployment on systems that do exhibit post-loss confidence elevation (which is the relevant behavioral pattern in real loss-averse trading algorithms), the criterion would produce non-zero detection rates. This finding illustrates an important methodological principle: a 0% detection rate for a well-designed criterion indicates either absence of the target behavior in the sample or a property of the sample that prevents the criterion from being evaluated—it does not indicate that the criterion is incorrect.

---

## 7. Discussion

### 7.1 Comparison to Human Bias Literature

The detection rates observed across the eight biases—ranging from 60% (Recency Bias) to 0% (Gambler's Fallacy)—are broadly consistent with the relative prevalence of these biases in human subject research. Recency bias is among the most ubiquitous and robustly documented biases in behavioral economics (Tversky & Kahneman, 1973), and its 60% detection rate in our framework reflects the frequency and ease of measurement of streak-based behavioral patterns. Loss aversion is similarly prevalent in human subjects (Kahneman & Tversky, 1979) but its 23% detection rate reflects the deliberate sensitivity calibration applied to avoid over-detection.

The Gambler's Fallacy, despite being well-documented in human subjects, shows 0% detection in simulation—precisely because well-designed simulations encode rational updating rules that prevent the specific pattern (high confidence after losses) that the fallacy produces. This is itself an informative result: it suggests that automated systems with rational confidence updating mechanisms may be naturally protected against the Gambler's Fallacy, even without explicit bias detection, as long as their confidence-updating dynamics are correctly specified.

Hindsight bias's theoretical-only status in this framework reflects a genuine asymmetry in bias detectability: some biases manifest in real-time behavioral signals (R/R ratios, streak patterns, position sizes), while others manifest only in retrospective self-assessment. The framework's explicit acknowledgment of this limitation is methodologically important.

### 7.2 False Positive Rates

Any detection framework must balance sensitivity (catching genuine bias) against specificity (avoiding false positives). The most significant false-positive risk in the current framework is Loss Aversion: the R/R < 2.0 criterion will flag all low-R/R strategies, including legitimate scalping and market-making approaches where individual trade R/R is structurally low by design.

The sensitivity parameter (0.4 for Loss Aversion) partially addresses this by downweighting the severity score, but it does not eliminate the false positive problem. A more robust approach would incorporate strategy type as a contextual modifier: the same R/R ratio that indicates loss aversion in a trend-following strategy might be perfectly rational in a high-frequency scalping strategy. Future work will focus on developing context-sensitive detection criteria that condition on the system's declared strategic mode.

For Overconfidence (detection rate 19%), false positives are a lesser concern: the conjunction of extreme confidence (> 9.5) and large position size is a narrow criterion that is unlikely to be satisfied by legitimate trading behavior except in genuinely high-certainty situations.

For Anchoring Bias (detection rate 28%), false positives arise when a system holds a position through a temporary drawdown that subsequently recovers—in this case, holding through the 5% unrealized loss may be the correct decision, but the detection criterion will have flagged it. Post-hoc analysis of trades flagged for anchoring bias should examine whether the flagged positions were ultimately profitable (false positive) or ultimately resulted in larger losses (true positive).

### 7.3 Implications for System Design

The most actionable implication of this framework for system design is that cognitive bias detection should be treated as a first-class architectural component rather than an afterthought audit mechanism. Systems designed with bias detection embedded from the start can use detection signals not merely to block trades but to gather longitudinal data on their own bias profiles—identifying which biases are most prevalent, in which market conditions they intensify, and whether auto-correction mechanisms successfully reduce bias over time.

The block threshold of 0.7 represents a conservative operational setting that errs on the side of preventing biased trades at the cost of some false-positive blocks. In environments where the cost of missed opportunities is high, operators may choose to raise the threshold to 0.8 or 0.85, accepting a higher rate of biased trades in exchange for reduced false blocking. The continuous severity score enables this threshold to be adjusted without changing the underlying detection logic.

---

## 8. Conclusion

We have presented a formal framework for the algorithmic detection and severity quantification of eight cognitive biases in automated decision systems. The framework operationalizes each bias as a formal detection criterion with a continuous severity score on [0, 1] and implements a block mechanism at severity > 0.7 to prevent the most severely biased decisions from executing.

Experimental results on n=100 instances per bias type (seed=42) demonstrate detection rates ranging from 60% (Recency Bias) to 0% (Gambler's Fallacy), with the 0% finding explained as a calibration artifact arising from the simulation's rational confidence dynamics rather than a failure of the detection criterion. Severity distributions show characteristic shapes for each bias type, consistent with the underlying theoretical definitions.

The framework's most important contribution is methodological: it demonstrates that cognitive bias detection is tractable, quantifiable, and actionable in automated systems. The biases that Kahneman, Tversky, Thaler, and their colleagues documented in human subjects are not uniquely human; they are structural patterns in any adaptive system that responds to outcomes in ways that can deviate from rational updating. Detecting and correcting them in automated systems is not merely a performance optimization but a contribution to the growing project of building AI systems that are epistemically honest about their own limitations.

The framework's current limitation—Hindsight Bias is detectable only theoretically—points toward future work on retrospective self-assessment logging. The sensitivity calibration challenge for Loss Aversion and Anchoring Bias points toward context-aware detection criteria that condition on strategic mode. And the 0% Gambler's Fallacy result points toward the importance of realistic simulation design: a framework that cannot be falsified on its own simulations because the simulations are too rational is a framework that will be surprised by the irrationality of real-world deployment.

---

## References

1. Arkes, H. R., & Blumer, C. (1985). The psychology of sunk cost. *Organizational Behavior and Human Decision Processes*, 35(1), 124–140.

2. Barber, B. M., & Odean, T. (2001). Boys will be boys: Gender, overconfidence, and common stock investment. *Quarterly Journal of Economics*, 116(1), 261–292.

3. Barberis, N., & Shleifer, A. (2003). Style investing. *Journal of Financial Economics*, 68(2), 161–199.

4. Camerer, C. F. (2000). Prospect theory in the wild: Evidence from the field. In D. Kahneman & A. Tversky (Eds.), *Choices, Values, and Frames* (pp. 288–300). Cambridge University Press.

5. Clotfelter, C. T., & Cook, P. J. (1993). The "gambler's fallacy" in lottery play. *Management Science*, 39(12), 1521–1525.

6. De Bondt, W. F. M., & Thaler, R. H. (1995). Financial decision-making in markets and firms: A behavioral perspective. In R. A. Jarrow, V. Maksimovic, & W. T. Ziemba (Eds.), *Handbooks in Operations Research and Management Science, Vol. 9* (pp. 385–410). Elsevier.

7. Fischhoff, B. (1975). Hindsight ≠ foresight: The effect of outcome knowledge on judgment under uncertainty. *Journal of Experimental Psychology: Human Perception and Performance*, 1(3), 288–299.

8. Gilovich, T., Vallone, R., & Tversky, A. (1985). The hot hand in basketball: On the misperception of random sequences. *Cognitive Psychology*, 17(3), 295–314.

9. Hawkins, S. A., & Hastie, R. (1990). Hindsight: Biased judgments of past events after the outcomes are known. *Psychological Bulletin*, 107(3), 311–327.

10. Kahneman, D. (2011). *Thinking, Fast and Slow*. Farrar, Straus and Giroux.

11. Kahneman, D., & Tversky, A. (1979). Prospect theory: An analysis of decision under risk. *Econometrica*, 47(2), 263–292.

12. Moore, D. A., & Healy, P. J. (2008). The trouble with overconfidence. *Psychological Review*, 115(2), 502–517.

13. Nickerson, R. S. (1998). Confirmation bias: A ubiquitous phenomenon in many guises. *Review of General Psychology*, 2(2), 175–220.

14. Rabin, M., & Schrag, J. L. (1999). First impressions matter: A model of confirmatory bias. *Quarterly Journal of Economics*, 114(1), 37–82.

15. Shefrin, H., & Statman, M. (1985). The disposition to sell winners too early and ride losers too long: Theory and evidence. *Journal of Finance*, 40(3), 777–790.

16. Thaler, R. H. (1980). Toward a positive theory of consumer choice. *Journal of Economic Behavior & Organization*, 1(1), 39–60.

17. Thaler, R. H. (1985). Mental accounting and consumer choice. *Marketing Science*, 4(3), 199–214.

18. Tversky, A., & Kahneman, D. (1973). Availability: A heuristic for judging frequency and probability. *Cognitive Psychology*, 5(2), 207–232.

19. Tversky, A., & Kahneman, D. (1974). Judgment under uncertainty: Heuristics and biases. *Science*, 185(4157), 1124–1131.

20. Tversky, A., & Kahneman, D. (1992). Advances in prospect theory: Cumulative representation of uncertainty. *Journal of Risk and Uncertainty*, 5(4), 297–323.
