#!/usr/bin/env python3
import os
import sqlite3
import json
import sys
from datetime import datetime

def list_conversations(db_path):
    if not db_path or not os.path.exists(db_path):
        print(f"Error: Database {db_path} not found")
        return []
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT key, value FROM cursorDiskKV WHERE key LIKE \"composerData:%\"")
        
        conversations = []
        for key, value in cursor.fetchall():
            try:
                data = json.loads(value)
                chat_id = key.split(":")[-1] if ":" in key else key
                created_at = data.get("createdAt")
                if created_at:
                    created_at = datetime.fromtimestamp(created_at / 1000)
                text = data.get("text", "")
                
                conversations.append({
                    "id": chat_id,
                    "created_at": created_at,
                    "text": text[:100] + "..." if len(text) > 100 else text
                })
            except Exception as e:
                print(f"Error parsing conversation {key}: {e}")
        
        conn.close()
        return conversations
        
    except Exception as e:
        print(f"Error accessing database: {e}")
        return []

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python list_conversations.py <database_path>")
        sys.exit(1)
    
    db_path = sys.argv[1]
    conversations = list_conversations(db_path)
    
    print(f"Found {len(conversations)} conversations:")
    for i, conv in enumerate(conversations):
        created = conv["created_at"].strftime("%Y-%m-%d %H:%M:%S") if conv["created_at"] else "Unknown"
        print(f"{i+1}. {conv["id"]} ({created})")
        print(f"   Query: {conv["text"]}\n")