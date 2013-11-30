// Put AJAX Requests for Manage in this File

// AJAX Request to subscribe to repository
$("button[name='subscribe']").click(function() {
    var button     = $(this);
    var buttonId   = this.id;
    var action     = this.value;
    var csrftoken  = $.cookie('csrftoken');
    var repoName   = $("#name-" + buttonId).val();
    var repoOwner  = $("#owner-" + buttonId).val();
    var repoSlug   = $("#slug-" + buttonId).val();
    var repoId     = $("#id-" + buttonId).val();
    var subCount   = $("#subscription-count");
    var sidebarSub = $("#sidebar-repos");

    // Send Ajax request to server
    $.ajax({
        type : 'POST',
        url  : '/' + action + '/',
        data : {
            'csrfmiddlewaretoken' : csrftoken,
            'repo-name' : repoName,
            'repo-owner' : repoOwner,
            'repo-slug' : repoSlug,
            'repo-id' : repoId,
            'action' : action
        },

        // Sucess: change button value to unsubscribe
        success : function () {
            if (action == 'subscribe') {
                $('#subscribed-' + buttonId).html('Yes');
                button.attr('value', 'unsubscribe');
                button.html('Unsubscribe');

                // Add new subscription to sidebar
                var newSubscription = '<li id="sidebar-'+repoOwner+'-'+
                repoSlug + '"><a href="/reports/'+repoOwner+'/'+repoSlug+'">'+
                repoName + '</a></li>';
                sidebarSub.append(newSubscription);

                // Add subscription to navbar
                var newCount = parseInt(subCount.text())+1;
                subCount.text(newCount);
            }

            else if (action == 'unsubscribe') {
                $('#subscribed-' + buttonId).html('No');
                button.attr('value', 'subscribe');
                button.html('Subscribe');

                // Remove old subcription from sidebar
                var subscriptionID = '#sidebar-'+repoOwner+'-'+repoSlug;
                var removeSubscription = $(subscriptionID);
                removeSubscription.remove();

                // Remove subscription from navbar
                var newCount = parseInt(subCount.text())-1;
                subCount.text(newCount);
            }
        },

        // Fail: show alert of failure
        error : function () {
            alert("Can't subscribed to " + repoName);
        },

    });

});