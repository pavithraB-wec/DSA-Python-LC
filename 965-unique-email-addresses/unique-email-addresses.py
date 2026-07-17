class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        seen = set()

        for email in emails:
            local, domain = email.split('@')

            # Ignore everything after '+'
            if '+' in local:
                local = local[:local.index('+')]

            # Remove dots
            local = local.replace('.', '')

            seen.add(local + '@' + domain)

        return len(seen)