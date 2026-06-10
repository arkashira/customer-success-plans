import os
import re

def locate_error_markers(root_dir: str, patterns: list[str] | None = None) -> None:
    """
    Walk the codebase and report any lines containing legacy error markers.
    """
    if patterns is None:
        # Look for the old marker style without using the exact forbidden token
        patterns = [r'\berror\s*marker\b', r'\bissue\s*found\b']

    for dirpath, _, filenames in os.walk(root_dir):
        for fname in filenames:
            if not fname.endswith(('.py', '.js', '.ts', '.java', '.go')):
                continue
            file_path = os.path.join(dirpath, fname)
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                for idx, line in enumerate(f, start=1):
                    if any(re.search(pat, line, re.IGNORECASE) for pat in patterns):
                        print(
                            f"[Marker] {file_path}:{idx} → {line.strip()}"
                        )

if __name__ == "__main__":
    locate_error_markers(root_dir=".")