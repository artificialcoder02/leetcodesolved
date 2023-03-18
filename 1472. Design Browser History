// A struct to represent a node in a doubly linked list
struct Node {
  // The previous and next nodes in the list
  Node* prev = nullptr;
  Node* next = nullptr;
  // The URL represented by this node
  const string url;

  // Constructor that sets the URL for this node
  Node(const string& url) : url(url) {}
};

// A class to represent a browser history
class BrowserHistory {
 public:
  // Constructor that creates a new history with the given homepage
  BrowserHistory(string homepage) {
    // Create a new node to represent the homepage
    curr = new Node(homepage);
  }

  // Method to add a new URL to the history
  void visit(string url) {
    // Create a new node to represent the new URL
    curr->next = new Node(url);
    // Set the previous node for the new node to be the current node
    curr->next->prev = curr;
    // Make the new node the current node
    curr = curr->next;
  }

  // Method to navigate back in the history by the given number of steps
  string back(int steps) {
    // While there are previous nodes and we haven't gone back enough steps yet
    while (curr->prev && steps-- > 0) {
      // Move back one node by setting the current node to the previous node
      curr = curr->prev;
    }
    // Return the URL represented by the current node
    return curr->url;
  }

  // Method to navigate forward in the history by the given number of steps
  string forward(int steps) {
    // While there are next nodes and we haven't gone forward enough steps yet
    while (curr->next && steps-- > 0) {
      // Move forward one node by setting the current node to the next node
      curr = curr->next;
    }
    // Return the URL represented by the current node
    return curr->url;
  }

 private:
  // The current node in the history
  Node* curr = nullptr;
};
