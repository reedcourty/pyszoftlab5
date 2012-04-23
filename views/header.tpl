<!DOCTYPE html>
<html>
    <head>
        <title>{{page_title}}</title>
        %for element in css_files:
            <link rel="stylesheet" type="text/css" href="{{element}}" />
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