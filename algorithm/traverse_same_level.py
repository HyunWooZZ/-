# 102. Binary Tree Level Order Traversal
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        # use bfs!
        # check the layer!
        # 1. use queue add all child
        # 2. add answer list all queue and start queue.pop until empty
        # 3. repeat that!
        answer = []
        if not root:
            return []
        
        layer = [root]
        while layer: # at the same level
            answer.append([elem.val for elem in layer if elem]) # add all the element by list
            temp = [] # list which will be the layer
            for node in layer: # all same level node
                temp.extend([node.left, node.right]) # add all children node
            layer = [node for node in temp if node] # if child is None do not add!
            
        return answer

# using queue
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        answer = []
        if root:
            layer = deque()
            layer.append(root)
        else:
            return []
        
        while layer: # if layer is not empty
            len_layer = len(layer) # loop size of level! 
            temp = []
            for _ in range(len_layer): # pop unitl same level node is gone!
                node = layer.popleft()
                if node: # if node is not empty
                    temp.append(node.val) # add all!
                    layer.extend([node.left, node.right]) # don`t mind if child is None! we knew that if node case catch them all!
            if temp:
                answer.append(temp)
        
        return answer