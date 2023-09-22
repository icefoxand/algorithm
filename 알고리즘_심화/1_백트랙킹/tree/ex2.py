class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, childNode):
        if not self.left:
            self.left = childNode
            return

        if not self.right:
            self.right = childNode
            return
        return

    def preorder(self):
        # 아무것도 없는 트리를 조회할때
        if self != None:
            print(self.value, end='')
            # 왼쪽이 있다면, 왼자식 조회
            if self.left:
                self.left.preorder()
            # 오른쪽 있다면, 오른자식 조회
            if self.right:
                self.right.preorder()

arr = [1,2,1,3,2,4,3,5,3,6]
# 이진트리 만들기
nodes = [TreeNode(i) for i in range(0,7)]
for i in range(0, len(arr), 2):
    parentNode = arr[i]
    childNode = arr[i+1]
    nodes[parentNode].insert(nodes[childNode])

test = 1