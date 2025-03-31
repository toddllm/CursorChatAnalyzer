# Cursor Chat Analyzer - Tutorial

This guide shows how to analyze Cursor's chat database files.

## 1. Finding Database Files

Cursor stores chat data in SQLite databases. Run this command to find them:

```bash
find ~/Library/Application\ Support/Cursor -name "*.vscdb" | grep -v CachedData | grep -v Crash
```

## 2. Listing Conversations

To list all conversations in a database, use this Python script:

## 3. Extracting Chat Content

To extract a specific conversation and analyze its content:

## 4. Generating Reports

This script generates different types of reports (terse, detailed, full) for a conversation:
## 5. Complete Example
