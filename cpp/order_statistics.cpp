#include <bits/stdc++.h>
#include <ext/pb_ds/detail/standard_policies.hpp>
#include <ext/pb_ds/assoc_container.hpp> // Common file
#include <ext/pb_ds/tree_policy.hpp> // Including tree_order_statistics_node_update

typedef __gnu_pbds::tree<int,
__gnu_pbds::null_type,
std::less<int>,
__gnu_pbds::rb_tree_tag,
__gnu_pbds::tree_order_statistics_node_update> ordered_set;

using namespace std;

int main() {
    int n;
    cin >> n;
    ordered_set vals;
    for (int i = 0; i < n; ++i) {
        int v;
        cin >> v;
        cout << "Order of " << v << " is " << vals.order_of_key(v) << endl;
        vals.insert(v);
    }
}
