// AJAX for Filter Type

$(".filter-type").click(function() {

    var buttonName = $(this).text();
    var parentName = $(this).parent();
    var filterType = $(this).attr("data-filter-type");
    var repoSlug   = parentName.attr("data-filter-repo");
    var repoOwner  = parentName.attr("data-filter-owner");
    var tableBody  = $("#issues-"+repoOwner+"-"+repoSlug);

    var showMoreButton = $("#show-more-"+repoOwner+"-"+repoSlug);
    var filterQueryStr = showMoreButton.attr("data-filter");
    var count = showMoreButton.attr("data-count");

    var getData = {
            'repo-owner'  : repoOwner,
            'repo-slug'   : repoSlug,
            'count' : count
        };

    // add any existing filtering options        
    if (filterQueryStr != '') {
        var nvPairs = filterQueryStr.split('&');
        for (var i=0; i < nvPairs.length; i++) {
            var nameVal = nvPairs[i].split('=');
            if (nameVal.length == 2) {
                getData[nameVal[0]] = nameVal[1];
            }
        }
    }

    // handle filter with all options
    if (filterType != '' && filterType != 'all'){
        getData['filter-type'] = filterType;
    } else
    if ('filter-type' in getData) {
        delete getData['filter-type'];
    }

    // compose updated query string
    var updatedFilterQueryStr = '';
    for (var k in getData) {
        var v = getData[k];
        if (k == 'filter-type' || k == 'filter-status') {
            updatedFilterQueryStr = updatedFilterQueryStr + '&' + k +'=' + v;
        }
    }
    //strip off leading '&'
    if (updatedFilterQueryStr != '' && updatedFilterQueryStr.substring(0,1) == "&") {
       updatedFilterQueryStr = updatedFilterQueryStr.substring(1, updatedFilterQueryStr.length);
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

            showMoreButton.attr("data-filter", updatedFilterQueryStr);
        },

        error : function() {
            alert('Cannot filter issues by type');
        }
    });

});