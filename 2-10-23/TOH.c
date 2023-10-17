
// tower of halloi
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