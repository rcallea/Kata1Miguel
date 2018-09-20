import math


class Solver:

    def demo(self, a, b, c):

        d = b ** 2 - 4 * a * c

        if d >= 0:

            disc = math.sqrt(d)

            root1 = (-b + disc) / (2 * a)

            root2 = (-b - disc) / (2 * a)

            print(root1, root2)

        else:

            raise Exception

    def tamano(self, cadena):
        tam = 0
        min = 9999999999999
        max = -9999999999999
        prom = 0.0
        if cadena!="":
            esplitiado = cadena.split(",")
            for x in esplitiado:
                if min>int(x):
                    min = int(x)
                if max < int(x):
                    max = int(x)
                prom = prom + float(x)
            tam = len(esplitiado)
            prom = prom / float(len(esplitiado))
        return([tam,min,max,prom])


Solver().demo(2, 1, 0)