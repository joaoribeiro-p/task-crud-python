let formParaDeletar = null;

function openDeleteModal(event) {
    event.preventDefault();
    event.stopPropagation();

    formParaDeletar = event.currentTarget;
    
    closeAllModals();

    document.getElementById("delete-modal").classList.add("active");
}

function confirmDelete() {
    if (formParaDeletar) {
        formParaDeletar.submit();
    }
}

function closeDeleteModal() {
    document.getElementById("delete-modal").classList.remove("active");
    formParaDeletar = null;
}