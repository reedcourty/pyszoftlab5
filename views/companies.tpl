%# Betöltjük a fejlécet:
%include header page_title=page_title, css_files=css_files, js_files=js_files
<div id="main">
    <article>
        <h1>Cégek</h1>
        
        <div id="kereso">
            <form id="kereso_form" method="post">
                <table id="search_form_table">
                    <tr>
                        <td><label for="nev">Név:</label></td>
                        <td><input id="nev" name="nev" type="search" /></td>
                        <td><label for="bankszamla">Bankszámla:</label></td>
                        <td><input id="bankszamla" name="bankszamla" type="search" /></td>
                        <td><label for="kapcsolattarto">Kapcsolattartó:</label></td>
                        <td><input id="kapcsolattarto" name="kapcsolattarto" type="search" /></td>   
                    </tr>
                    <tr>
                        <td><input id="operator_and" name="operator" type="radio" value="AND" checked="checked" /></td>
                        <td colspan="5" style="text-align: left;"><label for="operator_and">A megadott feltételek mind illeszkedjenek</label></td>
                    </tr>
                    <tr>
                        <td><input id="operator_or" name="operator" type="radio" value="OR" /></td>
                        <td colspan="3" style="text-align: left;"><label for="operator_or">A megadott feltételek bármelyike illeszkedjen</label></td>
                        <td colspan="2"><input type="submit" value="Keresés" /></td>
                    </tr>
                </table>
            </form>
            %#{if $Query}<p>A keresési paraméterekből száramazó SQL lekérdezés: <br />{$Query}</p>{/if}
        </div>
        
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
                                <td><a href="/company-details/{{company['id']}}">{{company['nev']}}</a></td>
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