# Research data management and release checklist

Use this checklist before adding real papers, datasets, annotations or experiment outputs to the repository.

## Source papers and corpus
- Record an immutable paper/source ID, full bibliographic metadata, official URL/DOI, version and access date.
- Record the relevant license, terms of use and redistribution permissions.
- Distinguish abstract access, selected-section access and full-text inspection.
- Do not upload PDFs or full-text passages merely because they are publicly accessible online. Confirm that redistribution is permitted.
- Prefer storing source IDs, evidence locations and short permitted quotations over copying entire papers into Git.

## Generated summaries and prompts
- Preserve exact input prompts, model/provider/version, generation settings and timestamps.
- Keep raw generated summaries unchanged; store normalized or segmented copies as derived artifacts.
- Retain citation marker-to-paper mappings so claim-citation pairs can be reconstructed.
- Do not silently repair fabricated or malformed citations; record verification outcomes.

## Human annotation
- Preserve independent annotator records as separate rows/files.
- Record annotation-guide version and source version for every annotation round.
- Keep adjudicated labels separate from original labels and retain adjudication rationale.
- Store evidence availability independently from support labels.
- Do not turn inaccessible or unretrieved material into NOT_SUPPORTED_IN_INSPECTED_SOURCE.

## Repository hygiene
- Keep restricted/raw data outside Git unless release terms permit publication.
- Use the provided ignored paths for local raw data, interim files, annotations, checkpoints and generated results.
- Never commit API keys, credentials, private links or personal data.
- Record checksums for large authorized datasets and model checkpoints without committing restricted files.

## Before releasing a dataset or result
- Verify all permissions and licenses.
- Confirm that no restricted source text or personally identifying data is included.
- Check paper-level split integrity.
- Document inclusion/exclusion criteria, missingness, access failures and retrieval failures.
- Record exact code revision, runtime, package versions, model revision, commands, seed and output checksums.
