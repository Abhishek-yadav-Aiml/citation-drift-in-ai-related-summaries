# AI assistance and debugging log

| ID | Date | Component | Observed issue | Evidence/status |
|---|---|---|---|---|
| DBG-001 | 2026-11-17 | AlignScore environment | Author reported ModuleNotFoundError for spaCy, then click; a later attempt reported that the selected environment had no pip module. | User-reported console errors. Successful AlignScore import and inference are not confirmed. |
| DBG-002 | 2026-11-17 | SciFact + DeBERTa experiment | User reported running an NLI experiment on SciFact dev. | Reported separately; original runnable notebook/script is not included in this repository. |

Do not mark dependencies as fixed without recording the successful command and output. Do not claim AlignScore has run unless a checkpoint-backed inference log exists.
