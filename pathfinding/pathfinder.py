
def path_lister(x, y, path):
    if (x>=1) and (y>=1):
        path_lister(x-1,y-1,[path,'diagonal'])
        path_lister(x-1,y,[path,'right'])
        path_lister(x,y-1,[path,'down'])
        
    elif x>=1:
        path_lister(x-1,y,[path,'right'])

    elif y>=1:
        path_lister(x,y-1,[path,'down'])
        
    else:
        print(path)
#path_lister(2,2,[])


def path_finder(x,y,path,board,score):
    global least_score 
    if score>least_score:
        return
    if (x>=1) and (y>=1):
        path_finder(x-1,y-1,[path,'diagonal'],board,score + board[x][y])
        path_finder(x-1,y,[path,'right'],board,score + board[x][y])
        path_finder(x,y-1,[path,'down'],board,score + board[x][y])
        
    elif x>=1:
        path_finder(x-1,y,[path,'right'],board,score + board[x][y])

    elif y>=1:
        path_finder(x,y-1,[path,'down'],board,score + board[x][y])
        
    else:
        least_score = score
        print([path,score])
        
#path_finder(2,2,[],test,0)

def check_legal(x,y,w,h):
    l = x < w
    r = x > 0
    u = y < h
    d = y > 0
    ru = r and u
    rd = r and d
    lu = l and u
    ld = l and d
    move_bools = [r,d,rd,l,u,lu,ld,ru]
    all_moves =[[-1,0],[0,-1],[-1,-1],[1,0],[0,1],[1,1],[1,-1],[-1,1]]
    legal_move =[]
    for i in range(0,8):
        if(move_bools[i]):
            legal_move.append(all_moves[i])
    return legal_move


test = [[1,2,3,4],[2,8,3,5],[12,4,0,8]]
least_score = 20
least_path = []
def path_finder_up(x,y,path,board,score):
    width = len(board)-1
    height = len(board[0])-1
    global least_score 
    legal_moves = check_legal(x,y,width,height)
    if score>least_score:
        return;
    if x==0 and y==0:
        least_score = score
        print([path,score])
    else:
        for move in legal_moves:
            path_finder_up(x+move[0],y+move[1],[path,[x,y]],board,score+board[x][y])

path_finder_up(2,3,[],test,0)
