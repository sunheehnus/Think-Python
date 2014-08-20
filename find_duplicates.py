#!/usr/bin/env python
# encoding: utf-8

import os
def walk(dirname):
    names = []
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            names.append(path)
        else:
            names.extend(walk(path))
    return names

def compute_checksum(filename):
    cmd = 'md5sum ' + filename
    return pipe(cmd)

def check_diff(name1, name2):
    cmd = 'diff %s %s' % (name1, name2)
    return pipe(cmd)

def pipe(cmd):
    fp = os.popen(cmd)
    res = fp.read()
    stat = fp.close()
    assert stat is None
    return res, stat

def compute_checksums(dirname, suffix):
    names = walk(dirname)

    d = {}
    names = [name for name in names if name.endswith(suffix)]
    for name in names:
        res, stat = compute_checksum(name)
        checksum, _ = res.split()

        if checksum in d:
            d[checksum].append(name)
        else:
            d[checksum] = [name]
    return d

def check_pairs(names):
    for name1 in names:
        for name2 in names:
            if name1 < name2:
                res, stat = check_diff(name1, name2)
                if res:
                    return False
    return True

def print_duplicates(d):
    for key, names in d.items():
        if len(names) > 1:
            print 'The following files have the same checksum:'
            for name in names:
                print name
            if check_pairs(names):
                print 'And they are identical.'

if __name__ == '__main__':
    d = compute_checksums('.', '.py')
    print_duplicates(d)
