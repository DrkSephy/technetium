// Put AJAX Requests for Manage in this File

// AJAX Request to subscribe to repository
$(":button").click(function() {
    var buttonId  = this.id;
    var repoName  = $("#name-" + buttonId).val();
    var repoOwner = $("#owner-" + buttonId).val();
    var repoSlug  = $("#slug-" + buttonId).val();
    alert("Subscribing to " + repoName);
})
