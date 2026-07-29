let currentTask = null;

function closeAllModals() {
    const modalIds = [
        "info-modal",
        "edit-modal",
        "reopen-modal",
        "delete-modal"
    ];

    modalIds.forEach((modalId) => {
        const modal = document.getElementById(modalId);

        if (modal) {
            modal.classList.remove("active");
        }
    });
}

function openInfoModal(id, title, desc, status, createdAt, completedAt) {
    closeAllModals();

    currentTask = {
        id,
        title,
        desc,
        status,
        createdAt,
        completedAt
    };

    document.getElementById("info-title").textContent = title;
    document.getElementById("info-desc").textContent = desc;
    document.getElementById("info-created").textContent = createdAt;
    document.getElementById("info-completed").textContent = completedAt || "Ainda não concluída";

    const statusElement = document.getElementById("info-status");
    const editButton = document.getElementById("edit-task-button");

    statusElement.textContent = status;
    statusElement.className = "status";

    if (status === "CONCLUIDA") {
        statusElement.classList.add("done");
        editButton.style.display = "none";

    } else if (status === "EXCLUIDA") {
        statusElement.classList.add("deleted");
        editButton.style.display = "none";

    } else {
        statusElement.classList.add("pending");
        editButton.style.display = "block";
    }

    document.getElementById("info-modal").classList.add("active");
}

function closeInfoModal() {
    document.getElementById("info-modal").classList.remove("active");
}

function openEditFromInfo() {
    if (!currentTask) return;

    closeAllModals();

    openEditModal(
        currentTask.id,
        currentTask.title,
        currentTask.desc
    );
}

function openEditModal(id, title, desc) {
    closeAllModals();

    document.getElementById("edit-form").action = `/editar/${id}`;
    document.getElementById("delete-form").action = `/delete/${id}`;
    document.getElementById("edit-title").value = title;
    document.getElementById("edit-desc").value = desc;

    document.getElementById("edit-modal").classList.add("active");
}

function closeEditModal() {
    document.getElementById("edit-modal").classList.remove("active");
}