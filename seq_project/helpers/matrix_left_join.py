import numpy as np

def join_by_left(key, r1, r2, mask=True):
    # figure out the dtype of the result array
    descr1 = r1.dtype.descr
    descr2 = [d for d in r2.dtype.descr if d[0] not in r1.dtype.names]
    descrm = descr1 + descr2 

    # figure out the fields we'll need from each array
    f1 = [d[0] for d in descr1]
    f2 = [d[0] for d in descr2]

    # cache the number of columns in f1
    ncol1 = len(f1)

    # get a dict of the rows of r2 grouped by key
    rows2 = {}
    for row2 in r2:
        rows2.setdefault(row2[key], []).append(row2)
    # figure out how many rows will be in the result
    nrowm = 0
    for k1 in r1[key]:
        if k1 in rows2:
            nrowm += len(rows2[k1])
        else:
            nrowm += 1

    # allocate the return array
    _ret = np.recarray(nrowm, dtype=descrm)
    if mask:
        ret = np.ma.array(_ret, mask=True)
    else:
        ret = _ret

    # merge the data into the return array
    i = 0
    for row1 in r1:
        if row1[key] in rows2:
            for row2 in rows2[row1[key]]:
                ret[i] = tuple(row1[f1]) + tuple(row2[f2])
                i += 1
        else:
            for j in range(ncol1):
                ret[i][j] = row1[j]
            i += 1

    return ret