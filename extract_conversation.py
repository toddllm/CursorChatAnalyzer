#!/usr/bin/env python3
import os
import sqlite3
import json
import sys
import re
from collections import Counter
from datetime import datetime

def extract_conversation(db_path, chat_id):
    if not os.path.exists(db_path):
        print(f"Error: Database {db_path} not found")
        return None
        
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        key = f"composerData:{chat_id}" if not chat_id.startswith("composerData:") else chat_id
        cursor.execute("SELECT value FROM cursorDiskKV WHERE key = ?", (key,))
        
        result = cursor.fetchone()
        conn.close()
        
        if not result:
            print(f"Error: Conversation {chat_id} not found")
            return None
            
        return json.loads(result[0])
        
    except Exception as e:
        print(f"Error accessing database: {e}")
        return None

def analyze_patterns(conversation_text):
    # Find common technologies
    tech_patterns = ["YOLOv8", "Flower", "flwr", "conda", "Python", "TensorFlow", "PyTorch", "npm", "React"]
    tech_counts = {}
    for tech in tech_patterns:
        count = conversation_text.count(tech)
        if count > 0:
            tech_counts[tech] = count
    
    # Find command patterns
    command_patterns = [r"cd [^ ]+", r"ls -[a-z]+", r"git [a-z\-]+", r"python -[a-z]"]
    commands = []
    for pattern in command_patterns:
        commands.extend(re.findall(pattern, conversation_text))
    
    # Extract file paths
    file_paths = re.findall(r"/[a-zA-Z0-9/_\-\.]+\.(py|js|ts|jsx|tsx|go|rs|json|yaml|yml)", conversation_text)
    
    return {
        "technologies": tech_counts,
        "commands": Counter(commands).most_common(10),
        "file_paths": Counter(file_paths).most_common(10)
    }

def generate_report(data, chat_id, patterns, output_dir=None):
    report = f"# {chat_id} - Analysis\n\n"
    
    # Main query
    report += f"## Query\n{data.get("text", "No query found")}\n\n"
    
    # Summary if available
    if data.get("latestConversationSummary"):
        report += "## Summary\n"
        report += str(data.get("latestConversationSummary"))
        report += "\n\n"
    
    # Key technologies
    report += "## Key Technologies\n"
    for tech, count in sorted(patterns["technologies"].items(), key=lambda x: x[1], reverse=True):
        report += f"- {tech} ({count} occurrences)\n"
    report += "\n"
    
    # Top commands
    report += "## Top Commands\n"
    for cmd, count in patterns["commands"]:
        report += f"- `{cmd}` ({count} occurrences)\n"
    report += "\n"
    
    # Most referenced files
    report += "## Most Referenced Files\n"
    for path, count in patterns["file_paths"]:
        report += f"- `{path}` ({count} occurrences)\n"
    
    if output_dir:
        output_path = os.path.join(output_dir, f"{chat_id.split(":")[-1]}_analysis.md")
        with open(output_path, "w") as f:
            f.write(report)
        print(f"Report written to {output_path}")
    
    return report

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python extract_conversation.py <database_path> <conversation_id> [output_dir]")
        sys.exit(1)
    
    db_path = sys.argv[1]
    chat_id = sys.argv[2]
    output_dir = sys.argv[3] if len(sys.argv) > 3 else None
    
    # Extract the conversation data
    data = extract_conversation(db_path, chat_id)
    if not data:
        sys.exit(1)
    
    # Convert to text for analysis
    conversation_text = json.dumps(data)
    
    # Analyze patterns
    patterns = analyze_patterns(conversation_text)
    
    # Generate report
    report = generate_report(data, chat_id, patterns, output_dir)
    
    # Print the report if no output directory was specified
    if not output_dir:
        print(report)
