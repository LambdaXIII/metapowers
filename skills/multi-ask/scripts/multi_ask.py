#!/usr/bin/env python3
import argparse
import html
import json
import re
import sys
import threading
import time
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

BLOCK_LANGS = {"single-choice": "radio", "multi-choice": "checkbox", "multiple-choice": "checkbox", "yes-or-no": "yes-no"}
BLOCK_HEAD_RE = re.compile(r"^<([^<>\s]+)>\s*(.*)$")
OPTION_LINE_RE = re.compile(r"^-\s*\[([ xX])\]\s*<([^<>\s]+)>\s*(.*)$")

FENCE_RE = re.compile(r"^( {0,3})(`{3,}|~{3,})(.*)$")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
LIST_RE = re.compile(r"^\s*([-*+]|\d{1,9}[.)])\s+(.*)$")
LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)\s]+)\)")
BOLD_RE = re.compile(r"\*\*(.+?)\*\*")
ITALIC_RE = re.compile(r"(?<![*\w])\*(?!\*)(.+?)(?<!\*)\*(?![*\w])")
UNDERSCORE_RE = re.compile(r"(?<![\w_])_([^_]+)_(?![\w_])")
CODE_SPAN_RE = re.compile(r"`([^`]+)`")

PAGE_TEMPLATE = """<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>问卷 · __NAME__</title>
<style>
* { box-sizing: border-box; }
:root {
  --paper: #f4f0e8;
  --card: #fdfbf6;
  --ink: #26221b;
  --muted: #6d6455;
  --line: #e2dbcc;
  --accent: #b23c26;
  --accent-deep: #97301d;
  --ring: rgba(178, 60, 38, .22);
}
html { scrollbar-color: #c9c0ad transparent; scroll-behavior: smooth; }
::-webkit-scrollbar { width: 10px; height: 10px; }
::-webkit-scrollbar-thumb { background: #c9c0ad; border-radius: 6px; border: 2px solid var(--paper); }
::-webkit-scrollbar-track { background: transparent; }
body { margin: 0; background: var(--paper); color: var(--ink); font: 15.5px/1.7 system-ui, -apple-system, "Segoe UI", "PingFang SC", "Microsoft YaHei", sans-serif; -webkit-font-smoothing: antialiased; text-rendering: optimizeLegibility; }
::selection { background: rgba(178, 60, 38, .18); }
.doc { max-width: 66rem; margin: 0 auto; padding: 3rem 1.5rem 2rem; }
.doc-name { font-size: .8125rem; color: var(--muted); letter-spacing: .04em; margin: 0 0 1.75rem; padding-bottom: 1.25rem; border-bottom: 1px solid var(--line); }
.doc h1 { font-size: clamp(1.75rem, 4.5vw, 2.25rem); line-height: 1.32; letter-spacing: -.02em; font-weight: 700; margin: 0 0 1rem; text-wrap: balance; }
.doc h2 { font-size: 1.3125rem; line-height: 1.45; letter-spacing: -.015em; font-weight: 650; margin: 2.25rem 0 .5rem; text-wrap: balance; }
.doc h3 { font-size: 1.0625rem; font-weight: 650; margin: 1.6rem 0 .4rem; }
.doc h1, .doc h2, .doc h3 { scroll-margin-top: 1.5rem; }
.doc h4, .doc h5, .doc h6 { font-size: 1rem; font-weight: 650; margin: 1.25rem 0 .35rem; }
.doc p { margin: .75rem 0; }
.doc a { color: var(--accent); text-underline-offset: 3px; text-decoration-thickness: 1px; }
.doc a:hover { color: var(--accent-deep); }
.doc code { background: #eae3d2; padding: .12em .38em; border-radius: 4px; font-family: ui-monospace, "Cascadia Mono", Consolas, monospace; font-size: .875em; }
.doc pre { background: #ece5d5; border: 1px solid var(--line); padding: .875rem 1.125rem; border-radius: 10px; overflow-x: auto; font-size: .8125rem; line-height: 1.6; }
.doc pre code { background: none; padding: 0; font-size: inherit; }
pre.mermaid { background: var(--card); border: 1px solid var(--line); padding: 1rem; border-radius: 10px; text-align: center; overflow-x: auto; }
.mermaid svg { max-width: 100%; height: auto; }
.mermaid.rendered { border: 0; background: none; padding: 0; }
.mermaid.failed { text-align: left; }
.mermaid.failed::before { content: 'mermaid（渲染不可用，以下为源码）'; display: block; margin-bottom: .5rem; color: var(--muted); font-size: .8125rem; }
.doc blockquote { margin: 1rem 0; padding: 0 0 0 1.25rem; color: var(--muted); border-left: 1px solid var(--line); }
.doc hr { border: 0; border-top: 1px solid var(--line); margin: 1.75rem 0; }
.doc ul, .doc ol { padding-left: 1.5rem; margin: .75rem 0; }
.doc li { margin: .25rem 0; }
.qa { margin: .75rem 0 1.5rem; padding-left: 1.5rem; }
.qa-question { margin: 0 0 .35rem; }
.qa-question > :first-child { margin-top: 0; }
.qa-question > :last-child { margin-bottom: 0; }
.comment-block { margin: 2rem 0 1rem; }
.opt { position: relative; display: flex; gap: .55rem; align-items: flex-start; padding: .15rem 0; border-radius: 8px; cursor: pointer; transition: background 150ms ease; }
.opt:hover { background: #f1ebdd; }
.opt:has(input:checked) { background: rgba(178, 60, 38, .07); }
.opt input { appearance: none; -webkit-appearance: none; width: 1.125rem; height: 1.125rem; margin: .3rem 0 0; flex: none; border: 1.5px solid #a99f8c; background: var(--card); cursor: pointer; transition: background 180ms cubic-bezier(.22, 1, .36, 1), border-color 150ms ease, box-shadow 180ms cubic-bezier(.22, 1, .36, 1); }
.opt input[type="radio"] { border-radius: 50%; }
.opt input[type="checkbox"] { border-radius: 5px; }
.opt input:hover { border-color: var(--accent); }
.opt input:checked { border-color: var(--accent); background-color: var(--accent); }
.opt input[type="radio"]:checked { box-shadow: inset 0 0 0 3px var(--card); }
.opt input[type="checkbox"]:checked { background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E%3Cpath d='M3.5 8.5l3 3 6-6.5' fill='none' stroke='%23fdfbf6' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E"); background-size: 100% 100%; }
.opt input:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.opt-text { flex: 0 1 auto; }
.opt-text.rec { font-weight: 650; background-image: linear-gradient(90deg, #c2410c, #b45309, #a16207, #15803d, #1d4ed8, #7e22ce, #be185d, #c2410c); background-size: 240px 100%; background-repeat: repeat-x; -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent; color: transparent; }
.qa textarea, .comment-block textarea { width: 100%; margin-top: .5rem; padding: .625rem .875rem; border: 1px solid var(--line); border-radius: 10px; background: var(--card); color: inherit; font: inherit; font-size: .9375rem; line-height: 1.6; resize: vertical; caret-color: var(--accent); transition: border-color 150ms ease, box-shadow 150ms ease; }
.qa textarea::placeholder, .comment-block textarea::placeholder { color: #7d7362; }
.qa textarea:hover, .comment-block textarea:hover { border-color: #cfc5b0; }
.qa textarea:focus, .comment-block textarea:focus { outline: none; border-color: var(--accent); box-shadow: 0 0 0 3px var(--ring); }
textarea:disabled, .opt input:disabled { opacity: .55; cursor: default; }
.actions { position: sticky; bottom: 0; background: var(--paper); border-top: 1px solid var(--line); padding: .08rem 1.5rem .1rem; }
.actions-inner { max-width: 66rem; margin: 0 auto; }
button { appearance: none; display: block; width: 100%; border: 0; border-radius: 8px; padding: .18rem 1rem; font: inherit; font-size: .8125rem; font-weight: 650; line-height: 1.25; letter-spacing: .01em; background: var(--accent); color: #fdfbf6; cursor: pointer; transition: background 150ms ease, transform 120ms cubic-bezier(.22, 1, .36, 1); }
button:hover { background: var(--accent-deep); }
button:active { transform: scale(.995); }
button:disabled { background: #d8cfc0; color: #8f8676; cursor: default; transform: none; }
button.ok { background: rgba(46, 106, 68, .12); color: #2e6a44; }
button.err { background: var(--accent); color: #fdfbf6; }
button:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.toc { position: fixed; top: 50%; left: 0; width: calc((100vw - 66rem) / 2); transform: translateY(-50%); display: none; justify-content: center; padding: 0 1rem; max-height: 80vh; overflow-y: auto; scrollbar-width: none; }
.toc::-webkit-scrollbar { display: none; }
@media (min-width: 1360px) { .toc { display: flex; } }
.toc nav ol { list-style: none; margin: 0; padding: 0; width: fit-content; max-width: min(13rem, 100%); font-size: .8125rem; line-height: 1.45; }
.toc li { margin: 0; }
.toc a { display: block; padding: .22rem .4rem .22rem .7rem; color: var(--muted); text-decoration: none; border-left: 2px solid transparent; border-radius: 0 4px 4px 0; transition: color 120ms ease, border-color 120ms ease, background 120ms ease; }
.toc a:hover { color: var(--ink); border-left-color: var(--line); background: rgba(0, 0, 0, .02); }
.toc a.active { color: var(--accent); border-left-color: var(--accent); font-weight: 650; }
.toc a.lvl-1 { color: var(--ink); font-weight: 650; margin-bottom: .3rem; }
.toc a.lvl-3 { padding-left: 1.45rem; }
</style>
</head>
<body>
<main class="doc">
<div class="doc-name">__NAME__</div>
__BODY__
<section class="comment-block">
<hr>
<textarea id="global" rows="3" placeholder="还有什么想说的？"></textarea>
</section>
</main>
<div class="actions">
<div class="actions-inner">
<button id="submit" type="button" aria-live="polite">提交答卷</button>
</div>
</div>
<script type="module">
(async function () {
  var targets = Array.prototype.slice.call(document.querySelectorAll('pre.mermaid'));
  if (!targets.length) { return; }
  try {
    var module = await import('https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs');
    var mermaid = module.default;
    mermaid.initialize({ startOnLoad: false, theme: 'neutral', securityLevel: 'strict' });
    for (var i = 0; i < targets.length; i += 1) {
      var el = targets[i];
      try {
        var result = await mermaid.render('mermaid-diagram-' + i, el.textContent);
        el.innerHTML = result.svg;
        el.classList.add('rendered');
      } catch (err) {
        el.classList.add('failed');
      }
    }
  } catch (err) {
    targets.forEach(function (el) { el.classList.add('failed'); });
  }
})();
</script>
<script>
(function () {
  var doc = document.querySelector('main.doc');
  if (!doc) { return; }
  var heads = Array.prototype.slice.call(doc.querySelectorAll('h1, h2, h3'));
  if (heads.length < 2) { return; }
  var wrap = document.createElement('aside');
  wrap.className = 'toc';
  var nav = document.createElement('nav');
  nav.setAttribute('aria-label', '目录');
  var list = document.createElement('ol');
  heads.forEach(function (head, i) {
    if (!head.id) { head.id = 'sec-' + (i + 1); }
    var li = document.createElement('li');
    var link = document.createElement('a');
    link.href = '#' + head.id;
    link.textContent = head.textContent.trim();
    link.className = 'lvl-' + head.tagName.charAt(1);
    li.appendChild(link);
    list.appendChild(li);
  });
  nav.appendChild(list);
  wrap.appendChild(nav);
  document.body.appendChild(wrap);

  var links = Array.prototype.slice.call(list.querySelectorAll('a'));
  var ticking = false;
  function sync() {
    ticking = false;
    var line = window.scrollY + 96;
    var current = 0;
    heads.forEach(function (head, i) {
      if (head.getBoundingClientRect().top + window.scrollY <= line) { current = i; }
    });
    if (window.innerHeight + window.scrollY >= document.documentElement.scrollHeight - 4) { current = heads.length - 1; }
    links.forEach(function (link, i) { link.classList.toggle('active', i === current); });
  }
  window.addEventListener('scroll', function () {
    if (!ticking) { ticking = true; requestAnimationFrame(sync); }
  }, { passive: true });
  window.addEventListener('resize', sync);
  sync();
})();
</script>
<script>
(function () {
  var button = document.getElementById('submit');
  button.addEventListener('click', async function () {
    var answers = [];
    document.querySelectorAll('section.qa').forEach(function (el) {
      var selected = [];
      if (el.dataset.type === 'checkbox') {
        el.querySelectorAll('input[type="checkbox"]:checked').forEach(function (input) {
          selected.push(input.value);
        });
      } else {
        var picked = el.querySelector('input:checked');
        if (picked) { selected = [picked.value]; }
      }
      answers.push({ block: el.dataset.qid, selected: selected, free: el.querySelector('textarea').value });
    });
    var payload = { answers: answers, global_comment: document.getElementById('global').value };
    button.disabled = true;
    button.className = '';
    button.textContent = '提交中…';
    try {
      var res = await fetch('/submit', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });
      if (!res.ok) { throw new Error('bad status'); }
      button.className = 'ok';
      button.textContent = '已提交，可以关闭本页。';
      document.querySelectorAll('textarea, input').forEach(function (el) { el.disabled = true; });
    } catch (e) {
      button.disabled = false;
      button.className = 'err';
      button.textContent = '提交失败，请重试。';
    }
  });
})();
</script>
</body>
</html>
"""

DONE_PAGE = """<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<title>答卷已提交</title>
<style>
* { box-sizing: border-box; }
body { margin: 0; display: flex; min-height: 100vh; align-items: center; justify-content: center; background: #f4f0e8; color: #26221b; font: 16px/1.85 system-ui, -apple-system, "Segoe UI", "PingFang SC", "Microsoft YaHei", sans-serif; }
div { text-align: center; padding: 2rem; }
svg { display: block; margin: 0 auto 1.25rem; }
h1 { font-size: 1.5rem; letter-spacing: -.015em; margin: 0 0 .5rem; }
p { color: #6d6455; margin: 0; }
</style>
</head>
<body>
<div>
<svg width="48" height="48" viewBox="0 0 48 48" fill="none" stroke="#b23c26" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="24" cy="24" r="21"/><path d="M15 24.5l6.5 6.5L33.5 17"/></svg>
<h1>答卷已提交</h1>
<p>可以关闭本标签页，答卷已写入磁盘。</p>
</div>
</body>
</html>
"""


def fence_close_re(fence):
    return re.compile(r"^ {0,3}" + re.escape(fence[0]) + "{" + str(len(fence)) + r",}\s*$")


def parse_option_line(line):
    match = OPTION_LINE_RE.match(line)
    if not match:
        return None
    text = match.group(3).strip()
    return {
        "id": match.group(2),
        "recommended": match.group(1).lower() == "x",
        "lines": [text] if text else [],
    }


def parse_choice_block(open_line, lang, body, issues, seen_ids):
    block = {"id": None, "type": BLOCK_LANGS[lang], "question": [], "options": [], "start": open_line, "end": open_line}
    head_line = None
    head_failed = False
    question_open = True
    current = None

    for lineno, raw in body:
        line = raw.rstrip()
        text = line.strip()
        if head_line is None:
            if not text:
                continue
            match = BLOCK_HEAD_RE.match(text)
            head_line = lineno
            if not match:
                head_failed = True
                issues.append((lineno, "问题块首行不是 `<id> 问题文本`", "首行写成 `<block-id> 问题文本`，如 `<answer-naming> 答卷文件怎么命名？`"))
                block["question"].append(text)
                continue
            block["id"] = match.group(1)
            rest = match.group(2).strip()
            if rest:
                block["question"].append(rest)
            continue
        option = parse_option_line(line)
        if option is not None:
            question_open = False
            option["line"] = lineno
            current = option
            block["options"].append(option)
            continue
        if re.match(r"^-\s*\[", line):
            issues.append((lineno, "选项行格式不合法", "写成 `- [ ] <选项id> 选项文本`；推荐项写 `- [x] <选项id> 选项文本`"))
            question_open = False
            current = None
            continue
        if not text:
            continue
        if question_open:
            block["question"].append(text)
        elif current is not None:
            current["lines"].append(text)

    if block["id"] is None and not head_failed:
        issues.append((open_line, "问题块缺少 `<id> 问题文本` 首行", "块首行写 `<block-id> 问题文本`"))
    elif block["id"] is not None:
        qid = block["id"]
        if qid in seen_ids:
            issues.append((head_line, "问题块 id `%s` 与第 %d 行重复" % (qid, seen_ids[qid]), "同一问卷内问题块 id 必须唯一，另取一个 id，如 `%s-2`" % qid))
        else:
            seen_ids[qid] = head_line
        if not block["question"]:
            issues.append((head_line, "问题文本为空", "在 `<id>` 之后写题面；题面可跨多行，直到第一个选项行"))

    option_ids = {}
    for option in block["options"]:
        opt_id = option["id"]
        lineno = option["line"]
        option["text"] = " ".join(option["lines"]).strip()
        option.pop("lines", None)
        if opt_id in option_ids:
            issues.append((lineno, "选项 id `%s` 在问题块内重复（另见第 %d 行）" % (opt_id, option_ids[opt_id]), "同一问题块内选项 id 必须唯一，改掉其中一个"))
        else:
            option_ids[opt_id] = lineno
        if not option["text"]:
            issues.append((lineno, "选项文本为空", "在 `<选项id>` 之后写选项文本；选项文本可跨多行"))

    if block["type"] == "yes-no":
        for option in block["options"]:
            if option["id"] not in ("yes", "no"):
                issues.append((option["line"], "yes-or-no 选项标签 `%s` 不合法" % option["id"], "yes-or-no 的选项只接受 `<yes>` 与 `<no>`，选项文本写在标签之后，如 `- [ ] <yes> 同意`"))
        if not block["options"]:
            block["options"] = [
                {"id": "yes", "text": "同意", "recommended": False},
                {"id": "no", "text": "驳回", "recommended": False},
            ]
    elif len(block["options"]) == 1:
        issues.append((block["options"][0]["line"], "选择题只有 1 个选项，校验不通过", "改成判断题 `yes-or-no`（把题面写成完整命题），或把同类问题合并为一道 `multi-choice` 多选题"))

    return block


def fence_hint(info):
    key = re.sub(r"[^a-z]", "", info.lower())
    if not key:
        return None
    for lang in sorted(BLOCK_LANGS):
        if re.sub(r"[^a-z]", "", lang) == key:
            return lang
    return None


def parse_blocks(text):
    lines = text.split("\n")
    blocks = []
    issues = []
    seen_ids = {}
    index = 0
    total = len(lines)
    while index < total:
        fence_match = FENCE_RE.match(lines[index])
        if not fence_match:
            index += 1
            continue
        fence = fence_match.group(2)
        info = fence_match.group(3).strip().split()[0].lower() if fence_match.group(3).strip() else ""
        closing = fence_close_re(fence)
        cursor = index + 1
        while cursor < total and not closing.match(lines[cursor]):
            cursor += 1
        closed = cursor < total
        end_line = cursor + 1 if closed else total
        if info in BLOCK_LANGS:
            body = [(number + 1, lines[number]) for number in range(index + 1, cursor if closed else total)]
            block = parse_choice_block(index + 1, info, body, issues, seen_ids)
            block["start"] = index + 1
            block["end"] = end_line
            blocks.append(block)
            if not closed:
                issues.append((index + 1, "问题块缺少闭合围栏", "在块末补上一行与开头相同的围栏"))
                break
        else:
            if not closed:
                issues.append((index + 1, "代码围栏缺少闭合", "在块末补上一行与开头相同的围栏；不补的话，本行之后的内容不会被当作问卷正文与问题块"))
                break
            hint = fence_hint(info)
            if hint:
                issues.append((index + 1, "围栏 `%s` 不是题型，整块按正文代码块处理" % info, "要让它成为问题块，围栏改成 `%s`" % hint))
        index = end_line
    if not blocks and not issues:
        issues.append((1, "问卷中没有可识别的问题块", "问题块用 ```single-choice、```multi-choice 或 ```yes-or-no 围栏，首行写 `<id> 问题文本`"))
    return blocks, issues


def load_questionnaire(path):
    qpath = Path(path)
    if not qpath.is_file():
        print("%s:1: 问卷文件不存在 \u2192 检查路径是否正确" % path)
        return None
    try:
        content = qpath.read_text(encoding="utf-8-sig")
    except UnicodeDecodeError:
        print("%s:1: 问卷不是 UTF-8 编码 \u2192 转存为 UTF-8 后重试" % path)
        return None
    content = content.replace("\r\n", "\n").replace("\r", "\n")
    blocks, issues = parse_blocks(content)
    if issues:
        issues.sort(key=lambda item: item[0])
        for line, message, fix in issues:
            print("%s:%d: %s \u2192 %s" % (path, line, message, fix))
        return None
    return blocks, content


def is_hr(text):
    return re.fullmatch(r"(?:-{3,}|\*{3,}|_{3,})", re.sub(r"\s+", "", text)) is not None


def render_link(text, url):
    if url.lower().startswith(("javascript:", "data:", "vbscript:")):
        return text
    return '<a href="%s" target="_blank" rel="noreferrer">%s</a>' % (url, text)


def inline(text):
    codes = []

    def stash(match):
        codes.append(match.group(1))
        return "\ue000%d\ue001" % (len(codes) - 1)

    out = CODE_SPAN_RE.sub(stash, text)
    out = html.escape(out)
    out = LINK_RE.sub(lambda match: render_link(match.group(1), match.group(2)), out)
    out = BOLD_RE.sub(r"<strong>\1</strong>", out)
    out = ITALIC_RE.sub(r"<em>\1</em>", out)
    out = UNDERSCORE_RE.sub(r"<em>\1</em>", out)
    out = re.sub(
        "\ue000(\\d+)\ue001",
        lambda match: "<code>%s</code>" % html.escape(codes[int(match.group(1))]),
        out,
    )
    return out


def is_block_start(line):
    text = line.strip()
    if not text:
        return True
    if FENCE_RE.match(line):
        return True
    if text[0] in "|>":
        return True
    return bool(HEADING_RE.match(text) or LIST_RE.match(line) or is_hr(text))


def render_markdown(lines):
    out = []
    index = 0
    total = len(lines)
    while index < total:
        line = lines[index]
        text = line.strip()
        if not text:
            index += 1
            continue
        fence_match = FENCE_RE.match(line)
        if fence_match:
            closing = fence_close_re(fence_match.group(2))
            cursor = index + 1
            body = []
            while cursor < total and not closing.match(lines[cursor]):
                body.append(lines[cursor])
                cursor += 1
            info = (fence_match.group(3).strip().split() or [""])[0].lower()
            if info == "mermaid":
                out.append('<pre class="mermaid">%s</pre>' % html.escape("\n".join(body)))
            else:
                out.append('<pre class="code"><code>%s</code></pre>' % html.escape("\n".join(body)))
            index = cursor + 1
            continue
        if text[0] == "|":
            body = []
            while index < total and lines[index].strip().startswith("|"):
                body.append(lines[index])
                index += 1
            out.append('<pre class="table"><code>%s</code></pre>' % html.escape("\n".join(body)))
            continue
        if is_hr(text):
            out.append("<hr>")
            index += 1
            continue
        heading = HEADING_RE.match(text)
        if heading:
            level = len(heading.group(1))
            out.append("<h%d>%s</h%d>" % (level, inline(heading.group(2)), level))
            index += 1
            continue
        if text[0] == ">":
            body = []
            while index < total and lines[index].strip().startswith(">"):
                body.append(re.sub(r"^\s*>\s?", "", lines[index]))
                index += 1
            out.append("<blockquote>%s</blockquote>" % render_markdown(body))
            continue
        list_match = LIST_RE.match(line)
        if list_match:
            ordered = list_match.group(1)[0].isdigit()
            items = []
            while index < total:
                item_match = LIST_RE.match(lines[index])
                if not item_match:
                    break
                items.append(item_match.group(2))
                index += 1
            tag = "ol" if ordered else "ul"
            out.append("<%s>%s</%s>" % (tag, "".join("<li>%s</li>" % inline(item) for item in items), tag))
            continue
        paragraph = []
        while index < total and not is_block_start(lines[index]):
            paragraph.append(lines[index].strip())
            index += 1
        if not paragraph:
            index += 1
            continue
        out.append("<p>%s</p>" % inline(" ".join(paragraph)))
    return "\n".join(out)


def render_widget(block, position):
    qid = block.get("id") or ""
    qtype = block.get("type") or "radio"
    options = block.get("options") or []
    escaped_id = html.escape(qid, quote=True)
    parts = [
        '<section class="qa" data-qid="%s" data-type="%s" role="group" aria-label="第 %d 题">' % (escaped_id, html.escape(qtype, quote=True), position + 1),
    ]
    question = render_markdown(block.get("question") or [])
    if question:
        parts.append('<div class="qa-question">%s</div>' % question)
    if options:
        input_type = "radio" if qtype in ("radio", "yes-no") else "checkbox"
        for opt in options:
            parts.append(render_choice(input_type, qid, opt["id"], opt["text"], opt["recommended"]))
    parts.append(
        '<textarea class="free" rows="2" placeholder="%s"></textarea>'
        % ("补充（可选）" if options else "作答（可选）")
    )
    parts.append("</section>")
    return "\n".join(parts)


def render_choice(input_type, qid, opt_id, opt_text, recommended=False):
    return (
        '<label class="opt"><input type="%s" name="%s" value="%s">'
        '<span class="opt-text%s">%s</span></label>'
        % (
            input_type,
            html.escape("q-" + qid, quote=True),
            html.escape(opt_id, quote=True),
            " rec" if recommended else "",
            inline(opt_text),
        )
    )


def render_page(content, blocks):
    lines = content.split("\n")
    parts = []
    position = 0
    for index, block in enumerate(blocks):
        parts.append(render_markdown(lines[position:block["start"] - 1]))
        parts.append(render_widget(block, index))
        position = block["end"]
    parts.append(render_markdown(lines[position:]))
    return "\n".join(part for part in parts if part)


def build_page(name, content, blocks):
    return PAGE_TEMPLATE.replace("__NAME__", html.escape(name)).replace("__BODY__", render_page(content, blocks))


def normalize_answers(blocks, payload):
    submitted = {}
    raw = payload.get("answers")
    if isinstance(raw, list):
        for item in raw:
            if isinstance(item, dict) and isinstance(item.get("block"), str):
                submitted[item["block"]] = item
    answers = []
    for block in blocks:
        item = submitted.get(block["id"]) or {}
        allowed = [opt["id"] for opt in block["options"]]
        chosen = item.get("selected")
        selected = []
        if isinstance(chosen, list):
            for value in chosen:
                if value in allowed and value not in selected:
                    selected.append(value)
        if block["type"] in ("radio", "yes-no") and len(selected) > 1:
            selected = selected[:1]
        free = item.get("free")
        answers.append({
            "block": block["id"],
            "selected": selected,
            "free": free if isinstance(free, str) else "",
        })
    return answers


def write_answers(qpath, answers, global_comment):
    stem = re.escape(qpath.stem)
    stamp = time.strftime("%Y%m%d-%H%M%S")
    base = "%s.answers.%s" % (qpath.stem, stamp)
    target = qpath.parent / (base + ".json")
    if target.exists():
        serial = re.compile(r"^" + stem + r"\.answers\." + re.escape(stamp) + r"\.(\d+)\.json$")
        numbers = []
        for entry in qpath.parent.iterdir():
            match = serial.match(entry.name)
            if match and entry.is_file():
                numbers.append(int(match.group(1)))
        index = max(numbers) + 1 if numbers else 1
        while True:
            target = qpath.parent / ("%s.%03d.json" % (base, index))
            if not target.exists():
                break
            index += 1
    data = {
        "questionnaire": str(qpath.resolve()),
        "answers": answers,
        "global_comment": global_comment,
    }
    target.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return target


def cmd_validate(path):
    loaded = load_questionnaire(path)
    if loaded is None:
        return 1
    blocks, _ = loaded
    print("OK: %d 题" % len(blocks))
    return 0


def cmd_show(path):
    loaded = load_questionnaire(path)
    if loaded is None:
        return 1
    blocks, content = loaded
    qpath = Path(path)
    page = build_page(qpath.name, content, blocks).encode("utf-8")
    state = {}
    payload_ready = threading.Event()

    class Handler(BaseHTTPRequestHandler):
        def _send(self, status, body, content_type="text/html; charset=utf-8"):
            data = body if isinstance(body, bytes) else body.encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(data)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(data)

        def do_GET(self):
            if self.path in ("/", "/index.html"):
                self._send(200, page)
            else:
                self._send(404, "not found", "text/plain; charset=utf-8")

        def do_POST(self):
            if self.path != "/submit":
                self._send(404, "not found", "text/plain; charset=utf-8")
                return
            try:
                length = int(self.headers.get("Content-Length") or 0)
            except ValueError:
                length = 0
            raw = self.rfile.read(length) if length > 0 else b""
            try:
                payload = json.loads(raw.decode("utf-8"))
            except (UnicodeDecodeError, ValueError):
                payload = None
            if not isinstance(payload, dict):
                self._send(400, "invalid payload", "text/plain; charset=utf-8")
                return
            state["payload"] = payload
            self._send(200, DONE_PAGE)
            payload_ready.set()

        def log_message(self, *args):
            pass

    try:
        server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    except OSError as error:
        print("%s:1: 无法启动本地服务（%s） \u2192 检查本机端口占用后重试" % (path, error))
        return 1

    url = "http://127.0.0.1:%d/" % server.server_port
    serving = threading.Thread(target=server.serve_forever, daemon=True)
    serving.start()
    try:
        opened = False
        try:
            opened = webbrowser.open(url)
        except Exception:
            opened = False
        if opened:
            print("问卷已就绪：%s" % url, flush=True)
        else:
            print("浏览器未能自动打开，请手动访问：%s" % url, flush=True)
        try:
            payload_ready.wait()
        except KeyboardInterrupt:
            print("已中断，未写答卷。", flush=True)
            return 130
    finally:
        server.shutdown()
        server.server_close()

    payload = state["payload"]
    answers = normalize_answers(blocks, payload)
    global_comment = payload.get("global_comment")
    target = write_answers(qpath, answers, global_comment if isinstance(global_comment, str) else "")
    print(str(target), flush=True)
    return 0


def quote_lines(prefix, value):
    parts = value.split("\n")
    lines = [("> " + prefix + parts[0]).rstrip()]
    for extra in parts[1:]:
        lines.append(("> " + extra).rstrip() if extra else ">")
    return lines


def option_label(block, opt_id):
    for opt in block["options"]:
        if opt["id"] == opt_id:
            return opt["text"]
    return opt_id


def render_answer(block, answer):
    if answer is None:
        body = ["> 未答"]
    else:
        selected = answer["selected"]
        free = answer["free"].strip()
        if selected:
            labels = "；".join(option_label(block, opt_id) for opt_id in selected)
            body = quote_lines("选：", labels)
            if free:
                body.extend(quote_lines("补充：", free))
        elif free:
            body = quote_lines("答：", free)
        else:
            body = ["> 未答"]
    question = list(block.get("question") or [])
    if not question:
        return body
    return question + [""] + body


def check_answers(blocks, data):
    issues = []
    by_id = {block["id"]: block for block in blocks}
    raw = data.get("answers")
    if not isinstance(raw, list):
        return [(1, "答卷缺少 `answers` 数组", "答卷需含 `answers` 数组，每项形如 `{\"block\": \"\u2026\", \"selected\": [], \"free\": \"\"}`")]
    seen = {}
    for index, item in enumerate(raw):
        if not isinstance(item, dict) or not isinstance(item.get("block"), str):
            issues.append((1, "`answers` 第 %d 项缺少字符串 `block`" % (index + 1), "每项必须有 `block`，值为问卷中的问题块 id"))
            continue
        qid = item["block"]
        if qid in seen:
            issues.append((1, "答卷重复记录问题块 `%s`" % qid, "每个问题块只保留一条 `answers` 记录"))
            continue
        seen[qid] = True
        block = by_id.get(qid)
        if block is None:
            issues.append((
                1,
                "答卷引用的问题块 `%s` 不在问卷中" % qid,
                "检查 id 拼写；若问卷在作答后被编辑，重新运行 show 生成答卷",
            ))
            continue
        selected = item.get("selected")
        if not isinstance(selected, list) or any(not isinstance(value, str) for value in selected):
            issues.append((1, "问题块 `%s` 的 `selected` 不是选项 id 数组" % qid, "`selected` 写选项 id 字符串数组，未选则写 `[]`"))
            continue
        allowed = [opt["id"] for opt in block["options"]]
        if not allowed and selected:
            issues.append((
                1,
                "问题块 `%s` 是开放题，答卷却记录了选项 %s" % (qid, "、".join("`%s`" % value for value in selected)),
                "开放题的 `selected` 只能为空数组，作答内容写进 `free`",
            ))
        else:
            for value in selected:
                if value not in allowed:
                    issues.append((
                        1,
                        "问题块 `%s` 引用了不存在的选项 `%s`" % (qid, value),
                        "改为问卷中该块的选项 id；问卷改动后需重新作答",
                    ))
        if block["type"] in ("radio", "yes-no") and len(selected) > 1:
            issues.append((
                1,
                "问题块 `%s` 是单选题，答卷记录了 %d 个选项" % (qid, len(selected)),
                "单选只保留一个选项 id",
            ))
        if not isinstance(item.get("free", ""), str):
            issues.append((1, "问题块 `%s` 的 `free` 不是字符串" % qid, "`free` 写自由输入文本，没有则写空串"))
    return issues


def cmd_assemble(path):
    answers_path = Path(path)
    if not answers_path.is_file():
        print("%s:1: 答卷文件不存在 \u2192 检查路径，或先运行 show 生成答卷" % path)
        return 1
    try:
        raw = answers_path.read_text(encoding="utf-8-sig")
        data = json.loads(raw)
    except UnicodeDecodeError:
        print("%s:1: 答卷不是 UTF-8 编码 \u2192 转存为 UTF-8 后重试" % path)
        return 1
    except ValueError as error:
        print("%s:1: 答卷不是合法 JSON（%s） \u2192 修正 JSON 语法后重试" % (path, error))
        return 1
    if not isinstance(data, dict):
        print("%s:1: 答卷顶层不是对象 \u2192 答卷需为含 `questionnaire`/`answers`/`global_comment` 的 JSON 对象" % path)
        return 1

    name = data.get("questionnaire")
    if not isinstance(name, str) or not name.strip():
        print("%s:1: 答卷缺少 `questionnaire` 问卷路径 \u2192 在答卷中写入问卷路径，如 `docs/release-plan.md`" % path)
        return 1
    qpath = Path(name)
    candidates = [qpath]
    if not qpath.is_absolute():
        candidates.append(answers_path.parent / qpath)
    candidates.append(answers_path.parent / qpath.name)
    found = next((candidate for candidate in candidates if candidate.is_file()), None)
    if found is None:
        print("%s:1: 按答卷记录的问卷路径 `%s` 找不到问卷 \u2192 检查路径；找不到时会在答卷同目录找同名文件" % (path, name))
        return 1
    qpath = found
    try:
        content = qpath.read_text(encoding="utf-8-sig").replace("\r\n", "\n").replace("\r", "\n")
    except UnicodeDecodeError:
        print("%s:1: 问卷不是 UTF-8 编码 \u2192 转存为 UTF-8 后重试" % path)
        return 1
    blocks, parse_issues = parse_blocks(content)
    if parse_issues:
        parse_issues.sort(key=lambda item: item[0])
        for line, message, fix in parse_issues:
            print("%s:%d: %s \u2192 %s" % (qpath, line, message, fix))
        return 1

    issues = check_answers(blocks, data)
    if issues:
        for line, message, fix in issues:
            print("%s:%d: %s \u2192 %s" % (path, line, message, fix))
        return 1

    answers = {}
    for item in data["answers"]:
        answers[item["block"]] = {
            "selected": item["selected"],
            "free": item.get("free", ""),
        }

    lines = content.split("\n")
    output = []
    position = 0
    for block in blocks:
        output.extend(lines[position:block["start"] - 1])
        output.extend(render_answer(block, answers.get(block["id"])))
        position = block["end"]
    output.extend(lines[position:])
    text = "\n".join(output).rstrip("\n")

    comment = data.get("global_comment")
    if isinstance(comment, str) and comment.strip():
        text += "\n\n---\n\n**总评**\n\n" + comment.strip()
    sys.stdout.write(text + "\n")
    return 0


def main(argv=None):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(prog="multi_ask", description="问卷校验、答卷收集与拼装")
    subparsers = parser.add_subparsers(dest="command", required=True)
    descriptions = {
        "validate": "校验问卷",
        "show": "打开交互页收集答卷",
        "assemble": "按答卷拼装文档",
    }
    for name, description in descriptions.items():
        command = subparsers.add_parser(name, help=description)
        command.add_argument("path", help="问卷 markdown 或答卷 JSON 的路径")
    args = parser.parse_args(argv)
    if args.command == "validate":
        return cmd_validate(args.path)
    if args.command == "show":
        return cmd_show(args.path)
    return cmd_assemble(args.path)


if __name__ == "__main__":
    sys.exit(main())
