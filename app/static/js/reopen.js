let formParaReabrir = null;

function openConfirmModal(event) {
    event.preventDefault();

    formParaReabrir = event.target;

    const modal = document.getElementById("reopen-modal");
    modal.classList.add("active");
}

function confirmReopen() {
    if (formParaReabrir) {
        formParaReabrir.submit();
    }
}

function closeReopenModal() {
    const modal = document.getElementById("reopen-modal");
    modal.classList.remove("active");

    formParaReabrir = null;
}