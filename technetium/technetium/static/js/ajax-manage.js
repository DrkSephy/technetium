// Put AJAX Requests for Manage in this File

BASEURL = 'http://127.0.0.1:8008'

// AJAX Request to subscribe to repository
$(":button").click(function() {
    var buttonId  = this.id;
    var action    = this.value;
    var repoName  = $("#name-" + buttonId).val();
    var repoOwner = $("#owner-" + buttonId).val();
    var repoSlug  = $("#slug-" + buttonId).val();

    $.ajax({
        type : 'POST',
        url  : BASEURL + '/subscribe/',
        data : {
            'repo-name' : repoName,
            'repo-owner' : repoOwner,
            'repo-slug' : repoSlug,
            'action' : action
        },
        success : function () {
            alert("Subscribed to " + this.repoName); },
        error : function () {
            alert("Can't subscribed to " + this.repoName); },

    });

});
