echo "problem10"
wc -l ./popular-names.txt

echo "problem11"
expand popular-names.txt

echo "problem12"
cut -f 1 popular-names.txt > col1_check.txt
cut -f 2 popular-names.txt > col2_check.txt

echo "problem13"
paste col1_check.txt col2_check.txt > merge_columns_check.tsv

echo "problem14"
head -n 3 popular-names.txt

echo "problem15"
tail -n 4 popular-names.txt

echo "problem16"
split -n 2 -d popular-names.txt popular-names_split_check-

echo "problem17"
cut -f 1 popular-names.txt | sort | uniq

echo "problem18"
cat ./popular-names.txt | sort -rnk 3 

echo "problem19"
cut -f 1 ./popular-names.txt | sort | uniq -c | sort -rn


