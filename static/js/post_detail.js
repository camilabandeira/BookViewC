function openModal(button) {
    const modal = document.getElementById('deleteModal');
    const form = document.getElementById('deleteForm');
    const action = button.closest('form').getAttribute('action');

    form.setAttribute('action', action);

    modal.style.display = 'flex';
}

function closeModal() {
    const modal = document.getElementById('deleteModal');
    modal.style.display = 'none';
}
