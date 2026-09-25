# Semaphores

A semaphore is a synchronization primitive that controls access to a resource pool by maintaining a counter. Threads decrement the counter to acquire a resource and increment it to release; if the counter is zero, acquiring threads block. Binary semaphores behave like mutexes; counting semaphores manage pools of limited resources.