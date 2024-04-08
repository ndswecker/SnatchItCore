document.addEventListener('DOMContentLoaded', (event) => {
    // Cloacal Protuberance Modal
    // Get the button and the modal
    var cpButton = document.querySelector('label[for="id_cloacal_protuberance"]');
    var cpModal = document.getElementById('cpModal');

    // Check if the button and the modal exist
    if (cpButton && cpModal) {
        // Create a new Bootstrap Modal instance
        var cpModalInstance = new bootstrap.Modal(cpModal);

        // Add a click event listener to the button
        cpButton.addEventListener('click', (event) => {
            console.log('cpButton clicked');
            // Prevent the button's default action
            event.preventDefault();

            // Show the modal
            cpModalInstance.show();
        });
    }

    // Brood Patch Modal
    // Get the button and the modal
    var bpButton = document.querySelector('label[for="id_brood_patch"]');
    var bpModal = document.getElementById('bpModal');

    // Check if the button and the modal exist
    if (bpButton && bpModal) {
        // Create a new Bootstrap Modal instance
        var bpModalInstance = new bootstrap.Modal(bpModal);

        // Add a click event listener to the button
        bpButton.addEventListener('click', (event) => {
            console.log('bpButton clicked');
            // Prevent the button's default action
            event.preventDefault();

            // Show the modal
            bpModalInstance.show();
        });
    }

      // Select the label using the 'for' attribute
    const cpLabel = document.querySelector('label[for="id_cloacal_protuberance"]');

    // Make sure the element exists before adding the event listener
    if (cpLabel) {
        cpLabel.addEventListener('click', function() {
        console.log('CP label was clicked!');
        });
  }
});