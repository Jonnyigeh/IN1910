## Project 2 for dilixiay and jonnyai
Github URI: https://github.uio.no/IN1910/H20_project2_dilixiay_Jonnyai

### Cost for array_list.cpp
#### Get element i by index:
- O(1), 3 operasjoner. Vi henter bare ut element med index i fra listen. Dette er samme antall operasjoner uavhengig av hvor mange element n lista inneholder.

#### Insert at front:
- O(n). O(n) når vi vil appende til f.eks element 0. Altså vil antall operasjoner avhenge av index i, og antall elementer i lista n. Vi må kjøre gjennom hele lista, og flytte n elementer et hakk til venstre.

#### Insert at back (append):
- O(1), til tider O(n). Er size < capacity vil det bli gjort like mange operasjoner uavhengig av n. Men i det tilfellet hvor size  == capacity må vi kalle på resize funksjonen, som øker lista fra n til 2n, og det krever n operasjoner (siden vi itererer gjennom hele lista for å kopiere hvert element)

#### Insert into middle of list:
- O(n), Vi utfører (n/2) operasjoner som tilsvarer O(n) siden vi fjerner koeffisienten når vi bruker big Oh notasjon. Vi må kjøre gjennom halve lista for å inserte midt i lista.

#### Remove element from front:
- O(n), vi må kjøre gjennom hele lista å flytte hvert element til høyre etter vi fjerner element med index 0 (Tilsvarende operasjoner som å inserte til index 0)

#### Remove element from back:
- O(1), utfører bare en operasjon, siden vi ikke trenger å "flytte" noen av elementene i lista. Selv om shrink_to_fit blir kalt vil dette max være et visst antall operasjoner uavhengig av størrelsen n.

#### Remove element from middle:
- O(n), tilsvarende som å inserte til midten av lista - vi må kjøre gjennom halve lista n/2 operasjoner

#### Print:
- O(n), vi må iterere over alle n elementer for å printe ut hele lista


### Costs for linked_list.cpp
#### Get element i by index:
 - O(n), vi må kalle på get_node funksjonen som itererer gjennom alle elementer for
 å "flytte" pointer fra head til neste node helt til vi treffer node med index i, og kan så hente ut value

#### Insert at front:
- O(n), dette fordi vi vil at hver node skal kunne peke til "previous", vi må dermed også her kalle på get_node funksjonen som itererer
over hele lista opp til index i. Hadde vi ikke hatt med previous i node structuren vår, ville dette bare kostet O(1) operasjoner. Kunne bare
definert at head skulle peke på en ny node.

#### Insert at back (append):
- O(n), vi må itererere over alle n elementer i lista, og det vil da koste oss n operasjoner.

#### Remove element from front:
- O(n), Vi må igjen kalle på get_node funksjonen som koster (n-i) operasjoner. Det betyr at algoritmen koster mer
jo større lista er siden i = 0.

#### Remove from back:
- O(n) Her vil i = n, og igjen bruker vi get_node funksjonen som koster i operasjoner (vi kjører i<index) og dermed
koster det n operasjoner å fjerne bakerste element.

#### Remove from middle:
- O(n). Her vil vi igjen bruke get_node for å hente ut element i, hvor i = n/2. Dermed koster det oss n/2 operasjoner, som
vi fjerne koeffisient gir oss O(n)

#### Print:
- O(n), vi må hente ut alle values fra alle noder i lista (med n elementer)




#### OPPGAVE 4G:
- Spørsmål: If 𝑛=68 and 𝑘=7, what location in the circle should you choose to survive the ordeal?
- Svar: According to our last_man_standing() function with given n=68 and k=7, the last surviver will be the number 68.
