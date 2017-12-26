import sys
import os

def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")

location = query_yes_no('Is this the direcotry where your lefse file located?\nAlso make sure the first row includes your subject information and the second row includes grouping variable!\n')

if not location:
    print('Please change to the direcotry where your lefse file located')
    os._exit(0)

if not os.path.exists('lefse_result'):
    os.makedirs('lefse_result/Figures')

for filename in os.listdir():
    if filename.endswith('.txt'):
        file_in = str(filename.split('.')[0]) + '.in'
        file_res = str(filename.split('.')[0]) + '.res'
        file_his = str(filename.split('.')[0]) + '.pdf'
        file_clad = str(filename.split('.')[0]) + '.cladogram.pdf'
        os.system('format_input.py ' + filename + ' ' + file_in + ' -c 2 -s 1')
        os.system('run_lefse.py ' + file_in + ' ' + file_res)
        os.system('plot_res.py ' + file_res + ' lefse_result/Figures/' + file_his + ' --format pdf')
        os.system('plot_cladogram.py ' + file_res + ' lefse_result/Figures/' + file_clad + ' --format pdf')

print('The script has (maybe) run successfully! The result has been stored in lefse_result.')
