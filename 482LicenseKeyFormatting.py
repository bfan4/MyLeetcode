class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        mod = 0
        S = S.replace('-', '').upper()
        mod = len(S) % K
        if mod == 0:
            mod += K
        
        while mod < len(S):
            S = S[:mod] + '-' + S[mod:]
            mod += K + 1
        return S