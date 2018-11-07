#!/usr/bin/env python

# for example we have vlans: 1,2,3,4,5,7,99,101,105,110
# we want to get like cisco representation
# 1-5,7,99,101-105,110
# composition of vlan tags
# sw1(config)# interface fa0/22
# sw1(config-if)# switchport trunk allowed vlan 1-2,10,15


# here we have example input
init = [1,2,3,4,5,7,99,101,102,103,104,105,110]
# init = [1,2,4,5,10,15,99,100,101,102,103,104,105]

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

print(outline)
