'''def TOH(n, src, aux, dest):

    if n == 1:

        print("I moved from "+src+" to " + dest)

        return

    TOH( n-1, src, dest, aux)

    print("I moved from "+src+" to " + dest)

    TOH( n-1, aux, src, dest)

n = 3

TOH(n, 'src', 'aux', 'dest')'''
#tower of halloi
'''
#include <stdio.h>

void towerOfHanoi(int n, char source, char auxiliary, char destination) {
    if (n == 1) {
        printf("Move disk 1 from %c to %c\n", source, destination);
        return;
    }

    towerOfHanoi(n - 1, source, destination, auxiliary);
    printf("Move disk %d from %c to %c\n", n, source, destination);
    towerOfHanoi(n - 1, auxiliary, source, destination);
}

int main() {
    int num_disks;
    
    printf("Enter the number of disks: ");
    scanf("%d", &num_disks);
    
    towerOfHanoi(num_disks, 'A', 'B', 'C');
    
    return 0;
}'''

#3*3 MATRIX 15 FROM ALL SIDES TOTAL/3=15-middle 5

'''def generate_magic_square(n):
    magic_square = [[0] * n for _ in range(n)]
    row, col = 0, n // 2  # Start from the middle of the first row
    for num in range(1, n * n + 1):
        magic_square[row][col] = num
        row -= 1
        col += 1

        if num % n == 0:
            row += 2
            col -= 1
        elif row < 0:
            row = n - 1
        elif col == n:
            col = 0
    return magic_square
def print_magic_square(square):
    for row in square:
        for num in row:
            print(num, end="\t")
        print()
n = 3
magic_square = generate_magic_square(n)
print("3x3 Magic Square:")
print_magic_square(magic_square)'''
