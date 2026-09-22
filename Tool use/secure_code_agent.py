import re

def is_code_safe(code_string: str) -> bool:
    # Look for risky modules or system execution patterns
    dangerous_patterns = [
        r"\bimport\s+os\b", r"\bfrom\s+os\b",
        r"\bimport\s+subprocess\b", r"\bfrom\s+subprocess\b",
        r"\bimport\s+sys\b", r"\bfrom\s+sys\b",
        r"\bimport\s+shutil\b",
        r"\bexec\b", r"\beval\b", r"\b__import__\b",
        r"\bopen\b", r"\bbuiltins\b"
    ]
    
    for pattern in dangerous_patterns:
        if re.search(pattern, code_string):
            return False # Contains prohibited dangerous command
            
    return True
