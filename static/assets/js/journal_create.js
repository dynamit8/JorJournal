// 1. Initial State: Add one block on load
window.onload = () => addLogBlock();

function addLogBlock() {
    const container = document.getElementById('logs-container');
    const blockHtml = `
        <div class="log-block border p-3 mb-3">
            <input type="text" class="form-control summary-input" placeholder="Summary (e.g. Basic Setup)">
            <div class="items-container mt-2">
                <input type="text" class="form-control item-input mb-1" placeholder="Item 1">
                <input type="text" class="form-control item-input mb-1" placeholder="Item 2">
            </div>
            <button type="button" class="btn btn-sm btn-link" onclick="addItem(this)">+ Add Item</button>
        </div>`;
    container.insertAdjacentHTML('beforeend', blockHtml);
}

function addItem(btn) {
    const itemHtml = `<input type="text" class="form-control item-input mb-1" placeholder="New Item">`;
    btn.previousElementSibling.insertAdjacentHTML('beforeend', itemHtml);
}

// 2. The Magic: Convert the UI into JSON before sending to Django
function prepareJson() {
    const logs = [];
    document.querySelectorAll('.log-block').forEach(block => {
        const summary = block.querySelector('.summary-input').value;
        const items = Array.from(block.querySelectorAll('.item-input'))
            .map(input => input.value)
            .filter(val => val !== ""); // Remove empty items

        if (summary) {
            logs.push({ summary: summary, items: items });
        }
    });
    document.getElementById('id_logs').value = JSON.stringify(logs);
}