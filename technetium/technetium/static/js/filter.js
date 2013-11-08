// Filters getIssues

function getIssues() {

  var url = '/issues';
  var type = document.getElementById("Type");
  var priority = document.getElementById("Priority");
  var status = document.getElementById("Status");
  var created = document.getElementById("Created");
  var assignee = document.getElementById("Assignee");

  if (type != null || priority != null || status != null || created != null || assignee != null){
    url += '?';
    if (type != null && type.value.trim() != ""){
      url += "Type="+type.value.trim();
    }
    if (priority != null && priority.value.trim() != ""){
      if (url.endsWith("?"))
        url += "Priority="+priority.value.trim();
      else
        url += "&Priority="+priority.value.trim();
    }
    if (status != null && status.value.trim() != ""){
      if (url.endsWith("?"))
        url += "Status="+status.value.trim();
      else
        url += "&Status="+status.value.trim();
    }
    if (created != null && created.value.trim() != ""){
      if (url.endsWith("?"))
        url += "Created="+created.value.trim();
      else
        url += "&Created="+created.value.trim();
    }
    if (assignee != null && assignee.value.trim() != ""){
      if (url.endsWith("?"))
        url += "Assignee="+assignee.value.trim();
      else
        url += "&Assignee="+assignee.value.trim();              
    }
}

  top.location = url;
}