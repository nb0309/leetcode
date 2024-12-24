//https://leetcode.com/problems/leaf-similar-trees/
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root1
 * @param {TreeNode} root2
 * @return {boolean}
 */
var leafSimilar = function(root1, root2) {
    function dfs(node,result){
        if (node!=null){
            dfs(node.left,result);
            
            
            if (node.left===null && node.right===null){
                result.push(node.val);
            }
            dfs(node.right,result);

        }
        return result
    }
    var r1=dfs(root1,[]);
    var r2=dfs(root2,[]);
    console.log(r1,r2);
    if (r1.length!==r2.length){
        return false
    }
    else{
        for (let i=0;i<r1.length;i++){
            if (r1[i]!==r2[i]){
                return false}
            }
        }
    return true
    
};