class Solution(object):
    def asteroidCollision(self, asteroids):
        stack = []

        for asteroid in asteroids:
            alive = True

            while alive and asteroid < 0 and stack and stack[-1] > 0:
                if stack[-1] < -asteroid:
                    # Stack asteroid explodes
                    stack.pop()
                elif stack[-1] == -asteroid:
                    # Both explode
                    stack.pop()
                    alive = False
                else:
                    # Current asteroid explodes
                    alive = False

            if alive:
                stack.append(asteroid)

        return stack