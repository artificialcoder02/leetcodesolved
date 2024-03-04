class Solution:
    def bagOfTokensScore(self, tokens, power):
        tokens.sort()   # Sort the tokens in ascending order
        s = 0                  # Current score
        maxi = 0               # Maximum score
        l, r = 0, len(tokens) - 1  # Pointers for the left and right ends of the sorted tokens
        
        # Iterate through the tokens using a two-pointer approach
        while l <= r:
            if power >= tokens[l]:   # If the remaining power is greater than or equal to the smallest token
                power -= tokens[l]   # Reduce power
                s += 1               # Increase score
                l += 1               # Move left pointer to the right
                maxi = max(maxi, s)  # Update maximum score if the current score is higher
            elif s > 0:      # If the current score is positive, consider trading tokens for power           
                power += tokens[r]   # Increase power
                s -= 1               # Decrease score
                r -= 1               # Move right pointer to the left
            else:
                # Exit the loop if neither condition is met
                break
        return maxi  # Return the maximum score
