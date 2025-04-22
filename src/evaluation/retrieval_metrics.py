def precision_at_k(retrieved_ids: List[str], relevant_ids: List[str], k: int = 5) -> float:
    """Calculate precision@k - the proportion of retrieved documents in the top-k that are relevant."""

def recall_at_k(retrieved_ids: List[str], relevant_ids: List[str], k: int = 5) -> float:
    """Calculate recall@k - the proportion of relevant documents that are retrieved in the top-k."""

def mean_reciprocal_rank(retrieved_ids: List[str], relevant_ids: List[str]) -> float:
    """Calculate Mean Reciprocal Rank (MRR)."""

def ndcg_at_k(retrieved_ids: List[str], relevant_ids_with_scores: Dict[str, float], k: int = 5) -> float:
    """Calculate Normalized Discounted Cumulative Gain (NDCG) at k."""

def f1_at_k(retrieved_ids: List[str], relevant_ids: List[str], k: int = 5) -> float:
    """Calculate F1 score at k - the harmonic mean of precision@k and recall@k."""

def evaluate_retrieval_for_query(retrieval_system: Any, query: str, relevant_ids: List[str], 
                               k_values: List[int] = [1, 3, 5, 10], relevant_scores: Dict[str, float] = None) -> Dict[str, float]:
    """Evaluate retrieval metrics for a single query."""

def evaluate_retrieval_performance(retrieval_system: Any, test_cases: List[Dict[str, Any]], 
                                 k_values: List[int] = [1, 3, 5, 10]) -> Dict[str, Any]:
    """Evaluate retrieval performance across multiple test queries."""

def evaluate_retrieval_by_category(retrieval_system: Any, test_cases: List[Dict[str, Any]], 
                                 k_values: List[int] = [1, 3, 5]) -> Dict[str, Any]:
    """Evaluate retrieval performance grouped by query category."""

def visualize_retrieval_performance(metrics_result: Dict[str, Any], output_path: str = "retrieval_performance.png"):
    """Create visualization of retrieval performance metrics."""

def evaluate_banking_product_retrieval(retrieval_system: Any, test_cases_path: str, 
                                     output_dir: str = "./evaluation_results") -> Dict[str, Any]:
    """Comprehensive evaluation of banking product information retrieval."""