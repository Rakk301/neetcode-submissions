class Solution:
    def compress(self, chars: List[str]) -> int:
        group_count = 0 
        curr_char = chars[0]
        s = []
        wp=0

        def app(c):
                nonlocal wp
                if group_count <= 1:
                    s.append(curr_char)
                    chars[wp] = curr_char
                    wp+=1
                else:
                    s.append(curr_char)
                    chars[wp] = curr_char
                    wp+=1
                    dig = str(group_count)
                    for d in dig:
                        s.append(d)
                        chars[wp] = d
                        wp+=1
        for c in chars:
            if c == curr_char :
                group_count += 1
            else :
                app(c)
                curr_char = c
                group_count = 1
        app(curr_char)
        return len(s)
