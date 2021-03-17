# Note

### 1. 2차원 배열에서 max()
2차원 배열에서 max()를 사용할 시, 1차원 배열에서 원소의 합이 가장 큰 값이 나온다. 
따라서 각 리스트를 순회하며 찾거나 map을 사용하여 찾는다.

<pre>
<code>
arr = [[1, 2, 3, 4], []5, 6, 7, 8]]
arr_max = max(map(max, arr))
</code>
</pre>

min도 마찬가지로 적용하면 된다.

### 2. 2차원 배열의 초기화
2차원 배열에서 초기화를 할 때,   
<pre>
<code>
arr = [[0 * n] * n]
</pre>
</code>    
이런식으로 하면 같은 객체로 인식하기 때문에    
<pre>
<code>
arr = [[0 * n] for _ in range(n)]
</pre>
</code>.   
으로 해야한다.   