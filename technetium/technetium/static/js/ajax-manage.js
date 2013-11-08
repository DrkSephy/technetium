// Put AJAX Requests for Manage in this File

// AJAX Request to subscribe to repository
$(":button").click(function() {
    var buttonId  = this.id;
    var action    = this.value;
    var csrftoken = $.cookie('csrftoken');
    var repoName  = $("#name-" + buttonId).val();
    var repoOwner = $("#owner-" + buttonId).val();
    var repoSlug  = $("#slug-" + buttonId).val();

    $.ajax({
        type : 'POST',
        url  : '/subscribe/',
        data : {
            'csrfmiddlewaretoken' : csrftoken,
            'repo-name' : repoName,
            'repo-owner' : repoOwner,
            'repo-slug' : repoSlug,
            'action' : action
        },
        success : function () {
            alert("Subscribed to " + repoName); },
        error : function () {
            alert("Can't subscribed to " + repoName); },

    });

});
