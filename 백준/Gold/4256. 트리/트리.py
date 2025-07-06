import sys

input = sys.stdin.readline

def get_postorder(preorder, inorder):
    if not preorder:
            return
            
    root = preorder[0]
    root_index = inorder.index(root)
    
    inorder_left_subtree = inorder[:root_index]
    inorder_right_subtree = inorder[root_index+1:]
    
    preorder_left_subtree = preorder[1:1+len(inorder_left_subtree)]
    preorder_right_subtree = preorder[1+len(inorder_left_subtree):]
    
    get_postorder(preorder_left_subtree, inorder_left_subtree)
    get_postorder(preorder_right_subtree, inorder_right_subtree)
    
    postorder.append(root)

T = int(input().strip())
for i in range(T):
    n = int(input().strip())
    preorder = list(map(int, input().strip().split()))
    inorder = list(map(int, input().strip().split()))

    postorder = []

    get_postorder(preorder, inorder)

    result = ' '.join(map(str, postorder))
    print(result)
