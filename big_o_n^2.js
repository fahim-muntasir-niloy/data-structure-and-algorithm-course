// n^2 notation
// if the function is `n` dependent, the complexity is n. however, 5n, 23n+5 etc are also called n complexity as the variables doesnt contribute


function iter(n){
    for(let i=0;i<=n;i++){
        // the complexity here is `n`
        for(let j=0;j<=n;j++)
        // complexity here is also `n`
        console.log(i,j);
    }
}

// so total comlexity is `n*n = n^2`

iter(3)