import os
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        # we create a valid adjacency list

        in_degree = {}
        adj = {}

        all_letters = set()
        for word in words:
            for char in word:
                all_letters.add(char)
        
        # print(all_letters)

        for l in all_letters:
            adj[l] = []
            in_degree[l] = 0

        # revamped graph building logic
        for i in range(1, len(words)):
            prev = words[i-1]
            cur = words[i]
            prefix = os.path.commonprefix([prev, cur])
            if prefix == cur and prefix != prev:
                return ""
            suffix_prev = prev[len(prefix):]
            suffix_cur = cur[len(prefix):]
            if suffix_prev and suffix_cur:
                frm = suffix_prev[0]
                if frm not in adj:
                    adj[frm] = []
                to = suffix_cur[0]
                if to not in adj[frm]:
                    adj[frm].append(to)
                    in_degree[to] += 1



            


        # print(adj)
        # print(in_degree)
        q = []
        for k, v in in_degree.items():

            if v == 0:
                q.append(k)

        order = ""
        
        while q:
            # print(q)
            # print(in_degree)
            
            char = q.pop(0)
            order += char

            for v in adj[char]:
                # print("decrementing", v)
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    q.append(v)
        

        return order if len(order) == len(in_degree) else ""

        

        
        

                
                

        