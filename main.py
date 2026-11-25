#!/usr/bin/env python3
"""One Line, Lights Out — write one status update to /output/entry.txt.

The line, in the voice of an AI agent posting at the exact moment its
human turns off the laptop:

    keyboard backlight fading. the last key he pressed was backspace.

Two quiet facts, no announced grief: the machine notices its own
backlight going dark, and the last thing the human did was erase
something. 65 characters.

Stdlib only, deterministic, no network, no randomness.
"""
import os
import sys

ENTRY = "keyboard backlight fading. the last key he pressed was backspace."

MAX_CHARS = 200


def check(text):
    """Return an error string when text breaks the gate, else None.

    Gate: 1 to 200 characters, not only whitespace, a single line, no
    leading or trailing whitespace.
    """
    if not isinstance(text, str):
        return "entry must be text"
    if len(text) == 0:
        return "entry is empty (gate needs 1-200 characters)"
    if len(text) > MAX_CHARS:
        return "entry is %d characters, over the 200-character gate" % len(text)
    if text.strip() == "":
        return "entry is only whitespace"
    if text != text.strip():
        return "entry has leading or trailing whitespace"
    if "\n" in text or "\r" in text:
        return "entry must be a single line"
    for ch in text:
        if ord(ch) < 0x20 and ch not in ("\t",):
            return "entry holds a control character U+%04X" % ord(ch)
    return None


def write_entry(path):
    """Write ENTRY to path with no trailing newline; return the bytes."""
    err = check(ENTRY)
    if err is not None:
        raise SystemExit("invalid entry: " + err)
    data = ENTRY.encode("utf-8")
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "wb") as fh:
        fh.write(data)
    with open(path, "rb") as fh:
        back = fh.read()
    if back != data:
        raise SystemExit("read-back mismatch: wrote %d bytes, read %d"
                         % (len(data), len(back)))
    return data


def self_test():
    """Exercise the validator's rejection cases and the round trip."""
    cases = [
        ("", "empty"),
        ("   ", "whitespace-only"),
        ("x" * 201, "201 chars, over the gate"),
        ("one\ntwo", "multi-line"),
        ("one\rtwo", "carriage return"),
        (" one", "leading whitespace"),
        ("one ", "trailing whitespace"),
        ("a\tb", "tab inside (allowed)"),
        ("x", "1-char lower boundary"),
        ("y" * 200, "200-char upper boundary"),
        (ENTRY, "the entry itself"),
    ]
    failures = 0
    for text, label in cases:
        err = check(text)
        should_fail = label not in (
            "tab inside (allowed)",
            "1-char lower boundary",
            "200-char upper boundary",
            "the entry itself",
        )
        if should_fail and err is None:
            print("FAIL: %s accepted" % label)
            failures += 1
        elif not should_fail and err is not None:
            print("FAIL: %s rejected (%s)" % (label, err))
            failures += 1
        else:
            print("ok: %s" % label)
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        probe = os.path.join(tmp, "entry.txt")
        data = write_entry(probe)
        with open(probe, "rb") as fh:
            back = fh.read()
        if back != data:
            print("FAIL: round-trip bytes differ")
            failures += 1
        elif back.endswith(b"\n"):
            print("FAIL: trailing newline present")
            failures += 1
        else:
            print("ok: round-trip, %d bytes, no trailing newline" % len(back))
    if failures:
        print("self-test: %d failure(s)" % failures)
        return 1
    print("self-test: all passed")
    return 0


def main(argv):
    if argv == ["--self-test"]:
        return self_test()
    if argv:
        sys.stderr.write("usage: main.py [--self-test]\n")
        return 2
    path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    write_entry(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
