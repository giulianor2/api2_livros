const API_URL = '/api/books';

document.addEventListener('DOMContentLoaded', () => {
    loadBooks();

    // Adicionar Livro
    document.getElementById('book-form').addEventListener('submit', async (e) => {
        e.preventDefault();
        const title = document.getElementById('title').value;
        const author = document.getElementById('author').value;
        const genre = document.getElementById('genre').value;

        await fetch(API_URL, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ title, author, genre })
        });

        document.getElementById('book-form').reset();
        loadBooks();
    });

    // Busca em tempo real
    document.getElementById('search').addEventListener('input', (e) => {
        loadBooks(e.target.value);
    });
});

async function loadBooks(query = '') {
    let url = API_URL;
    if (query) url += `?q=${query}`;

    const response = await fetch(url);
    const books = await response.json();
    const list = document.getElementById('book-list');
    list.innerHTML = '';

    books.forEach(book => {
        const card = document.createElement('div');
        card.className = `book-card ${book.is_loaned ? 'loaned' : ''}`;
        card.innerHTML = `
            <h3>${book.title}</h3>
            <p><strong>Autor:</strong> ${book.author}</p>
            <p><strong>Gênero:</strong> ${book.genre}</p>
            <p>Status: <strong>${book.is_loaned ? 'Emprestado' : 'Disponível'}</strong></p>
            <div class="actions">
                <button class="btn-loan" onclick="toggleLoan(${book.id})">
                    ${book.is_loaned ? 'Devolver' : 'Emprestar'}
                </button>
                <button class="btn-delete" onclick="deleteBook(${book.id})">Excluir</button>
            </div>
        `;
        list.appendChild(card);
    });
}

async function toggleLoan(id) {
    await fetch(`${API_URL}/${id}/toggle-loan`, { method: 'PUT' });
    loadBooks();
}

async function deleteBook(id) {
    if(confirm('Tem certeza?')) {
        await fetch(`${API_URL}/${id}`, { method: 'DELETE' });
        loadBooks();
    }
}
