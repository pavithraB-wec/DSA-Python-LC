from collections import Counter
import heapq

class Solution:
    def rearrangeBarcodes(self, barcodes):
        freq = Counter(barcodes)

        # Max heap: use negative frequency
        heap = [(-count, barcode) for barcode, count in freq.items()]
        heapq.heapify(heap)

        result = []
        prev_count = 0
        prev_barcode = None

        while heap:
            count, barcode = heapq.heappop(heap)

            # If same as previous, use the next most frequent barcode
            if barcode == prev_barcode:
                count2, barcode2 = heapq.heappop(heap)

                result.append(barcode2)
                count2 += 1

                if count2 < 0:
                    heapq.heappush(heap, (count2, barcode2))

                heapq.heappush(heap, (count, barcode))

                prev_barcode = barcode2

            else:
                result.append(barcode)
                count += 1

                if count < 0:
                    heapq.heappush(heap, (count, barcode))

                prev_barcode = barcode

        return result