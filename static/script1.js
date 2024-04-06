document.addEventListener('DOMContentLoaded', function() {
    console.log("Dom is loaded")
    let cells = document.querySelectorAll('.cell');
    cells.forEach(function(cell) {
        cell.addEventListener('click', function(){
            console.log("Clicked");
        });
    });
});
