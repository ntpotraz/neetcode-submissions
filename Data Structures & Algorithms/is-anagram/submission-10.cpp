class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> count;
        for (char c : s) {
            if (count.contains(c)) {
                count[c] += 1;
            } else {
                count[c] = 1;
            }
        }

        for (char c : t) {
            if (count.contains(c)) {
                count[c] -= 1;
            } else {
                count[c] = 1;
            }

        }

        for (const auto& [c, freq] : count) {
            if (freq != 0) {
                return false;
            }
        }
        return true;

    }
};
