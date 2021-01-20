from collections import deque
import sys
dx = [-1,1,0,0]
dy = [0,0,-1,1]
input = sys.stdin.readline
r,c = map(int, input().split())
forest = []
for i in range(r):
	forest.append(list(input()))
visited = [[0]*c for i in range(r)]
w_queue = deque()
s_queue = deque()
for i in range(r):		#search initial location of porcupine and water
	for j in range(c):
		if(forest[i][j]=='S'):
			forest[i][j] = 0
			s_queue.append((i,j))
			visited[i][j] = 1
		if(forest[i][j]=='*'):
			w_queue.append((i,j))
		if(forest[i][j]=='D'):	#destination location saved
			d_x = i
			d_y = j
while(w_queue or s_queue):
	s = []
	w = []
	while(s_queue):
		frsx, frsy = s_queue.popleft()
		if forest[frsx][frsy] != '*':
			for i in range(4):
				nx = frsx + dx[i]
				ny = frsy + dy[i]
				if(nx<0 or ny<0 or nx>=r or ny>=c or forest[nx][ny]=='X' or forest[nx][ny]=='*'):
					continue
				if(visited[nx][ny]==0):
					s.append((nx,ny))
					visited[nx][ny] = 1
					forest[nx][ny] = forest[frsx][frsy] +1
	for i in s:
		s_queue.append(i)
	while(w_queue):
		frwx, frwy = w_queue.popleft()
		for i in range(4):
			nx = frwx + dx[i]
			ny = frwy + dy[i]
			if(nx<0 or ny<0 or nx>=r or ny>=c or (d_x==nx and d_y==ny)):
				continue
			if(forest[nx][ny]!='*' and forest[nx][ny]!='X'):
				forest[nx][ny] = '*'
				w.append((nx,ny))
	for i in w:
		w_queue.append(i)
if forest[d_x][d_y] =='D':
	print("KAKTUS")
else:
	print(forest[d_x][d_y])