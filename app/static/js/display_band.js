function updateFormattedDisplay() {
    var input = document.getElementById('id_band_number').value.replace(/\D/g, ''); // Remove non-digit characters
    var formatted = '';

    // Pad or slice the input to exactly 9 characters, filling missing with '#'
    input = input.padEnd(9, '_').slice(0, 9);

    // Extract parts with the exact format
    var part1 = input.slice(0, 4); // First 4 digits
    var part2 = input.slice(4, 9); // Last 5 digits

    // Build the formatted string, keeping '#' where digits are missing
    formatted = `${part1}-${part2}`;

    // Update the formatted band number display
    document.getElementById('formatted-band-number').textContent = formatted;
}

// Event listener for input changes
document.getElementById('id_band_number').addEventListener('input', updateFormattedDisplay);

// Initial call on page load
document.addEventListener('DOMContentLoaded', updateFormattedDisplay);
