class Solution {
public:
    int minMutation(string startGene, string endGene, vector<string>& bank) {
        unordered_set<string> dict(bank.begin(), bank.end());
        if (!dict.count(endGene)) return -1;
        static const char letters[4] = {'A', 'C', 'G', 'T'};
        queue<string> q;
        q.push(startGene);
        for (int steps = 0; !q.empty(); ++steps) {
            for (int sz = q.size(); sz; --sz) {
                string gene = q.front(); q.pop();
                if (gene == endGene) return steps;
                dict.erase(gene);
                for (int i = 0; i < 8; ++i) {
                    char orig = gene[i];
                    for (char c : letters) {
                        gene[i] = c;
                        if (dict.count(gene)) {
                            q.push(gene);
                            dict.erase(gene);
                        }
                    }
                    gene[i] = orig;
                }
            }
        }
        return -1;
    }
};
