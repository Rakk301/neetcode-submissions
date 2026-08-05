class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen_emails = set()
        for s in emails: 
            name = s[:s.index('@')]
            domain = s[s.index('@')+1:]
            pos = name.find('+')
            if pos != -1:
                name = name[:pos]
            name = name.replace('.','')
            clean_email = name+domain
            seen_emails.add(clean_email)
        return len(seen_emails)
        