import json
import argparse
import glob
import os

def loadjson_data(filename):
    with open(filename, 'r', encoding='utf-8') as fr:
        samples = json.load(fr)
        fr.close()
    return samples


def writejson_data(filename, data):
    with open(filename, 'w', encoding='utf-8') as fw:
        data = json.dumps(data, indent=2, ensure_ascii=False)
        fw.write(data)
        fw.close()
    return True

def get_connected_components(graph):
    seen = []
    components = []
    count = 0

    for node in graph.keys():
        if node not in seen:
            count += 1
            component = []
            nodes = [node]
            while nodes:
                node = nodes[-1]
                nodes = nodes[:-1]
                seen.append(node)
                component.append(node)
                for n in graph[node]:
                    if n not in nodes and n not in seen:
                        nodes.append(n)
            components.append(component)
    components.sort()
    return components

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--inputpath', default='data/task1_test_new/output', type=str,
                        help="list of input folder")
    parser.add_argument('--outputpath', default='data/task1_test_new/output',
                        help="list of output folder")
    args = parser.parse_args()

    list_file_score = glob.glob(os.path.join(args.inputpath, "*.json"))
    list_file_score.sort()
    print(len(list_file_score))
    duplicate = {}
    list_paragraph_duplicate = []
    for f in list_file_score:
        print(f)
        d = loadjson_data(f)
        for para_query in d:
            for i in range(len(para_query['candidates'])-1):
                if abs(para_query['candidates'][i]['bm25'] - para_query['candidates'][i+1]['bm25']) < 0.001 and para_query['candidates'][i]['id'].split('-')[1] == para_query['candidates'][i+1]['id'].split('-')[1]: #
                    pair = [para_query['candidates'][i]['id'], para_query['candidates'][i+1]['id']]
                    pair.sort()
                    list_paragraph_duplicate.append(tuple(pair))

    list_paragraph_duplicate = list(set(list_paragraph_duplicate))
    print(len(list_paragraph_duplicate))
    for d in list_paragraph_duplicate:
        if d[0].split('-')[0] not in duplicate.keys():
            duplicate[d[0].split('-')[0]] = {d[1].split('-')[0]:1}
        else:
            if d[1].split('-')[0] not in duplicate[d[0].split('-')[0]].keys():
                duplicate[d[0].split('-')[0]][d[1].split('-')[0]] = 1
            else:
                duplicate[d[0].split('-')[0]][d[1].split('-')[0]] += 1

        if d[1].split('-')[0] not in duplicate.keys():
            duplicate[d[1].split('-')[0]] = {d[0].split('-')[0]: 1}
        else:
            if d[0].split('-')[0] not in duplicate[d[1].split('-')[0]]:
                duplicate[d[1].split('-')[0]][d[0].split('-')[0]] = 1
            else:
                duplicate[d[1].split('-')[0]][d[0].split('-')[0]] += 1
    for case_id in list(duplicate.keys()):
        for k in list(duplicate[case_id].keys()):
            if duplicate[case_id][k] <= 2:
                del duplicate[case_id][k]
        if duplicate[case_id] == {}:
            del duplicate[case_id]
    for case_id in list(duplicate.keys()):
        duplicate[case_id] = list(duplicate[case_id].keys())
    clusters = get_connected_components(duplicate)

    len_can = 0
    for c in clusters:
        len_can += len(c)
    print(len(duplicate), len(clusters), len_can)

    writejson_data(args.outputpath + '/cluster_test.json', clusters)
    cluster_id_to_case = {}
    case_to_cluster_id = {}

    for i, cluster in enumerate(clusters):
        cluster_id = 'duplicate@'+str(i)
        cluster_id_to_case[cluster_id] = cluster
        for case in cluster:
            case_to_cluster_id[case] = cluster_id

    writejson_data(args.outputpath + '/cluster_to_case_test.json', cluster_id_to_case)
    writejson_data(args.outputpath + '/case_to_cluster_test.json', case_to_cluster_id)

