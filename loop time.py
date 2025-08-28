#!/usr/bin/env python3
"""
LoopTime – A cute Python time-complexity guesser 🐣✨
--------------------------------------------------
Paste a short Python snippet and I'll make a best-effort guess at its
asymptotic time complexity (Big-O). This is heuristic (not a full parser!),
so treat results as guidance for learning.

Features
- Detects nested loops → O(n), O(n^2), O(n^3) …
- Detects typical logarithmic loops (n//=2, while hi-lo binary search) → O(log n)
- Detects simple recursion and multiplicative branching → O(n), O(2^n), O(b^d)
- Detects sorting calls (sorted, .sort) → O(n log n)
- Prints a tiny ASCII growth chart so it's ✨aesthetic✨

Usage
$ python loop_time_analyzer.py
(paste code) … then press Ctrl+D (Linux/Mac) or Ctrl+Z then Enter (Windows)
"""
from __future__ import annotations
import re
import sys
from collections import defaultdict

# ------------------------- Helpers -------------------------
LOOP_RE = re.compile(r"^\s*(for\s+|while\s+)")
DIV2_RE = re.compile(r"n\s*//=\s*2|n\s*/=\s*2|>>=\s*1")
SORT_RE = re.compile(r"\.sort\(|sorted\(")
FUNC_DEF_RE = re.compile(r"^\s*def\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(")
CALL_RE_TMPL = r"(?<!def\s)\b{name}\s*\("
BINARY_SEARCH_HINTS = ("low", "high", "mid", "left", "right")

ANSI = {
    "pink": "\033[95m",
    "blue": "\033[94m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "bold": "\033[1m",
    "reset": "\033[0m",
}

# ---------------------- Core analysis ----------------------

def estimate_nested_loops(lines: list[str]) -> int:
    """Return max loop nest depth based on indentation levels."""
    stack = []  # (indent, is_loop)
    max_depth = 0
    for line in lines:
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip(" "))
        # pop to current indent
        while stack and stack[-1][0] >= indent:
            stack.pop()
        is_loop = bool(LOOP_RE.match(line))
        stack.append((indent, is_loop))
        # compute depth counting only loops in the stack
        depth = sum(1 for _, is_lp in stack if is_lp)
        max_depth = max(max_depth, depth)
    return max_depth


def has_log_loop(code: str) -> bool:
    # divide-by-two loop or binary-search style
    if DIV2_RE.search(code):
        return True
    # heuristic: while and mentions of low/high/mid
    if "while" in code and sum(h in code for h in BINARY_SEARCH_HINTS) >= 2:
        return True
    return False 



def detect_recursion(code: str) -> tuple[bool, int]:
    """Return (is_recursive, branching_factor)."""
    func_names = FUNC_DEF_RE.findall(code)
    is_recursive = False
    calls = 0
    for name in func_names:
        if re.search(CALL_RE_TMPL.format(name=re.escape(name)), code):
            is_recursive = True
            # very rough: count occurrences to guess branching
            calls += len(re.findall(CALL_RE_TMPL.format(name=re.escape(name)), code))
    # branching factor estimate (>=2 suggests exponential)
    b = 1
    if is_recursive:
        b = max(1, calls // max(1, len(func_names)))
    return is_recursive, b


def guess_complexity(code: str) -> str:
    lines = code.splitlines()
    depth = estimate_nested_loops(lines)
    recursive, branch = detect_recursion(code)
    uses_sort = bool(SORT_RE.search(code))

    # Sorting usually dominates
    if uses_sort:
        return "O(n log n)"

    # Exponential recursion (e.g., fib naive)
    if recursive and branch >= 2:
        return "O(b^n) ~ exponential"

    # Linear recursion
    if recursive and branch == 1:
        return "O(n)"

    # Log loops
    if has_log_loop(code):
        if depth >= 1:
            return "O(n log n)"  # loop + log loop → n log n
        return "O(log n)"

    # Pure loops by nesting depth
    if depth == 0:
        return "O(1)"
    if depth == 1:
        return "O(n)"
    if depth == 2:
        return "O(n^2)"
    if depth == 3:
        return "O(n^3)"
    return f"O(n^{depth})"

# ---------------------- Cute chart -------------------------

def tiny_chart(label: str) -> str:
    sizes = [2, 4, 8, 16, 32]
    def f(n):
        if "log" in label:
            import math
            return max(1, int(math.log2(n)))
        if "n^2" in label:
            return n*n
        if "n^3" in label:
            return n*n*n
        if "b^n" in label:
            return 2**(len(bin(n))-3)  # very rough
        if "O(1)" in label:
            return 1
        return n
    bars = []
    for n in sizes:
        val = f(n)
        bars.append(f"n={n:>2}: " + "▮" * max(1, int(val)))
    return "\n".join(bars)

# ------------------------- Main ----------------------------

def main():
    print(ANSI["bold"] + "LoopTime (Python)" + ANSI["reset"], "🐥💫")
    print("Paste your Python code below. End input with Ctrl+D (mac/Linux) or Ctrl+Z then Enter (Windows).\n")
    code = sys.stdin.read()
    if not code.strip():
        print("No code provided. Bye! ✨")
        return
    guess = guess_complexity(code)
    palette = ["pink", "blue", "green", "yellow"]
    color = ANSI[palette[hash(guess)%len(palette)]]
    print(f"\nResult: {color}{ANSI['bold']}⏳ Time Complexity ≈ {guess}{ANSI['reset']}")
    print("\nMini growth chart (bigger bar = more work):")
    print(tiny_chart(guess))
    print("\nNote: This is a friendly heuristic, not a formal proof. Keep learning & stay curious! ✨🧠")

if __name__ == "__main__":
    main()
