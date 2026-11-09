from evalforge.storage.sqlite_store import (
    get_all_runs,
    get_run_results,
)

def main():
    runs = get_all_runs()
    
    print("\n============== EVALUATION HISTORY ===============")
    
    for run in runs:
        print(f"\nRun ID : {run['run_id']}")
        print(f"Dataset: {run['dataset_name']}")
        print(f"Accuracy: {run['accuracy']}")
        print(f"Total tests: {run['total_tests']}")
        
    if runs:
        latest_run = runs[0]
        
        results = get_run_results(latest_run['run_id'])
        
        print("\n============ LATEST RUN DETAILS ==========")
        
        for result in results:
            print(f"\nTest ID : {result['test_id']}")
            print(f"\nPassed : {bool(result['passed'])}")
            print(f"\nLatency : {result['execution_time']:.3f}s")
            
if __name__ == "__main__":
    main()