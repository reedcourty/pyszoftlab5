%# Betöltjük a fejlécet:
%include header page_title=page_title, css_files=css_files, js_files=js_files
<div id="main">
    <article>
        <h1>Cégek</h1>
        %if len(errors) > 0:
            %for error in errors:
                <div class="error">
                    <p>{{error}}</p>
                </div>
            %end
        %else:
            %# Ha kaptunk a cégekről listát, akkor megjelenítünk egy táblázatot:
            %if len(companies) > 0:
                <table id="result_table">
                    <thead> 
                        <tr>
                            <th>Név</th>
                            <th>Kapcsolattartó</th>
                        </tr>
                    </thead>
                    <tbody>
                    
                        %for company in companies:
                            <tr>
                                <td>{{company['nev']}}</a></td>
                                <td>{{company['kapcsolattarto']}}</td>
                            </tr>
                        %end
                    </tbody>
                </table>
            %else:
                <p>Nincs megjeleníthető cég az adatbázisban.</p>
            %end
        %end
    </article>
</div>
%# Betöltjük a láblécet
%include footer now=now