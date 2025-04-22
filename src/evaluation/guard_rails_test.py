def test_prompt_injection_defense(rag_system: Any, injection_attempts: List[Dict[str, Any]]) -> Dict[str, float]:
    """Test if the system can detect and block prompt injection attacks."""

def test_sensitive_info_protection(rag_system: Any, sensitive_queries: List[Dict[str, Any]]) -> Dict[str, float]:
    """Test if the system properly protects sensitive banking information."""

def test_out_of_domain_handling(rag_system: Any, out_of_scope_queries: List[Dict[str, Any]]) -> Dict[str, float]:
    """Test if the system appropriately handles queries outside its domain."""

def test_hallucination_prevention(rag_system: Any, factual_queries: List[Dict[str, str]]) -> Dict[str, float]:
    """Test the system's ability to avoid generating hallucinated content."""

def test_pii_detection(rag_system: Any, pii_containing_queries: List[Dict[str, Any]]) -> Dict[str, float]:
    """Test the system's ability to detect and handle personally identifiable information."""

def evaluate_safety_for_query_type(rag_system: Any, test_cases: List[Dict[str, Any]], 
                                 safety_type: str) -> Dict[str, float]:
    """Evaluate a specific type of safety mechanism."""

def evaluate_overall_safety(rag_system: Any, test_suite: Dict[str, List[Dict[str, Any]]]) -> Dict[str, Any]:
    """Evaluate the overall safety of the system across different dimensions."""

def visualize_safety_performance(safety_results: Dict[str, Any], output_path: str = "safety_performance.png"):
    """Create visualization of safety evaluation results."""

def evaluate_banking_guard_rails(rag_system: Any, test_cases_path: str, 
                               output_dir: str = "./evaluation_results") -> Dict[str, Any]:
    """Comprehensive evaluation of banking assistant guard rails and safety measures."""