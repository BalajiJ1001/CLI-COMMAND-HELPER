def extract_command(output):
    lines = output.split("\n")

    for i, line in enumerate(lines):
        if "command" in line.lower():
            parts = line.split(":", 1)

            if len(parts) > 1 and parts[1].strip():
                return parts[1].strip().strip("`")

            if i + 1 < len(lines):
                return lines[i + 1].strip().strip("`")

    return None
