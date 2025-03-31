# CursorChatAnalyzer

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
./extract_conversation.py ~/Library/Application\ Support/Cursor/User/globalStorage/state.vscdb b6030831-dc69-4fae-b0b0-071b04e2757a ~/chat_logs/
```

## Data Locations

Cursor stores its data in different locations depending on your operating system:

### macOS
```
~/Library/Application Support/Cursor/
```

Key subdirectories:
- `User/globalStorage/state.vscdb` - Main database containing chat history
- `User/workspaceStorage/<workspace-hash>/` - Workspace-specific data
- `extensions/` - Installed extensions
- `logs/` - Application logs

### Windows
```
%APPDATA%/Cursor/
```
Expected subdirectories follow a similar structure to macOS:
- `User/globalStorage/state.vscdb` - Main database
- `User/workspaceStorage/<workspace-hash>/` - Workspace data
- `extensions/` - Installed extensions

### Linux
```
$HOME/.config/Cursor/
```
Or:
```
$XDG_CONFIG_HOME/Cursor/
```

Similar structure to other platforms:
- `User/globalStorage/state.vscdb` - Main database
- `User/workspaceStorage/<workspace-hash>/` - Workspace data
- `extensions/` - Installed extensions

### Important Notes

1. The `state.vscdb` file is a SQLite database containing:
   - Chat history
   - Workspace state
   - Editor preferences
   - Debug configurations

2. The `workspaceStorage` directory contains workspace-specific data:
   - Each workspace gets a unique hash
   - Contains workspace-specific settings and state
   - May include temporary files and caches

3. Backup Considerations:
   - Back up the entire Cursor directory to preserve all settings
   - The `state.vscdb` file is particularly important as it contains chat history
   - Consider excluding the `extensions` directory from backups (can be reinstalled)
   - Workspace storage can be large; consider selective backup

4. Security Note:
   - The database may contain sensitive information from chats
   - Consider encrypting backups
   - Be cautious when sharing database files
   - Review chat content before sharing

5. Migration:
   - When moving to a new machine, copy the entire Cursor directory
   - Extensions will need to be reinstalled on the new machine
   - Some paths may need to be updated in workspace settings

For more detailed analysis of your chat history, you can use the tools in this repository to extract and analyze the conversations stored in the `state.vscdb` file.

## Contributing

To contribute to this project, please create a pull request on GitHub. The repository is available at: [GitHub - CursorChatAnalyzer](https://github.com/toddllm/CursorChatAnalyzer)

## License

MIT
