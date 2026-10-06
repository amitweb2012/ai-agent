# RAG Documentation

Retrieval-Augmented Generation grounds an LLM answer in external knowledge.

Pipeline:

    Documents -> embedding model -> document vectors
    Question  -> embedding model -> question vector
                                      |
                                      v
                              cosine similarity
                                      |
                                      v
                               best document
                                      |
                                      v
                             similarity threshold
                                      |
                                      v
                               LLM + context
                                      |
                                      v
                               grounded answer

Cosine similarity is:

    cos(A,B) = (A dot B) / (||A|| * ||B||)

The current implementation embeds complete text files and selects the highest-scoring document. For production, add chunking, metadata, top-k retrieval, pgvector, reranking, citations, and evaluation.