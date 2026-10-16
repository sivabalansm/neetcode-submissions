class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        adj = defaultdict(set)
        email_name = {}
        for account in accounts:
            name = account[0]
            emails = account[1:]
            if len(emails) == 1:
                adj[emails[0]] = set()
                email_name[emails[0]] = name

            for i in range(1, len(emails)):
                email1 = emails[i - 1]
                email2 = emails[i]
                adj[email1].add(email2)
                adj[email2].add(email1)
                email_name[email1] = name
                email_name[email2] = name
        all_visit = set()
        def dfs(node, visit):
            if node in visit:
                return
            visit.add(node)

            for nei in adj[node]:
                dfs(nei, visit)
        res = []
        for node in adj:
            if node not in all_visit:
                print(node)
                visits = set()
                dfs(node, visits)
                all_visit.update(visits)

                visits = list(visits)
                name = email_name[visits[0]]
                res.append([name] + sorted(visits))
        return res
        




        


            

            
