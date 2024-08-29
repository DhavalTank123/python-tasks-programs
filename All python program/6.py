'''Paresh owns a company that moves containers between two islands. He has N trips booked,
and each trip has P containers.
Paresh has M boats for transporting containers, and each boat's maximum capacity is C containers.
Given the number of containers going on each trip, determine whether or not Paresh can perform all trips using no more
than
 boats per individual trip.
If this is possible, print Yes; otherwise, print No.
Input Format
The first line contains three space-separated integers describing the respective values of N(number of trips), C (boat
capacity),
and M(total number of boats).
The second line contains space-separated integers describing the value for container for each trip.
Constraints
* 1<= m,c ,p<=100
Output Format
Print Yes if Paresh can perform
booked trips using no more than boats per trip; otherwise, print No.
Sample Input 0
5 2 2
1 2 1 4 3
Sample Output
0
Yes
Sample Input
0
5 1 2
 1 2 1 4 3
Sample Output 0
No
'''

def can_perform_trip(n,c,m,containers):
    for p in containers:
        bots_want = (p+c-1)//c
        if bots_want>m:
            return "no"
    return "yes"
if __name__ == '__main__':
    n,c,m=map(int,input().strip().split())
    container = list(map(int,(input().strip().split())))
    res = can_perform_trip(n,c,m,container)
    print(res)