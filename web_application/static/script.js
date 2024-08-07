$(document).ready(function() {
    // Add an event listener to the form submission
    $('#predictionForm').on('submit', function(event){
        // Prevent the default form submission behavior
        event.preventDefault();
        
        // Show the prediction modal
        //$('#resultModal').modal('show');
        //var frm = document.getElementById('predictionForm')
        //frm.reset()

        $.ajax({
            url: '/predict',
            type: 'POST',
            data: $('#predictionForm').serialize(),
            // Selects the message to be displayed based on the response from the server
            success: function(response) {
                $('#prediction-text').text( response.prediction)
                $('#resultModal').modal('show');
            }
        });

        var frm = document.getElementById('predictionForm')
        frm.reset()
    });
});