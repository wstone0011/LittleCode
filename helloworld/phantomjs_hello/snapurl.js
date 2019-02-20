args = require('system').args;
url = args[1];
png = args[2];

page = new WebPage();
page.settings.userAgent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36";

page.open(url, function (status) {
    page.render(png);
    phantom.exit();
});