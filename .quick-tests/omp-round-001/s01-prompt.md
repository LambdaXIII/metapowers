You are performing a documentation audit — a simulated usage test of a skill document. Your goal is NOT to actually search the web or execute real tasks. Your goal is to read the skill document, pretend to follow its instructions as an AI agent would, and report what happens.

## Hard Constraints

- DO NOT call web_search. DO NOT call browser_navigate or any browser tool.
- DO NOT make any network requests.
- You are NOT actually searching for information. You are TESTING whether the skill document's instructions are clear and complete.
- Allowed tools: read (to load skill files), bash (only for file listing, not for curl/network).

## Skill Under Test

The skill is located at: C:\Users\Cxalio\AppData\Local\hermes\skills\research\web-search-protocol\

Load it with: read C:\Users\Cxalio\AppData\Local\hermes\skills\research\web-search-protocol\SKILL.md

The skill is a "Web Search Protocol" — a decision tree and tool chain for searching the web and extracting content. It covers search discovery, content extraction (3-layer fallback), GitHub API, and browser tools.

## Scenario

**User profile:** A developer who knows Python.  
**What the user wants:** "I need to understand Python asyncio's TaskGroup feature. I don't know where to find the documentation."  
**Entry:** The agent loads this skill via its main SKILL.md (正门 / main entrance).  
**Context level:** Bare — the agent has no prior knowledge about web searching or this skill's tools.

## Simulation Rules

**清空 (Clear your mind):** Pretend you have never seen this document before. Enter without any preset conclusions.

**逐步骤跟随 (Follow step by step):** Trace the skill's decision tree as an agent would — don't skip, don't invent. When you hit something ambiguous, contradictory, or missing, RECORD it as a confusion point and continue.

**边界刨 (Probe the edges):** Deliberately try at least two unusual paths:
1. Skip a section (e.g., jump from §1 directly to §4 without reading §2-3)
2. Misunderstand a term (e.g., confuse "web_extract" with "web_search")
Document whether the skill catches or handles these edge cases.

## Required Report Format

After completing the simulation, report:

1. **Complete path traced** — file → section → file → ... (every hop you took)
2. **Pause/Confusion/Misunderstanding points** — each with file:line (approximate) + description
3. **Dead links, broken anchors, terminology inconsistencies**
4. **Any unexpected positive or negative findings**

Do NOT score or rate the skill. Scoring requires global comparison across scenarios, done by the coordinator later.

## Failure Behavior

If you hit an insurmountable obstacle (files don't exist, all paths broken), report "推演中止" (simulation aborted) with the specific location and reason. Do NOT try to work around systemic failures.
