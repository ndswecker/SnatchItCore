document.addEventListener('DOMContentLoaded', () => {
    // Function to initialize a modal
    function initModal(buttonSelector, modalId) {
        const button = document.querySelector(buttonSelector);
        const modal = document.getElementById(modalId);

        if (button && modal) {
            const modalInstance = new bootstrap.Modal(modal);
            button.addEventListener('click', (event) => {
                console.log(`${modalId} button clicked`);
                event.preventDefault();
                modalInstance.show();
            });
        }
    }

    // Initialize each modal
    initModal('label[for="id_cloacal_protuberance"]', 'cpModal');
    initModal('label[for="id_brood_patch"]', 'bpModal');
    initModal('label[for="id_ff_wear"]', 'ffWearModal');
    initModal('label[for="id_fat"]', 'fatModal');
    initModal('label[for="id_skull"]', 'skullModal');
    initModal('label[for="id_age_WRP"]', 'ageWRPModal');
    // Add more as needed
});
