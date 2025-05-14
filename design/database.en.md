# Data Persistence 

## Technology Choice

The selected database is **MongoDB**, a document-based NoSQL database well-suited for storing JSON-like data structures and handling high-volume datasets with flexibility and performance.

### Justifications:

- **Schema flexibility**: Allows data structure changes without complex migrations.
- **Large-scale performance**: Built-in support for horizontal sharding.
- **JSON compatibility**: Naturally integrates with the API data format.
- **Horizontal scalability**: Easily grows to match increasing demand.
- **Powerful indexing**: Enables optimized read/write operations.

---

## Persistence Strategy

- Each entry from the `POST /data` endpoint is stored as a document in a MongoDB collection.
- Expected fields:
  - `id`: integer (unique key)
  - `name`: string
  - `value`: float

### Considerations:

- The `id` field is indexed to improve search and prevent duplicates.
- Data is validated before persistence to ensure consistency.

---

## Modeling and Scalability

- JSON document structure allows for easy replication and partitioning.
- As volume increases, data can be distributed across multiple shards.
- Asynchronous replication ensures high availability and fault tolerance.

---

## Future Optimizations

- Use of **TTL Indexes** to automatically expire old data (if needed).
- Index analysis for compound indexes based on real-world queries.
- Optional use of cache layers (e.g., Redis) for frequently accessed reads.
