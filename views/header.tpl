<!DOCTYPE html>
<html>
    <head>
        <title>{{page_title}}</title>
        %for element in css_files:
            <link rel="stylesheet" type="text/css" href="{{element}}" />
        %end
    </head>
    <body>
        <div id="menu">
        </div>