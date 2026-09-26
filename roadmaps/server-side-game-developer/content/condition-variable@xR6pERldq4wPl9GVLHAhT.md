# Condition Variable

A condition variable allows threads to block and wait until a specific condition becomes true, then be woken by another thread. It is used alongside a mutex: one thread holds the mutex, checks a condition, waits on the variable if not met, and is signaled when another thread changes the state.

Visit the following resources to learn more:

- [@official@Using Condition Variables - IBM](https://www.ibm.com/docs/ssw_aix_71/com.ibm.aix.genprogc/condition_variables.htm)
- [@official@std::condition_variable - cppreference](https://en.cppreference.com/cpp/thread/condition_variable)
- [@article@Condition Variables – ModernesC++](https://www.modernescpp.com/index.php/condition-variables/)