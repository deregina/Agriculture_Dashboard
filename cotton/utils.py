import matplotlib.pyplot as plt
import base64
from io import BytesIO

def draw_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def draw_plot(x, y, year_feature):
    plt.switch_backend('AGG')

    plt.figure(figsize = (8, 4))
    plt.title(f"Canopy Cover Average ({year_feature[-4:]})")
    plt.plot(x, y)
    plt.xticks(rotation=45)
    plt.tight_layout()

    graph = draw_graph()
    return graph
