%%
	29th July 2021
%%

#algorithm #interview-prep  

---
# Complexity Analysis

### How complexity analysis done?
- The actual running time of computer programs or algorithms depends on various factors like - 
	- the processor - the number of processor/core used in your computer, clock speed of the processor
	- time to write into memory and read from memory
	- how the computer processing instructions - sequential or multiple concurrent instructions
	- **the volume of input** data
 - all of the above from the list except **the volume of input** data depends on particular type of computer and hardware implementation. So to judge the efficiency of an algorithm considering these factor will not be wise. If we want to compare the efficiency of different algorithm we only consider the volume of input. 
#### The model machine concept
-	since everyone is using different machine, calculating the actual running time in seconds for different algorithm is not possible. So a model machine concept is introduced to deduce the running time of a algorithm in seconds. All algorithm is run on this machine to get approximate time.
-	![[calculating -complexity-in-model-machine.png]]
	-	**NOTE**: 
		-	besides each line we write the cost of complexity according to the model machine
			-	at line 1 assignment takes 1 unit time
			-	at line 2 there are 2 operations - comparison and increments so it takes 2 seconds
		-total time <span>`T`<sub>`sumoflist`</sub></span>`=1+2(n+1)+2n+1`
			- at line 2 there is `n+1` comparison because there 1 extra comparison for the false condition
			- 1, 2, 2, 1 are constant
		- often while you want to ignore the constant the expression could (the second one in the above image) be written like `Cn+C'` 

### The time function T(n) graph, and relation between big-o notation and time function T(n)
- In the above section we've deduce time function `T(n)` for our model computer. Most often we don't use these long calculation, cause we are only interested about the <span class="stress2">rate of growth of the function</span>. In that case big-o notation is used.


![[big-o-and-function-relation.png]]
- **NOTE:**
	- O (big-o) is a way of defining a set of functions.
		- big-O represent a pure set of functions
		- O(n) - defines set of all function of the form `an+c`, set of all first order function
			- $T_{1}(n)=25n+1$
			- $T_{2}(n)=4n+26$
			- all linear time function (of the form -$An+C$ )like $T_{1}, T_{2} \in O(n)$ 
		- Similarly, $O(n)$ - defines set of all function of the form **$an^2+bn+c$**
			- $T_{3}(n)=5n^2 +2n +1$
			- $T_{4}(n)=8n^2+19n +25$
			- $T_{5}(n)=15n^2+23$
			-  $T_{6}(n)=17n^2$
			- all `quadratic function` like $T_{3}, T_{4}, T_{5}, T_{6} \in O(n)$
		- $O(k)$ - defines all function of the form $T(n)=k$
			-  $T_{7}(n)=15$
			-  $T_{8}(n)=87$
			- all function like $T_{7}, T_{8} \in O(k)$
				- you can write any constant instead of `k`. $O(k),O(1), O(2), O(3)...$ all are same thing. 
				- by convention we use $O(1)$


### Complexity analysis - some general rules
- ![[big-o-n2.png]]
	- the above graph is a graph of $O(n^2)$
	- if you draw this graphs for all $T_{3}, T_{4}, T_{5}$ you can notice after some certain value of `n` (say $n_{0}$), the growth of the functions will not faster than $O(n^2)$

 - <span class="stress3">**Rules to calculate complexity from $T(n)$ expression:**</span> (based on the above fact)
	 - from the time function, drop all the lower order terms
	- from the time function, drop all constant constant multipliers
	- now take only the higher order term, and that will be your complexity 
	- **Example:**
		- $53n^3 +27n^2 + 25n +11$ (dropping lower order terms) => $53n^3$ =>(dropping constant multipliers) =>$n^3$ =>  $O(n^3)$ 
		![[complexity-analysis-rules-1.png]]

- <span class="stress3">**Some simplification rules of $O(n)$**</span>
	- if your code have multiple branches (due to the if else) to execute and each branch has different time complexity ==> complexity ==> complexity of the larger branch
		- ![[complexity-analysis-rules-4.png]]
	-  if you algorithm has multiple code fragment of different order of complexity sum them up and simplify
		- $O(n) + O(n^2) + O(1)$ (summing up simplify)==> $O(n^2)$
		- **Example:**
		- ![[complexity-analysis-rules-2.png]] ![[complexity-analysis-rules-3.png]]


- **General rules summary:**
	- drop the lower order terms from the expression
	- drop the multiplying constants from the expression 
	- pick the higher order while your code has multiple fragments of different complexity  
	- pick the higher order from if/else/switch branches 

### Determine the complexity - short way | exercises

