import os
from dotenv import load_dotenv

# Load environment variables (must be before LangChain imports)
load_dotenv()

from chains.extraction_chain import extraction_chain
from chains.matching_chain import matching_chain
from chains.scoring_chain import scoring_chain
from chains.explaination_chain import explanation_chain
from data.resume import STRONG_RESUME, AVERAGE_RESUME, WEAK_RESUME
from data.job_description import JOB_DESCRIPTION


def screen_resume(resume: str, candidate_type: str) -> dict:
    """
    Full pipeline: Extract → Match → Score → Explain
    """
    print(f"\n{'='*60}")
    print(f"Processing: {candidate_type} Candidate")
    print('='*60)

    # Step 1: Skill Extraction
    print("\n[Step 1] Extracting skills...")
    extraction_result = extraction_chain.invoke({"resume": resume})
    extracted_info = extraction_result.content
    print(extracted_info)

    # Step 2: Matching
    print("\n[Step 2] Matching with job requirements...")
    match_result = matching_chain.invoke({
        "extracted_info": extracted_info,
        "job_description": JOB_DESCRIPTION
    })
    match_output = match_result.content
    print(match_output)

    # Step 3: Scoring
    print("\n[Step 3] Scoring the candidate...")
    score_result = scoring_chain.invoke({
        "match_result": match_output,
        "job_description": JOB_DESCRIPTION
    })
    score_output = score_result.content
    print(score_output)

    # Step 4: Explanation
    print("\n[Step 4] Generating explanation...")
    explanation_result = explanation_chain.invoke({
        "score": score_output,
        "match_result": match_output,
        "extracted_info": extracted_info
    })
    explanation_output = explanation_result.content
    print(explanation_output)

    return {
        "candidate_type": candidate_type,
        "extracted_info": extracted_info,
        "match_result": match_output,
        "score": score_output,
        "explanation": explanation_output
    }


if __name__ == "__main__":
    resumes = [
        (STRONG_RESUME, "Strong"),
        (AVERAGE_RESUME, "Average"),
        (WEAK_RESUME, "Weak"),
    ]

    results = []
    for resume, label in resumes:
        result = screen_resume(resume, label)
        results.append(result)

    # Summary
    print("\n\n" + "="*60)
    print("FINAL SUMMARY")
    print("="*60)
    for r in results:
        print(f"\n{r['candidate_type']} Candidate → {r['score'].strip()}")
        print(f"Recommendation: {r['explanation'][:200]}...")