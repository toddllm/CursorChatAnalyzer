#!/usr/bin/env python3
import os
import sys

def find_cursor_dbs():
    locations = [
        os.path.expanduser("~/Library/Application Support/Cursor/User/globalStorage"),
        os.path.expanduser("~/Library/Application Support/Cursor/User/workspaceStorage")
    ]
    
    db_files = []
    for location in locations:
        if os.path.exists(location):
            for root, _, files in os.walk(location):
                for file in files:
                    if file == "state.vscdb":
                        db_files.append(os.path.join(root, file))
    
    return db_files

if __name__ == "__main__":
    dbs = find_cursor_dbs()
    print(f"Found {len(dbs)} database files:")
    for i, db in enumerate(dbs):
        print(f"{i+1}. {db}")