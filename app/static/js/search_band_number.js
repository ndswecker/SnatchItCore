function searchByBandNumber() {
    // Get the search input value
    var input = document.getElementById("searchInput");
    var filter = input.value.toUpperCase();
    var table = document.getElementById("recordsTable");
    var tr = table.getElementsByTagName("tr");

    // Loop through all table rows, and hide those that don't match the search query
    for (var i = 0; i < tr.length; i++) {
        var td = tr[i].getElementsByClassName("band-number")[0];
        if (td) {
            var txtValue = td.textContent || td.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }       
    }
}
