$(document).ready(function() {
    $('#id_capture_code').on('change', function() {
        console.log('Capture code changed');
        var captureCode = $(this).val();
        var bandSizeSelect = $('#id_band_size'); // Assuming the ID for the band size select field is 'id_band_size'

        if (captureCode === 'R') {
            // Set the band size select field to "R" and trigger change event for Select2 to update
            bandSizeSelect.val('R').trigger('change');
            
            // Optionally, if you want to make the band size field readonly/disabled when "R" is selected
            // You might need to also handle re-enabling it if a different capture code is selected
            bandSizeSelect.prop('disabled', true);
        } else {
            // Re-enable the band size field if another capture code is selected
            bandSizeSelect.prop('disabled', false);
        }
    });
});

