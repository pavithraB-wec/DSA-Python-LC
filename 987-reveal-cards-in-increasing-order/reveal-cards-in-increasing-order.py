from collections import deque

class Solution(object):
    def deckRevealedIncreasing(self, deck):
        deck.sort()

        n = len(deck)
        positions = deque(range(n))

        answer = [0] * n

        for card in deck:
            # Position where this card will be revealed
            index = positions.popleft()
            answer[index] = card

            # Move the next position to the back
            if positions:
                positions.append(positions.popleft())

        return answer