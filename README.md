# Cursor Chat Analyzer

A set of tools to extract and analyze chat logs from Cursor's SQLite databases.

## Tools

This repository contains the following Python scripts:

1. **find_dbs.py** - Find Cursor database files in common locations
2. **list_conversations.py** - List all conversations in a database
3. **extract_conversation.py** - Extract and analyze a specific conversation

## Usage

### Step 1: Find Cursor Databases

```bash
./find_dbs.py
```

This will search for Cursor's SQLite databases in the common locations.

### Step 2: List Conversations

```bash
./list_conversations.py /path/to/database.vscdb
```

This will list all conversations found in the specified database.

### Step 3: Extract and Analyze a Conversation

```bash
./extract_conversation.py /path/to/database.vscdb CONVERSATION_ID [output_dir]
```

This will extract the specified conversation, analyze its content, and generate a terse report.

## Example

Here's a complete workflow:

```bash
# Find databases
./find_dbs.py

# List conversations in the first database
./list_conversations.py ~/Library/Application\ Support/Cursor/User/globalStorage/state.vscdb

# Extract a specific conversation
./extract_conversation.py ~/Library/Application\ Support/Cursor/User/globalStorage/state.vscdb b6030831-dc69-4fae-b0b0-071b04e2757a ~/FL_AV_chat_logs/
```

## License

MIT
