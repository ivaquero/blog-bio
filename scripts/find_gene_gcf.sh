#!/bin/bash /bin/zsh
declare -a gcf_files
declare -a gene_objects

# your gcf files
gcf_files=(011058795.1_ASM1105879v1_cds)
# your gene gene_objects
gene_objects=(dnaA)
# your data path
data="."
# your output folder
output="genes"

if [[ ! -d $output ]]; then
    mkdir -p $output
fi

for gcf_file in "${gcf_files[@]}"; do
    for gene_object in "${gene_objects[@]}"; do
        rg -U ">lcl.+gene=${gene_object}.+[\w\n]+" <${data}/GCF_"${gcf_file}"_from_genomic.fna >${output}/"${gene_object}".txt
    done
done
