// AJAX for Issue Tracker

// Show more issues
$(".btn-show-more").click(function() {
    // Get button name and table body to add issues
    var button    = $(this);
    var repoOwner = button.attr("data-owner");
    var repoSlug  = button.attr("data-slug");
    var repoCount = button.attr("data-count");
    var tableBody = $('#issues-' + repoOwner + '-' + repoSlug);
    var filterQueryStr = button.attr("dissue_urlissue_urlata-filter");
    button.attr("disabled", "disabled");

    var getData = {
            'repo-owner' : repoOwner,
            'repo-slug'  : repoSlug,
            'count' : repoCount
        };

    if (filterQueryStr != '') {
        var nvPairs = filterQueryStr.split('&');
        for (var i=0; i < nvPairs.length; i++) {
            var nameVal = nvPairs[i].split('=');
            if (nameVal.length == 2) {
                getData[nameVal[0]] = nameVal[1];
            }
        }
    }

    // Ajax request to get next set of issues
    $.ajax({
        type : 'GET',
        url  : '/fetch-more-issues',
        data : getData,

        success : function(data) {
            // Append rows of issues to table
            var moreIssues = $(data).hide();
            moreIssues.appendTo(tableBody).show(duration=800);

            // Increment repo count
            var newCount = parseInt(repoCount) + 10;
            button.attr('data-count', newCount);
            button.removeAttr('disabled');
        },

        error : function() {
            alert('Cannot fetch any more issues');
        }
    });
});


// Grab issue detail
$(".grab-issue").click(function() {
    // Grab the variables
    var get_link  = $(this);
    var issue_id  = get_link.attr("data-issue-id");
    var issue_uri = get_link.attr("data-issue-uri");
    // alert(issue_id + '\n' + issue_uri);

});