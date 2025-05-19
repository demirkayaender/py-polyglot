# py-polyglot
Python based vibe (AI) transpiler

This is nowhere close to a complete project. I'm currently evaluating Claude (or another agent) as a potential transpiler. AI is known to halucinate where you don't typically want to use to generate your production code. However, there seems to be ways to imrpove its precision and better test it after the fact, which is what I'm trying to do in this project. This README will be updated once I have something working at a reasonable scale.

## Requirements
To make this project work, you need to have a programmatic access to Claude. Once you have that, create a command line tool that can take your prompts and outputs the results. This project assumes the following command to do that:
```
claude -p <prompt>
```

Create a `CLAUDE.md` file(s) to hint the transpiler (a better name will probably be selected in the future). This file will provide the guidelines to the transpiler. Explain what kind of output you want, define transpiling rules (especially when they may not be obvious for a generic transpiler), anything else that can be useful under that folder. If there are specific rules for any subfolder, create another `CLAUDE.md` under that folder. Using such guideline file significantly improves the consistency and the performance of this transpiler.

## Warnings
A code base might have hundreds of thousands of lines of code. Every keyword is counted as a `token` that will cost you. Similarly, every output keyword is counted as `token` which will come with a cost. Make sure you understand how much running this tool is going to cost you based on your API credit costs. This project will introduce a caching layer later to avoid regenerating unchanged functions, files, etc. but it's not implemented yet.
