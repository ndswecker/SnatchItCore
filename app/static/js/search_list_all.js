document.addEventListener('DOMContentLoaded', function() {
    const bandInput = document.getElementById('searchBandInput');
    const speciesInput = document.getElementById('searchSpeciesInput');
    const participantInput = document.getElementById('searchParticipantInput');
    const table = document.getElementById("recordsTable");
    const tr = table.getElementsByTagName("tr");

    function filterTable() {
        console.log('filtering table');
        const bandFilter = bandInput.value.toUpperCase();
        const speciesFilter = speciesInput.value.toUpperCase();
        const participantFilter = participantInput.value.toUpperCase();

        for (let i = 0; i < tr.length; i++) {
            const bandTd = tr[i].getElementsByClassName('band-number')[0];
            const speciesTd = tr[i].getElementsByClassName('species')[0];
            const participantTd = tr[i].getElementsByClassName('participant-initials')[0];
            if (bandTd && speciesTd && participantTd) {
                const bandText = bandTd.textContent || bandTd.innerText;
                const speciesText = speciesTd.textContent || speciesTd.innerText;
                const participantText = participantTd.textContent || participantTd.innerText;

                const displayBand = bandFilter === '' || bandText.toUpperCase().indexOf(bandFilter) > -1;
                const displaySpecies = speciesFilter === '' || speciesText.toUpperCase().indexOf(speciesFilter) > -1;
                const displayParticipant = participantFilter === '' || participantText.toUpperCase().indexOf(participantFilter) > -1;

                tr[i].style.display = displayBand && displaySpecies && displayParticipant ? "" : "none";
            }
        }
    }

    bandInput.addEventListener('keyup', filterTable);
    speciesInput.addEventListener('keyup', filterTable);
    participantInput.addEventListener('keyup', filterTable);
});
