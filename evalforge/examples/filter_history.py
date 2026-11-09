from evalforge.storage.sqlite_store import filter_runs

def main():
    print("\n--- Runs with accuracy >= 0.9 ---")
    
    runs = filter_runs(min_accuracy = 0.9)
    
    for run in runs:
        print(run['dataset_name'],run['accuracy'],run["run_id"],)
        
    print("\n--- General Knowledge runs ---")
    
    runs = filter_runs(dataset_name = "General Knowledge")
    
    for run in runs:
        print(run['dataset_name'],run['accuracy'],run["run_id"],)
        
if __name__ == "__main__":
    main()