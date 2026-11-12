
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / "ai-product-designer"
SKILL_FILE = SKILL_DIR / "SKILL.md"
REFERENCES_DIR = SKILL_DIR / "references"

errors = []
warnings = []


def check(condition, message):
    if condition:
        print(f"PASS: {message}")
    else:
        errors.append(message)
        print(f"FAIL: {message}")


print("\nAI PRODUCT DESIGNER SKILL VALIDATION")
print("=" * 45)

# 1. Check required files
check((ROOT / "README.md").is_file(), "README.md exists")
check((ROOT / "LICENSE").is_file(), "LICENSE exists")
check(SKILL_FILE.is_file(), "SKILL.md exists")
check(REFERENCES_DIR.is_dir(), "References directory exists")

# 2. Check SKILL.md content
if SKILL_FILE.is_file():
    content = SKILL_FILE.read_text(encoding="utf-8")

    # Frontmatter
    frontmatter = re.match(
        r"\A---\s*\n(.*?)\n---\s*\n",
        content,
        re.DOTALL
    )

    check(frontmatter is not None, "Valid frontmatter delimiters")

    if frontmatter:
        metadata = frontmatter.group(1)

        name = re.search(r"(?m)^name:\s*\S+", metadata)
        description = re.search(
            r"(?m)^description:\s*.+",
            metadata
        )

        check(name is not None, "Skill name is defined")
        check(description is not None, "Skill description is defined")

    check(len(content.strip()) > 1000, "SKILL.md has substantial content")

    # 3. Check references linked in SKILL.md
    links = re.findall(
        r"\[[^\]]+\]\(([^)]+)\)",
        content
    )

    local_links = [
        link for link in links
        if not link.startswith(("http://", "https://", "mailto:", "#"))
    ]

    for link in local_links:
        target = (SKILL_DIR / link.split("#")[0]).resolve()

        check(
            target.is_relative_to(SKILL_DIR.resolve()) and target.is_file(),
            f"Reference link exists: {link}"
        )

# 4. Check reference documents
if REFERENCES_DIR.is_dir():
    reference_files = list(REFERENCES_DIR.rglob("*.md"))

    check(
        len(reference_files) > 0,
        "At least one Markdown reference document exists"
    )

    for file in reference_files:
        check(
            file.stat().st_size > 0,
            f"Reference is not empty: {file.relative_to(ROOT)}"
        )

# 5. Final report
print("\n" + "=" * 45)
print(f"Errors: {len(errors)}")
print(f"Warnings: {len(warnings)}")

if errors:
    print("\nVALIDATION FAILED")
    sys.exit(1)

print("\nVALIDATION PASSED")
sys.exit(0)
