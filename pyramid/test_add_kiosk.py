# coding=utf-8
__author__ = 'jim'
# k_dict = {}
# k_upc = "u1"
# k_upc2 = "u2"
# k_id = "k1"
# k_id2 = "k2"
# k_dict[k_id] = [k_upc]
# k_dict[k_id].append(k_upc2)
# k_dict[k_id2] = [k_upc]
# k_dict[k_id2].append(k_upc2)
# print k_dict
# for index in k_dict:
#     print index


def recursion(a):
    if a > 10:
        return "Finished"
    else:
        a += 1
        print a
        recursion(a)


if __name__ == "__main__":
    a = {"1": "2"}
    if a:
        for i in range(2):
            print "1   ",
    else:
        print 2
    import sys

    a = sys.argv[1:]
    for arg in a:
        try:
            arg = int(arg)
        except ValueError as e:
            print "%s is not int" % arg
