## Finding Markers for Cell Differentiation

Researchers collected cells at each of the stages of cardiomyocyte differentiation to study how cell identity changes as differentiation progresses. To evaluate differentations on a stage-by-stage basis, we needed to find markers that distinguished each stage of cardiomyocyte differentiation from one another.

During RNA-seq, all of the mRNA of the cell is collected and processed into DNA by the action of an enzyme called reverse transcriptase. This cDNA ("copy" DNA) is then sequenced; the levels of cDNA for each gene directly correlate with its mRNA levels, and thus its gene expression.

We thus parsed the given RNA-seq data using regular expressions to extract the common gene names and the levels of cDNA corresponding to the specified stage of differentiation.