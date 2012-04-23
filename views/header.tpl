<!DOCTYPE html>
<html>
    <head>
        <title>{{page_title}}</title>
        %# Betöltjük a CSS leírókat:
        %for element in css_files:
            <link rel="stylesheet" type="text/css" href="{{element}}" />
        %end
        %# Betöltjük a scripteket:
        %for element in js_files:
            <script type="text/javascript" src="{{element}}"></script>
        %end
    </head>
    <body>
        <div id="frame">
            <div id="menu">
                <p>
                    <a href="/">Kezdő oldal</a>
                    <a href="/companies">Cégek</a>
                    <a href="/company-details">Cég részletezése</a>
                </p>
            </div>