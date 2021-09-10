import sys
import networkx as nx
import pygame
#from pygame.locals import *
#import matplotlib.pyplot as plt

pygame.init()
screen = pygame.display.set_mode((1024, 768))

def make_graph():
    """ making a test graph to play around with """
    G = nx.DiGraph()
    G.add_node("Start Node")
    
    G.add_nodes_from([1, 2, 3, 4, 5, 6, 7])
    
    print(f"Nodes of the graph: {G.nodes()}")
    print(f"edges of the graph: {G.edges()}")
    
    G.add_edge("Start Node", 1)
    G.add_edge("Start Node", 2)
    G.add_edge("Start Node", 3)
    
    edge = (2, 3)
    G.add_edge(*edge)
    edge = (1, 3)
    G.add_edge(*edge)
    edge = (1, 4)
    G.add_edge(*edge)
    edge = (3, 5)
    G.add_edge(*edge)
    edge = (4, 6)
    G.add_edge(*edge)
    edge = (6, 7)
    G.add_edge(*edge)
    edge = (5, 7)
    G.add_edge(*edge)
    
    for n in G:
        for nbr in G[n]:
            print(f"nbr {nbr}")
    
    print(f"{G.adj}")
    
    print(f"Nodes of the graph: {G.nodes()}")
    print(f"edges of the graph: {G.edges()}")
    
    #nx.draw(G, with_labels=True)
    
    #plt.savefig('test.png')
    #plt.show()
    return G

def main():
    font = pygame.font.SysFont('Arial', 25)
    G = make_graph()

    while 1:
        for event in pygame.event.get():
            if event.type in (pygame.QUIT, pygame.KEYDOWN):
                sys.exit()

        show_graph(G, screen, font)
        pygame.display.update()
        pygame.time.delay(100)

def show_graph(graph, screen, font):
    # Draw circles and text for each node, eventually edges
    x = 0
    y = 0
    for node in graph:
        pygame.draw.circle(screen, (100, 100, 100), (x, y), 20)
        text = font.render(str(node), True, (223,223,223))
        screen.blit(text, (x+35, y))
        x += 20
        y += 20


if __name__ == '__main__':
    main()
