# LLM Integration in Flutter for Synct

## Date: 2026-07-18
## Status: Complete (architecture + implementation)

---

## 1. Available Approaches

| Approach | Package | Version | Likes | License | Platforms | Notes |
|---|---|---|---|---|---|---|
| **On-device (llama.cpp)** | `llama_cpp_dart` | 0.2.2 | 81 | MIT | Android, iOS, Linux, macOS, Windows | FFI bindings + ManagedIsolate for Flutter |
| **Cloud API** | `http` (built-in) | — | — | — | all | OpenAI-compatible |
| **Local server** | `http` → ollama :11434 | — | — | — | all | Requires ollama on device |

### 1a. llama_cpp_dart (chosen for on-device)

**Strengths:**
- Full Flutter support via ManagedIsolate (non-blocking)
- Three abstraction levels: FFI, High-Level, Isolate
- Chat format support: ChatML, Llama2, Gemma, Mistral
- Quantization support (Q4_K_M recommended)
- RAG example included

**Requirements:**
- Compiled llama.cpp shared library (.dll / .so / .dylib)
- GGUF model file (7B Q4_K_M ~4GB, 3B Q4_K_M ~2GB)
- ~2-4GB RAM for 3B-7B models (feasible on modern phones)

**Reference:** https://pub.dev/packages/llama_cpp_dart

### 1b. Cloud API (OpenAI-compatible)

**Strengths:**
- Zero binary size overhead
- Any model size (GPT-4, Claude, etc.)
- Streaming support
- Fast iteration

**Weaknesses:**
- Requires internet connection
- API key management
- Latency
- Privacy concerns (HRV data)

---

## 2. Architecture Decision

**Hybrid approach** (`LLMBackendType.hybrid`):

```
┌─────────────────────────────────────────────────┐
│                  LLMService                      │
│  (abstract interface)                           │
├─────────────────────────────────────────────────┤
│  generate() | chat() | analyzeSession()         │
│  generateRule() | generateStream()              │
└────────────────┬────────────────────────────────┘
                 │
        ┌────────┴────────┐
        ▼                 ▼
┌──────────────┐  ┌──────────────┐
│ LocalBackend │  │ CloudBackend │
│ (llama_cpp)  │  │ (HTTP API)   │
└──────────────┘  └──────────────┘
        │                 │
        └────────┬────────┘
                 ▼
┌─────────────────────────────────────────────────┐
│             HybridLLMBackend                     │
│  local if loaded, else cloud                    │
│  auto-fallback on failure                       │
└─────────────────────────────────────────────────┘
```

**Integration with IAC:**
```
┌──────────┐   generateRule()   ┌──────────┐
│   LLM    │ ─────────────────► │   IAC    │
│  Service │                    │  Engine   │
│          │ ◄───────────────── │          │
└──────────┘   patterns/triggers └──────────┘
```

---

## 3. Files Created

| File | Lines | Purpose |
|---|---|---|
| `core/llm/llm_config.dart` | 112 | Config types, LLMBackendType, LLMMessage, LLMResult, LLMStats |
| `core/llm/llm_service.dart` | 28 | Abstract interface (6 methods) |
| `core/llm/backends/cloud_llm_backend.dart` | 155 | OpenAI-compatible HTTP API + streaming + retries |
| `core/llm/backends/local_llm_backend.dart` | 143 | llama_cpp_dart wrapper + offline fallback |
| `core/llm/backends/hybrid_llm_backend.dart` | 97 | Auto-select local/cloud, fallback logic |
| `core/llm/llm_provider.dart` | 192 | Riverpod StateNotifier + 4 selectors + built-in heuristics |
| `core/llm/llm_iac_integration.dart` | 83 | LLM↔IAC bridge: analyzeSession, generateRule, getAdvice |
| `core/llm/llm.dart` | 13 | Barrel export |
| `features/llm_chat/llm_chat_screen.dart` | 275 | Chat UI + config dialog + analyze button |
| `test/llm_test.dart` | 68 | 6 tests (config round-trip, backends) |
| `research/llm_in_flutter.md` | this | Research document |

**Total: ~1076 lines added**

---

## 4. Usage Flow

```
1. App start → LLMNotifier.initialize()
   ├─ LocalBackend: loads GGUF via llama_cpp_dart (if model path set)
   └─ CloudBackend: tests API connection (if API key set)

2. Practice complete → _onPracticeComplete()
   ├─ IAC cycle() → update model
   └─ LLMIACIntegrator.analyzeLastSession() → feedback (fire-and-forget)

3. User opens chat → LLMChatScreen
   ├─ Send message → LLMService.generate()
   ├─ "Анализ IAC" → LLMIACIntegrator.analyzeLastSession()
   └─ ⚙ Config → switch backend / set API key
```

---

## 5. Future Improvements

- [ ] Download GGUF model from within the app (first-run setup)
- [ ] Fine-tune a small model (3B) on HRV session data
- [ ] Voice input for chat
- [ ] Real-time coaching narration via LLM + TTS
- [ ] Privacy mode: enforce local-only, no cloud fallback

---

## 6. References

- llama_cpp_dart: https://pub.dev/packages/llama_cpp_dart
- llama.cpp: https://github.com/ggml-org/llama.cpp
- GGUF models: https://huggingface.co/models?library=gguf
