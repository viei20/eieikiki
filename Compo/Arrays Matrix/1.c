#include <stdio.h>
int main(){
    //รับค่าขนาดmatrix
    int num_row, num_col;
    scanf("%d %d", &num_row, &num_col);
        
    int matrix_a[num_row][num_col];
    int matrix_b[num_row][num_col];

    //รับค่าเลขในmatrixA
    for(int i = 0; i < num_row; i++){
        for(int j = 0; j < num_col; j++){
            scanf("%d", &matrix_a[i][j]);
        }
    }
    //รับค่าเลขในmatrixB
    for(int i = 0; i < num_row; i++){
        for(int j = 0; j < num_col; j++){
            scanf("%d", &matrix_b[i][j]);
        }
    }

    int matrix_c[num_row][num_col];
    for(int i =0;i < num_row; i++){
        for(int j = 0; j < num_col; j++){
            matrix_c[i][j] = matrix_a[i][j] + matrix_b[i][j];
        }
    }

    //แสดงผลค่าMatrix  เฉยๆ
    for(int i = 0; i < num_row; i++){
        for(int j = 0; j < num_col; j++){
            printf("%d ", matrix_c[i][j]);
        }
        printf("\n");
    }
}
