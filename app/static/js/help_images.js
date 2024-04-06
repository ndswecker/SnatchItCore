document.addEventListener('DOMContentLoaded', (event) => {
    // Get the div where you want to insert the modal
    var cp_div = document.getElementById('div_id_cloacal_protuberance');

    // Create the modal button
    var cpModalButton = document.createElement('button');
    cpModalButton.type = 'button';
    cpModalButton.id = 'view-cp-info-modal';
    cpModalButton.className = 'btn btn-lg btn-danger w-100';
    cpModalButton.dataset.bsToggle = 'modal';
    cpModalButton.dataset.bsTarget = '#cpModal';
    cpModalButton.textContent = 'CP Scores';

    // Insert the modal button into the div
    cp_div.appendChild(cpModalButton);

    // Create the modal
    var cpModal = document.createElement('div');
    cpModal.className = 'modal fade';
    cpModal.id = 'cpModal';
    cpModal.tabIndex = '-1';
    cpModal.ariaLabelledby = 'cpModalLabel';
    cpModal.ariaHidden = 'true';
    cpModal.innerHTML = `
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="cpModalLabel">CP Scores</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <img src="/static/img/cloacal_protuberance.png" alt="Cloacal Protuberance" class="img-fluid">
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                </div>
            </div>
        </div>
    `;

    // Insert the modal into the body
    document.body.appendChild(cpModal);

    // Initialize the modal
    var cpModalInstance = new bootstrap.Modal(cpModal);

    // Get the div where you want to insert the modal
    var bp_div = document.getElementById('div_id_brood_patch');

    // Create the modal button
    var bpModal = document.createElement('button');
    bpModal.type = 'button';
    bpModal.id = 'view-bp-info-modal';
    bpModal.className = 'btn btn-lg btn-danger w-100';
    bpModal.dataset.bsToggle = 'modal';
    bpModal.dataset.bsTarget = '#bpModal';
    bpModal.textContent = 'BP Scores';

    // Insert the modal button into the div
    bp_div.appendChild(bpModal);

    // Create the modal
    var modal = document.createElement('div');
    modal.className = 'modal fade';
    modal.id = 'bpModal';
    modal.tabIndex = '-1';
    modal.ariaLabelledby = 'bpModalLabel';
    modal.ariaHidden = 'true';
    modal.innerHTML = `
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="bpModalLabel">BP Scores</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <img src="/static/img/brood_patch.png" alt="Brood Patch" class="img-fluid">
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                </div>
            </div>
        </div>
    `;

    // Insert the modal into the body
    document.body.appendChild(modal);

    // Initialize the modal
    var bpModal = new bootstrap.Modal(modal);
});

