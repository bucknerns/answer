from collections import Counter
from io import StringIO
import csv


# does not support duplicate items
def array_diff(current, target):
    cset, tset = set(current), set(target)
    adds = list(tset - cset)
    dels = list(cset - tset)
    print("additions: {0}".format(adds))
    print("deletions: {0}".format(dels))
    return adds, dels


def array_diff_dup_support(current, target):
    cset, tset = Counter(current), Counter(target)
    adds_dict = tset - cset
    dels_dict = cset - tset
    adds = [i for i, c in adds_dict.items() for _ in range(c)]
    dels = [i for i, c in dels_dict.items() for _ in range(c)]
    print("additions: {0}".format(adds))
    print("deletions: {0}".format(dels))
    return adds, dels


def get_followers(csv_file=None):
    if csv_file is not None:
        fp = open(csv_file)
    else:
        fp = StringIO()
        fp.write(u"postId, repostId, followers\n1, -1, 120\n2, 1, 60\n3, 1, 30"
                 u"\n4, 2, 90\n5, 3, 40\n6, 4, 10\n7, -1, 240\n8, 7, 190\n9, 7"
                 u", 50")
        fp.seek(0)

    reader = csv.reader(fp, delimiter=",")
    posts = {}
    for pid, rpid, followers in list(reader)[1:]:
        pid, rpid, followers = int(pid), int(rpid), int(followers)
        if rpid == -1:
            posts[pid] = {"pids": set()}
            posts[pid]["pids"].add(pid)
            posts[pid]["followers"] = followers
            continue
        else:
            for _, dic in posts.items():
                if rpid in dic["pids"]:
                    dic["pids"].add(pid)
                    dic["followers"] += followers
    for pid, dic in posts.items():
        print("{0}: {1}".format(pid, dic["followers"]))

        
if __name__ == "__main__":
    data = {"current": [1, 3, 5, 6, 8, 9], "target": [1, 2, 5, 7, 9]}
    data2 = {"current": [1, 1, 3, 5, 6, 8, 9], "target": [1, 2, 5, 7, 9]}
    array_diff(**data)
    array_diff_dup_support(**data2)
    get_followers()
