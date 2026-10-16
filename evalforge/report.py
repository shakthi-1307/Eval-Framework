
def print_report(metrics, results):
    print("\n" + "=" * 45)
    print("           EVALFORGE REPORT")
    print("=" * 45)

    print(f"Total tests:       {metrics.total_tests}")
    print(f"Passed tests:      {metrics.passed_tests}")
    print(f"Failed tests:      {metrics.failed_tests}")
    print(f"Pass rate:         {metrics.pass_rate:.2%}")

    if metrics.ci_lower is not None and metrics.ci_upper is not None:
        print(
            f"95% Confidence:    "
            f"{metrics.ci_lower:.2%} - {metrics.ci_upper:.2%}"
        )

    print(f"Average latency:   {metrics.average_latency_seconds:.4f}s")

    print("\nIndividual Results")
    print("-" * 45)

    for execution, grading in results:
        if execution.error:
            status = "ERROR"
            detail = execution.error
        elif grading is None:
            status = "NOT GRADED"
            detail = "No grading result available."
        else:
            status = "PASS" if grading.passed else "FAIL"
            detail = grading.reason

        print(f"\nTest ID: {execution.test_id}")
        print(f"Status:  {status}")
        print(f"Input:   {execution.input}")
        print(f"Output:  {execution.actual_output}")
        print(f"Details: {detail}")

    print("\n" + "=" * 45)
