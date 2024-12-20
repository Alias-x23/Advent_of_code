
t = open("input5.txt")
text = t.read()
text_list = text.split("\n\n")

page_order = text_list[0].split("\n")
page_list = text_list[1].split("\n")

order_dict = {}

for p in page_order:
    if p.split("|")[0] not in order_dict.keys():
        order_dict[p.split("|")[0]] = [p.split("|")[1]]
    else:
        order_dict[p.split("|")[0]].append(p.split("|")[1])

mid_sum = 0

for pages in page_list:
    good_page = True
    p = pages.split(",")
    p.reverse()
    for i in range(len(p) - 1):
        num = p[i]
        if num not in order_dict.keys():
            continue
        if any([x for x in p[i+1:] if x in order_dict[num]]):
            good_page = False
            break
    if good_page:
        mid_point = int(len(p)/2)
        mid_sum += int(p[mid_point])


print(mid_sum)


sort_lod = []
for od_key, od_list in order_dict:
    out_dict = {od_key: 0}
    val = 1
    for num in od_list:
        out_dict[num] = val
        val += 1
    sort_lod.append(out_dict)


from toposort import toposort_flatten
new_order = {}

for p in page_order:
    if p.split("|")[1] not in new_order.values():
        new_order[p.split("|")[1]] = [p.split("|")[0]]
    else:
        new_order[p.split("|")[1]].append(p.split("|")[0])

for key in new_order.keys():
    new_order[key] = set(new_order[key])

# apparently this needs something called a topological sort
#graph = dict(zip(order_dict.keys(), map(set, order_dict.values())))
#sorted_graph = toposort_flatten(graph, sort=True)

fix_sum = 0

for pages in page_list:
    p = set(pages.split(","))

    # there are circular refs if you use the whole set but we can just take the values the occur in each list
    mini_sort = {k: order_dict[k] for k in order_dict.keys() if k in p}
    graph = dict(zip(mini_sort.keys(), map(set, mini_sort.values())))
    sorted_graph = toposort_flatten(graph, sort=True)

    p = [x for x in sorted_graph if x in p]

    mid_point = int(len(p)/2)
    fix_sum += int(p[mid_point])


fix_sum -= mid_sum

print(fix_sum)

print("hello")
