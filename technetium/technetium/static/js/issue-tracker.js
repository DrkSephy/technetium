// AJAX for Issue Tracker

// Show more issues
$(".btn-show-more").click(function() {
    // Get button name and table body to add issues
    var button     = $(this);
    var buttonName = this.name;
    var tableBody  = 'issues-' + buttonName;

    // Ajax request to get next set of issues
    alert(tableBody);
});