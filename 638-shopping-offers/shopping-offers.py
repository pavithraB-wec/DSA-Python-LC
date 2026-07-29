class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        memo = {}

        def dfs(needs):
            key = tuple(needs)

            if key in memo:
                return memo[key]

            # Buy all items individually
            cost = 0
            for i in range(len(price)):
                cost += needs[i] * price[i]

            # Try every special offer
            for offer in special:
                new_needs = []
                valid = True

                for i in range(len(price)):
                    if offer[i] > needs[i]:
                        valid = False
                        break
                    new_needs.append(needs[i] - offer[i])

                if valid:
                    cost = min(cost, offer[-1] + dfs(new_needs))

            memo[key] = cost
            return cost

        return dfs(needs)