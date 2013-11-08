// Filters getIssues

function getIssues() {

  var url = '/issues';
  var type = document.getElementById("Type");
  var priority = document.getElementById("Priority");
  var status = document.getElementById("Status");
  var created = document.getElementById("Created");

  if (type != null || priority != null || status != null || created != null){
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
}

  top.location = url;
}