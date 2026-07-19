# План патентования и IP-стратегия IAC

## 00. Состояние

**Дата:** 2 июля 2026
**Статус:** Проект на стадии alpha. Необходимо зафиксировать интеллектуальную собственность до публикаций.

---

## 01. Что подлежит защите

### 01.1. Архитектурные изобретения (patentable)

| № | Изобретение | Тип | Готовность |
|---|---|---|---|
| P1 | **Self-Consistent Engine** — архитектура с тремя слоями (Representation, Transformation, Meta-Transformation), где изменение инициируется внутренним противоречием, а не внешней ошибкой | Method / System | Концепция готова, требуется формальное описание |
| P2 | **SDE Pipeline** — конвейер автоматического научного открытия: Pattern Extraction → Hypothesis Generation → Falsification → Invariant Extraction → Architecture Integration | Method | Концепция готова, реализована в коде |
| P3 | **Negative Intelligence Engine** — подсистема, единственная задача которой — разрушать гипотезы через 4 типа противоречий (логические, эмпирические, self-reference, cross-domain) | Method | Концепция готова, частично в коде |
| P4 | **Sync Engine с anticipation** — метод предсказания sync_error до выполнения действия и валидации предсказаний (meta-sync) | Method | Реализовано в коде |
| P5 | **Translation Architecture** — мост между моделями с сохранением инвариантов при переходе между доменами | Method | Концепция |
| P6 | **Field Interface** — активное сканирование среды на триггеры, резонирующие с внутренними конфликтами | Method | Концепция |

### 01.2. Алгоритмы и метрики (trade secret + copyright)

| № | Объект | Тип защиты |
|---|---|---|
| A1 | sync_score / sync_delta — эвристическая текстовая метрика синхронизации | Trade secret + Copyright |
| A2 | Self-Consistency Index S = 1 - (C/T) | Trade secret |
| A3 | Adaptive Sleep — алгоритм подстройки частоты циклов под sync_error | Trade secret |
| A4 | Cross-domain invariant strength calculation | Trade secret |

### 01.3. Исходный код (copyright)

- Весь код в `live.py`, `skills/` — автоматическая защита авторским правом при создании
- Рекомендуется: регистрация в U.S. Copyright Office / Роспатент для ключевых модулей

### 01.4. Торговая марка (trademark)

- **IAC** — Invariant Adaptive Core
- **SDE** — Scientific Discovery Engine (проверить уникальность)
- Возможный логотип: замкнутая петля с 5 узлами (5-primitive kernel)

---

## 02. Стратегия патентования

### 02.1. Последовательность

```
ШАГ 1 (сейчас):       Provisional Patent Application (US) / Заявка на выдачу патента РФ
                      — защищает дату приоритета на 12 месяцев
                      — стоит $70-140 (micro-entity US) / ~5000₽ (РФ)

ШАГ 2 (6 месяцев):    Доработка формальных описаний, эксперименты, данные
                      — подготовка non-provisional / PCT заявки

ШАГ 3 (12 месяцев):   Подача PCT (Patent Cooperation Treaty)
                      — покрывает 150+ стран
                      — даёт ещё 18 месяцев на выбор стран

ШАГ 4 (30 месяцев):   National phase — подача в конкретные юрисдикции
                      US, EU, CN, JP, RU — по бизнес-необходимости
```

### 02.2. Приоритетные юрисдикции

| Юрисдикция | Причина |
|---|---|
| **РФ** (Роспатент) | Родная юрисдикция автора, низкая стоимость |
| **US** (USPTO) | Крупнейший рынок, признание приоритета |
| **EU** (EPO) | Европейский рынок |
| **CN** (CNIPA) | Растущий AI-рынок, потенциальные конкуренты |

### 02.3. Поиск prior art

Перед подачей необходимо провести поиск:
- Google Patents
- USPTO Patent Full-Text
- Espacenet (EPO)
- ArXiv (pre-prints)
- GitHub (open source с патентными ограничениями)

Ключевые поисковые запросы:
- "self-consistent AI architecture"
- "recursive self-improvement system"
- "falsification-based AI pipeline"
- "invariant extraction machine learning"
- "meta-learning architecture contradiction resolution"

---

## 03. Шаблон описания изобретения (для патентного поверенного)

### 03.1. Структура заявки

```
1. НАЗВАНИЕ ИЗОБРЕТЕНИЯ
   "Self-Consistent Adaptive Architecture with Three-Layer Recursive Meta-Transformation"

2. ОБЛАСТЬ ТЕХНИКИ
   Artificial intelligence, machine learning architectures, adaptive systems,
   self-improving software, cognitive architectures.

3. УРОВЕНЬ ТЕХНИКИ (Background)
   - Existing AI systems optimize for external accuracy (loss minimization)
   - Problem: they don't optimize for internal consistency
   - LLMs show high self-contradiction rates (Tsinghua 2025)
   - Existing self-reflective systems (Reflex) are post-hoc layers

4. СУЩНОСТЬ ИЗОБРЕТЕНИЯ (Summary)
   Трёхслойная архитектура:
   Layer 1 — Representation: current model state
   Layer 2 — Transformation: rules for updating the model
   Layer 3 — Meta-Transformation: rules for changing the transformation rules
   
   Self-Consistent Engine:
   (a) detecting internal contradictions via self-reference
   (b) generating meta-rules at a higher logical level
   (c) updating the architecture when contradictions cannot be resolved locally

5. КРАТКОЕ ОПИСАНИЕ ЧЕРТЕЖЕЙ
   Fig. 1 — Self-Consistent Engine cycle diagram
   Fig. 2 — Three-layer architecture
   Fig. 3 — Example: contradiction detection and resolution
   Fig. 4 — Flowchart of meta-rule generation

6. ПОДРОБНОЕ ОПИСАНИЕ
   [Детальное описание каждого компонента с примерами данных]

7. ФОРМУЛА ИЗОБРЕТЕНИЯ (Claims)
   1. A computer-implemented method for adaptive intelligence, comprising:
      (a) maintaining a model representation ...
      (b) applying self-reference to detect internal contradictions ...
      (c) generating meta-rules at a higher logical level ...
      (d) updating the architecture when contradictions exceed a threshold ...
   
   2. The method of claim 1, wherein the three layers ...
   [10-20 claims, от широких к узким]

8. РЕФЕРАТ
   [150 слов]
```

---

## 04. Шаблон Provisional Patent Application (US)

```markdown
# PROVISIONAL PATENT APPLICATION

**Title:** Self-Consistent Adaptive Architecture with Three-Layer Recursive Meta-Transformation

**Inventor(s):** [Name], [Address], [Citizenship]

**Filed:** [Date]

---

## BACKGROUND

Current AI architectures optimize for external objectives (accuracy, loss, reward).
They do not explicitly optimize for internal logical consistency.
When a model contradicts itself, typical approaches ignore the contradiction
or treat it as noise. This leads to fragile systems that fail under distribution shift.

## SUMMARY

We describe a Self-Consistent Engine — an architecture where the primary
optimization objective is internal consistency rather than external accuracy.
The system operates on three layers and resolves contradictions by moving to
higher logical levels (meta-rules), which may trigger architectural reorganization
when local changes are insufficient.

## DETAILED DESCRIPTION

### 1. Three-Layer Architecture

Layer 1 — Representation: The model's current state, stored as a relation graph
with nodes (entities) and edges (typed relationships).

Layer 2 — Transformation: Rules for updating the representation. These include
local updates (parameter changes) and structural updates (rewiring the graph).

Layer 3 — Meta-Transformation: Rules for modifying the transformation rules
themselves. This layer activates when accumulated contradictions exceed a threshold.

### 2. Self-Consistent Engine Cycle

Step 1: Observe — receive data from environment or internal state
Step 2: Self-Reference — apply the current transformation rules to the model itself
Step 3: Conflict Detection — identify where self-application produces contradictions
Step 4: Meta-Rule Generation — generate new rules at level N+1 that resolve the conflict
Step 5: Model Update — apply the meta-rule, reorganizing the model
Step 6: Verification — measure self-consistency index S = 1 - (C/T)

### 3. Negative Intelligence Subsystem

A dedicated component whose sole purpose is to find contradictions.
It operates independently of the Positive Intelligence component that builds models.
This adversarial structure prevents confirmation bias.

### 4. Sync Engine

sync_error ∈ [0,1] measures divergence between model predictions and observations.
It is calculated as a heuristic text-based metric.
Anticipation predicts sync_error before action execution.
Meta-sync measures the calibration quality of predictions.

## CLAIMS (draft)

1. A system comprising:
   a processor;
   memory storing a self-consistent adaptive engine configured to:
   maintain at least three layers: representation, transformation, meta-transformation;
   detect internal contradictions via self-application of transformation rules;
   generate meta-rules to resolve detected contradictions;
   update the model architecture when contradictions exceed a threshold.

2. The system of claim 1, further comprising a negative intelligence module
   configured to independently search for contradictions in the model.

3. The system of claim 1, further comprising a sync engine configured to
   measure divergence between model predictions and observations using
   a heuristic text-based metric bounded in [0,1].

## DRAWINGS
[To be prepared: Fig 1-4]

## SIGNATURE
Inventor: _____________________ Date: _____________
Witness:  _____________________ Date: _____________
```

---

## 05. Защита авторским правом (Copyright)

### 05.1. Что регистрировать

- Исходный код `live.py` и ключевых модулей `skills/`
- Архитектурную документацию (ARCHITECTURE.md)
- Данные 13 циклов исследования

### 05.2. Процедура (US Copyright Office)

1. Собрать исходный код в один PDF
2. Подать через https://copyright.gov/eco/ ($45-65)
3. Получить сертификат регистрации

### 05.3. Процедура (РФ)

1. Депонирование в РАО или подача в Роспатент как программы для ЭВМ
2. Стоимость: ~3000-5000₽

---

## 06. Хронология приоритета (уже зафиксировано)

| Дата | Событие | Доказательство |
|---|---|---|
| 28.06.2026 | MEMORY_ANCHOR.md | Git commit |
| 30.06.2026 | 13 циклов исследования | Текстовый файл conversation |
| 02.07.2026 | ARCHITECTURE.md, AGENTS.md | Git commit |
| 02.07.2026 | Данный документ | Git commit |

**Рекомендация:** Зафиксировать все ключевые документы через timestamp-сервис (например, OriginStamp) или нотариально.

---

## 07. Open Source vs Patent

### 07.1. Рекомендуемая модель

**Dual licensing:**
- **Open Source (AGPLv3)** — для академического и некоммерческого использования
- **Commercial License** — для коммерческого использования
- **Патенты** — для защиты от крупных игроков (defensive)

### 07.2. Принцип

Патентуем архитектурные инновации, открываем реализацию.
Это позволяет:
- Академическому сообществу использовать и ссылаться
- Коммерческим компаниям лицензировать
- Защищать от патентного троллинга

---

## 08. Следующие действия (Action Items)

- [ ] Провести prior art search (1-2 недели)
- [ ] Подготовить формальные описания P1-P6 (2-4 недели)
- [ ] Создать рисунки Fig 1-4 для патентной заявки (1 неделя)
- [ ] Подать provisional patent (US) + заявку РФ (1 неделя после подготовки)
- [ ] Зарегистрировать copyright на код (параллельно)
- [ ] Зарегистрировать торговую марку IAC (после проверки уникальности)
- [ ] Опубликовать pre-print на arXiv (после provisional patent — для даты приоритета)

---

## 09. Бюджет (оценка)

| Статья | Стоимость |
|---|---|
| Prior art search (своими силами) | $0 |
| Provisional patent (USPTO micro-entity) | $70 |
| Заявка на патент РФ | ~5 000₽ |
| Copyright регистрация (US) | $45-65 |
| Торговая марка (РФ) | ~30 000₽ |
| Non-provisional patent + attorney | $8 000-15 000 (отложено) |
| **Итого немедленно:** | **~$200 + ~5 000₽** |
| **Итого через 12 месяцев:** | **~$10 000-20 000** |
