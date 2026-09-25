# Usecases

Bitmaps are used for feature flags, daily active user tracking, and attendance records where each bit represents one entity or time period. They offer extremely compact storage: tracking 100 million users requires only about 12 MB. Operations like `BITCOUNT` and `BITOP` make aggregation across bitmap sets straightforward.