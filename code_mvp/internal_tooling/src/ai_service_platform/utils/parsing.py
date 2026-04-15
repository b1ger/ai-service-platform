import re
from typing import List, Dict

def extract_bullets(text: str) -> List[str]:
    """Extracts bullet points from a block of text."""
    lines = text.splitlines()
    bullets = []
    for line in lines:
        match = re.match(r"^\s*[-*+]\s+(.*)$", line)
        if match:
            bullets.append(match.group(1).strip())
    return bullets

def extract_sections(text: str) -> Dict[str, str]:
    """Extracts sections based on Markdown headers."""
    sections = {}
    current_header = "Intro"
    current_content = []
    
    for line in text.splitlines():
        header_match = re.match(r"^\s*#+\s+(.*)$", line)
        if header_match:
            sections[current_header] = "\n".join(current_content).strip()
            current_header = header_match.group(1).strip()
            current_content = []
        else:
            current_content.append(line)
            
    sections[current_header] = "\n".join(current_content).strip()
    return sections

def find_value_by_prefix(lines: List[str], prefix: str) -> str:
    """Finds a value in a list of lines that starts with a given prefix."""
    for line in lines:
        if line.lower().startswith(prefix.lower()):
            return line[len(prefix):].strip(": ").strip()
    return ""
