let currentTask = null;

function openInfoModal(id, title, desc, status, createdAt, completedAt) {
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
    statusElement.textContent = status;
    statusElement.className = "status";

    if (status === "CONCLUIDA") {
        statusElement.classList.add("done");
    } else {
        statusElement.classList.add("pending");
    }

    document.getElementById("info-modal").classList.add("active");

    const editButton = document.getElementById("edit-task-button");

    if (status === "CONCLUIDA") {
        statusElement.classList.add("done");
        editButton.style.display = "none";
    } else {
        statusElement.classList.add("pending");
        editButton.style.display = "block";
    }
}

function closeInfoModal() {
    document.getElementById("info-modal").classList.remove("active");
}

function openEditFromInfo() {
    if (!currentTask) return;

    closeInfoModal();

    openEditModal(
        currentTask.id,
        currentTask.title,
        currentTask.desc
    );
}

function openEditModal(id, title, desc) {
    document.getElementById("edit-form").action = `/editar/${id}`;
    document.getElementById("edit-title").value = title;
    document.getElementById("edit-desc").value = desc;

    document.getElementById("edit-modal").classList.add("active");
}

function closeEditModal() {
    document.getElementById("edit-modal").classList.remove("active");
}