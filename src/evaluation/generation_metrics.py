def calculate_bleu_score(generated_responses: List[str], reference_responses: List[str]) -> float:
    """Calculate BLEU score to measure the overlap of n-grams between generated and reference responses."""

def calculate_rouge_scores(generated_responses: List[str], reference_responses: List[str]) -> Dict[str, Dict[str, float]]:
    """Calculate ROUGE scores to measure the overlap of word sequences."""

def calculate_meteor_score(generated_responses: List[str], reference_responses: List[str]) -> float:
    """Calculate METEOR score for evaluation of generated text."""

def calculate_factual_consistency(generated_responses: List[str], source_documents: List[str]) -> float:
    """Evaluate how well the generated responses stick to facts from the source documents."""

def calculate_answer_relevance(generated_responses: List[str], queries: List[str]) -> float:
    """Measure how relevant the generated responses are to the original queries."""

def evaluate_generation_for_query(rag_system: Any, query: str, reference_answer: str, 
                                context_docs: List[str] = None) -> Dict[str, float]:
    """Evaluate text generation quality for a single query."""

def evaluate_generation_performance(rag_system: Any, test_cases: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Evaluate text generation performance across multiple test queries."""

def evaluate_generation_by_category(rag_system: Any, test_cases: List[Dict[str, Any]]) -> Dict[str, Dict[str, float]]:
    """Evaluate text generation quality grouped by query category."""

def visualize_generation_performance(metrics_result: Dict[str, Any], output_path: str = "generation_performance.png"):
    """Create visualization of text generation performance metrics."""

def evaluate_banking_response_quality(rag_system: Any, test_cases_path: str, 
                                    output_dir: str = "./evaluation_results") -> Dict[str, Any]:
    """Comprehensive evaluation of banking response generation quality."""