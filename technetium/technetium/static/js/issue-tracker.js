// AJAX for Issue Tracker

// Show more issues
$(".btn-show-more").click(function() {
    // Get button name and table body to add issues
    var button    = $(this);
    var repoOwner = button.attr("data-owner");
    var repoSlug  = button.attr("data-slug");
    var repoCount = button.attr("data-count");
    var tableBody = $('#issues-' + repoOwner + '-' + repoSlug);
    button.attr("disabled", "disabled");

    // Ajax request to get next set of issues
    $.ajax({
        type : 'GET',
        url  : '/fetch-more-issues',
        data : {
            'repo-owner' : repoOwner,
            'repo-slug'  : repoSlug,
            'count' : repoCount
        },

        success : function(data) {
            // Append rows of issues to table
            tableBody.append(data);

            // Increment repo count
            var newCount = parseInt(repoCount) + 10;
            $(this).attr('data-count', toString(newCount));
            button.removeAttr('disabled');
        },

        error : function() {
            alert('Error trying to fetch more issues');
        }
    });
});