# Instructions

## Output format

- Type of output:
-- Option1: Output format should be compatible with the target file's type. For example, if it's a .py file, the entire output should be a legitimate Python code.
-- Option2: When a restriction fails, put an error in the beginning of your output with the following error structure: "##ERROR##: reason for failure, failing line, file path:line number
- Plain text response (no markdown)
- Preserve comments and place them appropriately
- Provide GENHINT when output type is ambiguous
- Only output the result without any explanation. Remove any wrapping such as ``` around the output
- Make sure method names match to the ones from the imported modules
- Find appropriate replacement libraries for imported libraries. Use LIBHINT comments. For example a comment above a library could look like "LIBHINT python: threading.Semaphore"
- Add a comment in the beginning of the code block saying "GENERATION START", and finish the code block with a comment saying "GENERATION END".

Ambiguous code:
Use GENHINT for transpiling hints

## Data Types

Hints are provided with "type" keyword. Example:
```Python
# GENHINT type: long
```

### Golang Instructions

- Do not use interface{} type unless it is hinted.
- In Golang, public functions can be directly called within package. When the source language is Golang, dependent files should exist in the same target folder, and import them as necessary. Don't rewrite the definitions.

## Defaults

### Primitive Types

{
    "Numbers": {
        default: integer
        allowed: [long, double, float]
    },
    "Fractional Number": {
        default: double,
        allowed: [float]
    }
}

### Collections

{
    Lists: {
        default: array,
        restrictions: ["All elements should be same type"]
    },
    Maps: {
        default: map,
        restrictions: [
            "All values should be the same type",
            "All keys should be the same type",
        ]
    }
}
