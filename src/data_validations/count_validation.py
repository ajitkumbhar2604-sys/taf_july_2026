import time
from src.utility.report_lib import write_output

def count_check(source, target):
    start_time = time.perf_counter()
    src_cnt = source.count()
    tgt_cnt = target.count()
    difference = abs(src_cnt - tgt_cnt)

    if difference == 0:
        status = "PASS"

        details ={
            f"Source={src_cnt}, "
            f"Target={tgt_cnt}, "
            f"Difference=0"
        }
        #print(details)
    else:
        status = "FAIL"

        details ={
            f"Source={src_cnt}, "
            f"Target={tgt_cnt}, "
            f"Difference={difference}"
        }
        #print(details)
    duration = round(time.perf_counter() - start_time,3)

    print("count func duration: ", duration)

    #Now we can add the write_output() in report_lib file,
    write_output(
        validation_type="Count Check",
        status=status,
        duration_seconds=duration,
        details=details
    )

    return status