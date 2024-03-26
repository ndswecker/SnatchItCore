$(document).ready(function() {
    $('#id_capture_code').on('change', function() {
        var captureCode = $(this).val();
        var bandSizeSelect = $('#id_band_size');
        var bandNumberInput = $('#id_band_number');
        var statusSelect = $('#id_status'); // Assuming the ID for the status select field is 'id_status'

        if (captureCode === 'R') {
            // For recaptured birds, set band size to "R", disable the field, and log the change
            bandSizeSelect.val('R').trigger('change').prop('disabled', true);
            console.log('Capture code set to Recaptured. Band size locked to "R".');
        } else if (captureCode === 'U') {
            // For unbanded birds, set band size to "U", clear band number, but do not disable the band size field
            // Additionally, set the status select to "0" for unbanded birds
            bandSizeSelect.val('U').trigger('change');
            bandNumberInput.val('');
            statusSelect.val('0').trigger('change'); // Set status to "0"
            console.log('Capture code set to Unbanded. Band size set to "U", band number cleared, and status set to "0".');
        } else {
            // For any other capture code, ensure band size, band number, and status fields are enabled
            bandSizeSelect.prop('disabled', false);
            bandNumberInput.prop('disabled', false);
            statusSelect.prop('disabled', false); // Ensure the status field is enabled for other capture codes
            console.log('Capture code changed. Band size, band number, and status fields are enabled.');
        }
    });
});
