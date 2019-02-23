var page = require('webpage').create();
var name = require("system").args[1];
var html_file = name+".html";
var pdf_file  = name+".pdf";

page.open(html_file, setInterval(function() {
    page.render(pdf_file);
    phantom.exit(0);
},30000));
