# Benchmark Summary

_122 segments × 12 queries; top-10 retrieval._

| Model | Variant | MRR | R@5 | R@10 | Median rank | ms/seg |
|---|---|---|---|---|---|---|
| `bge-m3:latest` | body | 1.000 | 1.00 | 1.00 | 1 | 131 |
| `bge-m3:latest` | terse | 1.000 | 1.00 | 1.00 | 1 | 84 |
| `nomic-embed-text-v2-moe:latest` | body | 1.000 | 1.00 | 1.00 | 1 | 94 |
| `qwen3-embedding:latest` | body | 1.000 | 1.00 | 1.00 | 1 | 921 |
| `embeddinggemma:300m` | body | 0.958 | 1.00 | 1.00 | 1 | 100 |
| `nomic-embed-text-v2-moe:latest` | terse | 0.958 | 1.00 | 1.00 | 1 | 83 |
| `mxbai-embed-large:latest` | body | 0.917 | 1.00 | 1.00 | 1 | 57 |
| `nomic-embed-text:latest` | body | 0.903 | 1.00 | 1.00 | 1 | 34 |
| `granite-embedding:30m` | body | 0.896 | 1.00 | 1.00 | 1 | 39 |
| `snowflake-arctic-embed:latest` | body | 0.555 | 0.67 | 0.92 | 2 | 51 |
