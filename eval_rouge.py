from rouge import Rouge

def calculate_rouge_score(generated_text, reference_text):
    # Initialize the Rouge object
    rouge = Rouge()

    # Calculate ROUGE scores
    scores = rouge.get_scores(generated_text, reference_text)

    # Extract individual ROUGE scores
    rouge_1 = scores[0]['rouge-1']
    rouge_2 = scores[0]['rouge-2']
    rouge_l = scores[0]['rouge-l']

    return {
        'rouge-1': rouge_1,
        'rouge-2': rouge_2,
        'rouge-l': rouge_l
    }

# Example usage
generated_text = "The paper presents a new approach to active learning called Cluster-Margin that achieves both efficiency and effectiveness. The proposed algorithm is shown to outperform existing methods like CoreSet and BADGE on various datasets. The authors provide initial theoretical guarantees to explain the improvements. The results on Open Images, a real-world dataset, are particularly impressive as they demonstrate good performance on a large-scale benchmark. The paper also provides a good comparison to other methods on the same dataset.Overall, the paper presents an interesting new approach to active learning that achieves good performance while being more efficient. The results provide evidence that the proposed method is of practical significance."
reference_text = "Reviewers reached a consensus by which the paper is not ready for publication.  Several concerns were raised, most notably: Only an upper bound on the excess risk is derived, which is insufficient for establishing a double descent phenomenon (for that, a matching lower bound is required). While experiments indicate that the upper bound may be tight after many iterations, it seems that in the early phases of a run it is not.  This is particularly problematic since in late stages of a run the model may in fact be close to convergence, and at convergence optimization reaches the Moore-Penrose solution, which was heavily analyzed in prior work (hinting that the regime in which the analysis is valid is one that is already well understood). The experiments on deep neural networks are somewhat disconnected from the theory, and this warrants a more thorough empirical investigation. I encourage the authors to make use of the above feedback in revising their paper towards future submission."

rouge_scores = calculate_rouge_score(generated_text, reference_text)

print("ROUGE-1 Score:")
print(f"  Precision: {rouge_scores['rouge-1']['p']:.4f}")
print(f"  Recall: {rouge_scores['rouge-1']['r']:.4f}")
print(f"  F1-score: {rouge_scores['rouge-1']['f']:.4f}")

print("\nROUGE-2 Score:")
print(f"  Precision: {rouge_scores['rouge-2']['p']:.4f}")
print(f"  Recall: {rouge_scores['rouge-2']['r']:.4f}")
print(f"  F1-score: {rouge_scores['rouge-2']['f']:.4f}")

print("\nROUGE-L Score:")
print(f"  Precision: {rouge_scores['rouge-l']['p']:.4f}")
print(f"  Recall: {rouge_scores['rouge-l']['r']:.4f}")
print(f"  F1-score: {rouge_scores['rouge-l']['f']:.4f}")

