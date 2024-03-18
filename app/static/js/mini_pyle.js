let popoverTriggerList = [].slice.call(document.querySelectorAll('#view-species-info-popover'));

let popoverList = popoverTriggerList.map(function(popoverTriggerEl) {
    return new bootstrap.Popover(popoverTriggerEl, {
        container: "body",
        html: true,
        trigger: "click",
        content: function() {
            let speciesNumber = $('#id_species_number').val();
            if (speciesNumber) {
                return fetchSpeciesInfo(speciesNumber);
            } else {
                return "Select a species to view its information.";
            }
        }
    });
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

// Ensure popover updates when species number changes
$('#id_species_number').change(function() {
    popoverList.forEach(function(popover) {
        popover.dispose();
    });
    popoverList = popoverTriggerList.map(function(popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl, {
            container: "body",
            html: true,
            trigger: "click",
            content: function() {
                let speciesNumber = $('#id_species_number').val();
                if (speciesNumber) {
                    return fetchSpeciesInfo(speciesNumber);
                } else {
                    return "Select a species to view its information.";
                }
            }
        });
    });
});
