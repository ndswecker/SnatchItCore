document.addEventListener('DOMContentLoaded', function() {
    var specialDatesElement = document.getElementById('specialDates');
    if (specialDatesElement) {
        var specialDates = JSON.parse(specialDatesElement.textContent);
        flatpickr("#id_date_range", {
            mode: "range",
            dateFormat: "Y-m-d",
            onDayCreate: function(dObj, dStr, fp, dayElem) {
                var dateStr = dayElem.dateObj.toISOString().slice(0, 10);
                if (specialDates.includes(dateStr)) {
                    dayElem.style.backgroundColor = '#ffc0cb';
                    dayElem.title = "Data available";
                }
            }
        });
    }

    window.clearDates = function() {
        var flatpickrInstance = flatpickr("#id_date_range");
        flatpickrInstance.clear();
        document.getElementById("date-form").submit();
    }
});
