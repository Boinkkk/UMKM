import requests
import pandas as pd
import csv
import networkx as nx
import matplotlib.pyplot as plt

# file = pd.read_csv(r'C:\Python\Web Scraping\CSV\UMKM_s.csv', delimiter=":")
#
# print(file.to_string())

#graph

G = nx.DiGraph()


arr_kecamatan = []
bidang_umkm = []
usaha_kecil = []
usaha_menangah = []
usaha_mikro = []


# with open(r'C:\Python\Web Scraping\CSV\UMKM_s.csv') as f:
#     data =  csv.reader(f)
#     next(data, None)
#     for row in data:
#         arr_kecamatan.append(row[2])

# with open(r'C:\Python\Web Scraping\CSV\UMKM_s.csv') as f:
#     data =  csv.reader(f)
#     next(data, None)
#     for row in data:
#         bidang_umkm.append(row[0])

with open(r'C:\Python\Web Scraping\CSV\UMKM_s.csv') as f:
    data =  csv.reader(f)
    next(data, None)
    for row in data:
        usaha_mikro.append(row[3])

with open(r'C:\Python\Web Scraping\CSV\UMKM_s.csv') as f:
    data =  csv.reader(f)
    next(data, None)
    for row in data:
        usaha_kecil.append(row[4])

with open(r'C:\Python\Web Scraping\CSV\UMKM_s.csv') as f:
    data =  csv.reader(f)
    next(data, None)
    for row in data:
        usaha_menangah.append(row[5])



filter_kecamatan = []
filter_bidang = []
convert_kecil = []
convert_mikro = []
convert_menengah = []
for x in usaha_mikro:
    convert_mikro.append(int(x))

for x in usaha_kecil:
    convert_kecil.append(int(x))

for x in usaha_menangah:
    convert_menengah.append(int(x))

sum_kecil = sum(convert_kecil)
sum_mikro = sum(convert_mikro)
sum_menengah = sum (convert_menengah)

# [filter_kecamatan.append(x) for x in arr_kecamatan if x not in filter_kecamatan]
# [filter_bidang.append(x) for x in bidang_umkm if x not in filter_bidang]

G.add_edge("Usaha_kecil", "Jawa barat", weight=sum_kecil)
G.add_edge("Usaha_Mikro", "Jawa barat", weight=sum_mikro)
G.add_edge("Usaha_menengah", "Jawa barat", weight=sum_menengah)

# Graph Visualitation


pos = nx.circular_layout(G)
edge_labels = nx.get_edge_attributes(G, 'weight')

nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', arrowsize=20)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.show()