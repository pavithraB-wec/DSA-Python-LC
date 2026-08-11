class Solution(object):
    def movesToStamp(self, stamp, target):
        stamp_len = len(stamp)
        target_len = len(target)

        target = list(target)
        result = []
        changed = True

        # Check whether stamp can erase target[start:start+stamp_len]
        def can_erase(start):
            matched = False

            for j in range(stamp_len):
                if target[start + j] == '?':
                    continue

                if target[start + j] != stamp[j]:
                    return False

                matched = True

            return matched

        # Keep finding places where the stamp can be applied
        while changed:
            changed = False

            for i in range(target_len - stamp_len + 1):
                if can_erase(i):
                    # Erase this part
                    for j in range(stamp_len):
                        target[i + j] = '?'

                    result.append(i)
                    changed = True

            if all(c == '?' for c in target):
                result.reverse()
                return result

        return []