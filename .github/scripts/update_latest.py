"""Rewrite the LATEST block in README.md with the most recent commit
across the shipped repos below. Run by .github/workflows/latest.yml on a
daily schedule. No external services -- just the public GitHub REST API,
stdlib only.
"""

from __future__ import annotations

import json
import re
import urllib.request
from pathlib import Path
from typing import TypedDict

REPOS = [
    "bradsward/mekiki",
    "bradsward/greenlight",
    "bradsward/hirogari",
    "saykai-systems/saykai-action",
]


class LatestCommit(TypedDict):
    repo: str
    message: str
    date: str
    sha: str


def latest_commit(repo: str) -> LatestCommit:
    url = f"https://api.github.com/repos/{repo}/commits?per_page=1"
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "bradsward-profile-readme",
        },
    )
    with urllib.request.urlopen(request, timeout=15) as response:
        data = json.load(response)
    commit = data[0]["commit"]
    return {
        "repo": repo.split("/")[-1],
        "message": commit["message"].splitlines()[0],
        "date": commit["committer"]["date"],
        "sha": data[0]["sha"][:7],
    }


def main() -> None:
    commits = [latest_commit(repo) for repo in REPOS]
    newest = max(commits, key=lambda c: c["date"])
    line = f"{newest['sha']}  {newest['message']}  ({newest['repo']})"

    readme = Path("README.md")
    text = readme.read_text(encoding="utf-8")
    block = (
        "<!-- LATEST:START -->\n"
        "```\n"
        "$ git log -1 --oneline --all-repos\n"
        f"{line}\n"
        "```\n"
        "<!-- LATEST:END -->"
    )
    new_text = re.sub(
        r"<!-- LATEST:START -->.*?<!-- LATEST:END -->",
        block,
        text,
        flags=re.DOTALL,
    )
    if new_text != text:
        readme.write_text(new_text, encoding="utf-8")
        print(f"updated: {line}")
    else:
        print("no change")


if __name__ == "__main__":
    main()
