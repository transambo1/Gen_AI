def generate_lab41_prompt():
    context = "CONTEXT: You will be provided with PyCharm GUI steps enclosed with {{{ STEPS }}} to execute a process enclosed with {{{ PROCESS }}}."
    task = "TASK: Convert the steps to CLI commands."

    process = "Commit and push files to a remote git branch"
    steps = [
        "1. Review changed files",
        "2. Stage the desired files",
        "3. Add a commit message",
        "4. Commit the files",
        "5. Validate branch name",
        "6. Push the changes to the remote branch"
    ]

    # Cấu trúc Prompt vật lý theo quy tắc 5S
    full_prompt = f"""
{context}
{task}

PROCESS: {{{{{ {process} }}}}}

STEPS: {{{{{
    {chr(10).join(steps)}
    }}}}}

CLI COMMANDS:
    """
    return full_prompt

if __name__ == "__main__":
    print("--- GENERATING IMPROVED PROMPT FOR LAB 4.1 ---")
    print(generate_lab41_prompt())