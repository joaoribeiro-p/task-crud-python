let formParaReabrir = null;

function openConfirmModal(event) {
    event.preventDefault();
    event.stopPropagation();

    closeAllModals();

    formParaReabrir = event.target;

    document.getElementById("reopen-modal").classList.add("active");
}

function confirmReopen() {
    if (formParaReabrir) {
        formParaReabrir.submit();
    }
}

function closeReopenModal() {
    document.getElementById("reopen-modal").classList.remove("active");
    formParaReabrir = null;
}