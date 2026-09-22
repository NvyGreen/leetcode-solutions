class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        uniqueEmails = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.replace('.', '')

            plus = local.find('+')
            if plus != -1:
                local = local[:plus]
            
            uniqueEmails.add(local + '@' + domain)
        
        return len(uniqueEmails)
