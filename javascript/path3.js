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
 * @param {number} targetSum
 * @return {number}
 */
var pathSum = function(root, targetSum) {
    let result=0;
    function dfs(node,path){

        if (node!=null){
            path.push(node.val);
            for (let i=0;i<path.length;i++){
                
                subpath=path.slice(i);
                const s=subpath.reduce((agg,curr)=> agg+curr);
                if (s===targetSum){
                    result++;
                }
            }

            dfs(node.left,path);
            dfs(node.right,path);
            path.pop();
        }
    }
    dfs(root,[]);
    return result
    
};