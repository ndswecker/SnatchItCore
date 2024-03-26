$(document).ready(function() {
    // Identifies the trigger element for the popover.
    let $popoverTrigger = $('#view-species-info-popover');

    // Function to initialize the popover with specific options.
    function initializePopover() {
        return $popoverTrigger.popover({
            container: "body", // Sets where the popover is appended in the DOM.
            html: true, // Allows HTML content inside the popover.
            trigger: "manual", // The popover is triggered programmatically.
            content: function() { // Function to dynamically set the content of the popover.
                let speciesNumber = $('#id_species_number').val(); // Gets the currently selected species number.
                if (speciesNumber) {
                    // If a species is selected, fetch and return its specific information.
                    return fetchSpeciesInfo(speciesNumber);
                } else {
                    // If no species is selected, return a default message.
                    return "Select a species to view its information.";
                }
            }
        });
    }

    let $popover = initializePopover(); // Initialize and store the popover instance.

    // Event listener for click events on the popover trigger.
    $popoverTrigger.on('click', function(e) {
        e.stopPropagation(); // Prevents the click event from propagating to other elements.
        $popover.popover('toggle'); // Toggles the visibility of the popover.
    });

    // Function to fetch specific species information based on the species number.
    function fetchSpeciesInfo(speciesNumber) {
        let content = "Loading..."; // Default loading message.
        let destination_url = `/maps/mini_pyle/${speciesNumber}/`; // URL to fetch species info from.
        $.ajax({
            url: destination_url,
            async: false, // Note: It's generally recommended to use asynchronous requests.
            success: function(htmlSnippet) {
                content = htmlSnippet; // On success, update content with the fetched HTML snippet.
            },
            error: function() {
                content = "Could not retrieve species information. Please try again."; // On error, display an error message.
            }
        });
        return content;
    }

    // Event listener for clicks on the document to close the popover when clicking outside of it.
    $(document).on('click', function(e) {
        if (!$(e.target).closest('#view-species-info-popover').length) {
            $popover.popover('hide'); // Hides the popover if the click is outside the popover trigger.
        }
    });

    // Event listener for changes in the species number select element.
    $('#id_species_number').change(function() {
        $popover.popover('dispose'); // Disposes of the current popover instance.
        $popover = initializePopover(); // Reinitializes the popover for the new species selection.
    });

    // Initialize Choices.js for the species_number field.
    var speciesSelect = document.getElementById('id_species_number');
    if (speciesSelect) {
        var choices = new Choices(speciesSelect, {
            searchEnabled: true,
            itemSelectText: '',
            removeItemButton: true,
        });
    }

    // Initialize Choices.js for the capture_code field.
    var captureCodeSelect = document.getElementById('id_capture_code');
    if (captureCodeSelect) {
        var choices = new Choices(captureCodeSelect, {
            searchEnabled: true,
            itemSelectText: '',
            removeItemButton: true,
        });
    }
});
