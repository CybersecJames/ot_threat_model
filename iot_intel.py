from mitreattack.stix20 import MitreAttackData
from pyvis.network import Network
import networkx as nx

# --- MITRE dataset ---
dataset = "ics-attack.json"

# --- Get all threat groups from MITRE ATT&CK ---
mitre_attack_data = MitreAttackData(dataset)

# --- Define the graph, add nodes and edges ---
def graph():
    groups = mitre_attack_data.get_groups()
    
    G = nx.DiGraph()
    for group in groups:
        group_name = group['name']
        G.add_node(
            group_name,
            group="group",
            title='test run',
            shape='square'
        )
        
        software = mitre_attack_data.get_software_used_by_group(group['id'])
        for s in software:
            software_name = s["object"]["name"]
            G.add_node(
                software_name,
                group="software",
                title='hmmmm',
                shape='dot'
            )
    
            G.add_edge(
                group_name,
                software_name
            )
            
    return G


# --- Write the graph to HTML using pyvis ---
def write_html(graph):
    net = Network(directed=True)
    net.from_nx(graph)
    net.write_html("maybeeee.html")
    print("done")
 
# --- Main function ---
def main():
    G = graph()
    write_html(G)

    
if __name__ == "__main__":
    main()
