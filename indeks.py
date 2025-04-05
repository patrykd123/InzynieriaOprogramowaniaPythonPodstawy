import re
from collections import defaultdict

def index_documents(documents: list[str], queries: list[str]) -> list[list[int]]:
    """
    Przetwarza dokumenty i zapytania, zwracając listy indeksów dokumentów,
    w których występuje zapytanie, posortowane według częstości wystąpienia
    danego wyrazu (malejąco), a w przypadku równych częstości - malejąco wg numeru dokumentu.

    Args:
        documents (list[str]): Lista dokumentów (każdy dokument to ciąg znaków).
        queries (list[str]): Lista zapytań (każdy zapytanie to pojedynczy wyraz).

    Returns:
        list[list[int]]: Lista wyników dla kolejnych zapytań.
    """
    # Normalizacja dokumentów: usunięcie interpunkcji i zamiana na małe litery
    normalized_docs = [
        re.findall(r'\b\w+\b', doc.lower()) for doc in documents
    ]

    # Tworzenie indeksu odwrotnego: słowo -> {dokument: liczba wystąpień}
    inverted_index = defaultdict(lambda: defaultdict(int))
    for doc_id, words in enumerate(normalized_docs):
        for word in words:
            inverted_index[word][doc_id] += 1

    # Przetwarzanie zapytań
    results = []
    for query in queries:
        query = query.lower()
        if query in inverted_index:
            # Pobierz dokumenty i ich liczby wystąpień
            doc_counts = inverted_index[query]
            # Posortuj według liczby wystąpień (malejąco), a potem wg numeru dokumentu (malejąco)
            sorted_docs = sorted(
                doc_counts.keys(),
                key=lambda doc_id: (-doc_counts[doc_id], -doc_id)
            )
            results.append(sorted_docs)
        else:
            # Jeśli słowo nie występuje w żadnym dokumencie, zwróć pustą listę
            results.append([])

    return results

# Przykładowe wywołanie:
if __name__ == "__main__":
    # Pobranie liczby dokumentów
    n = int(input("Podaj liczbę dokumentów: "))
    documents = []
    print("Wprowadź kolejne dokumenty:")
    for _ in range(n):
        documents.append(input())

    # Pobranie liczby zapytań
    m = int(input("Podaj liczbę zapytań: "))
    queries = []
    print("Wprowadź kolejne zapytania:")
    for _ in range(m):
        queries.append(input().strip())

    # Przetworzenie zapytań
    results = index_documents(documents, queries)

    # Wypisanie wyników
    print("Wyniki:")
    for res in results:
        print(res)