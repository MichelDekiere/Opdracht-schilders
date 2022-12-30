README korte uitleg over structuur

Mijn project is opgedeeld in verschillende folders. Dit zijn de stappen die ik
ondernomen heb om dit project uit te voeren.

1. Scraping images
	In deze folder vindt u 2 notebooks.

	Een notebook waarin mijn 2 verschillende pogingen staan om de schilderijen van
	Rembrandt te scrapen (de 2e poging is de poging die dan uiteindelijk de definitieve
	werd).
	Een tweede notebook met daarin de code van de scraping van de schilderijen van
	Vincent Van Gogh.

2. Data exploration & setup
	Hierin vindt u een notebook waarin ik toelicht hoe ik mijn eigen GPU gebruikt heb en
	hoe ik dit opgezet heb. U vindt ook bewijs dat mijn GPU daadwerkelijk ook beschikbaar
	was voor het gebruik van het trainen voor modellen.

	Ook vindt u de data exploration die ik gedaan heb. Data cleanup, een sampling methode
	kiezen en mijn logica erachter, een slideshow van de images in de dataset en ook het 
	opsplitsen van de data in train-, validatie- en testset vindt u in deze notebook.

3. Modellen uit het boek
	In de opgave van de opdracht werd gevraagd om de verschillende modellen uit het boek
	eens toe te passen op de opdracht. 
	Deze code van de verschillende modellen vindt u in de notebook van deze folder.
	De modellen zelf vindt u in de 'models' map in deze folder.

4. Eigen Modellen
	4.1 Eigen Convolutioneel Netwerk
		In deze map vindt u een notebook waarin ik eens mijn eigen convolutionele
		netwerk heb opgesteld voor de classificatie van de schilderijen.
		Ook de getrainde modellen vindt u in deze map.
	
	4.2 CNN met transfer learning
		Hierin vindt u een notebook waarin ik met behulp van transferlearning verschillende
		modellen opstel. Ik maakte gebruik van VGG16 en ResNet.
		Wederom vindt u ook hier de bestanden van de getrainde modellen.

5. Web App
	In deze folder vindt u de code van mijn webapplicatie die ik gemaakt. Hierop kunt u een
	afbeelding van een schilderij uploaden en mijn model zal dan voorspellen van welke schilder
	dit schilderij geschilderd is.

	U vindt een webApp python file met daarin de Flask code van deze web app.
	Ook een PaintingPredictor python file, die in de webApp file geïmporteerd wordt.
	In deze klasse wordt mijn model ingeladen en is ook verantwoordelijk voor het effectieve
	voorspellen van de images.











