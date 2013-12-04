// AJAX for Filter Status

$(".filter-status").click(function() {

    var buttonName = $(this).text();
    var parentName = $(this).parent();
    var filterStatus = $(this).attr("data-filter-status");
    var repoSlug   = parentName.attr("data-filter-repo");
    var repoOwner  = parentName.attr("data-filter-owner");
    var tableBody  = $("#issues-"+repoOwner+"-"+repoSlug);

    var getData = {
            'repo-owner'  : repoOwner,
            'repo-slug'   : repoSlug
        };
        
    if (filterStatus != '' && filterStatus != 'all'){
    	getData['filter-status'] = filterStatus;
    }

   // Ajax request to grab filtered issues
    $.ajax({
        type : 'GET',
        url  : '/filter-issues-status',
        data : getData,

        success : function(data) {
            // Empty old issues and show new filter issues
            tableBody.empty();
            tableBody.html(data).hide();
            tableBody.show(800);
        },

        error : function() {
            alert('Cannot filter issues by Status');
        }
    });

});