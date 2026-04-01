"""
Discontinuity Metrics Module

Implements various metrics for measuring code discontinuities
based on Software First Principles (FP-012).
"""

import ast
import re
from pathlib import Path
from typing import Dict, List, Tuple, Set, Optional
from dataclasses import dataclass
from collections import defaultdict
import networkx as nx


@dataclass
class DiscontinuityMeasure:
    """Comprehensive discontinuity measurement for code"""
    
    # Basic counts
    file_imports: int = 0
    external_calls: int = 0
    class_transitions: int = 0
    function_calls: int = 0
    
    # Depth metrics
    max_call_depth: int = 0
    avg_call_depth: float = 0.0
    
    # Cognitive metrics
    namespace_switches: int = 0
    context_switches: int = 0
    abstraction_jumps: int = 0
    
    # Computed scores
    total_discontinuities: int = 0
    weighted_score: float = 0.0
    predicted_comprehension_time: float = 0.0
    
    def calculate_totals(self, weights: Optional[Dict[str, float]] = None) -> None:
        """Calculate total discontinuity score with optional weights"""
        if weights is None:
            # Default weights based on cognitive load research
            weights = {
                'file_imports': 1.0,
                'external_calls': 0.5,
                'class_transitions': 2.0,
                'function_calls': 0.3,
                'namespace_switches': 3.0,
                'context_switches': 2.5,
                'abstraction_jumps': 4.0,
            }
        
        self.total_discontinuities = (
            self.file_imports +
            self.external_calls +
            self.class_transitions +
            self.function_calls +
            self.namespace_switches +
            self.context_switches +
            self.abstraction_jumps
        )
        
        self.weighted_score = (
            self.file_imports * weights.get('file_imports', 1.0) +
            self.external_calls * weights.get('external_calls', 0.5) +
            self.class_transitions * weights.get('class_transitions', 2.0) +
            self.function_calls * weights.get('function_calls', 0.3) +
            self.namespace_switches * weights.get('namespace_switches', 3.0) +
            self.context_switches * weights.get('context_switches', 2.5) +
            self.abstraction_jumps * weights.get('abstraction_jumps', 4.0)
        )
        
        # FP-012 model: T = T_base × (1 + α)^d
        T_base = 5.0  # Base comprehension time in minutes
        alpha = 0.2   # 20% penalty per discontinuity
        self.predicted_comprehension_time = T_base * ((1 + alpha) ** self.weighted_score)


class CodeAnalyzer:
    """Analyzes code for discontinuities"""
    
    def __init__(self):
        self.current_file: Optional[Path] = None
        self.import_graph = nx.DiGraph()
        self.call_graph = nx.DiGraph()
        self.file_contents_cache: Dict[Path, str] = {}
        
    def analyze_file(self, filepath: Path) -> DiscontinuityMeasure:
        """Analyze a single file for discontinuities"""
        self.current_file = filepath
        
        # Read file content
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading {filepath}: {e}")
            return DiscontinuityMeasure()
        
        self.file_contents_cache[filepath] = content
        measure = DiscontinuityMeasure()
        
        # Determine file type and analyze accordingly
        if filepath.suffix == '.py':
            measure = self.analyze_python_file(content, measure)
        elif filepath.suffix in ['.js', '.ts', '.jsx', '.tsx']:
            measure = self.analyze_javascript_file(content, measure)
        elif filepath.suffix in ['.java']:
            measure = self.analyze_java_file(content, measure)
        elif filepath.suffix in ['.ex', '.exs']:
            measure = self.analyze_elixir_file(content, measure)
        
        measure.calculate_totals()
        return measure
    
    def analyze_python_file(self, content: str, measure: DiscontinuityMeasure) -> DiscontinuityMeasure:
        """Analyze Python file for discontinuities"""
        try:
            tree = ast.parse(content)
        except SyntaxError:
            return measure
        
        # Count imports
        for node in ast.walk(tree):
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                measure.file_imports += 1
                if isinstance(node, ast.ImportFrom) and node.module:
                    # Track external vs internal imports
                    if not node.module.startswith('.'):
                        measure.external_calls += 1
        
        # Analyze function calls and class usage
        class CallVisitor(ast.NodeVisitor):
            def __init__(self, measure):
                self.measure = measure
                self.current_class = None
                self.current_function = None
                self.call_depth = 0
                self.max_depth = 0
                
            def visit_ClassDef(self, node):
                prev_class = self.current_class
                self.current_class = node.name
                if prev_class:
                    self.measure.class_transitions += 1
                self.generic_visit(node)
                self.current_class = prev_class
                
            def visit_FunctionDef(self, node):
                prev_func = self.current_function
                self.current_function = node.name
                self.call_depth += 1
                self.max_depth = max(self.max_depth, self.call_depth)
                self.generic_visit(node)
                self.current_function = prev_func
                self.call_depth -= 1
                
            def visit_Call(self, node):
                self.measure.function_calls += 1
                # Check if it's a method call on different object
                if isinstance(node.func, ast.Attribute):
                    if isinstance(node.func.value, ast.Name):
                        # Different object context
                        self.measure.context_switches += 1
                self.generic_visit(node)
        
        visitor = CallVisitor(measure)
        visitor.visit(tree)
        measure.max_call_depth = visitor.max_depth
        
        # Detect namespace switches (module.function patterns)
        namespace_pattern = r'(\w+)\.(\w+)\('
        namespace_matches = re.findall(namespace_pattern, content)
        measure.namespace_switches = len(set(namespace_matches))
        
        # Detect abstraction jumps (decorators, metaclasses, etc.)
        measure.abstraction_jumps = content.count('@') + content.count('super()')
        
        return measure
    
    def analyze_javascript_file(self, content: str, measure: DiscontinuityMeasure) -> DiscontinuityMeasure:
        """Analyze JavaScript/TypeScript file for discontinuities"""
        # Count imports
        import_pattern = r'import\s+.*?from\s+[\'"](.+?)[\'"]'
        imports = re.findall(import_pattern, content)
        measure.file_imports = len(imports)
        measure.external_calls = sum(1 for imp in imports if not imp.startswith('.'))
        
        # Count function calls
        call_pattern = r'(\w+)\s*\('
        calls = re.findall(call_pattern, content)
        measure.function_calls = len(calls)
        
        # Count class transitions
        class_pattern = r'class\s+(\w+)'
        classes = re.findall(class_pattern, content)
        measure.class_transitions = len(classes) - 1 if classes else 0
        
        # Count context switches (this., super., etc.)
        measure.context_switches = content.count('this.') + content.count('super.')
        
        # Count async/await (abstraction jumps)
        measure.abstraction_jumps = content.count('async ') + content.count('await ')
        
        return measure
    
    def analyze_java_file(self, content: str, measure: DiscontinuityMeasure) -> DiscontinuityMeasure:
        """Analyze Java file for discontinuities"""
        # Count imports
        import_pattern = r'import\s+(.*?);'
        imports = re.findall(import_pattern, content)
        measure.file_imports = len(imports)
        
        # Count method calls
        call_pattern = r'(\w+)\s*\('
        calls = re.findall(call_pattern, content)
        measure.function_calls = len(calls)
        
        # Count class usage
        new_pattern = r'new\s+(\w+)'
        news = re.findall(new_pattern, content)
        measure.class_transitions = len(news)
        
        # Context switches
        measure.context_switches = content.count('this.') + content.count('super.')
        
        # Abstraction jumps (interfaces, abstracts, annotations)
        measure.abstraction_jumps = (
            content.count('@') + 
            content.count('implements ') + 
            content.count('extends ')
        )
        
        return measure
    
    def analyze_elixir_file(self, content: str, measure: DiscontinuityMeasure) -> DiscontinuityMeasure:
        """Analyze Elixir file for discontinuities"""
        # Count imports/aliases
        import_pattern = r'(import|alias|use)\s+(\w+)'
        imports = re.findall(import_pattern, content)
        measure.file_imports = len(imports)
        
        # Count function calls (including pipe operator)
        pipe_pattern = r'\|>\s*(\w+)'
        pipes = re.findall(pipe_pattern, content)
        measure.function_calls = len(pipes)
        
        # Count module references
        module_pattern = r'(\w+)\.(\w+)\('
        modules = re.findall(module_pattern, content)
        measure.namespace_switches = len(set(modules))
        
        # Pattern matching creates cognitive load
        pattern_matches = content.count('case ') + content.count('with ')
        measure.context_switches = pattern_matches
        
        # Macros and behaviours are abstraction jumps
        measure.abstraction_jumps = (
            content.count('defmacro') + 
            content.count('@behaviour') +
            content.count('use ')
        )
        
        return measure
    
    def analyze_directory(self, directory: Path, extensions: List[str] = None) -> Dict[Path, DiscontinuityMeasure]:
        """Analyze all files in a directory"""
        if extensions is None:
            extensions = ['.py', '.js', '.ts', '.jsx', '.tsx', '.java', '.ex', '.exs']
        
        results = {}
        for filepath in directory.rglob('*'):
            if filepath.is_file() and filepath.suffix in extensions:
                # Skip common non-source files
                if any(skip in str(filepath) for skip in ['node_modules', '__pycache__', '.git', 'build', 'dist']):
                    continue
                    
                print(f"Analyzing {filepath}")
                results[filepath] = self.analyze_file(filepath)
        
        return results
    
    def calculate_coupling(self, directory: Path) -> Dict[Tuple[Path, Path], float]:
        """Calculate coupling between files based on imports"""
        coupling_scores = {}
        
        # Build import relationships
        for filepath in directory.rglob('*.py'):  # Example for Python
            if filepath.is_file():
                try:
                    with open(filepath, 'r') as f:
                        content = f.read()
                    tree = ast.parse(content)
                    
                    for node in ast.walk(tree):
                        if isinstance(node, ast.ImportFrom) and node.module:
                            if node.module.startswith('.'):
                                # Relative import - indicates coupling
                                imported_file = self.resolve_import(filepath, node.module)
                                if imported_file:
                                    coupling_scores[(filepath, imported_file)] = 1.0
                                    
                except Exception:
                    continue
        
        return coupling_scores
    
    def resolve_import(self, current_file: Path, import_path: str) -> Optional[Path]:
        """Resolve relative import to actual file path"""
        # Simplified implementation
        parts = import_path.strip('.').split('.')
        base_dir = current_file.parent
        
        # Go up directories for leading dots
        dot_count = len(import_path) - len(import_path.lstrip('.'))
        for _ in range(dot_count - 1):
            base_dir = base_dir.parent
        
        # Build target path
        target = base_dir
        for part in parts:
            target = target / part
        
        # Check for Python file
        if (target.with_suffix('.py')).exists():
            return target.with_suffix('.py')
        
        # Check for package
        init_file = target / '__init__.py'
        if init_file.exists():
            return init_file
            
        return None


class TemporalAnalyzer:
    """Analyzes temporal patterns in code changes"""
    
    def __init__(self):
        self.change_sequences: List[List[Path]] = []
        self.file_timestamps: Dict[Path, List[float]] = defaultdict(list)
        
    def add_change_sequence(self, files: List[Path], timestamp: float) -> None:
        """Add a sequence of files changed together"""
        self.change_sequences.append(files)
        for file in files:
            self.file_timestamps[file].append(timestamp)
    
    def calculate_temporal_coupling(self) -> Dict[Tuple[Path, Path], float]:
        """Calculate temporal coupling between files"""
        coupling = defaultdict(int)
        
        # Count co-occurrences
        for sequence in self.change_sequences:
            for i, file1 in enumerate(sequence):
                for file2 in sequence[i+1:]:
                    pair = tuple(sorted([file1, file2]))
                    coupling[pair] += 1
        
        # Normalize by total changes
        normalized_coupling = {}
        for (file1, file2), count in coupling.items():
            total_changes = min(len(self.file_timestamps[file1]), 
                              len(self.file_timestamps[file2]))
            if total_changes > 0:
                normalized_coupling[(file1, file2)] = count / total_changes
        
        return normalized_coupling
    
    def identify_hotspots(self, threshold: float = 0.8) -> List[Path]:
        """Identify files that change frequently"""
        hotspots = []
        
        for file, timestamps in self.file_timestamps.items():
            if len(timestamps) > len(self.change_sequences) * threshold:
                hotspots.append(file)
        
        return hotspots


def calculate_exponential_penalty(discontinuities: int, alpha: float = 0.2) -> float:
    """
    Calculate the exponential comprehension penalty.
    Based on FP-012: T = T_base × (1 + α)^d
    """
    return (1 + alpha) ** discontinuities


def compare_models(discontinuities: List[int], times: List[float]) -> Dict[str, Dict]:
    """Compare different comprehension models against empirical data"""
    import numpy as np
    from scipy.optimize import curve_fit
    
    # Define models
    def exponential_model(d, t_base, alpha):
        return t_base * ((1 + alpha) ** d)
    
    def linear_model(d, t_base, slope):
        return t_base + slope * d
    
    def logarithmic_model(d, t_base, scale):
        return t_base * np.log(1 + scale * d)
    
    # Fit each model
    results = {}
    
    try:
        # Exponential fit
        popt_exp, _ = curve_fit(exponential_model, discontinuities, times, p0=[5.0, 0.2])
        exp_pred = [exponential_model(d, *popt_exp) for d in discontinuities]
        exp_error = np.mean((np.array(times) - np.array(exp_pred))**2)
        results['exponential'] = {
            'params': {'t_base': popt_exp[0], 'alpha': popt_exp[1]},
            'mse': exp_error,
            'predictions': exp_pred
        }
    except:
        results['exponential'] = {'error': 'Failed to fit'}
    
    try:
        # Linear fit
        popt_lin, _ = curve_fit(linear_model, discontinuities, times, p0=[5.0, 1.0])
        lin_pred = [linear_model(d, *popt_lin) for d in discontinuities]
        lin_error = np.mean((np.array(times) - np.array(lin_pred))**2)
        results['linear'] = {
            'params': {'t_base': popt_lin[0], 'slope': popt_lin[1]},
            'mse': lin_error,
            'predictions': lin_pred
        }
    except:
        results['linear'] = {'error': 'Failed to fit'}
    
    try:
        # Logarithmic fit
        popt_log, _ = curve_fit(logarithmic_model, discontinuities, times, p0=[5.0, 1.0])
        log_pred = [logarithmic_model(d, *popt_log) for d in discontinuities]
        log_error = np.mean((np.array(times) - np.array(log_pred))**2)
        results['logarithmic'] = {
            'params': {'t_base': popt_log[0], 'scale': popt_log[1]},
            'mse': log_error,
            'predictions': log_pred
        }
    except:
        results['logarithmic'] = {'error': 'Failed to fit'}
    
    return results