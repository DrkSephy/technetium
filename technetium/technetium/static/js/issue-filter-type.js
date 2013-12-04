// AJAX for Filter Type

$(".filter-type").click(function() {

    var buttonName = $(this).text();
    var parentName = $(this).parent();
    var filterType = $(this).attr("data-filter-type");
    var repoSlug   = parentName.attr("data-filter-repo");
    var repoOwner  = parentName.attr("data-filter-owner");

   // Ajax request to grab filtered issues
    $.ajax({
        type : 'GET',
        url  : '/filter-issues-type',
        data : {
            'repo-owner'  : repoOwner,
            'repo-slug'   : repoSlug,
            'filter-type' : filterType
        },

        success : function(data) {
            // Append rows of issues to table
            alert('Successfully filtered issues');
        },

        error : function() {
            alert('Cannot filter issues by type');
        }
    });

});