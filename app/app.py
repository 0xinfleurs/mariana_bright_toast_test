import streamlit as st
import numpy as np
import pandas as pd
import requests
from PIL import Image


st.set_page_config(layout='wide')
st.title(":sparkler: Welcome to Bright Toast! :sparkler:")
st.text(" Bright Toast is a powerful machine learning model that given a description of your ideal wine gives you the perfect matches for your next wine tasting! ")
#st.image('./header.png')

st.image("app\img_streamlit_2.jpg")
element = st.empty()
element = st.empty()
#clicked = st.button ("Click to find your Bright Toast... :sparkles:")
#image = Image.open("C:\Users\mariana\OneDrive\Pictures\Saved Pictures\neon3.jpg")


descriptors_ = st.sidebar.text_input('Describe your ideal wine making sure to detail the look, smell, and taste.')
st.sidebar.markdown(":star2: Example of a correct wine description: Aromas include tropical fruit, broom, brimstone and dried herb. The palate isn't overly expressive, offering unripened apple, citrus and dried sage alongside brisk acidity.")


clicked_2 = st.sidebar.button("advanced optional parameters")
if "more_stuff" not in st.session_state:
    st.session_state.more_stuff = False

if clicked_2:
    st.session_state.more_stuff = True

grape_varieties = ['White Blend', 'Portuguese Red', 'Pinot Gris', 'Riesling',
        'Pinot Noir', 'Tempranillo-Merlot', 'Frappato', 'Gewürztraminer',
        'Cabernet Sauvignon', 'Nerello Mascalese', 'Chardonnay', 'Malbec',
        'Tempranillo Blend', 'Meritage', 'Red Blend', 'Merlot',
        "Nero d'Avola", 'Chenin Blanc', 'Gamay', 'Sauvignon Blanc',
        'Viognier-Chardonnay', 'Primitivo', 'Catarratto', 'Inzolia',
        'Petit Verdot', 'Monica', 'Bordeaux-style White Blend', 'Grillo',
        'Sangiovese', 'Cabernet Franc', 'Champagne Blend',
        'Bordeaux-style Red Blend', 'Aglianico', 'Petite Sirah',
        'Touriga Nacional', 'Carmenère', 'Albariño', 'Petit Manseng',
        'Rosé', 'Zinfandel', 'Vernaccia', 'Rosato', 'Grüner Veltliner',
        'Viognier', 'Vermentino', 'Grenache Blanc', 'Syrah', 'Nebbiolo',
        'Shiraz-Cabernet Sauvignon', 'Pinot Blanc', 'Alsace white blend',
        'Barbera', 'Rhône-style Red Blend', 'Portuguese White', 'Graciano',
        'Tannat-Cabernet', 'Sauvignon', 'Sangiovese Grosso', 'Torrontés',
        'Prugnolo Gentile', 'G-S-M', 'Verdejo', 'Fumé Blanc', 'Furmint',
        'Pinot Bianco', 'Bonarda', 'Shiraz', 'Montepulciano', 'Moscato',
        'Grenache', 'Ugni Blanc-Colombard', 'Syrah-Viognier',
        'Blaufränkisch', 'Friulano', 'Assyrtico', 'Carignan-Grenache',
        'Sagrantino', 'Savagnin', 'Cabernet Sauvignon-Syrah', 'Prosecco',
        'Vignoles', 'Sparkling Blend', 'Muscat', 'Muscadelle',
        'Shiraz-Viognier', 'Garganega', 'Pinot Grigio', 'Tempranillo',
        'Zierfandler', 'Cortese', 'Mencía', 'Zweigelt', 'Melon',
        'Rhône-style White Blend', 'Vidal', 'Cannonau', 'Verdelho',
        'Marsanne', 'Scheurebe', 'Kerner', 'Syrah-Grenache', 'Dolcetto',
        'Vilana', 'Glera', 'Viura', 'Garnacha Tintorera', 'Pinot Nero',
        'Roter Veltliner', 'Pinotage', 'Sémillon', 'Pinot Noir-Gamay',
        'Antão Vaz', 'Cabernet Sauvignon-Carmenère', 'Verdejo-Viura',
        'Verduzzo', 'Verdicchio', 'Silvaner', 'Colombard', 'Carricante',
        'Sylvaner', 'Fiano', 'Früburgunder', 'Sousão', 'Roussanne',
        'Avesso', 'Cinsault', 'Chinuri', 'Tinta Miúda',
        'Muscat Blanc à Petits Grains', 'Portuguese Sparkling',
        'Monastrell', 'Xarel-lo', 'Greco', 'Trebbiano',
        'Corvina, Rondinella, Molinara', 'Port', 'Chenin Blanc-Chardonnay',
        'Insolia', 'Merlot-Malbec', 'Ribolla Gialla',
        'Cabernet Sauvignon-Merlot', 'Duras', 'Weissburgunder', 'Roditis',
        'Traminer', 'Papaskarasi', 'Tannat-Syrah', 'Marsanne-Roussanne',
        'Charbono', 'Merlot-Argaman', 'Prié Blanc', 'Sherry',
        'Provence red blend', 'Tannat', 'Zibibbo', 'Falanghina',
        'Garnacha', 'Negroamaro', 'Mourvèdre', 'Syrah-Cabernet',
        'Müller-Thurgau', 'Pinot Meunier', 'Cabernet Sauvignon-Sangiovese',
        'Austrian Red Blend', 'Teroldego', 'Pansa Blanca',
        'Muskat Ottonel', 'Sauvignon Blanc-Semillon', 'Claret',
        'Semillon-Sauvignon Blanc', 'Bical', 'Moscatel', 'Rosado',
        'Viura-Chardonnay', 'Baga', 'Malvasia Bianca',
        'Gelber Muskateller', 'Malbec-Merlot', 'Monastrell-Syrah',
        'Malbec-Tannat', 'Malbec-Cabernet Franc', 'Turbiana', 'Refosco',
        'Alvarinho', 'Manzoni', 'Aragonês', 'Agiorgitiko', 'Malagousia',
        'Assyrtiko', 'Ruché', 'Welschriesling', 'Tinta de Toro',
        'Cabernet Moravia', 'Rieslaner', 'Traminette', 'Chambourcin',
        'Nero di Troia', 'Lambrusco di Sorbara', 'Cesanese',
        'Feteasca Neagra', 'Lagrein', 'Tinta Fina', 'St. Laurent',
        'Marsanne-Viognier', 'Cabernet Sauvignon-Shiraz',
        'Syrah-Cabernet Sauvignon', 'Gewürztraminer-Riesling',
        'Pugnitello', 'Cerceal', 'Touriga Nacional Blend',
        'Austrian white blend', 'Tocai', 'Tinta Roriz',
        'Chardonnay-Viognier', 'Fernão Pires',
        'Cabernet Franc-Cabernet Sauvignon', 'Grenache-Syrah',
        'Seyval Blanc', 'Muscat Canelli', 'Cabernet Merlot',
        'Tempranillo-Cabernet Sauvignon', 'Arinto', 'Aragonez',
        'Merlot-Cabernet Franc', 'Syrah-Petite Sirah', 'Cabernet Blend',
        'Maturana', 'Pecorino', 'Rotgipfler', 'Kinali Yapincak',
        'Cabernet Franc-Carmenère', 'Magliocco', 'Gamay Noir',
        'Sauvignon Gris', 'Spätburgunder', 'Picpoul', 'Vidal Blanc',
        'Albanello', 'White Port', 'Arneis', 'Malvasia', 'Plavac Mali',
        'Lemberger', 'Saperavi', 'Altesse', 'Blanc du Bois',
        'Provence white blend', 'Nosiola', 'Dornfelder',
        'Roussanne-Viognier', 'Ojaleshi', 'Godello', 'Mondeuse',
        'Perricone', 'Pedro Ximénez', 'Auxerrois', 'Syrah-Merlot',
        'Albana', 'Muskat', 'Lambrusco', 'Cabernet Sauvignon-Malbec',
        'Tinto Fino', 'Malbec-Cabernet Sauvignon', 'Moschofilero',
        'Grechetto', 'Encruzado', 'Carignano', 'Cabernet Franc-Merlot',
        'Torbato', 'Syrah-Petit Verdot', 'Garnacha Blanca', 'Pallagrello',
        'Morava', 'Syrah-Mourvèdre', 'Aleatico', 'Carcajolu', 'Kisi',
        'Shiraz-Grenache', 'Palomino', 'Grenache-Carignan', 'Nascetta',
        'Siria', 'Malbec-Syrah', 'Asprinio', 'Feteascǎ Regalǎ',
        'Lambrusco Grasparossa', 'Marselan', 'Tocai Friulano', 'Schiava',
        'Alfrocheiro', 'Chardonnay-Semillon', 'Corvina', 'Norton',
        'Alicante Bouschet', 'Tokaji', 'Moscadello',
        'Cabernet Sauvignon-Tempranillo', 'Carignan', 'Loureiro-Arinto',
        'Cabernet-Syrah', 'Sauvignon Blanc-Chardonnay', 'Symphony',
        'Edelzwicker', 'Madeira Blend', 'Black Muscat', 'Grenache Noir',
        'Durella', 'Xinomavro', 'Tinto del Pais',
        'Merlot-Cabernet Sauvignon', 'Cercial', 'Johannisberg Riesling',
        'Petite Verdot', 'Passerina', 'Valdiguié',
        'Colombard-Sauvignon Blanc', 'Kangoun', 'Loureiro', 'Posip',
        'Uva di Troia', 'Gros and Petit Manseng', 'Jacquère',
        'Kalecik Karasi', 'Karasakiz', 'Mourvèdre-Syrah', 'Negrette',
        'Zierfandler-Rotgipfler', 'Clairette', 'Raboso', 'País', 'Mauzac',
        'Pinot Auxerrois', 'Chenin Blanc-Sauvignon Blanc', 'Diamond',
        'Marzemino', 'Tinta Barroca', 'Chardonnay-Sauvignon Blanc',
        'Castelão', 'Trebbiano Spoletino', 'Teran', 'Trepat', 'Freisa',
        'Neuburger', 'Sämling', 'Chasselas', 'Hárslevelü', 'Trincadeira',
        'Merlot-Tannat', 'Rkatsiteli', 'Melnik', 'Siegerrebe',
        'Trousseau Gris', 'Grenache Blend', 'Gros Manseng',
        'Portuguese Rosé', 'Brachetto', 'Mantonico', 'Ekigaïna',
        'Muskateller', 'Aligoté', 'Sangiovese Cabernet',
        'Touriga Nacional-Cabernet Sauvignon', 'Muscat Blanc', 'Argaman',
        'Viognier-Roussanne', 'Pallagrello Bianco', 'Bobal',
        'Malvasia Istriana', 'Cabernet Sauvignon-Cabernet Franc',
        'Baco Noir', 'Veltliner', 'Tempranillo-Tannat', 'Morillon',
        'Touriga Franca', 'Picolit', 'Barbera-Nebbiolo', 'Prieto Picudo',
        'Gaglioppo', 'Tokay', 'Sacy', 'Piedirosso', 'Piquepoul Blanc',
        'Mansois', 'Chardonnay-Sauvignon', 'Tempranillo-Garnacha',
        'Carmenère-Cabernet Sauvignon', 'Chenin Blanc-Viognier',
        'Susumaniello', 'Vitovska', 'Orange Muscat', 'Grauburgunder',
        'Carignane', 'Moscatel Roxo', 'Tannat-Merlot', 'Nerello Cappuccio',
        'Counoise', 'Macabeo', 'Mazuelo', 'Sauvignon-Sémillon',
        'Tinta del Pais', 'Vranec', 'Mavrud', "Cesanese d'Affile",
        'Moscato Giallo', 'Debit', 'Verdil', 'Cabernet',
        'Verduzzo Friulano ', 'Treixadura', "Loin de l'Oeil",
        'Coda di Volpe', 'Grenache-Mourvèdre', 'Forcallà', 'Viura-Verdejo',
        'Bombino Bianco', 'Pinot-Chardonnay', 'Syrah-Tempranillo',
        'Cabernet Sauvignon-Barbera', 'Merlot-Cabernet',
        "Muscat d'Alexandrie", 'Jaen', 'Tinta del Toro', 'Timorasso',
        'Pigato', 'Sangiovese-Cabernet Sauvignon', 'Shiraz-Cabernet',
        'Viognier-Gewürztraminer', 'Prunelard',
        'Sauvignon Blanc-Chenin Blanc', 'Gros Plant',
        'Malbec-Petit Verdot', 'Colombard-Ugni Blanc', 'Grignolino',
        'Garnacha-Syrah', 'Rufete', 'Tempranillo-Shiraz', 'Mtsvane',
        'Chardonnay-Pinot Gris', 'Marawi', 'Chardonnay-Pinot Blanc',
        'Mataro', 'Tinta Cao', 'Blauer Portugieser', 'Ugni Blanc',
        'Groppello', 'Semillon-Chardonnay', 'Irsai Oliver', 'Alvarelhão',
        'Poulsard', 'Grenache-Shiraz', 'Baga-Touriga Nacional', 'Carineña',
        'Pignoletto', 'Muscatel', 'Mavrodaphne', 'Ciliegiolo',
        'Viognier-Grenache Blanc', 'Greco Bianco',
        'Cabernet Sauvignon-Merlot-Shiraz', 'Sciaccerellu', 'Zelen',
        'Alicante', 'Emir', 'Rosenmuskateller', 'Tsolikouri', 'Narince',
        'Malbec-Cabernet', 'Touriga', 'Grecanico', 'Carmenère-Syrah',
        'Madeleine Angevine', 'Mavroudi', 'Pinot Blanc-Pinot Noir',
        'Muscat Hamburg', 'Tempranillo Blanco', 'Casavecchia',
        'Pinot Gris-Gewürztraminer', 'White Riesling', 'Tinto Velasco',
        'Hondarrabi Zuri', 'Nuragus', 'Xynisteri', 'Kadarka',
        'Sauvignon Musqué', 'Roussanne-Marsanne', 'Incrocio Manzoni',
        'Terrantez', 'Bual', 'Okuzgozu', 'Rivaner', 'Doña Blanca',
        'Graševina', 'Lambrusco Salamino', 'Sangiovese-Syrah',
        'Tannat-Cabernet Franc', 'Thrapsathiri', 'Fer Servadou', 'Mission',
        'Kekfrankos', 'Cococciola', 'Blauburgunder', 'Marquette',
        'Romorantin', 'Verdejo-Sauvignon Blanc', 'Braucol',
        'Malvasia-Viura', 'Savatiano', 'Cabernet Franc-Malbec',
        'Pallagrello Nero', 'Rebula', 'Vespolina', 'Shiraz-Malbec', 'Rebo',
        'Macabeo-Chardonnay', 'Tempranillo-Malbec', 'Tamjanika',
        'Trousseau', 'Bacchus', 'Syrah-Malbec', 'Syrah-Cabernet Franc',
        'Macabeo-Moscatel', 'Cariñena-Garnacha', 'Plyto',
        'Códega do Larinho', 'Sideritis', 'Çalkarası', 'Azal',
        'Moscatel Graúdo', 'Viosinho', 'Moschofilero-Chardonnay',
        'Paralleda', 'Rara Neagra', 'Malvasia di Candia', 'Maria Gomes',
        'Molinara', 'Malvar', 'Airen', 'Erbaluce', 'Muscat of Alexandria',
        'Verdosilla', 'Abouriou', 'Pinot Noir-Syrah', 'Nielluciu',
        'Malbec-Bonarda', 'Vespaiolo', 'Malbec-Carménère', 'Biancolella',
        'Sauvignon Blanc-Verdejo', 'Aidani', 'Garnacha-Monastrell',
        'Vinhão', 'Souzao', 'Roter Traminer', 'Moscatel de Alejandría',
        'Rolle', 'Tinta Francisca', 'Malvasia Nera', 'Orangetraube',
        'Riesling-Chardonnay', 'Žilavka', 'Portuguiser', 'Listán Negro',
        'Pinotage-Merlot', 'Muscadine', 'Maria Gomes-Bical', 'Grolleau',
        'Zlahtina', 'Syrah-Grenache-Viognier', 'Jacquez', 'Gouveio',
        'Canaiolo', 'Carignan-Syrah', 'Bombino Nero',
        'Chardonnay-Riesling', 'Malagouzia-Chardonnay', 'Mavrotragano',
        'Bovale', 'Frankovka', 'Shiraz-Roussanne', 'Cabernet-Shiraz',
        'Syrah-Carignan', 'Elbling', 'Gragnano', 'Garnacha Blend',
        'Pinot Blanc-Chardonnay', 'Schwartzriesling', 'Petit Meslier',
        'Bastardo', 'Vidadillo', 'Misket', 'Chardonnay Weissburgunder',
        'Other', 'Robola', 'Merlot-Shiraz', 'Malagouzia', 'Folle Blanche',
        'Malbec Blend', 'Merlot-Syrah', 'Tamianka', 'Cabernet Pfeffer',
        'Morio Muskat', 'Rabigato', 'Babić', 'Roviello', 'Yapincak',
        'Sauvignonasse', 'Viognier-Marsanne', 'Mandilaria', 'Meseguera',
        'Alvarinho-Chardonnay', 'Saperavi-Merlot', 'Pinot Blanc-Viognier',
        'Teroldego Rotaliano', 'Biancu Gentile', 'Garnacha-Tempranillo',
        'Xinisteri', 'Sauvignon Blanc-Sauvignon Gris',
        'Trebbiano di Lugana', 'Albarossa', 'Ryzlink Rýnský', 'Verdeca',
        'Cabernet Sauvignon Grenache', 'Tămâioasă Românească',
        'Black Monukka', 'Merlot-Grenache', 'Vranac', 'Tempranillo-Syrah',
        'Chardonel', 'Silvaner-Traminer', 'Uvalino',
        'Merseguera-Sauvignon Blanc', 'Cabernet-Malbec', 'Boğazkere',
        'Gelber Traminer', 'Vermentino Nero', 'Cayuga', 'Tinta Amarela',
        'Tinta Negra Mole', 'Moscato Rosa', 'Chelois',
        'Sauvignon Blanc-Assyrtiko', 'Muscadel', 'Shiraz-Tempranillo',
        'Roussanne-Grenache Blanc', 'Biancale', 'Ansonica',
        'Syrah-Bonarda', 'Durif', 'Franconia', 'Malbec-Tempranillo',
        'Nasco', 'Monastrell-Petit Verdot', 'Sirica', 'Vital', 'Espadeiro',
        'Apple', 'Pinot Grigio-Sauvignon Blanc', 'Blatina', 'Karalahna',
        'Feteasca', 'Sercial', 'Valvin Muscat', 'Malvasia Fina',
        'Roditis-Moschofilero', 'St. Vincent', 'Chancellor', 'Premsal',
        'Jampal', 'Tokay Pinot Gris', 'Colorino', 'Picapoll', 'Blauburger',
        'Tinta Madeira', 'Centesimino', 'Grenache Gris', 'Trajadura',
        'Merlot-Petite Verdot', 'Ramisco', 'Catalanesca',
        'Garnacha-Cabernet', 'Garnacha-Cariñena', 'Gamza',
        'Cabernet Franc-Lemberger', 'Chardonnay-Albariño',
        'Shiraz-Mourvèdre', 'Mavrokalavryta', 'Favorita', 'Babosa Negro',
        'Tintilia ', 'Dafni', 'Petit Courbu', 'Kotsifali', 'Parraleta',
        'Moscato di Noto', 'Roscetto', 'Torontel', 'Otskhanuri Sapere',
        'Viognier-Valdiguié', 'Trollinger', 'Tsapournakos', 'Francisa',
        'Kuntra', 'Pignolo', 'Caprettone', 'Ondenc', 'Athiri',
        'Bobal-Cabernet Sauvignon']
provinces_dictionary = {'Portugal':['Douro', 'Alentejano', 'Alentejo', 'Beira Atlantico',   
       'Vinho Verde', 'Tejo', 'Lisboa', 'Península de Setúbal', 'Port',
       'Dão', 'Bairrada', 'Ribatejano', 'Duriense', 'Beiras',
       'Vinho Espumante', 'Terras do Dão', 'Beira Interior', 'Minho',
       'Bucelas', 'Estremadura', 'Portuguese Table Wine', 'Setubal',
       'Trás-os-Montes', 'Table wine', 'Moscatel de Setúbal', 'Ribatejo',
       'Palmela', 'Alenquer', 'Obidos', 'Vinho Espumante de Qualidade',
       'Madeira', 'Algarve', 'Terras do Sado', 'Vinho da Mesa',
       'Portugal', 'Moscatel do Douro', 'Vinho Licoroso', 'Colares',
       'Alenteo', 'Távora-Varosa'], 'US':['Oregon', 'Michigan', 'California', 'Virginia', 'Washington',
       'New York', 'Idaho', 'Texas', 'Pennsylvania', 'America',
       'New Jersey', 'Missouri', 'New Mexico', 'Nevada', 'Colorado',
       'Arizona', 'Massachusetts', 'Ohio', 'Illinois',
       'Washington-Oregon', 'North Carolina', 'Iowa', 'Vermont',
       'Kentucky', 'Connecticut', 'Rhode Island', 'Hawaii'], 'Spain':['Northern Spain', 'Galicia', 'Central Spain', 'Catalonia',
       'Levante', 'Andalucia', 'Spanish Islands', 'Spain Other'], 'Italy':['Sicily & Sardinia', 'Southern Italy', 'Central Italy', 'Tuscany',
       'Piedmont', 'Northeastern Italy', 'Veneto', 'Italy Other',
       'Lombardy', 'Northwestern Italy'], 'France':['Alsace', 'Beaujolais', 'Bordeaux', 'Champagne', 'France Other',
       'Southwest France', 'Burgundy', 'Rhône Valley',
       'Languedoc-Roussillon', 'Provence', 'Loire Valley'], 'Germany':['Rheinhessen', 'Mosel', 'Rheingau', 'Franken', 'Ahr', 'Nahe',
       'Pfalz', 'Württemberg', 'Baden', 'Mosel-Saar-Ruwer', 'Germany',
       'Mittelrhein', 'Landwein Rhein'], 'Argentina':['Other', 'Mendoza Province'], 'Chile':['Colchagua Valley', 'Maule Valley', 'Maipo Valley', 'Rapel Valley',
       'Leyda Valley', 'Aconcagua Valley', 'Loncomilla Valley',
       'Casablanca Valley', 'Curicó Valley', 'Limarí Valley',
       'Colchagua Costa', 'Central Valley', 'Lontué Valley', 'Chile',
       'Rio Claro', 'Cachapoal Valley', 'Aconcagua Costa',
       'Bío Bío Valley', 'Peumo', 'Elqui Valley', 'Marchigue',
       'Puente Alto', 'San Antonio', 'Itata Valley', 'Santa Cruz',
       'Lolol Valley', 'Cauquenes Valley', 'Apalta', 'Malleco',
       'Choapa Valley', 'Sagrada Familia', 'San Clemente', 'Buin',
       'Maipo Valley-Colchagua Valley', 'Leyda Valley-Maipo Valley',
       'Pirque', 'Molina', 'Curicó and Maipo Valleys',
       'Curicó and Leyda Valleys', 'Casablanca-Curicó Valley', 'Coelemu',
       'Requinoa', 'Casablanca & Leyda Valleys'], 'Australia':['South Australia', 'Victoria', 'Western Australia',
       'Australia Other', 'Tasmania', 'New South Wales'], 'Austria':['Burgenland', 'Leithaberg', 'Kremstal', 'Weinviertel',
       'Niederösterreich', 'Wagram', 'Kamptal', 'Steiermark',
       'Südsteiermark', 'Südoststeiermark', 'Wiener Gemischter Satz',
       'Wachau', 'Traisental', 'Thermenregion', 'Carnuntum',
       'Weinland Österreich', 'Wagram-Donauland', 'Vienna',
       'Neusiedlersee', 'Mittelburgenland', 'Eisenberg', 'Austria',
       'Südburgenland'], 'South Africa':['Stellenbosch', 'Simonsberg-Stellenbosch', 'Western Cape',
       'Coastal Region', 'Darling', 'Robertson', 'Swartland',
       'Walker Bay', 'Paarl', 'Constantia', 'South Africa', 'Franschhoek',
       'Elgin', 'Wellington', 'Simonsberg-Paarl', 'Overberg',
       'Olifants River', 'Groenekloof', 'Lutzville Valley', 'Durbanville',
       'Breedekloof', 'Cederberg', 'Philadelphia', 'Jonkershoek Valley',
       'Eilandia', 'Tulbagh', 'Hemel en Aarde', 'Cape South Coast',
       'Northern Cape', 'Breede River Valley', 'Elim', 'Vlootenburg',
       'Polkadraai Hills', 'Bot River', 'Paardeberg', 'Helderberg',
       'Cape Peninsula', 'Malgas', 'Devon Valley', 'Cape Agulhas'], 'New Zealand':['Marlborough', "Hawke's Bay", 'Martinborough', 'Central Otago',
       'Awatere Valley', 'Canterbury', 'Wairau Valley', 'Kumeu', 'Nelson',
       'Waipara Valley', 'South Island', 'Gisborne', 'Wairarapa',
       'Waipara', 'New Zealand', 'Waitaki Valley', 'East Coast',
       'Waiheke Island', 'Gladstone'], 'Israel':['Judean Hills', 'Galilee', 'Dan', 'Negev Hills', 'Upper Galilee',
       'Ella Valley', 'Shomron', 'Samson', 'Galil', 'Israel',
       'Haut-Judeé', 'Golan Heights', 'Negev', 'Jerusalem Hills'], 'Hungary':['Tokaj', 'Tokaji', 'Villány', 'Hungary', 'Eger', 'Mátra',
       'Szekszárd', 'Sopron'], 'Greece':['Santorini', 'Crete', 'Corinth', 'Halkidiki', 'Epanomi', 'Nemea',
       'Peloponnese', 'Drama', 'Pangeon', 'Mantinia', 'Chalkidiki',
       'Rapsani', 'Pageon', 'Naoussa', 'Atalanti Valley', 'Macedonia',
       'Samos', 'Patras', 'Korinthia', 'Greece', 'Florina',
       'Mavrodaphne of Patras', 'Attica', 'Thraki', 'Monemvasia',
       'Ismarikos', 'Sithonia', 'Agioritikos', 'Beotia', 'Retsina',
       'Amindeo', 'Cephalonia', 'Cyclades', 'Achaia', 'Amyndeon',
       'Central Greece', 'Mavrodaphne de Cephalonie', 'Goumenissa',
       'Messinia', 'Lakonia', 'Markopoulo', 'Krania Olympus', 'Corinthia',
       'Mount Athos', 'Sterea Ellada', 'Muscat of Patras', 'Imathia',
       'Letrinon', 'Muscat of Kefallonian', 'Thessalikos', 'Limnos',
       'Arcadia', 'Vin de Pays de Velvendo', 'Lesbos'], 'Romania':['Recas', 'Dealu Mare', 'Jidvei', 'Panciu', 'Romania', 'Tarnave',
       'Viile Timisului', 'Sebes', 'Murfatlar', 'Dealurile Munteniei',
       'Vânju Mare', 'Dealurile Hușilor', 'Viile Timis'], 'Mexico':['Valle de Guadalupe', 'San Vicente',
       'San Antonio de las Minas Valley'], 'Canada':['Ontario', 'British Columbia', 'Canada Other'], 'Turkey':['Thrace', 'Aegean', 'Ankara', 'Elazığ-Diyarbakir', 'Turkey',
       'Elazığ', 'Cappadocia', 'Urla-Thrace'], 'Czech Republic':['Moravia'],'Slovenia':['Slovenia', 'Primorska', 'Vipavska Dolina', 'Kras', 'Goriska Brda',
       'Brda', 'Dolenjska', 'Slovenska Istra'], 'Luxembourg': ['Moselle Luxembourgeoise'], 'Croatia':['Istria', 'Peljesac', 'Korčula', 'Croatia', 'Podunavlje',
       'Dalmatian Coast', 'Middle and South Dalmatia', 'Kutjevo',
       'North Dalmatia', 'Hvar', 'Dingač', 'Hrvatsko Primorje', 'Krk'], 'Georgia':['Kakheti', 'Georgia'], 'Uruguay': ['Canelones', 'Uruguay', 'Atlantida', 'Juanico', 'Montevideo',
       'San Jose', 'Progreso'], 'England':['England'], 'Lebanon':['Lebanon', 'Bekaa Valley'], 'Serbia':['Pocerina', 'Fruška Gora'], 'Brazil':['Pinto Bandeira', 'Santa Catarina', 'Serra Gaúcha',
       'Vale dos Vinhedos', 'Brazil', 'Vale Trentino', 'Serra do Sudeste',
       'Campanha'], 'Moldova':['Moldova', 'Cahul', 'Codru Region'], 'Morocco':['Zenata', 'Guerrouane', 'Morocco'], 'Peru': ['Ica'], 'India':['Nashik'], 'Bulgaria':['Thracian Valley', 'Danube River Plains', 'Black Sea Coastal',
       'Bulgaria'], 'Cyprus':['Cyprus', 'Pitsilia Mountains', 'Pafos', 'Lemesos', 'Commandaria',
       'Kathikas'], 'Armenia':['Armenia'], 'Switzerland':['Valais', 'Switzerland', 'Ticino', 'Neuchâtel'], 'Bosnia and Herzegovina':['Mostar'], 'Ukraine':['Ukraine'], 'Slovakia':['Muzla'], 'Macedonia':['Tikves'], 'China':['China']}
if st.session_state.more_stuff:
    st.sidebar.markdown(":star2: These are optional parameters, don't worry if you don't know :) ")
    variety =   st.sidebar.multiselect('Select a variety',grape_varieties)
    countries = st.sidebar.multiselect('select a country',list(provinces_dictionary.keys()))
        #regions= st.multiselect('Select a region(France)',[''])
    if len(countries) > 0:
        provinces_total = []
        for c in range(len(countries)):
            provinces_total = provinces_total + list(provinces_dictionary[countries[c]])       
        provinces = st.sidebar.multiselect('Select a province', provinces_total)
    min_price = st.sidebar.number_input('Minimum price')
    max_price = st.sidebar.number_input('Maximum price (sky is the limit)')
    wineries = st.sidebar.multiselect('Select a winery',['Nicosia', 'Quinta dos Avidagos', 'Rainstorm','Mas de Pampelonne', 'Bodegas Eidosela', 'Penedo Borges'])
    #st.markdown(":star2: However, the description is mandatory! ")
    #descriptors_ = st.text_input('Describe your ideal wine making sure to detail the look, smell, and taste.')
    #st.markdown(":star2: Example of a correct wine description: Aromas include tropical fruit, broom, brimstone and dried herb. The palate isn't overly expressive, offering unripened apple, citrus and dried sage alongside brisk acidity.")

#def basic_cleaning(descriptors_):
    #
## Let's call our API in order to retreive a prediction

#url = 'x'
   # if url == 'x'

#params ={'descriptors'; descriptors,
         #'countries'; countries
         #'provinces';provinces,
         # 'regions'; regions
         # 'varieties; varieties
         # 'wineries'; wineries
         # 'min_price'; min price
         # 'max_price'; max_price }

#req = requests.get(url, params=params)
# req.json()



