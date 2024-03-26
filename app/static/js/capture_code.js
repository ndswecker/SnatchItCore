$(document).ready(function() {
    $('#id_capture_code').on('change', function() {
        let captureCode = $(this).val();
        let bandSizeSelect = $('#id_band_size');
        let bandNumberInput = $('#id_band_number');
        let statusSelect = $('#id_status'); 

        if (captureCode === 'R') {
            bandSizeSelect.val('R').trigger('change')
            console.log('Capture code set to Recaptured. Band size locked to "R".');
        } else if (captureCode === 'U') {
            bandSizeSelect.val('U').trigger('change');
            bandNumberInput.val('');
            statusSelect.val('0').trigger('change'); // Set status to "0"
            console.log('Capture code set to Unbanded. Band size set to "U", band number cleared, and status set to "0".');
        }
    });
});
