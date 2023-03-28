class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def fix_email(email):
            chars = []
            i=0
            
            while i<len(email) and email[i] != '@':
                if email[i] == '.':
                    i+=1
                    continue
                
                if email[i] == '+':
                    i+=1
                    while email[i] != '@' and i<len(email):
                        i+=1
                else:
                    chars.append(email[i])
                    i+=1
            
            while i<len(email):
                chars.append(email[i])
                i+=1
            
            return ''.join(chars)
        
        unique_emails = set()
        for email in emails:
            email = fix_email(email)
            unique_emails.add(email)
        
        return len(unique_emails)