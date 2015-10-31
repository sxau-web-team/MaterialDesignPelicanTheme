(function($){
  $(function(){

    $('.button-collapse').sideNav();

  }); // end of document ready
})(jQuery); // end of jQuery name space
$('.button-collapse').sideNav({menuWidth: 240, activationWidth: 70});
function dispatch() {
    var q = document.getElementById("search-field");
    if (q.value != "") {
        var url = 'http://www.google.com/search?q=site:dbqf.xyz%20' + q.value;
        if (navigator.userAgent.indexOf('iPad') > -1 || navigator.userAgent.indexOf('iPhone') > -1 || navigator.userAgent.indexOf('iPhone') > -1) {
            location.href = url;
        } else {
            window.open(url, "_blank");
        }
        return false;
    } else {
        return false;
    }
}