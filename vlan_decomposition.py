#!/usr/bin/env python

from __future__ import print_function

# init = [1,2,4,5,7,99,101,102,103,104,105,110,111,113]
init = [1,2,4,5,10,15,99,100,101,102,103,104,105,400,402,403,404,405,407]

def composition_vlans(init):
    def next_item(arr):
        for item in arr:
            yield item

    myinit = next_item(init)
    k=myinit.next()
    outline=""
    new_range=True
    while k>0:
        try:
            new=myinit.next()
        except StopIteration:
            outline+=str(init[-1])
            break
        if new - k != 1:
            outline+="{},".format(k)
            new_range=True
        else:
            if new_range:
                outline+="{}-".format(k)
                new_range=False
        k=new
    return outline

def decomposition_vlans(deinit):
    OUT=[]
    def print_vlans(deinit, attr):
        if attr == "commaonly":
            out = deinit.split(",")
            for id in out:
                OUT.append(int(id))
        if attr == "dashonly":
            out = deinit.split("-")
            for id in range(int(out[0]),int(out[1])+1):
                OUT.append(int(id))
        if attr == "none":
            OUT.append(int(deinit))
        return

    if "," not in deinit and "-" not in deint:
        print_vlans(deinit,"none")
    if "," in deinit and '-' not in deinit:
        print_vlans(deinit, "commaonly")
    if "," not in deinit and "-" in deinit:
        print_vlans(deinit, "dashonly")

    if "," in deinit and "-" in deinit:
        out = deinit.split(",")
        if len(out)>0:
            for item in out:
                if "," not in item and "-" not in item:
                    print_vlans(item,"none")
                if "," in item and '-' not in item:
                    print_vlans(item, "commaonly")
                if "," not in item and "-" in item:
                    print_vlans(item, "dashonly")
    return OUT


def main():
    print (init)
    line = composition_vlans(init)
    print(line)
    result = decomposition_vlans(line)
    print (result)

if __name__ == '__main__':
    main()
