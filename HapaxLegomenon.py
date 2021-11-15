import re
import time

def HapaxCounter():
    file = open("test", "r")
    myStr = file.read().lower()
    myDict = dict()
    trimmedStr = ""
    myList = []
    for pm in [",", ".", "!", "?", ":", "_", "*", '"', "[", "]", "(", ")", "&", ";", "-", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
        myStr = myStr.replace(pm, "")
    for wr in myStr.split():
        if myDict.get(wr) == None:
            myDict[wr] = 1
        else:
            myDict[wr] += 1
    for i in myDict:
        if myDict.get(i) > 1:
            continue
        else:
            myList.append(i)
            print(i)
    print(myList)
    file.close()


def WriteNewFile():
    file = open("test", "r")
    output = open("SASSandLESSex", "w")
    oldlines = file.readlines()
    print(oldlines)
    for i in range(len(oldlines)):
        output.write(f"({i+1}) {oldlines[i]}")
    file.close()
    output.close()


def WordLenAvg():
    file = open("test", "r")
    myStr = file.read().lower()
    ttl_l = 0
    for wr in myStr.split():
        ttl_l += len(wr)
    print("{:.2f}".format(ttl_l / len(myStr.split())))
    file.close()


def sent_split():
    file = open("test", "r")
    myStr = file.read().replace("\n", " ")
    output = open("sent-split-output", "w")
    pattern1 = "[a-z]\.[a-z]"
    pattern2 = ".[0-9]"
    for l in myStr.split():
        if "." in l:
            if l[0].isupper():
                print(l[0])
                output.write(f"{l} ")
            elif re.search(pattern1, l):
                output.write(f"{l} ")
            elif re.search(pattern2, l):
                output.write(f"{l} ")
            else:
                output.write(f"{l}\n")
        elif "?" in l or "!" in l:
            output.write(f"{l}\n")
        else:
            output.write(f"{l} ")
    file.close()
    output.close()


# I tried my best sir...
ttl_travs = 0
def XtraChallenge(u):
    adjlist = {
        'audino': [],
        'bagon': ['nosepass'],
        'baltoy': ['yamask'],
        'banette': ['emboar', 'emolga', 'exeggcute'],
        'bidoof': ['jellicent', 'jumpluff'],
        'braviary': ['yamask'],
        'bronzor': ['registeel', 'relicanth', 'remoraid', 'rufflet'],
        'carracosta': ['audino'],
        'charmeleon': ['nosepass'],
        'cresselia': ['audino'],
        'croagunk': ['kangaskhan', 'kricketune'],
        'darmanitan': ['nosepass'],
        'deino': [],
        'emboar': ['registeel', 'relicanth', 'remoraid', 'rufflet'],
        'emolga': ['audino'],
        'exeggcute': ['emboar', 'emolga'],
        'gabite': ['emboar', 'emolga', 'exeggcute'],
        'girafarig': ['gabite', 'gulpin'],
        'gulpin': ['nosepass'],
        'haxorus': ['sableye', 'scolipede', 'scrafty', 'seaking', 'sealeo', 'silcoon', 'simisear', 'snivy', 'snorlax', 'spoink', 'starly'],
        'heatmor': ['registeel', 'relicanth', 'remoraid', 'rufflet'],
        'heatran': ['nosepass'],
        'ivysaur': ['registeel', 'relicanth', 'remoraid', 'rufflet'],
        'jellicent': ['tirtouga', 'trapinch', 'treecko', 'tyrogue'],
        'jumpluff': [],
        'kangaskhan': ['nosepass'],
        'kricketune': ['emboar', 'emolga', 'exeggcute'],
        'landorus': ['sableye', 'scolipede', 'scrafty', 'seaking', 'sealeo', 'silcoon', 'simisear', 'snivy', 'snorlax', 'spoink', 'starly'],
        'ledyba': ['audino'],
        'loudred': ['darmanitan', 'deino'],
        'lumineon': ['nosepass'],
        'lunatone': ['emboar', 'emolga', 'exeggcute'],
        'machamp': ['petilil', 'pidgeotto', 'pikachu', 'pinsir', 'poliwrath', 'poochyena', 'porygon2', 'porygonz'],
        'magnezone': ['emboar', 'emolga', 'exeggcute'],
        'mamoswine': ['emboar', 'emolga', 'exeggcute'],
        'nosepass': ['sableye', 'scolipede', 'scrafty', 'seaking', 'sealeo', 'silcoon', 'simisear', 'snivy', 'snorlax', 'spoink', 'starly'],
        'petilil': ['landorus', 'ledyba', 'loudred', 'lumineon', 'lunatone'],
        'pidgeotto': [],
        'pikachu': [],
        'pinsir': ['registeel', 'relicanth', 'remoraid', 'rufflet'],
        'poliwrath': ['haxorus', 'heatmor', 'heatran'],
        'poochyena': ['audino'],
        'porygon2': [],
        'porygonz': [],
        'registeel': ['landorus', 'ledyba', 'loudred', 'lumineon', 'lunatone'],
        'relicanth': ['haxorus', 'heatmor', 'heatran'],
        'remoraid': ['darmanitan', 'deino'],
        'rufflet': ['tirtouga', 'trapinch', 'treecko', 'tyrogue'],
        'sableye': ['emboar', 'emolga', 'exeggcute'],
        'scolipede': ['emboar', 'emolga', 'exeggcute'],
        'scrafty': ['yamask'],
        'seaking': ['gabite', 'girafarig', 'gulpin'],
        'sealeo': [],
        'silcoon': ['nosepass'],
        'simisear': ['registeel', 'relicanth', 'remoraid', 'rufflet'],
        'snivy': ['yamask'],
        'snorlax': [],
        'spoink': ['kangaskhan', 'kricketune'],
        'starly': ['yamask'],
        'tirtouga': ['audino'],
        'trapinch': ['haxorus', 'heatmor', 'heatran'],
        'treecko': [],
        'tyrogue': ['emboar', 'emolga', 'exeggcute'],
        'vigoroth': ['haxorus', 'heatmor', 'heatran'],
        'vulpix': [],
        'wailord': ['darmanitan', 'deino'],
        'wartortle': ['emboar', 'emolga', 'exeggcute'],
        'whismur': ['registeel', 'relicanth', 'remoraid', 'rufflet'],
        'wingull': ['landorus', 'ledyba', 'loudred', 'lumineon', 'lunatone'],
        'yamask': ['kangaskhan', 'kricketune']
    }

    status = {} #UEX = unexplored, TRV = traversed, FEX = fully explored
    parent = {}
    trav_time = {} #traversals done
    all_paths = []
    dfs_output = []

    # initialise directed graph
    for node in adjlist.keys():
        status[node] = "UEX"
        parent[node] = None
        trav_time[node] = [-1, -1]


    def dfs(current_node):
        global ttl_travs
        status[current_node] = "TRV"
        trav_time[current_node][0] = ttl_travs
        dfs_output.append(current_node)
        ttl_travs += 1

        for vertex in adjlist[current_node]:
            if status[vertex] == "UEX":
                parent[vertex] = current_node
                dfs(vertex)
            elif adjlist[vertex] == None:
                all_paths.append(dfs_output)
        status[current_node] = "FEX"
        trav_time[current_node][1] = ttl_travs


        trav_dist = {}
        longest_path = trav_time.get('audino')[1]-trav_time.get('audino')[0]
        for paths in trav_time.items():
            trav_dist[paths[0]] = paths[1][1]-paths[1][0]
            longest_path = max(paths[1][1]-paths[1][0], longest_path)

        for i in range(len(dfs_output)):
            if dfs_output[i-1][-1] == dfs_output[i][0] and i != 0:
                continue
            else:
                all_paths.append(dfs_output[0:i-1])

        return longest_path, dfs_output

    print(dfs(u))


XtraChallenge('machamp')
#after extensive testing, I found machamp to have the biggest tree

