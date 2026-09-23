class Solution(object):
    def transformStr(self, s, strs):
        n = len(s)

        source_prefix = [0] * (n + 1)

        for i in range(n):
            source_prefix[i + 1] = (
                source_prefix[i] + (1 if s[i] == '1' else 0)
            )

        total_ones = source_prefix[n]

        answer = []

        for target in strs:
            fixed_total = 0
            question_total = 0

            for ch in target:
                if ch == '1':
                    fixed_total += 1
                elif ch == '?':
                    question_total += 1

            # Target must be able to contain exactly
            # the same number of 1s as s.
            if total_ones < fixed_total:
                answer.append(False)
                continue

            if total_ones > fixed_total + question_total:
                answer.append(False)
                continue

            fixed_prefix = 0
            question_prefix = 0
            possible = True

            for i in range(n):
                if target[i] == '1':
                    fixed_prefix += 1
                elif target[i] == '?':
                    question_prefix += 1

                # Fixed 1s in the prefix cannot exceed
                # the number of 1s available in s's prefix.
                if fixed_prefix > source_prefix[i + 1]:
                    possible = False
                    break

                fixed_suffix = fixed_total - fixed_prefix
                question_suffix = question_total - question_prefix

                # Minimum number of 1s that must already
                # be placed in this prefix.
                required = total_ones - fixed_suffix - question_suffix

                if required > source_prefix[i + 1]:
                    possible = False
                    break

            answer.append(possible)

        return answer