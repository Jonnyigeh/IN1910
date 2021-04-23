"""
Oppgave 1: IN1910 prosjekt del 3
"""
import matplotlib.pyplot as plt
import numpy as np
from numpy import random as rn

class chaosTriangle:
    def __init__(self, c0, c1, c2):
        """
        Tar inn hjørnene til trekanten vi skal bruke når vi itererer.
        Parameter:
            - c_i = hjørne nummer i.
        """
        self.c0 = c0
        self.c1 = c1
        self.c2 = c2
        self.corners = np.array([c0, c1, c2])

    def scatterplot(self):
        """
        Plotter hjørnene i trekanten, og
            rette linjer mellom punktene.
        """
        plt.scatter(*zip(*self.corners))
        lines = list(self.corners)              # Gjøres for at det skal plottes linje tilbake til
        lines.append(self.c0)                   # startpunkt (c0).
        x, y = zip(*(lines))
        plt.plot(x, y, "r-")
        plt.title("Likesidet trekant")
        plt.show()

    def startingpoint(self):
        """
        Finner en tilfeldig generert startposisjon
            vi bruker for å starte iterasjonen vår.
        """
        weights = np.zeros(3)
        for i in range(3):
            weights[i] = rn.random()
        weights *= (1 / sum(weights))
        startpoint = np.dot(weights, self.corners)
        return startpoint

    def iteration(self):
        """
        Starter iterasjon ved å hente ut tilfeldig start
            og forkaster første 5 punkter, og lagrer neste
                10000 punkter i array X.
        Plotter deretter de 10000 punktene i scatterplot.
        """
        X0 = self.startingpoint()
        for i in range(5):
            j = rn.randint(0,3)
            X0 = (X0 + self.corners[j]) / 2
        X = np.zeros((10000, 2))
        X[0] = X0
        for i in range(10000-1):
            j = rn.randint(0,3)
            X[i+1] = (X[i] + self.corners[j]) / 2
        plt.scatter(*zip(*X), marker=".", s=0.1)
        plt.axis("equal")
        plt.show()

    def iterationwithcolor(self):
        """
        Starter iterasjon ved å hente ut tilfeldig start
            og forkaster første 5 punkter, og lagrer neste
                10000 punkter i array X.
        Plotter deretter de 10000 punktene i scatterplot,
            men nå i farger rød grønn blå.
        """
        X0 = self.startingpoint()
        colors = ["red", "green", "blue"]
        for i in range(5):
            j = rn.randint(0,3)
            X0 = (X0 + self.corners[j]) / 2
        X = np.zeros((1000, 2))
        X[0] = X0
        for i in range(1000-1):
            j = rn.randint(0,3)
            X[i+1] = (X[i] + self.corners[j]) / 2
            plt.scatter(*X[i+1], color = colors[j], marker=".", s=0.1)
        plt.axis("equal")
        plt.show()

    def iterationwithaltcolor(self):
        """
        Starter iterasjon ved å hente ut tilfeldig start
            og forkaster første 5 punkter, og lagrer neste
                10000 punkter i array X.
        Plotter deretter de 10000 punktene i scatterplot,
            men nå i RGB fargespekter.
        RGB fargene finnes på samme måte som vi finner punktene
            med en differenslikning. Matrisen C er fargekodene RGB.
        """
        X0 = self.startingpoint()
        C0 = [0,0,0]
        r = np.array(([1,0,0], [0,1,0], [0,0,1]))
        X0 = self.startingpoint()
        for i in range(5):
            j = rn.randint(0,3)
            X0 = (X0 + self.corners[j]) / 2
            C0 = (C0 + r[j]) / 2
        X = np.zeros((10000, 2))
        C = np.zeros((10000, 3))
        X[0] = X0
        C[0] = C0
        for i in range(10000-1):
            j = rn.randint(0,3)
            X[i+1] = (X[i] + self.corners[j]) / 2
            C[i+1] = (C[i] + r[j]) / 2
        plt.scatter(*zip(*X),c = C, marker = ".", s=0.2)
        plt.axis("equal")
        plt.show()


if __name__ == "__main__":
    instance = chaosTriangle([0,0], [0.5,np.sqrt(3)/2], [1,0])       # Brukte Pythagoras til å finne høyden i trekanten

    x = np.zeros(1000)
    y = np.zeros(1000)
    for i in range(1000):
        x[i], y[i] = instance.startingpoint()                           # Henter ut 1000 tilfeldige punkter, plotter
    plt.scatter(x,y)                                                    # for å sjekke at de faktisk ligger inni trekanten

    instance.iteration()
    instance.iterationwithcolor()
    instance.iterationwithaltcolor()
