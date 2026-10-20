
from src.utility.report_lib import write_output
import time


def uniqueness_check(df, unique_cols):
    """Validate that specified columns have unique values."""

    start_time = time.perf_counter()

    # Validate column names
    missing_columns = [
        column for column in unique_cols
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Columns not found in DataFrame: {missing_columns}"
        )

    # Dictionary to collect duplicate group counts per column
    duplicate_counts = {}

    for column in unique_cols:
        dup_df = (
            df.groupBy(column)
            .count()
            .filter("count > 1")
        )

        count_duplicates = dup_df.count()
        duplicate_counts[column] = count_duplicates

        print(f"Duplicate count for {column}: {count_duplicates}")

    print("Duplicate counts:", duplicate_counts)

    total_records = df.count()

    # PASS only when every specified column is unique
    if all(count == 0 for count in duplicate_counts.values()):
        status = "PASS"
        details = (
            f"Target={total_records}; "
            f"duplicate_counts={duplicate_counts}; "
            "Uniqueness check=All specified columns are unique"
        )

    else:
        status = "FAIL"
        # Collect sample duplicate values for failing columns
        sample_duplicates = {}

        for column, count in duplicate_counts.items():
            if count > 0:
                dup_df = (
                    df.groupBy(column)
                    .count()
                    .filter("count > 1")
                    .limit(5)
                )

                sample_duplicates[column] = [
                    row.asDict() for row in dup_df.collect()
                ]

        details = (
            f"Target={total_records}; "
            f"duplicate_counts={duplicate_counts}; "
            f"sample_duplicates={sample_duplicates}"
        )

    duration = round(
        time.perf_counter() - start_time,
        3
    )

    print("uniqueness_check duration:", duration)

    write_output(
        validation_type="Uniqueness Check",
        status=status,
        duration_seconds=duration,
        details=details
    )

    return status
