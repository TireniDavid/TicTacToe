var symbol_pc;
document.addEventListener('DOMContentLoaded', function () {
    console.log("Dom is loaded")
    const urlParams = new URLSearchParams(window.location.search);
    const symbol = urlParams.get('symbol');

    const symbols = ['x', 'o'];
    const index = symbols.indexOf(symbol);
    symbols.splice(index, 1);

    symbol_pc = symbols.pop()
    if (symbol === 'x' || symbol === 'o') {
        clicked_cell(symbol);
    }
})


/////// CLICKED CELL FUNCTION
function clicked_cell(symbol) {
    let cells = document.querySelectorAll('.cell');
        cells.forEach(function (cell) {
            cell.addEventListener('click', function (event) {

                console.log("Clicked");

                clickedCell = event.target;

                const cellId = clickedCell.id;
                const cell_pos = (cellId[4]-1);

                // send info to flask
                const xhr_send = new XMLHttpRequest();
                const url_send_to = '/update_user_move';

                console.log(cellId);
                console.log(cell_pos);

                const send_data = JSON.stringify({
                    cellName: cellId,
                    position: cell_pos
                });
                xhr_send.open('POST', url_send_to, true);
                xhr_send.setRequestHeader('Content-Type', 'application/json');
                xhr_send.send(send_data);

                cell.classList.add(symbol)


                // receive Response info from flask
                const xhr_receive = new XMLHttpRequest();
                const url_receive_from = '/send_computer_move';
                xhr_receive.onreadystatechange = function () {
                    if (xhr_receive.readyState === XMLHttpRequest.DONE) {
                        if (xhr_receive.status === 200) {
                            // Parse the response text as JSON
                            const response_data = JSON.parse(xhr_receive.responseText);
                            console.log('Received data from Flask:', response_data);
                            // Handle the response data accordingly

                            // extract data using object's key
                            const pos_no = response_data.computerPositionChoice;
                            // manipulate data
                            const str_cell_id = "cell" + (pos_no + 1);
                            let cell_id = document.getElementById(str_cell_id);
                            setTimeout(function(){cell_id.classList.add(symbol_pc)}
                            ,1000)

                        }
                    }
                }
                xhr_receive.open('GET', url_receive_from, true);
                xhr_receive.send();

            });
        });
}