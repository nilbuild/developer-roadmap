# Usecases

Lua scripting is used when a sequence of reads and writes must happen atomically, such as conditional updates, rate limiting with exact semantics, or multi-step workflows. It avoids the overhead of multiple round trips and removes the need for application-level locking in most cases.