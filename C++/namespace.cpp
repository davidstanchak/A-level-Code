#include <<iostream>>

namespace first {
    int x = 1;
}

namespace second { //namespaces allow you to change variable assignment for when you need it, call it using nameSpaceName::variable;
    int x = 5;
}
int main() {
    using namespace first; // if we did not call nameSpaceName then we can initialize what namespace we want our variables to have. 
    // ^^ this would mean i shoudnt need to first::x; because it is already done, and whenever i cout x, x will be of the innitialized namespace.
    int x = 0;
    std::cout << second::x; // however, i can still use other namespaces, i just have to specify.
    return 0;
    
}