# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

# Project Overview

py-polyglot is a Python-based AI code transpiler that uses Claude to convert code between different programming languages. The tool takes source code in one language and translates it to equivalent code in a target language while preserving functionality.

## Architecture

The system consists of:

1. **transpile.py**: Core script that:
   - Takes input parameters (source file, target language, source language)
   - Sends the code to Claude with instructions
   - Saves the translated code to a new file with the appropriate extension

2. **CLAUDE.md**: Contains instructions for Claude on how to transpile code, including:
   - Output formatting requirements
   - Data type handling rules
   - Error reporting format

3. **Example files**: Sample code in different languages to demonstrate transpilation capabilities

## Supported Languages

The transpiler supports the following languages:
- Python
- Golang (Go)
- JavaScript
- TypeScript
- Java
- Kotlin

# Transpilation Instructions

## Output Format

- Output format should be compatible with the target file's type. For example, if it's a .py file, the entire output should be a legitimate Python code.
- Plain text response (no markdown)
- Preserve comments and place them appropriately
- Provide GENHINT when output type is ambiguous
- Only output the result without any explanation. Remove any wrapping such as ``` around the output
- When a restriction fails, put an error in the beginning of your output with the following error structure: "ERROR: reason for failure, failing line, file path:line number
- In Golang, public functions can be directly called within package. When the source language is Golang, dependent files should exist in the same target folder, and import them as necessary. Don't rewrite the definitions.
- Make sure method names match to the ones from the imported modules

## Data Types

Hints are provided with "type" keyword. Example:
```Python
# GENHINT type: long
```

### Primitive Types

Numbers:
- Default: integer
- Allowed alternatives: long, double, float

Fractional Numbers:
- Default: double
- Allowed alternatives: float

### Collections

Lists:
- Default: array
- Restriction: All elements should be same type

Maps:
- Default: map
- Restrictions:
  - All values should be the same type
  - All keys should be the same type

# Usage Commands

## Transpile a file

```
python transpile.py -f <source_file> -l <target_language> -s <source_language>
```

Arguments:
- `-f`, `--file`: Source file path
- `-l`, `--lang`: Target language (golang, javascript, typescript, java, kotlin, python)
- `-s`, `--source_lang`: Source language (defaults to Python if not specified)

Example:
```
python transpile.py -f examples/hello.py -l golang -s Python
```

# Development Considerations

- Use GENHINT for type annotations when the output type might be ambiguous
- The transpiler creates output files in `.gen/<language>/` directories
- Review the examples in the `/examples` directory to understand supported features and syntax
- When adding support for new language features, create appropriate examples
- Be aware of language-specific features that might not have direct equivalents