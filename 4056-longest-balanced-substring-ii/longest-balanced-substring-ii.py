class Solution(object):
    def longestBalanced(self, s):
        n = len(s)
        ans = 1

        curr = 1
        for i in range(1, n):
            if s[i] == s[i - 1]:
                curr += 1
            else:
                curr = 1
            ans = max(ans, curr)

        def solve_pair(x, y):
            best = 0
            mp = {0: -1}
            cx = cy = 0

            for i, ch in enumerate(s):
                if ch == x:
                    cx += 1
                elif ch == y:
                    cy += 1
                else:
                    cx = cy = 0
                    mp = {0: i}
                    continue

                d = cx - cy
                if d in mp:
                    best = max(best, i - mp[d])
                else:
                    mp[d] = i

            return best

        ans = max(ans, solve_pair('a', 'b'))
        ans = max(ans, solve_pair('a', 'c'))
        ans = max(ans, solve_pair('b', 'c'))

        A = B = C = 0
        mp = {(0, 0): -1}
        for i, ch in enumerate(s):
            if ch == 'a':
                A += 1
            elif ch == 'b':
                B += 1
            else:
                C += 1

            key = (A - B, A - C)
            if key in mp:
                ans = max(ans, i - mp[key])
            else:
                mp[key] = i

        return ans