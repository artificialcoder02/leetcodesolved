class Solution {
public:
    int nearestExit(vector<vector<char>>& maze, vector<int>& entrance) {
        //Declaring Row and Coloumn Variable
        int rows=maze.size();
        int columns=maze[0].size();

        //We will perform bfs as shorter distance node will be traverse at first level
        //define queue
        queue<pair<int,int>>q;
        int steps=1;

        //entering all the valid traversal directions
        vector<vector<int>>directions= {{0,1},{0,-1},{1,0},{-1,0}};

        //push the entry to the queue and make it visited and apply bfs
        q.push({entrance[0],entrance[1]}); //q.push(x,y)

        //make it visited also making sure the starting point is an entry 
        maze[entrance[0]][entrance[1]]='+';

        while(!q.empty()){
            //check the node at that level
            int l = q.size();
            //for every node in the queue visit all of its adjacent nodes which are not yet visited
            for(int i=0;i<1;i++)
            {
                auto[x_cord,y_cord]=q.front();
                q.pop();

                //check in all the 4 directions for the visited nodes
                for(int k=0;k<4;k++)
                {
                    int x=x_cord+directions[k][0];
                    int y=y_cord+directions[k][1];

                    //if it is an invalid move (visited,out of bounds) continue
                    if(x<0||y<0||x>=rows||y>=columns||maze[x][y]=='+')
                    continue;
                    //if we have reached the exit then we calculate the current steps to reach the exit 
                    if(x==0||y==0||x==rows-1||y==columns-1)
                    return steps;
                    //block the visited cell and push in the queue
                    maze[x][y]='+';
                    q.push({x,y});
                }
            }
            //increment the steps, if incase we couldnt find the soln in level one
            steps++;
        }
        return -1;


    }
};
