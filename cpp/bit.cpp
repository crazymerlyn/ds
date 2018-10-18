#include <stdint.h>
#include <vector>
#include <assert.h>

template<typename T>
class Bit {
public:
    Bit(int n): ar(n+1) {}
    T operator [](std::size_t i) {
        T res{};
        while (i > 0) {
            res += ar[i];
            i = i & (i - 1);
        }
        return res;
    }

    void update(int i, T val) {
        while (i < ar.size()) {
            ar[i] += val;
            i += i & (-i);
        }
    }
private:
    std::vector<T> ar;
};

int main() {
    using namespace std;
    int n = 1000;
    vector<int> vec(n);
    for (int i = 0; i < n; ++i) vec[i] = n - i;
    Bit<int> b(n);
    long long res = 0;
    for (int i = n-1; i >= 0; --i) {
        res += b[vec[i]];
        b.update(vec[i], 1);
    }
    assert(res == n * (n-1) / 2);
}
