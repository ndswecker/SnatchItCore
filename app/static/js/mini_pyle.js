$(document).ready(function() {
    let $popoverTrigger = $('#view-species-info-popover');

    function initializePopover() {
        return $popoverTrigger.popover({
            container: "body",
            html: true,
            trigger: "manual",
            content: function() {
                let speciesNumber = $('#id_species_number').val();
                if (speciesNumber) {
                    return fetchSpeciesInfo(speciesNumber);
                } else {
                    return "Select a species to view its information.";
                }
            }
        });
    }

    let $popover = initializePopover(); // Initialize the popover

    $popoverTrigger.on('click', function(e) {
        // Prevent closing on click inside the popover
        e.stopPropagation();
        // Toggle popover
        $popover.popover('toggle');
    });

    function fetchSpeciesInfo(speciesNumber) {
        let content = "Loading...";
        let destination_url = `/maps/mini_pyle/${speciesNumber}/`;
        $.ajax({
            url: destination_url,
            async: false, // Note: Synchronous requests are discouraged
            success: function(htmlSnippet) {
                content = htmlSnippet;
            },
            error: function() {
                content = "Could not retrieve species information. Please try again.";
            }
        });
        return content;
    }

    // Close the popover when clicking outside
    $(document).on('click', function(e) {
        if (!$(e.target).closest('#view-species-info-popover').length) {
            $popover.popover('hide');
        }
    });

    // Ensure popover updates when species number changes
    $('#id_species_number').change(function() {
        $popover.popover('dispose'); // Dispose of the current popover
        $popover = initializePopover(); // Reinitialize the popover
    });
});
