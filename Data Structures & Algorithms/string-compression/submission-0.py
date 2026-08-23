class Solution:
    def compress(self, chars: List[str]) -> int:
        group_count = 0 
        curr_char = chars[0]
        s = []

        def app(c):
                if group_count <= 1:
                    s.append(curr_char)
                else:
                    s.append(curr_char)
                    dig = str(group_count)
                    for d in dig:
                        s.append(d)
        for c in chars:
            if c == curr_char :
                group_count += 1
            else :
                app(c)
                curr_char = c
                group_count = 1
        app(chars[0])

        for i in range(len(s)):
            chars[i] = s[i]
        
        return len(s)
