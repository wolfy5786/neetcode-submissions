class Solution {
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        int m = matrix[0].length;

        for(int i=0;i<n/2;i++)
        {
            for(int j=i; j<m-i-1;j++)
            {
                System.out.println(i + "" + j);
                int k=0;
                int x = i;
                int y = j;
                int sub = matrix[i][j];
                while(k<=2)
                {
                    matrix[x][y] = matrix[m-y-1][x];
                    System.out.println(x + " = x, " + "y =" + y + ", m ="+matrix[x][y] );
                    int s = x;
                    x = m-y-1;
                    y = s;
                    k++;
                }
                matrix[x][y] =sub;
            }
        }
    }
}
