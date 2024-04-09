document.addEventListener('DOMContentLoaded', function() {
    // Calculate current time rounded down to the nearest 10 minutes
    const now = new Date();
    now.setMinutes(Math.floor(now.getMinutes() / 10) * 10);
    now.setSeconds(0);

    flatpickr(".timepicker", {
        enableTime: true,
        noCalendar: true,
        dateFormat: "H:i",
        minuteIncrement: 10,
        defaultDate: now,
        onClose: function(selectedDates, dateStr, instance) {
            console.log("Called onClose")
            const timeContainer = document.getElementById('time-info-container');
            const inputTime = timeContainer.getAttribute('data-input-time');
            console.log(inputTime); 
            
            if (selectedDates.length > 0) {
                // Get the selected date
                let selectedDate = selectedDates[0];

                // Adjust minutes to the nearest 10-minute increment
                selectedDate.setMinutes(Math.round(selectedDate.getMinutes() / 10) * 10);

                // Update the flatpickr instance with the adjusted time
                instance.setDate(selectedDate, true); // The 'true' parameter triggers the onChange event
            }
        }
    });
});
