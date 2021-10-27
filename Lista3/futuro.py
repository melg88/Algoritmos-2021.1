class Node(object):
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.height = 0
        self.left = None
        self.right = None


class AVLTree(object):

    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
            print(self.root.key + " foi adicionado com sucesso!")
            return self.root
        else:
            new_node = self._insert(self.root, key)

            self.walkUp(new_node)

    def _insert(self, node, key):
        if key < node.key:
            if not node.left:
                node.left = Node(key)
                node.left.parent = node
                print(key + " foi adicionado com sucesso!")
                return node.left
            return self._insert(node.left, key)
        elif(key > node.key):
            if not node.right:
                node.right = Node(key)
                node.right.parent = node
                print(key + " foi adicionado com sucesso!")
                return node.right
            return self._insert(node.right, key)
        else:
            print(key + " ja existe.")

    def find(self, value, node):
        if node is None:
            return False
        if node.key > value:
            return self.find(value, node.left)
        elif node.key < value:
            return self.find(value, node.right)
        return node

    def remove(self, node):

        parent_node = node.parent
        childrenN = self.children(node)

        if childrenN == 0:

            if not parent_node:
                self.root = None
            elif parent_node.left == node:
                parent_node.left = None
            else:
                parent_node.right = None
            return parent_node

        elif childrenN == 1:
            if node.left:
                child = node.left
            else:
                child = node.right

            if not parent_node:
                self.root = child
            elif parent_node.left == node:
                parent_node.left = child
            else:
                parent_node.right = child
            child.parent = parent_node
            return parent_node

        else:
            successor = self.maxNode(node.left)
            node.key = successor.key
            self.delete(successor)

    def children(self, node):
        children = 0
        if node.left:
            children += 1
        if node.right:
            children += 1
        return children

    def walkUp(self, node):
        if not node:
            return
        else:
            self.checkNode(node)
            return self.walkUp(node.parent)

    def checkNode(self, node):
        left_height = 0
        right_height = 0
        if node.left:
            left_height = node.left.height
        if node.right:
            right_height = node.right.height
        if abs(left_height - right_height) > 1:
            if left_height < right_height:
                self.leftRotate(node, node.right)
            else:
                self.rightRotate(node, node.left)
        else:
            node.height = max(left_height, right_height) + 1
            return node.height

    def leftRotate(self, node, child_node):
        if child_node.left:
            node.right = child_node.left
            node.right.parent = node
        else:
            node.right = None

        if node != self.root:
            child_node.parent = node.parent
            node.parent.right = child_node
        else:
            child_node.parent = None
            # because we are not replacing the parent node('node') with the
            # child node('child_node'), self.root is still pointing at the parent node.
            self.root = child_node

        child_node.left = node
        node.parent = child_node

        node.height -= 1

    def rightRotate(self, node, child_node):
        if child_node.right:
            node.left = child_node.right
            node.left.parent = node
        else:
            node.left = None

        if node != self.root:
            child_node.parent = node.parent
            node.parent.left = child_node
        else:
            child_node.parent = None
            self.root = child_node

        child_node.right = node
        node.parent = child_node

        node.height -= 1

    def minNode(self, Node):
        if Node == None or Node.left is None:
            return Node
        else:
            return self.minNode(Node.left)

    def maxNode(self, Node):
        if Node == None or Node.right is None:
            return Node
        else:
            return self.maxNode(Node.right)

        """"def inOrder(self, root):
            if root is not None:
                self.inOrder(root.left)
                print(root.key, end=' ')
                self.inOrder(root.right)
            else:
                print("PRE-ORDER DA ARVORE: ")
"""

    def inOrder(self, aux=None):

        temp = ''
        if not (aux):
            aux = self.root

        if aux.left != None:
            temp += self.inOrder(aux.left)

        temp += str(aux.key) + " "

        if aux.right != None:
            temp += self.inOrder(aux.right)

        return(temp)

    def heightN(self, root):
        if root is None:
            return 0
        else:
            hLeft = 1 + self.heightN(root.left)
            hRight = 1 + self.heightN(root.right)
            return max(hLeft, hRight)


if __name__ == "__main__":
    tree = AVLTree()
    rootN = None
    nCommand = int(input())

    while nCommand > 0:
        command = input()

        if(command == "Oh, arvore sagrada, quero adicionar o seguinte nome"):
            name = input()
            rootN = tree.insert(name)

        elif(command == "Arvore sagrada, gostaria que voce removesse para mim o seguinte nome"):

            name = input()
            node = tree.find(name, tree.root)

            if(node != False):
                rootN = tree.remove(node)

                print(name + " deletado com sucesso.")

            else:
                print(name + " nao foi encontrado.")

        elif tree.root == None:
            if command != None:
                print("A arvore esta vazia...")

        else:
            if(command == "Coe planta, qual o menor nome ai?"):

                nodeM = tree.minNode(tree.root)
                print("O menor eh: " + nodeM.key)

            elif(command == "Salve minha floresta amazonica de uma arvore so, qual o maior nome ai?"):
                nodeMax = tree.maxNode(tree.root)
                print("O maior eh: " + nodeMax.key)

            elif(command == "Nossa, ce ta tao grande, qual tua altura?"):
                h = tree.heightN(tree.root)
                print("A altura da arvore eh: " + str(h))
        nCommand -= 1

    if tree.root != None:
        temp = tree.inOrder(tree.root)
        auxPrint = temp[:-1]
        print("PRE-ORDER DA ARVORE: " + auxPrint)
    else:
        print("PRE-ORDER DA ARVORE:")
