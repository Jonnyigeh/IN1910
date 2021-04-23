#include <iostream>
#include <vector>
#include <stdexcept>
class ArrayList {
private:
  int *data;
  int capacity;
  int growth_factor = 2;
void resize() {
    /*
    * Lager en ny, større array tmp ved growth factor * lengde til data.
    * Kopierer elemenete fra data over til tmp.
    * Sletter data, og redifenerer data lik tmp.
    */
    capacity *= growth_factor;
    int *tmp = new int[capacity];
    for (int i=0; i<size;i++) {
      tmp[i] = data[i];
    }
    delete[] data;
    data = tmp;
  }
public:
    int size;
ArrayList() {             // Konstruktør
    capacity = 1;
    size = 0;
    data = new int[capacity];
}
ArrayList(std::vector<int> initial_list) {
  /*
  Overload av konstruktør, slik at vi kan initialisere
  ArrayList med en eksisterende vector.
  */
  capacity = 2;
  int i = 1;
  size = initial_list.size();
  while (capacity < size) {
    capacity *= growth_factor;
  }
  data = new int[capacity];
  for (int i=0;i<size;i++) {
    data[i] = initial_list[i];
  }
}

~ArrayList() {        // Destruktør
    delete[] data;
  }

int& operator[](int i) {
  /*
  * Returnerer en referanse til element i i data
  * som gir oss mulighet til å get og set element i.
  */
  if ((i > size) || (i < 0)) {
    throw std::range_error("Index is out of bounds");
  } return data[i];
}
void append(int n) {
    /*
    * @param Tar inn integer som skal legges til i liste
    * Sjekker at det er "plass" i lista, og legger til elementet
    * Er det ikke mer plass, kalles resize funksjonen slik at vi får
    * en større array.
    */
    if (size >= capacity) {
      resize();
    }
    if (size < capacity) {
        data[size] = n;
        size += 1;
      }
    }
void insert(int val, int index) {
  /*
  * @param Verdi, og index hvor vi ønsker å sette verdi.
  * Flytter også hvert element for i>index et hakk "oppover"
  * for å gjøre plass til elementet vi inserter.
  */
  if (size == capacity) {
    resize();
  }
  if ((index < 0) || (index > size)) {
    throw std::range_error("Index out of bounds!");
  }
  if (index == size) {
    append(val);
  }
  int i = 0;
  while (size-i > index) {
    data[size-i] = data[size-i-1];
    i += 1;
  } data[index] = val;
  size += 1;
}

void remove(int index) {
  /*
  * Fjerner element data[index]
  * og minsker size med 1. Kaller shrink_to_fit når size <= 25% av capacity
  */
  for (int i=index;i<size-1;i++) {
    data[i] = data[i+1];
  } size -= 1;
  if (capacity/4 >= size) {
    shrink_to_fit();
  }
}
int pop(int index) {
  /*
  * Fjerner, og returnerer element data[index]
  */
  int tmp = data[index];
  remove(index);
  return tmp;
}
int pop() {
  /*
  * Fjerner, og returnerer siste element i data
  */
  pop(size-1);
}
void shrink_to_fit() {
  /*
  Krymper kapasitet for å frigi minne som ikke blir
  brukt ved å finne minste n s.a 2^n > size.
  */
  int n = capacity;
  while (n >= 2*size) {
    n = n/2;
  } capacity = n;
}
int getcapacity() {
  /*
  * Returnerer kapasitet, altså hvor mye minne som er
  * satt av til data.
  */
  return capacity;
}
int length() {
  /*
  * Returner lengden til listen generert ved klassen ArrayList
  */
    return size;
  }
void print() {
  /*
  * Printer ut hele listen lagret i data
  * på formen [1, 2, .., n]
  */
  std::cout << "[" << "";
  for (int i=0; i<size-1;i++) {
    std::cout << data[i] << ", ";
  }
  std::cout << data[size-1] << "]" << std::endl;
}

};
bool is_prime(int N) {
  /*
  * @param Tar en integer N > 0, kaster feilmelding om N <= 0.
  * Sjekker om N er et primtall
  * @return true er N primtall, false ellers
  */
  if (N <= 0) {
    throw std::range_error("N must be > 0");
  }
  if (N == 1) {
    return false;
  }
  for (int d=2; d<N;d++) {
    if (N % d == 0) {
      return false;
    }
  }
  return true;
}
void test_prime_arraylist() {
  /*
  Testfunksjon av klassen opg.1e)
  Lager liste med 10 første primtall, og printer til terminal.
  */
  ArrayList primelist;
  int N = 1;
  while (primelist.length() < 10) {
    if (is_prime(N)) {
      primelist.append(N);
    }
  N += 1;
  }
  std::cout << "First 10 primenumbers:" << " ";
  primelist.print();
}
void test_shrink_to_fit() {
  /*
  * Testfunksjon av shrink_to_fit, opg 1i)
  * Sjekker at kapasiteten minsker når den skal
  * og printer til terminal.
  */
  ArrayList p({0,0,0,0});
  std::cout << "Initial capacity = " << p.getcapacity() << std::endl;
  p.append(2);
  std::cout << "Expected = 8, computed = " << p.getcapacity() << std::endl;
  p.remove(2);
  p.shrink_to_fit();
  std::cout << "Expected = 4, computed = " << p.getcapacity() << std::endl;
}
int main() {
  /*
  Kjøreeksempel for å teste funksjonalitet
  ihht opg. 1a) og 1d)
  */
  ArrayList instance;
  std::cout << "length = " << instance.length() << std::endl;
  instance.append(1);
  std::cout << "length = " << instance.length() << std::endl;
  for (int i=2; i<10;i++) {
    instance.append(i);
  }
  instance.print();

  test_prime_arraylist(); // Kjører testfunksjonen 1e)
  // Kjøreeksempel 1f, 1g, 1h, 1j
  ArrayList primes({2, 3, 5, 8, 11});
  primes.print();
  primes[2] = 0;
  primes.print();
  primes.insert(5, 3);
  primes.print();
  std::cout << primes.pop(3) <<std::endl;
  primes.print();
  primes.pop();
  std::cout << primes.getcapacity() << std::endl;
  primes.pop();
  primes.pop();
  primes.print();
  std::cout << primes.getcapacity() << std::endl;

  test_shrink_to_fit(); // Testfunksjon for shrink_to_fit 1i
  return 0;
}
