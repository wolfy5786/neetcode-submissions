class Solution {
    public boolean isValidSudoku(char[][] board) {
        int [][] sudoko = new int[9][9];
        for (int i=0;i<board.length;i++)
        {
            for(int j =0; j <board[i].length; j++)
            {
                if(board[i][j]=='.')
                {
                    board[i][j]='0';
                }
                sudoko[i][j] = Character.getNumericValue(board[i][j]);
            }
        }

        int [][][] cell = new int[3][3][10];
        for (int i=0; i<sudoko.length;i++)
        {
            int [] row = new int[10];
            int [] column = new int[10];
            for(int j=0;j<sudoko[i].length;j++)
            {
                if(row[sudoko[i][j]] != 0 || column[sudoko[j][i]] !=0)
                {
                    System.out.println("for row or column");
                    return false;
                }
                row[sudoko[i][j]] = sudoko[i][j];
                column[sudoko[j][i]] = sudoko[j][i];
                if(cell[i/3][j/3][sudoko[i][j]] != 0)
                {
                    System.out.println("for cell");
                    return false;
                }
                cell[i/3][j/3][sudoko[i][j]] = sudoko[i][j];
            }
        }
        return true;
    }
}
