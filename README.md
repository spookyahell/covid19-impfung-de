# Coronavirus-Impfdaten aus Deutschland (covid19-impfung-de)
### Impfdaten werden (bereits länger) nicht mehr eingespeist
Siehe [Issue #3](https://github.com/spookyahell/covid19-impfung-de/issues/3#issuecomment-1413422311)

### Zahlen zu Impfstofflieferungen & verimpften Dosen
Impfdaten, wie sie auf https://impfdashboard.de/daten verfügbar sind, und verwandelt in das erheblich bessere JSON-Datenformat (seit 18. Januar 2022)

Leider hat das Projekt letztes mal nicht so wie geplant funktioniert. Hoffentlich ist es beim zweiten Anlauf besser.

Aktuell erfolgt eine Einsendung der Daten noch ausschließlich manuell/händisch, das soll sich aber auch weiterhin zukünftig ändern.

Weil die Einsendung aber gegenwärtig noch manuell erfolgt, kann leider nicht garantiert werden, dass die Einsendung stets zum Zeitpunkt der Verfügbarkeit oder in einem ununterbrochenem Rhythmus passiert).

_Fall Sie es immer noch nicht wissen (dann wird es langsam aber mal Zeit)..._ "Comirnaty" ist der Name des BioNTech/Pfizzer-Impfstoffs.

## Die Daten (JSON)
[Zeitreihe der bundesweiten Impfungen](json/germany_vaccinations_timeseries_v2.json)

‼️ Diese Daten sind sehr umfangreich, im Gegensatz zu den Originaldaten, da die Überschriften für die jeweiligen Daten (gemäß JSON-Format) je Datensatz erwähnt werden müssen.
Daher habe ich beschlossen, diese Daten ab sofort zusätzlich in nach Monate aufgeteilten Dateien anzubieten.

**Folgende Monate lassen sich einzeln betrachten:**<br>
**2020:** [2020-12 (Dezember)](json/germany_vaccinations_timeseries_v2_monthly/germany_vaccinations_timeseries_v2-2020-12.json)

**2021**<br>
[2021-01 (Januar)](json/germany_vaccinations_timeseries_v2_monthly/germany_vaccinations_timeseries_v2-2021-01.json)<br>
[2021-02 (Februar)](json/germany_vaccinations_timeseries_v2_monthly/germany_vaccinations_timeseries_v2-2021-02.json)<br>
[2021-03 (März)](json/germany_vaccinations_timeseries_v2_monthly/germany_vaccinations_timeseries_v2-2021-03.json)<br>
[2021-04 (April)](json/germany_vaccinations_timeseries_v2_monthly/germany_vaccinations_timeseries_v2-2021-04.json)<br>
[2021-05 (Mai)](json/germany_vaccinations_timeseries_v2_monthly/germany_vaccinations_timeseries_v2-2021-05.json)<br>
[2021-06 (Juni)](json/germany_vaccinations_timeseries_v2_monthly/germany_vaccinations_timeseries_v2-2021-06.json)<br>
[2021-07 (Juli)](json/germany_vaccinations_timeseries_v2_monthly/germany_vaccinations_timeseries_v2-2021-07.json)<br>
[2021-08 (August)](json/germany_vaccinations_timeseries_v2_monthly/germany_vaccinations_timeseries_v2-2021-08.json)<br>
[2021-09 (September)](json/germany_vaccinations_timeseries_v2_monthly/germany_vaccinations_timeseries_v2-2021-09.json)<br>
[2021-10 (Oktober)](json/germany_vaccinations_timeseries_v2_monthly/germany_vaccinations_timeseries_v2-2021-10.json)<br>
[2021-11 (November)](json/germany_vaccinations_timeseries_v2_monthly/germany_vaccinations_timeseries_v2-2021-11.json)<br>
[2021-12 (Dezember)](json/germany_vaccinations_timeseries_v2_monthly/germany_vaccinations_timeseries_v2-2021-12.json)<br>

**2022**<br>
[2022-01 (Januar)](json/germany_vaccinations_timeseries_v2_monthly/germany_vaccinations_timeseries_v2-2022-01.json)<br>
[2022-02 (Februar)](json/germany_vaccinations_timeseries_v2_monthly/germany_vaccinations_timeseries_v2-2022-02.json)<br>
[2022-03 (März)](json/germany_vaccinations_timeseries_v2_monthly/germany_vaccinations_timeseries_v2-2022-03.json)
<hr/>

[Zeitreihe der Impfstofflieferungen](json/germany_deliveries_timeseries_v2.json) (gesondert optimiert)

[Impf-Fortschritt nach Bundesland](json/germany_vaccinations_by_state.json) 

Eine Besichtigung von JSON-Daten (ganz allgemein) funktioniert übrigens besonders gut, mit diesem Online-Viewer: http://jsonviewer.stack.hu/

## Originaldaten (TSV)
[Zeitreihe der bundesweiten Impfungen](tsv/germany_vaccinations_timeseries_v2.tsv)

[Zeitreihe der Impfstofflieferungen](tsv/germany_deliveries_timeseries_v2.tsv)

[Impf-Fortschritt nach Bundesland](tsv/germany_vaccinations_by_state.tsv)<br> <br>

## Datenquelle
https://impfdashboard.de/daten

### spezifisch
[Zeitreihe der bundesweiten Impfungen](https://impfdashboard.de/static/data/germany_vaccinations_timeseries_v2.tsv)

[Zeitreihe der Impfstofflieferungen](https://impfdashboard.de/static/data/germany_deliveries_timeseries_v2.tsv)

[Impf-Fortschritt nach Bundesland](https://impfdashboard.de/static/data/germany_vaccinations_by_state.tsv)

Der Datenstand der aktuellen, offiziellen Daten kann [hier (im JSON-Format)](https://impfdashboard.de/static/data/metadata.json) abgefragt werden.
