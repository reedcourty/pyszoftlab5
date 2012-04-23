%# Betöltjük a fejlécet:
%include header page_title=page_title, css_files=css_files, js_files=js_files
<div id="main">
    <article>
        <h1>Cég részletei</h1>
        %if len(errors) > 0:
            %for error in errors:
                <div class="error">
                    <p>{{error}}</p>
                </div>
            %end
        %else:
            %# Ha kaptunk a cégről infót, akkor megjelenítünk egy táblázatot:
            %if len(company) > 0:
                <table id="result_table">
                    <thead> 
                        <tr>
                            <th>Azonosító</th>
                            <th>Név</th>
                            <th>Bankszámla</th>
                            <th>Kapcsolattartó</th>                           
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>{{company['id']}}</td>
                            <td>{{company['nev']}}</td>
                            <td>{{company['bankszamla']}}</td>
                            %if company['kapcsolattarto'] != None:
                                <td>{{company['kapcsolattarto']}}</td>
                            %else:
                                <td>nincs megadva</td>
                            %end
                        </tr>
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