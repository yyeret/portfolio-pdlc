# Coding-agent configuration as a harness

Assess **the effective instruction and tool path for one agent, working directory, and task class**. An instruction file alone is not the harness. Reconstruct the hierarchy, installed skills/plugins/commands, hooks/checks, and what actually triggers them. If possible, use the agent's own context/config inspection command to confirm loaded files without running a task. Treat hidden system instructions and model behavior as Unknown unless documented by the vendor.

| Layer | Question |
|---|---|
| Vendor baseline | What does this installed version do without custom files? Use current official documentation or local product code; distinguish general coding capability from a required PDLC workflow. |
| Organization/user | Which managed and home-level instructions, settings, skills, hooks, plugins, and tools are enabled? Which are only present on disk? |
| Repo/ancestor | Which instruction files apply at the chosen working directory? Follow documented precedence and imports. |
| Task/path | Which nested rule, command, skill, workflow profile, or runtime selection is triggered for this task? |
| Output/run evidence | Does a sample run show the documented behavior? This corroborates configuration but is not required for a white-box score. |

Use separate columns for **baseline**, **added by configuration**, **not reached/optional**, and **Unknown**. Attribute each finding to the narrowest active layer. A user rule that says “run tests” does not prove the agent ran them; a hook that executes a check and blocks completion is stronger evidence than prose. A built-in code-edit/test loop does not imply discovery, product validation, or a compounding meta-loop.

When only one layer is supplied, you may score that **layer's documented task path** if its owner files and completion boundary are inspectable. Put “repo overlay only” (or the analogous layer) in the chart title and verdict. Leave the **effective-installation score Unknown** until missing baseline, higher-priority overrides, runtime activation, and relevant tools are checked. A zero on the bounded layer means no connected mechanism in its inspected owner path; it does not mean the full agent lacks one.

## Official starting points (verify freshness at assessment time)

- **Codex:** [OpenAI AGENTS.md guide](https://developers.openai.com/codex/guides/agents-md) and the installed Codex configuration/skill documentation. Check global, ancestor, repo and nested instruction files, override/fallback behavior, enabled skills, and active tools. Do not assume every available skill was invoked.
- **Claude Code:** [Claude memory and instruction files](https://code.claude.com/docs/en/memory) and [settings precedence](https://code.claude.com/docs/en/settings). Check managed, user, project, local, nested and imported instructions; current documentation also describes AGENTS.md support. Check skills, rules, hooks and settings separately from CLAUDE.md prose. Use `/context` or the current equivalent when available to confirm loading.
- **Gemini CLI:** [GEMINI.md context hierarchy](https://geminicli.com/docs/cli/gemini-md/) and [configuration](https://geminicli.com/docs/reference/configuration/). Check global, workspace/ancestor and just-in-time context, configured alternate filenames/imports, commands and tools. Use `/memory show` or the current equivalent when available to confirm effective context.

Vendor behavior and paths change. Refresh official docs for the specific installed version; cite the exact page and access date. If the agent is not installed or its config cannot be read, assess only the supplied files and label the effective-path inference provisional. Do not claim one agent is “PDLC-ready out of the box” from general tool availability or marketing examples.
