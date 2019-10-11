import folium


def MapCreation():
	#creation d'une carte HTML centree sur la finistere nord
	card=folium.Map(location=[48.38955,-4.089069], zoom_start=10,nzoom_control=False)
	fichier = open("card.html","a")				
	#inclusion de notre js 													#creation de la carte centree sur region concernee
	fichier.write("<script src='interaction.js'></script>")
	fichier.close()
	card.save('card.html')


g = geocoder.osm('11 Wall Street, New York')
g.osm
MapCreation()
