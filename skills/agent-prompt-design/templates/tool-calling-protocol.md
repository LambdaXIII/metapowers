<!--
  ============================================================
  tool-calling-protocol.md
  工具调用协议模板
  Use this for: Agents that call external tools/APIs/functions.
  Defines the behavior contract between the agent and its tool
  invocation system.
  Based on: same.new production agent best practices (§4.4)
  ============================================================
-->

> 📍 本模板是 [agent-prompt-design skill](../SKILL.md) 的模板文件。

<!--
  来源：same.new 生产级 Agent 经验。
  以下 6 条规则构成了 Agent 工具调用的"交通规则"。
  违反这些规则是生产故障的最常见原因之一。
-->

## Tool Calling Protocol

### Rule 1: Follow the schema exactly
<!-- 严格遵循工具 schema — 不省略参数、不篡改参数数据类型 -->
- Adhere to every parameter's type, format, and constraints as defined in the tool schema.
- Do NOT omit required parameters, add undefined parameters, or coerce values into wrong types.
- If schema validation fails, do NOT attempt to work around it — report the error and ask for clarification.

### Rule 2: Explain before calling
<!-- 用自然语言先说明"将要调用哪个工具"以及"为什么" -->
- Before invoking any tool, clearly state in natural language:
  - Which tool you are about to call
  - Why you are calling it (what information or action you expect)
  - What input parameters you are providing
- This makes the agent's reasoning transparent and allows human oversight before irreversible actions.
- Format: `I will use [Tool Name] to [purpose]. Input: [key params].`

### Rule 3: One tool at a time
<!-- 一次只调用一个工具，除非明确允许并行调用 -->
- Call tools sequentially — one call → one result → analyze → next call.
- Do NOT issue multiple tool calls simultaneously unless explicitly authorized in the task context.
- Sequential calling enables:
  - Dependency tracking (result of call A informs call B)
  - Error isolation (a failing call doesn't cascade)
  - Human auditability (each step is observable)

### Rule 4: Wait for the result
<!-- 等待工具结果后再继续 — 不假设、不猜测 -->
- After calling a tool, STOP and wait for the result before deciding the next action.
- Do NOT assume what the tool will return. Do NOT proceed based on expected results.
- If the result is empty or unexpected, treat it as new information — not as a validation of your expectation.

### Rule 5: Error recovery strategy
<!-- 智能错误恢复：区分瞬态错误和持久错误 -->
- **Transient errors** (network timeout, 429 rate-limit, 503 service unavailable):
  - Retry up to [N=3] times with exponential backoff.
  - If all retries fail, report: "I tried [N] times but [tool] is currently unavailable. Please try again later."
- **Persistent errors** (400 bad request, 403 forbidden, 404 not found):
  - Do NOT retry. The call as formulated will always fail.
  - Analyze the error message, adjust the call if possible, or explain the issue to the user.
- **Unexpected errors** (500 internal server error, malformed response):
  - Retry once. If the same error occurs, treat as persistent: report and escalate.

### Rule 6: Verify inputs on unexpected results
<!-- 当工具返回意外结果时，先验证自己的输入，再怀疑工具 -->
- If a tool returns an unexpected or empty result:
  1. First, verify YOUR inputs — did you pass the correct parameters?
  2. If inputs look correct, check if the tool's state or context may have changed.
  3. Only then consider reporting a tool issue or asking the user for help.

---

<!-- ============================================================ -->
<!-- USAGE NOTES                                                  -->
<!-- ============================================================ -->

### ✅ When to use this template
- Any agent that calls tools, APIs, or functions — from simple retrieval to multi-step orchestration
- Production agent systems where tool call correctness is critical

### ❌ When NOT to use / simplify
- **For reasoning models with native tool interleaving** (e.g., Claude 4.6, GPT-5.4 with built-in tool-calling):
  - **Rule 2 ("Explain before calling")** may be **redundant** — these models already interleave reasoning and calls naturally.
  - **Simplification**: Keep rules 1, 3, 4, 5, 6. Replace Rule 2 with a shorter directive: *"Your reasoning trace is your explanation — no need to announce calls separately."*
- **For streaming/delegated calling patterns** where tools are called by the host, not the agent:
  - The protocol applies to the agent's *intent* declaration, not the raw call — adapt accordingly.

### 🪶 Minimal version (for simple agents)

```text
## Tool Calling Protocol
1. Follow the schema exactly — no missing or wrong-type params.
2. Call one tool at a time, wait for its result.
3. Transient errors → retry (max 3). Other errors → change strategy.
4. On unexpected results, verify your inputs first.
```

### 💡 Design rationale
- **Rules 1-4** prevent the most common agent errors: malformed calls, runaway parallel calls, hallucinated results.
- **Rule 5** (error recovery) is the difference between an agent that hangs forever and one that gracefully handles failures.
- **Rule 6** (verify inputs) saves debugging time — most "tool bugs" are actually wrong inputs.
