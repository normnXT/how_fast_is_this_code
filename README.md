# how_fast_is_this_code
A cProfile loop and performance counter average loop over a specified number of tests. Copy-paste code and run to get some idea of its performance.

cProfile loop function:
- As arguments, it takes the function to test, the number of runs, and the functions args or kwargs if needed.
- Returns cProfile table with execution times in seconds
- Performs specified number of tests and presents total time, total time per call, cumulative time, and cumulative time per call.
- cProfile: https://docs.python.org/3/library/profile.html

Performance counter average function:
- Take the same arguments. The function to test, the number of runs, and the functions args or kwargs. 
- Returns average seconds 
- It records all runs and then divides by the number of runs and presents the mean. 
- perf_counter: https://docs.python.org/3/library/time.html
