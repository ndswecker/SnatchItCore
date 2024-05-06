document.addEventListener('DOMContentLoaded', function () {
    var taxonSelect = document.getElementById('id_taxon');
    if (taxonSelect) {
        var choices = new Choices(taxonSelect, {
            searchEnabled: true,
            itemSelectText: '',
            removeItemButton: true,
            shouldSort: true
        });
    }
});
