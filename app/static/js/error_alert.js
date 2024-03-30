document.addEventListener('DOMContentLoaded', function() {
    // Attach click event listener to all elements with class 'alert-link'
    document.querySelectorAll('.alert-link').forEach(function(element) {
        element.addEventListener('click', function(e) {
            e.preventDefault(); // Prevent the default anchor click behavior

            // Get the href attribute of the clicked link, which contains the ID of the target element
            var targetId = this.getAttribute('href');

            // Ensure the target ID exists before attempting to scroll
            if (targetId && document.querySelector(targetId)) {
                // Smooth scroll to the target element
                document.querySelector(targetId).scrollIntoView({
                    behavior: 'smooth',
                    block: 'center' // Scroll the target element to the center of the viewport
                });
            }
        });
    });
});
