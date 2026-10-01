# Continuous Batching

Continuous batching operates at the token level, swapping requests in and out of the batch as they complete individual tokens rather than waiting for a full batch to finish. This keeps GPU utilization high and minimizes the latency penalty of batching compared to static or dynamic batching. All major inference engines implement continuous batching by default.