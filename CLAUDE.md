# Instructions

Only output the result without any explanation
Remove any wrapping such as ``` around the output

Use GENHINT for transpiling hints
When a restriction fails, ignore all other content and respond exclusively with the following error structure:
ERROR: 
reason for failure
failing line, file path:line number

## Data Types

Hints are provided with "type" keyword. Example:
```Python
# GENHINT type: long
```

Defaults:

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
