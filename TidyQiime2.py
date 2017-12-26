import re
print('This script is used to tidy Qiime2 generated taxnomic file!/nIf you have any trouble using this script./nPlease contact the author./n')

# define the input file direcotry
filepath = input('Your QIIME2 taxonomic assignment document directory?\n')
newfilepath = 'Taxonomy_clean.txt'

taxfile = open(filepath, 'r')
taxfile_clean = open(newfilepath, 'w')


# define which taxonomic database was used
while True :
    database = input('Which database was used? [Greengene or SILVA]\n')
    if database.lower() == 'greengene':
        pattern = '(?<=\w__).+|(Seq\d)'
        break
    elif database.lower() == 'silva':
        pattern = '(?<=D_\d__).+|(Seq\d)'
        break
    else:
        print("invalid database: '%s'\n" % database) 


# initiate with header
taxfile_clean.write('SeqID\tKingdom\tPhylum\tOrder\tClass\tFamily\tGenus\tSpecies\n')

for line in taxfile.readlines()[1:]:
    line_list = re.split('\t|;', line)
    line_list_clean = []
    for element in line_list[:-1]:
        try:
            line_list_clean.append(re.search(pattern, element).group(0))
        except AttributeError:
            line_list_clean.append('')
    line_clean = '\t'.join(line_list_clean)
    taxfile_clean.write(line_clean + '\n')

taxfile.close()
taxfile_clean.close()

print('Job finished! Tidyed file "Taxonomy_clean.txt" is generrated under your working directory!')