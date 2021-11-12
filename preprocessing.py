import json
from collections import defaultdict, Counter

import numpy as np
import pandas as pd
import networkx
import networkx as nt
from fuzzywuzzy import fuzz
from matplotlib import pyplot as plt
from networkx.algorithms.components.connected import connected_components

WIKI_FIELDS = ['gender', 'occupation_ids', 'citizenship_id']

class CliqueFinder:
    def __init__(self, occ_set):
        self.occ_set = occ_set
        self.G = None
        
    def get_dist_matrix(self, threshold = 90):
    
        length = len(self.occ_set)
        r = np.zeros((length, length))
        for _, i in enumerate(range(length)):
            for _, j in enumerate(range(length)):
                if i != j:
                    r[i, j] = fuzz.partial_ratio(self.occ_set[i], self.occ_set[j]) > threshold
        self.distance = r
    
    def find_clique(self):
        
        self.get_dist_matrix()
        occupations_graph = nt.convert_matrix.from_numpy_matrix(self.distance)
        self.G = occupations_graph
        cliques = list(nt.find_cliques(occupations_graph))
        
        return cliques

    def find_clique_final(self):
        cliques = self.find_clique()

        return cliques
    
def select_by_index(item, index):
    item = item.copy()
    
    for field in WIKI_FIELDS:
        item[field] = item[field][index]
    return item

class Graph:
    
    "Creates graph"
    
    def __init__(self, l):
        self.list = l
    
        
    def make_graph(self):
        G = nt.Graph()
        for pair in self.list:
            G.add_nodes_from(pair)
            G.add_edges_from(list(zip(pair[:-1], pair[1:])))
        return G

    
def define_cluster(occupation, clusters_occ_dict):
    for item, cluster in clusters_occ_dict.items():
        if occupation in cluster:
            return item