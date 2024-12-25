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
var goodNodes = function(root) {
    let good=0;
    function dfs(node,path){
        if (node===null){
            
            node.val>=Math.max(path) ? (good++) : (good);
            path.push(node.val);
            dfs(node.left,path);
            dfs(node.right,path);
            path.pop();
            return path;
        }
    }
    dfs(root,[]);
    return good;
    
};