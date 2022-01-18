# Coronavius-Impfdaten aus Deutschland (covid19-impfung-de)
Impfdaten, wie sie auf https://impfdashboard.de/daten verfügbar sind, und verwandelt in das erheblich bessere JSON-Datenformat (seit 18. Januar 2022)

Leider hat das Projekt letztes mal nicht so wie geplant funktioniert. Hoffentlich ist es beim zweiten Anlauf besser.

Aktuell erfolgt eine Einsendung der Daten noch ausschließlich manuell/händisch, das soll sich aber auch weiterhin zukünftig ändern.

Weil die Einsendung aber gegenwärtig noch manuell erfolgt, kann leider nicht garantiert werden, dass die Einsendung stets zum Zeitpunkt der Verfügbarkeit oder in einem ununterbrochenem Rhythmus passiert).

_Fall Sie es immer noch nicht wissen (dann wird es langsam aber mal Zeit)..._ "Comirnaty" ist der Name des BioNTech/Pfizzer-Impfstoffs.

## Die Daten (JSON)
[Zeitreihe der bundesweiten Impfungen](json/germany_vaccinations_timeseries_v2.json)

[Zeitreihe der Impfstofflieferungen](json/germany_deliveries_timeseries_v2.json) (gesondert optimiert)

[Impf-Fortschritt nach Bundesland](json/germany_vaccinations_by_state.json) 

Eine Besichtigung von JSON-Daten (ganz allgemein) funktioniert übrigens besonders gut, mit diesem Online-Viewer: http://jsonviewer.stack.hu/

## Originaldaten (TSV)
[Zeitreihe der bundesweiten Impfungen](tsv/germany_vaccinations_timeseries_v2.tsv)

[Zeitreihe der Impfstofflieferungen](tsv/germany_deliveries_timeseries_v2.tsv)

[Impf-Fortschritt nach Bundesland](tsv/germany_vaccinations_by_state.tsv)

Der Datenstand der aktuellen, offiziellen Daten kann [hier (im JSON-Format)](https://impfdashboard.de/static/data/metadata.json) abgefragt werden.<br> <br>

## Datenquelle
https://impfdashboard.de/daten

### spezifisch
[Zeitreihe der bundesweiten Impfungen](https://impfdashboard.de/static/data/germany_vaccinations_timeseries_v2.tsv)

[Zeitreihe der Impfstofflieferungen](https://impfdashboard.de/static/data/germany_deliveries_timeseries_v2.tsv)

[Impf-Fortschritt nach Bundesland](https://impfdashboard.de/static/data/germany_vaccinations_by_state.tsv)
