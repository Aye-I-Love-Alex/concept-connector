import wikipediaapi
from Connection import Connection
from flask import Flask, render_template, request, send_file
import networkx as nx
from pyvis.network import Network
import pandas as pd

wikipedia = wikipediaapi.Wikipedia("en")
app = Flask(__name__, static_folder='graph')


def connection(first_topic, second_topic):
    first_page = wikipedia.page(first_topic)
    second_page = wikipedia.page(second_topic)

    first_links = set(first_page.links.keys())
    second_links = set(second_page.links.keys())
    common_links = first_links.intersection(second_links)

    if second_topic in first_links:
        common_links.add(second_topic)

    if first_topic in second_links:
        common_links.add(first_topic)

    return common_links


@app.route("/", methods=["POST", "GET"])
def index():
    net = ""
    if request.method == "POST":
        first = request.form.get("firstword")
        second = request.form.get("secondword")
        if len(first) > 0 and len(second) > 0:
            connection = Connection(first, second)
            path = connection.find_connection()
            if len(path) > 0:
                source = []
                dest = []
                for path_index in range(len(path) - 1):
                    source.append(path[path_index])
                    dest.append(path[path_index + 1])
                df = pd.DataFrame({"Source": source, "Target": dest, "Weight": [1] * len(source)})
                graph = nx.from_pandas_edgelist(df, source="Source", target="Target", edge_attr="Weight")
                net = Network()
                net.from_nx(graph)
                net.save_graph("./graph/graph.html")
    return render_template("index.html", connection=net)

@app.route('/graph/graph.html')
def show_graph():
    return send_file('./graph/graph.html')

if __name__ == "__main__":
    app.run(debug=True)
