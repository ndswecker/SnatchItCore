document.addEventListener('DOMContentLoaded', function() {
    const timeInfoContainer = document.getElementById('time-info-container');
    const existingDateTime = timeInfoContainer ? timeInfoContainer.getAttribute('data-datetime') : null;

    if (existingDateTime) {
        // Assuming existingDateTime is in the format "YYYY-MM-DD HH:MM"
        const parts = existingDateTime.split(' ');
        const prevDate = parts[0]; // Extract the date part "YYYY-MM-DD"
        const prevTime = parts[1]; // Extract the time part "HH:MM"

        // Set the date input to the previous date
        const dateInput = document.getElementById('id_capture_year_day');
        if (dateInput) {
            dateInput.value = prevDate;
        }

        // Initialize flatpickr for the time picker
        flatpickr(".timepicker", {
            enableTime: true,
            noCalendar: true,
            dateFormat: "H:i",
            minuteIncrement: 10,
            defaultDate: prevTime,
            onClose: function(selectedDates, dateStr, instance) {
                if (selectedDates.length > 0) {
                    let selectedDate = selectedDates[0];
                    selectedDate.setMinutes(Math.round(selectedDate.getMinutes() / 10) * 10);
                    instance.setDate(selectedDate, true);
                }
            }
        });
    }
});
