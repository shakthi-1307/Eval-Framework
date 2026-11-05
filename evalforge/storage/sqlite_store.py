import sqlite3
from pathlib import Path 

DB_PATH = Path("evalforge.db")

def initialize_database():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("PRAGMA foreign_keys = ON")
        
        conn.execute("""
            CREATE TABLE IF NOT EXISTS evaluation_runs (
                run_id TEXT PRIMARY KEY,
                dataset_name TEXT NOT NULL,
                generated_at TEXT NOT NULL,
                total_tests INTEGER NOT NULL,
                passed_tests INTEGER NOT NULL,
                failed_tests INTEGER NOT NULL,
                accuracy REAL NOT NULL,
                average_execution_time REAL NOT NULL,
                total_execution_time REAL NOT NULL
            )
        """)
        
        conn.execute("""
            CREATE TABLE IF NOT EXISTS test_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                run_id TEXT NOT NULL,
                test_id TEXT NOT NULL,
                input TEXT NOT NULL,
                actual_output TEXT,
                expected_output TEXT,
                passed INTEGER,
                error TEXT,
                execution_time REAL NOT NULL,
                timestamp TEXT,
                
                FOREIGN KEY (run_id)
                    REFERENCES evaluation_runs(run_id)
                    ON DELETE CASCADE,
                    
                UNIQUE (run_id,test_id)
            )
        """)
        
def save_report(report):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("PRAGMA foreign_keys = ON")
        
        conn.execute("""
            INSERT INTO evaluation_runs (
                run_id,
                dataset_name,
                generated_at,
                total_tests,
                passed_tests,
                failed_tests,
                accuracy,
                average_execution_time,
                total_execution_time
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            str(report.run_id),
            report.dataset_name,
            report.generated_at.isoformat(),
            report.total_tests,
            report.passed_test,
            report.failed_tests,
            report.accuracy,
            report.average_execution_time,
            report.total_execution_time,
        ))
        
        for result in report.results:
            conn.execute("""
                INSERT INTO test_results (
                    run_id,
                    test_id,
                    input,
                    actual_output,
                    expected_output,
                    passed,
                    error,
                    execution_time,
                    timestamp
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                str(report.run_id),
                result.test_id,
                result.input,
                result.actual_output,
                result.expected_output,
                None if result.passed is None else int(result.passed),
                result.error,
                result.execution_time,
                result.timestamp.isoformat()
                    if result.timestamp else None,
            ))
            
if __name__ == "__main__":
    initialize_database()
    print(f"Database initialized : {DB_PATH.resolve()}")