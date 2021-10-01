from collections import defaultdict
from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_mails = defaultdict(set)

        def parse_email(email):
            prefix, domain = email.split('@')
            local = prefix.split('+')[0].replace('.', '')
            return local, domain

        for email in emails:
            local, domain = parse_email(email)
            unique_mails[domain].add(local)

        return sum(len(unique_mails[domain]) for domain in unique_mails)
