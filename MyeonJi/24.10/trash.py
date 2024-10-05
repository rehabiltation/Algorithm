def solution(D, T):
    N = len(D) #집의 수
    #가장 먼 집 찾고, 가는데 시간 더하고, 쓰레기 치우고, 왕복시간 더하기
    #쓰레기 종류별로 트럭별 시간 더해주기
    
    trucks = {'P': 0, 'G': 0, 'M': 0}
    pp, gg, mm = 0, 0, 0
    
    for i in range(N):
        trash = T[i] #현재 집의 쓰레기
        going_time = sum(D[:i+1])
        print("편도시간", going_time)
        
        if 'P' in trash:
            p_count = trash.count('P')
            print("p", p_count)
            pp += p_count
            trucks['P'] = going_time * 2 + pp
        
        if 'G' in trash:
            g_count = trash.count('G')
            gg += g_count
            print("g", g_count)
            trucks['G'] = going_time * 2 + gg

        if 'M' in trash:
            m_count = trash.count('M')
            mm += m_count
            print("m", m_count)
            trucks['M'] = going_time * 2 + mm

        print(trucks)
        print("-----")
    round_time = max(trucks['P'], trucks['G'], trucks['M'])
    return(round_time)
		
D =[2, 5]
T = ["PGP", "M"]
solution(D, T)