// function updateFormattedDisplay() {
//     var input = document.getElementById('id_band_number').value.replace(/\D/g, ''); // Remove non-digit characters
//     var formatted = '';

//     // Pad or slice the input to exactly 9 characters, filling missing with '#'
//     input = input.padEnd(9, '_').slice(0, 9);

//     // Extract parts with the exact format
//     var part1 = input.slice(0, 4); // First 4 digits
//     var part2 = input.slice(4, 9); // Last 5 digits

//     // Build the formatted string, keeping '#' where digits are missing
//     formatted = `${part1}-${part2}`;

//     // Update the formatted band number display
//     document.getElementById('formatted-band-number').textContent = formatted;
// }

// // Event listener for input changes
// document.getElementById('id_band_number').addEventListener('input', updateFormattedDisplay);

// // Initial call on page load
// document.addEventListener('DOMContentLoaded', updateFormattedDisplay);

// function clearPlaceholderValue() {
//     console.log("ATTEMPTING TO CLEAR BAND NUMBER")
//     var bandNumberField = document.getElementById('id_band_number');
//     if (bandNumberField.value === '____-_____') {
//         bandNumberField.value = '';
//     }
// }

// // Event listener for form submission
// document.querySelector('form').addEventListener('submit', clearPlaceholderValue);

$(document).ready(function() {
    function updateFormattedDisplay() {
        var input = $('#id_band_number').val().replace(/\D/g, ''); // Remove non-digit characters
        var formatted = '';

        // Pad or slice the input to exactly 9 characters, filling missing with '_'
        input = input.padEnd(9, '_').slice(0, 9);

        // Extract parts with the exact format
        var part1 = input.slice(0, 4); // First 4 digits
        var part2 = input.slice(4, 9); // Last 5 digits

        // Build the formatted string, keeping '_' where digits are missing
        formatted = `${part1}-${part2}`;

        // Update the formatted band number display
        $('#formatted-band-number').text(formatted);
    }

    $('#id_band_number').on('input', updateFormattedDisplay);
    $(document).on('DOMContentLoaded', updateFormattedDisplay);

    $('#id_capture_code').on('change', function() {
        let captureCode = $(this).val();
        let bandSizeSelect = $('#id_band_size');
        let bandNumberInput = $('#id_band_number');
        let statusSelect = $('#id_status');

        if (captureCode === 'R') {
            bandSizeSelect.val('R').trigger('change');
            bandNumberInput.prop('disabled', false);
            console.log('Capture code set to Recaptured. Band size locked to "R".');
        } else if (captureCode === 'U') {
            bandSizeSelect.val('U').trigger('change');
            bandNumberInput.val('').prop('disabled', true); // Clear and disable band number input
            statusSelect.val('0').trigger('change'); // Set status to "0"
            console.log('Capture code set to Unbanded. Band size set to "U", band number cleared, and status set to "0".');
            $('#formatted-band-number').text('____-_____'); // Reset formatted display
        } else {
            bandNumberInput.prop('disabled', false); // Enable band number input for other capture codes
        }
    });

    // Ensure the formatted display is updated on form submission to reflect any changes
    $('form').on('submit', function() {
        updateFormattedDisplay();
    });

    // Initial call on page load
    updateFormattedDisplay();
});
