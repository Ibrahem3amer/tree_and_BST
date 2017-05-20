# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
                '''usr_in = open('/home/ibrahem3amer/PycharmProjects/week1/tests/05')
                self.n = int(usr_in.readline())
                self.parent = list(map(int, usr_in.readline().split()))
                '''
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))

                # help program to remember previous calculated results.
                self.cache = [0] * self.n

        '''finds the path from given node up to the root node'''
        def find_path(self, currnet_node):
                #tree with one node || I reached the top of the tree.
                parent = self.parent[currnet_node]
                if parent == -1:
                    return 1

                #if previously calculated, return stored result.
                if self.cache[currnet_node]:
                    return self.cache[currnet_node]

                #there still nodes, navigate each one.
                #store calculation
                self.cache[currnet_node] = 1 + self.find_path(self.parent[currnet_node])
                return self.cache[currnet_node]


        def compute_height(self):
            #for each index in range n, find the maximum path.
            return max([self.find_path(i) for i in range(self.n)])


def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
