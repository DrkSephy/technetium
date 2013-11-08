// Put AJAX Requests for Manage in this File

// AJAX Request to subscribe to repository
$(":button").click(function() {
    var button_id = this.id;
    var fields = $("#"+button_id+":input")
    alert(fields)
    // alert("Subscribing to " + button_id);
})
