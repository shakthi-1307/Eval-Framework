import sqlite3

from evalforge.storage.sqlite_store import (
    initialize_database,
    DB_PATH,
)

def main():
    initialize_database()
    
    with sqlite3.connect(DB_PATH) as conn:
        runs = conn.execute(
            "SELECT COUNT(*) FROM evaluation_runs"
        ).fetchone()[0]
        
        results = conn.execute(
            "SELECT COUNT(*) FROM test_results"
        ).fetchone()[0]
        
    print("Stored evaluation runs:", runs)
    print("Stored test results:", results)
    
if __name__ == "__main__":
    main()