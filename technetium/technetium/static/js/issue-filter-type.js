// AJAX for Filter Type

$(".filter-type").click(function() {

    var buttonName = $(this).text();
    var parentName = $(this).parent();
    var filterType = $(this).attr("data-filter-type");
    var repoSlug   = parentName.attr("data-filter-repo");
    var repoOwner  = parentName.attr("data-filter-owner");
    var tableBody  = $("#issues-"+repoOwner+"-"+repoSlug);

    var getData = {
            'repo-owner'  : repoOwner,
            'repo-slug'   : repoSlug
        };
        
    if (filterType != '' && filterType != 'all'){
        getData['filter-type'] = filterType;
    }

   // Ajax request to grab filtered issues
    $.ajax({
        type : 'GET',
        url  : '/filter-issues-type',
        data : getData,

        success : function(data) {
            // Empty old issues and show new filter issues
            tableBody.empty();
            tableBody.html(data).hide();
            tableBody.show(800);
        },

        error : function() {
            alert('Cannot filter issues by type');
        }
    });

});