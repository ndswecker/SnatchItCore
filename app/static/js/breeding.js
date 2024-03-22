/**
 * Handles the form submission by
 * preventing the default submit action.
 * Submit process is handled manually.
 */
function handleSubmit(e) {
    e.preventDefault();
    return false;
}


const statusModal = new bootstrap.Modal('#status-modal', {});

/**
 * Make status cells display modal on click
 */
document.querySelectorAll(".status").forEach(function(el) {
    el.addEventListener("click", function() {
        // TODO: update modal title to match bird
        document.getElementById("species").setAttribute('value', el.dataset.species);
        document.getElementById("period").setAttribute('value', el.dataset.period);
        statusModal.show();
    });
});

/**
 * Asynchronously submit form and update cell with selected status
 */
document.getElementById("submit-button").addEventListener("click", function () {
    statusModal.hide();

    const form = document.getElementById("status-form");
    const formData = new FormData(form);

    fetch(form.action, {
        method: 'post',
        body: formData,
    }).then(response => {
        if (response.ok) {
            let el = document.getElementById(`${formData.get('species')}-${formData.get('period')}`);
            el.innerHTML = formData.get('status').toString();
            return response.json();
        } else {
            throw new Error('Failed to submit form');
        }
    }).catch(error => {
        console.error(error);
    });
});
