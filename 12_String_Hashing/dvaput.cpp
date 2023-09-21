#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1e9 + 7;
const int BAS = 200;

long long ok(const string& s, int n) {
    if (n == 0) return true;
    if (n == 1) {
        set<char> uniq(s.begin(), s.end());
        return uniq.size() != s.size();
    }
    
    long long cur = 0;
    long long rem = 1;
    for (int i = 0; i < n - 1; i++) {
        rem = (rem * BAS) % MOD;
    }

    unordered_map<long long, bool> seen;
    for (int i = 0; i < n; i++) {
        cur = (cur * BAS) % MOD;
        cur = (cur + s[i]) % MOD;
    }
    
    seen[cur] = true;
    for (int i = n; i < (int)s.size(); i++) {
        cur = (cur - s[i - n] * rem) % MOD;
        if (cur < 0) cur += MOD;
        
        cur = (cur * BAS) % MOD;
        cur = (cur + s[i]) % MOD;

        if (seen.count(cur)) return true;
        seen[cur] = true;
    }

    return false;
}

int high_bound(const string& a) {
    int l = 0, r = a.size();
    int ans = -1;
    while (l < r) {
        int mid = (l + r) / 2;
        if (ok(a, mid)) {
            ans = mid;
            l = mid + 1;
        } else {
            r = mid;
        }
    }
    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    
    int h;
    cin >> h;
    cin.ignore();
    
    string s;
    getline(cin, s);

    cout << high_bound(s) << "\n";

    return 0;
}