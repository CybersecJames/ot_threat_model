import networkx as nx
from pyvis.network import Network
from mitreattack.stix20 import MitreAttackData

# --- MITRE dataset ---
dataset = "ics-attack.json"


# --- Get all threat groups from MITRE ATT&CK ---
mitre_attack_data = MitreAttackData(dataset)
groups = mitre_attack_data.get_groups()

def get_groups():
    ics_groups = []
    for group in groups:
        ics_groups.append(group["name"])

    return ics_groups 


# --- Build a NetworkX graph of the groups --- 
def build_group_graph(group_list) -> nx.DiGraph:
    G = nx.DiGraph()
    for group in group_list:
        group_name = group
        G.add_node(
            group_name,
            node_type = "group"            
        )
    return G

# --- Write the graph to HTML using pyvis ---
def write_html(graph):
    net = Network()
    net.from_nx(graph)
    net.write_html("my.html")
    print(f"done")


# --- Main function ---
def main():
    ics_groups = get_groups()
    group_graph = build_group_graph(group_list=ics_groups)
    write_html(graph=group_graph)
    
if __name__ == "__main__":
    main()



