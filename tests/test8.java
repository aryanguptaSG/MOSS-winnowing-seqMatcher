public void traversePostOrderWithoutRecursion() {
    Stack<Node> stack = new Stack<Node>();
    Node prev = root;
    Node current = root;
    stack.push(root);

    while (!stack.isEmpty()) {
        current = stack.peek();
        boolean hasChild = (current.left != null || current.right != null);
        boolean isPrevLastChild = (prev == current.right || 
          (prev == current.left && current.right == null));

        if (!hasChild || isPrevLastChild) {
            current = stack.pop();
            visit(current.value);
            prev = current;
        } else {
            if (current.right != null) {
                stack.push(current.right);
            }
            if (current.left != null) {
                stack.push(current.left);
            }
        }
    }   
}