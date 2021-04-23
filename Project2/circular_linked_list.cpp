#include <iostream>
#include <vector>
using namespace std;

struct Node {
    /*
    Lager Node med en value, en node som peker til neste og en til forrige Node.
    La til to initializer som tar imot enten kun verdi som blir gitt eller med inkludert pekere.
    */
    int value;
    Node *next;
    Node *prev;

    Node(int n) {
    value = n;
    next = nullptr;
    prev = nullptr;
    }
    Node(int n, Node *p, Node *q) {
    value = n;
    next = p;
    prev = q;
    }
};


class CircLinkedList {
    private:
        Node *head;
        Node *tail;
        int size;
    /*
    get_node som henter node ved gitt index ligger i private fordi vi vil ikke at det skal bli endret på utenfor classen.
    Here I also tested if every node is connected and link in correct way. 
    */
        Node* get_node(int index) {
            if (head==nullptr) {
                throw range_error("IndexError: Index out of range");
            }
            Node* current = head;
            for (int i=0; i<index; i++) {
                current = current->next;
                
            }
            return current;
        }


    public:
        CircLinkedList(){
            size = 0;
            head = nullptr;
            tail = nullptr;
        }

        CircLinkedList(int value){
            size = 0;
            head = nullptr;
            tail = nullptr;
            //Her appender vi inn initial listen en og en, slik som om vi hadde gjort det for hvert enkelte tall.
            for (int i = 1; i < value+1; i++){
                append(i);
            }
        }

        int lenght(){
            return size;
        }

        /*
        Append metoden fungerer slik som double link list men denne gangen peker den siste til første også.
        */
        void append(int val) {
            Node* newnode; 
            newnode = new Node(val);
            newnode->prev = newnode;
            newnode->next = newnode;

            if (head == nullptr){
                head = newnode;
                tail = head;
                size += 1;
            }
            else {
                tail->next = newnode;
                newnode->prev = tail;
                newnode->next = head;
                head->prev = newnode;
                tail = tail->next;
                size += 1;
            }
        }

        void print() {
            Node* temp = head;
            cout << "[";
            while (temp->next != head) {
                cout << temp->value;
                cout << ", ";
                temp = temp->next;
            }
            cout << temp->value << "]" << endl;
            }


        int& operator[](int index) {
            return get_node(index)->value;
        }


        /*
        I remove metoden, sjekker vi om current (som henter noden fra get_node metoden) er den første eller siste, 
        for da må vi endre på hvordan koblingen blir dersom det er den første og siste noden i forhold til de i midten.
        */
        void remove(int index){
            Node* current = get_node(index);
            
           if (current == head){
               tail->next = current->next;
               head = current->next;
               delete current;
               size -= 1;
               
           } 
           else if(current == tail){
               tail = current->prev;
               tail->next = head;
               delete current;
               size -= 1;
           }
           else{
            current->prev->next = current->next;
            current->next->prev = current->prev;
            delete current;
            size -= 1;  
           }
        }
        /*
        Vi looper gjennom linked listen og "sletter" (free) fra listen samtidig som vi legger slettede tallet i ny vector.
        */
        vector<int> josephus_sequence(int k){
            vector<int> newlist;
            vector<int> vec;
            Node* current = head;
            Node* tmp;
            int i;

            for (int j = 0; j < size; j++){
                for (int l = 0; l < k-1; l++){
                    tmp = current;
                    current = current->next;
                }
                i = current->value;
                tmp->next = current->next;
                free(current);
                current = tmp->next;
                vec.push_back(i);
            }

            return vec;
        }
        
};

int last_man_standing(int n, int k){
       vector<int> vec;
       CircLinkedList a(n);
       vec = a.josephus_sequence(k);
        int lastman;
       for (int i=0; i<vec.size(); i++){
           cout << "next person to go: "<< vec[i] << endl;
           if (i == vec.size()-1){
               lastman = vec[i];
           }
       }
    return lastman;
   }

int main() {
    cout << endl;

    CircLinkedList a;
    a.append(11);
    a.append(13);
    a.append(14);
    a.append(16);
    a.append(18);
    cout << "When appending five numbers in to the list: ";
    a.print();
    cout << "length of the list: " << a.lenght() << endl << endl;

   
   CircLinkedList b(6);
   cout << "Giving the class initializer from 1 to 6: ";
   b.print();
   cout << "size of the list: " << b.lenght() << endl << endl;
   


    cout << "from the list above, we eliminate every 3rd number: ";
    vector<int> vec = b.josephus_sequence(3);
   for (int i = 0; i < vec.size(); i++){
       cout << vec[i] << ",";
   }
   cout << endl << endl;

   cout << "now with our stand alone function with n=10, k=2, we will get both elimination order and last man standing: "<< endl;
   int lastman = last_man_standing(10, 2);
    cout << "Last man standing: " << lastman << endl;
   
}
