#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)  O(n)

    While loop iteration depend on the value of a and as we can see in each iteration n*n add to a value of a. So we can take out n*n from the while loop. Now we can say the time complexity of while loop is 0(n) and the operation inside the while loop is 0(1).

        0(1*n) = 0(n)

b)  O(n(log n))

    The for loop complexity is 0(n) and as you can see the operation inside the inner while loop reduces the no of iteration of while the loop so its time complexity 0(log n).
 

c)  O(n)

    A recursive algorithm that reduces the input by 1 for each call to the itself. As this function doesn't do anything to the input within, it will run O(n) times.

## Exercise II

I will use Binary Search Algorithm

Condition One:

if Max and Min floor height are same
 -Then we have found the max floor

Condition Two:

Consider floor f to be between of max and min search height
 - Drop an egg
 - check the egg break?
     - Yes: Reduce the max search height to 1 less than the floor
     - No:  Increase the min search height to 1 more than the floor
 - Repeat


