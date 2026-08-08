class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen_emails = set()
        for s in emails: 
            breakpoint = s.index('@')
            name = s[:breakpoint]
            domain = s[breakpoint+1:]
            pos = name.find('+')
            if pos != -1:
                name = name[:pos]
            name = name.replace('.','')
            clean_email = name+domain
            seen_emails.add(clean_email)
        return len(seen_emails)
        