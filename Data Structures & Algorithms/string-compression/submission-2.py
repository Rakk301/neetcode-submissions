class Solution:
    def compress(self, chars: List[str]) -> int:
        group_count = 0 
        curr_char = chars[0]
        wp=0

        def app(c):
                nonlocal wp
                if group_count <= 1:
                    chars[wp] = curr_char
                    wp+=1
                else:
                    chars[wp] = curr_char
                    wp+=1
                    dig = str(group_count)
                    for d in dig:
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
        return wp
