# Basic Agent

The basic module is the first learning layer.

Flow:

    User input -> Tool Manager -> deterministic tool result
              or -> LLM -> conversational response

Tools include current time, dice, secure password generation, and local text-file reading.

Run:

    uv run ai-basic

This layer makes the primitives visible before introducing agent frameworks.