/*Navigation function */
function openNav() {
  document.getElementById("mySidenav").style.width = "260px";
  document.getElementById("main").style.marginLeft = "260px";
}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
  document.getElementById("main").style.marginLeft = "0";
}
/*  for loading content dynamically in section */
$(document).ready(function() {
  $("#content1").load("index.html");
});

$("#nav a").click(function() {
  var page = $(this).attr("href");
  $("#content1").load(page);
  /*used to avoid event  bubbling */
  return false;
});
