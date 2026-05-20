function openEditModal(id, title, desc) {
    const modal = document.getElementById("edit-modal");
    const form = document.getElementById("edit-form");
    const titleInput = document.getElementById("edit-title");
    const descInput = document.getElementById("edit-desc");

    form.action = `/editar/${id}`;
    titleInput.value = title;
    descInput.value = desc;

    modal.classList.add("active");
}

function closeEditModal() {
    const modal = document.getElementById("edit-modal");
    modal.classList.remove("active");
}