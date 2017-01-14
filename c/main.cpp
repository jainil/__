#include <iostream> // Include for I/O streams

using namespace std; // Streams are in the std namespace (standard library)

int main()
{
//    int myInt;

//    // Prints to stdout (or terminal/screen)
//    cout << "Enter your favorite number:\n";
//    // Takes in input
//    cin >> myInt;

//    // cout can also be formatted
//    cout << "Your favorite number is " << myInt << "\n";
//    // prints "Your favorite number is <myInt>"

//    cerr << "Used for error messages";

    string foo = "I am foo";
    string bar = "I am bar";

    string& barRef = bar;

    string& fooRef = foo; // This creates a reference to foo.
    fooRef += ". Hi!"; // Modifies foo through the reference
    cout << fooRef << endl; // Prints "I am foo. Hi!"

    // Doesn't reassign "fooRef". This is the same as "foo = bar", and
    //   foo == "I am bar"
    // after this line.
    // cout << &fooRef << endl; //Prints the address of foo
    // fooRef = bar; // this modifies foo, not the reference
    // cout << &fooRef << endl; //Still prints the address of foo
    // cout << fooRef << endl;  // Prints "I am bar"
    // cout << foo;

    cout << &fooRef << endl;
    fooRef = barRef; 
    cout << &fooRef << endl;
    cout << fooRef << endl;
    cout << foo << endl;

    //The address of fooRef remains the same, i.e. it is still referring to foo.
}