// AJAX for Filter Type

$(".filter-type").click(function() {

    var buttonName  = $(this).text();
    var parentName  = $(this).parent();
    var filterType  = $(this).attr("data-filter-type");
    var filterRepo  = parentName.attr("data-filter-repo");
    var filterOwner = parentName.attr("data-filter-owner");

    alert("You clicked on " + filterOwner);

});