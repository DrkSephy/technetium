// AJAX for Issue Tracker

// Show more issues
$(".btn-show-more").click(function() {
    // Get button name and table body to add issues
    var button    = $(this);
    var repoOwner = button.attr("data-owner");
    var repoSlug  = button.attr("data-slug");
    var repoCount = button.attr("data-count");
    var tableBody = $('#issues-' + repoOwner + '-' + repoSlug);
    var filterQueryStr = button.attr("data-filter");
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
    var getLink        = $(this);
    var repoOwner      = $(this).parents("tbody").attr("data-repo-owner");
    var repoSlug       = $(this).parents("tbody").attr("data-repo-slug");
    var issueId        = getLink.attr("data-issue-id");
    var issueType      = getLink.attr("data-issue-type");
    var issueTitle     = getLink.attr("data-issue-title");
    var issueContent   = getLink.attr("data-issue-content");
    var issueReporter  = getLink.attr("data-issue-reporter");
    var issueAssignee  = getLink.attr("data-issue-assignee");
    var bitbucketLink  = "https://bitbucket.org/"+repoOwner+"/"+repoSlug+"/issue/"+issueId;

    // Update modal information by pieces
    $("#issues-bitbucket-url").attr("href", bitbucketLink);
    $("#issues-modal-type").text(issueType);
    $("#issues-modal-title").text(issueTitle);
    $("#issues-modal-reporter").text(issueReporter);
    $("#issues-modal-assignee").text(issueAssignee);
    $("#issues-modal-content").text(issueContent);

});

