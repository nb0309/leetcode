/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxDepth = function(root) {
    function depth(node){
        if (node===null){
            return 0
        }
        else{
            var leftdepth=depth(node.left);
            var rightdepth=depth(node.right);
        }
        return Math.max(leftdepth,rightdepth)+1;
    }
    return depth(root)   
};