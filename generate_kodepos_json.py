import sys
import csv
import json

def _main(compressed=False):
    data = []
    with open('tbl_kodepos.csv', 'r') as f:
        data = list(csv.reader(f))
        data = [i[1:] for i in data]
    kodepos = {}
    for i, record in enumerate(data):
        print('Accessing data #%d... ' % (i + 1), end='')
        if record[3] not in kodepos.keys():
            kodepos[record[3]] = {}
        if record[2] not in kodepos[record[3]].keys():
            kodepos[record[3]][record[2]] = {}
        if record[1] not in kodepos[record[3]][record[2]].keys():
            kodepos[record[3]][record[2]][record[1]] = {}
        kodepos_elemen = '%s - %s' % (record[4], record[0])
        kodepos[record[3]][record[2]][record[1]][kodepos_elemen] = kodepos_elemen
        print('done.')
    filename = 'kodepos.min.json' if compressed else 'kodepos.json'
    with open(filename, 'w') as f:
        if compressed:
            json.dump(kodepos, f, separators=(',',':'))
        else:
            json.dump(kodepos, f, indent=2)
    print('Save to %s' % filename)
    return 0


if __name__ == '__main__':
    compressed = False
    if len(sys.argv) > 1:
        if sys.argv[1] == 'compress':
            compressed = True
    sys.exit(_main(compressed))
