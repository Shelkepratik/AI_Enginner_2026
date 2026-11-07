
// FastAPI Backend URL
const API_BASE = "http://127.0.0.1:8000";

// HTML Elements
const tableBody = document.getElementById("patientTable");
const searchInput = document.getElementById("searchInput");
const modal = document.getElementById("patientModal");
const form = document.getElementById("patientForm");

let patients = {};
let editingId = null;


// Calculate BMI
function bmiOf(patient) {
    const height = Number(patient.height);
    const weight = Number(patient.weight);

    if (height <= 0) return "—";

    return (weight / (height * height)).toFixed(2);
}


// Calculate BMI Verdict
function verdictOf(patient) {
    const bmi = Number(bmiOf(patient));

    if (bmi < 18.5) {
        return "Underweight";
    }
    else if (bmi < 25) {
        return "Normal";
    }
    else if (bmi < 30) {
        return "Overweight";
    }
    else {
        return "Obese";
    }
}


// Show Notification
function showToast(message) {
    const toast = document.getElementById("toast");

    toast.textContent = message;
    toast.classList.add("show");

    setTimeout(() => {
        toast.classList.remove("show");
    }, 2600);
}


// Show Error Message
function setMessage(message = "") {
    document.getElementById("message").textContent = message;
}


// Common API Request Function
async function apiRequest(path, options = {}) {

    const response = await fetch(`${API_BASE}${path}`, {
        ...options,

        headers: {
            "Content-Type": "application/json",
            ...(options.headers || {})
        }
    });

    const raw = await response.text();

    let data = {};

    try {
        data = raw ? JSON.parse(raw) : {};
    }
    catch {
        data = { detail: raw };
    }

    if (!response.ok) {
        throw new Error(data.detail || `Request failed: ${response.status}`);
    }

    return data;
}


// GET API - Fetch All Patients
async function loadPatients() {

    setMessage("");

    try {

        patients = await apiRequest("/view");

        if (!patients || typeof patients !== "object" || Array.isArray(patients)) {
            patients = {};
        }

        document.getElementById("apiStatus").textContent = "API connected";
        document.getElementById("apiStatus").className = "api-status online";

        renderPatients();

    }
    catch (error) {

        document.getElementById("apiStatus").textContent = "API disconnected";
        document.getElementById("apiStatus").className = "api-status offline";

        tableBody.innerHTML = `
            <tr>
                <td colspan="9" class="empty">
                    Cannot connect to FastAPI: ${escapeHtml(error.message)}
                </td>
            </tr>
        `;

    }
}


// Prevent HTML Injection
function escapeHtml(value) {

    return String(value ?? "").replace(/[&<>"']/g, character => ({
        "&": "&amp;",
        "<": "&lt;",
        ">": "&gt;",
        '"': "&quot;",
        "'": "&#39;"
    }[character]));

}


// Display Patients in Dashboard
function renderPatients() {

    const entries = Object.entries(patients);

    const searchValue = searchInput.value.trim().toLowerCase();

    const filteredPatients = entries.filter(([id, patient]) => {

        return [
            id,
            patient.name,
            patient.city
        ].some(value =>
            String(value ?? "").toLowerCase().includes(searchValue)
        );

    });


    // Dashboard Statistics
    document.getElementById("totalPatients").textContent =
        entries.length;

    document.getElementById("normalCount").textContent =
        entries.filter(([, p]) => verdictOf(p).toLowerCase() === "normal").length;

    document.getElementById("attentionCount").textContent =
        entries.filter(([, p]) => verdictOf(p).toLowerCase() !== "normal").length;


    if (filteredPatients.length === 0) {

        tableBody.innerHTML = `
            <tr>
                <td colspan="9" class="empty">
                    No patient records found.
                </td>
            </tr>
        `;

        return;
    }


    // Generate Table Rows
    tableBody.innerHTML = filteredPatients.map(([id, patient]) => {

        const bmi = bmiOf(patient);
        const verdict = verdictOf(patient);

        return `
            <tr>

                <td class="id">${escapeHtml(id)}</td>

                <td>${escapeHtml(patient.name)}</td>

                <td>${escapeHtml(patient.city)}</td>

                <td>${escapeHtml(patient.age)}</td>

                <td>${escapeHtml(patient.height)}</td>

                <td>${escapeHtml(patient.weight)}</td>

                <td>${bmi}</td>

                <td>
                    <span class="pill ${escapeHtml(verdict.toLowerCase())}">
                        ${escapeHtml(verdict)}
                    </span>
                </td>

                <td>
                    <div class="actions">

                        <button
                            class="secondary"
                            data-action="edit"
                            data-id="${escapeHtml(id)}">
                            Edit
                        </button>

                        <button
                            class="danger"
                            data-action="delete"
                            data-id="${escapeHtml(id)}">
                            Delete
                        </button>

                    </div>
                </td>

            </tr>
        `;

    }).join("");

}


// Open Add / Update Modal
function openModal(mode, id = "") {

    editingId = mode === "edit" ? id : null;

    form.reset();

    document.getElementById("modalTitle").textContent =
        editingId ? `Update ${id}` : "Add patient";

    document.getElementById("patientId").disabled =
        Boolean(editingId);

    document.getElementById("patientId").value = id;


    if (editingId) {

        const patient = patients[id];

        document.getElementById("height").value = patient.height ?? "";
        document.getElementById("weight").value = patient.weight ?? "";

        document.getElementById("name").value = patient.name ?? "";
        document.getElementById("city").value = patient.city ?? "";
        document.getElementById("age").value = patient.age ?? "";
        document.getElementById("gender").value = patient.gender ?? "";

        // Disable other fields because PUT updates only height and weight
        ["name", "city", "age", "gender"].forEach(id => {
            document.getElementById(id).disabled = true;
        });

        document.getElementById("formHint").textContent =
            "Only height and weight will be updated.";

    }
    else {

        ["name", "city", "age", "gender"].forEach(id => {
            document.getElementById(id).disabled = false;
        });

        document.getElementById("formHint").textContent =
            "Enter all required patient details.";

    }


    document.getElementById("saveBtn").textContent =
        editingId ? "Update height & weight" : "Save patient";

    modal.classList.remove("hidden");

}


// Close Modal
function closeModal() {

    modal.classList.add("hidden");

}


// POST API - Add New Patient
// PUT API - Update Height and Weight
form.addEventListener("submit", async function (event) {

    event.preventDefault();

    const value = id =>
        document.getElementById(id).value;

    try {

        if (editingId) {

            // PUT API
            const updateData = {
                height: Number(value("height")),
                weight: Number(value("weight"))
            };

            await apiRequest(`/edit/${encodeURIComponent(editingId)}`, {

                method: "PUT",

                body: JSON.stringify(updateData)

            });

            showToast("Patient updated successfully!");

        }

        else {

            // POST API
            const patientData = {

                id: value("patientId").trim(),

                name: value("name").trim(),

                city: value("city").trim(),

                age: Number(value("age")),

                gender: value("gender"),

                height: Number(value("height")),

                weight: Number(value("weight"))

            };


            await apiRequest("/create", {

                method: "POST",

                body: JSON.stringify(patientData)

            });

            showToast("Patient added successfully!");

        }


        closeModal();

        await loadPatients();

    }

    catch (error) {

        document.getElementById("formHint").textContent =
            error.message;

    }

});


// DELETE API - Delete Patient
tableBody.addEventListener("click", async function (event) {

    const button = event.target.closest("button[data-action]");

    if (!button) return;

    const patientId = button.dataset.id;

    const action = button.dataset.action;


    // Edit Patient
    if (action === "edit") {

        openModal("edit", patientId);

    }


    // Delete Patient
    if (action === "delete") {

        const confirmDelete = confirm(
            `Are you sure you want to delete patient ${patientId}?`
        );

        if (!confirmDelete) return;

        try {

            await apiRequest(`/delete/${encodeURIComponent(patientId)}`, {

                method: "DELETE"

            });

            showToast("Patient deleted successfully!");

            await loadPatients();

        }

        catch (error) {

            setMessage(error.message);

        }

    }

});


// Add Patient Button
document.getElementById("showAddBtn")
    .addEventListener("click", function () {

        openModal("add");

    });


// Close Button
document.getElementById("closeModal")
    .addEventListener("click", closeModal);


// Cancel Button
document.getElementById("cancelBtn")
    .addEventListener("click", closeModal);


// Refresh Button
document.getElementById("refreshBtn")
    .addEventListener("click", loadPatients);


// Search Patient
searchInput.addEventListener("input", renderPatients);


// Close Modal on Outside Click
modal.addEventListener("click", function (event) {

    if (event.target === modal) {

        closeModal();

    }

});


// Initial API Call
loadPatients();
