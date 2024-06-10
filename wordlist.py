import itertools
import os

def create_wordlist(name):
    wordlist = []

    wordlist.append(name)

    wordlist.append(name.upper())
    wordlist.append(name.lower())

    subs = {"a": "4", "e": "3", "i": "1", "o": "0", "s": "$"}
    for key, value in subs.items():
        wordlist.append(name.replace(key, value))
        wordlist.append(name.replace(key, value))
        wordlist.append(name.replace(key, value).lower())
        wordlist.append(name.replace(key, value).upper())

    for char in name:
        wordlist.append(name + char)
        wordlist.append(char + name)

    wordlist.append(name[::-1])

    for letter in name:
        wordlist.append(name.replace(letter, letter.upper()))
        wordlist.append(name.replace(letter, letter.lower()))



    for n in range(100):
        wordlist.append(str(n) + name)

    for n in range(100):
        wordlist.append(name + str(n))

    for n in range(100):
        wordlist.append(str(n) + name + str(n))


    return wordlist

def names_combinations(names):
    combinations = []

    permutation = itertools.permutations(names)

    for perm in permutation:
        combination_perm = "".join(perm)
        combinations.append(combination_perm)

    return combinations


def write_file(wordlist):
    with open("wordlist.txt", "a") as file:
        for word in wordlist:
            file.write(word + "\n")

def check_size(name_file):
    if (os.path.exists(name_file)):
        size = os.path.getsize(name_file)
        return size
    else:
        return None


if __name__ == "__main__":
    print('''\033[1;92m
               ⠀⣀⡀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⣴⣾⡿⠿⠿⠿⠷⠦⠿⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⡉⠛⢠⣾⣷⡀⠰⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠸⠇⠀⣈⣀⣀⣀⣀⠈⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠲⣶⡄⠘⠛⠛⠛⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⡀⠻⣿⠿⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⢴⣶⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢁⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠋⣉⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣀⣠⣤⣶⠶⠶⠟⠛⠛⠛⠋⠁⠀⠀⠀⣿⣿⣿⣧⠀⣀⡀⠀⠀⠀⠀
⠀⠀⠀⠰⣿⣿⠷⠶⠶⠿⠿⠿⠿⠿⠿⠿⠿⠿⢁⣿⣿⣿⣿⠀⠿⢛⣻⡆⠀⠀
⠀⠀⢀⣠⣤⣤⣤⣶⣶⣶⣶⣶⡶⠶⠖⠒⢀⣤⣾⣿⣿⣿⡟⢀⣾⣿⡿⠃⠀⠀
⠀⠀⠘⠿⣿⣿⣿⣷⣶⣶⣶⣶⣶⣶⣶⣿⣿⣿⣿⡿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ A simple wordlist gerator
    \33[m''')


    while (True):
        try:
            opc = str(input("[?] Use name combination?(Y/N)").upper())

            if (opc == "Y"):
                names = str(input("[*] Space-separated names (ex: network password):")).split()
                if not names:
                    print("\033[1;91m[!] Empty area, try again\033[m")
                    continue
                else:
                    combinations = names_combinations(names)

                    for comb in combinations:
                        print("\033[1;92m[*] creating wordlist from combination:\033[m{}".format(comb))
                        wordlist = create_wordlist(comb)
                        try:
                           write_file(wordlist)

                        except Exception as e:
                            print("\033[1;91m[!] error creating txt file:{}\033[m".format(e))
                            break

            elif (opc == "N"):
                name = str(input("[*] Name for the wordlist:"))
                if not name:
                    print("\033[1;91m[!] Empty field, please try again\033[m")
                    continue
                else:
                    wordlist = create_wordlist(name)
                    try:
                        write_file(wordlist)

                    except Exception as e:
                        print("\033[1;91m[!] error creating txt file:{}\033[m".format(e))
                        break

                    print("\033[1;92m[*] wordlist created, name: wordlist.txt\033[m")
            wordlist_size = check_size("wordlist.txt")
            if (wordlist_size is not None):
                print("\n\033[1;92m[*] size of wordlist.txt in bytes:\033[m{}".format(wordlist_size))
            else:
                print("\n\033[1;91m[!] wordlist.txt not found.\033[m")
            break
        except KeyboardInterrupt:
            print("\n\n\033[1;91m[!] Operation interrupted by user\033[m")
