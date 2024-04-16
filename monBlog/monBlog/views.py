from django.shortcuts import render
from django.http import HttpResponse

articles = [
    {
        "title": "Article 1",
        "author": "John Doe",
        "date": "02-27-2023",
        "description": "Explorez les mystères fascinants de l'espace alors que nous plongeons dans les profondeurs infinies de l'univers.",
        "content": "L'univers est une toile complexe tissée de galaxies, d'étoiles et de phénomènes célestes énigmatiques. Dans cet article, nous plongerons dans les secrets les plus profonds de l'espace, en examinant les phénomènes tels que la naissance et la mort des étoiles, les trous noirs et les mystères de la matière noire. Préparez-vous à élargir votre esprit et à contempler l'immensité de l'univers."
    },
    {
        "title": "Article 2",
        "author": "Jane Smith",
        "date": "03-01-2023",
        "description": "Découvrez les dernières avancées et applications de l'intelligence artificielle qui façonnent notre avenir technologique.",
        "content": "L'intelligence artificielle (IA) est à l'avant-garde de l'innovation technologique, transformant nos vies de manière inédite. Dans cet article, nous explorerons les récentes percées en IA, des algorithmes d'apprentissage profond aux applications pratiques telles que la conduite autonome et la médecine personnalisée. Nous discuterons également des défis éthiques et des implications sociétales de l'essor de l'IA, offrant un aperçu perspicace de l'avenir de cette révolution technologique."
    },
    {
        "title": "Article 3",
        "author": "Bob Johnson",
        "date": "03-05-2023",
        "description": "Découvrez les conséquences dévastatrices de la déforestation sur la biodiversité de notre planète et pourquoi la préservation des forêts est cruciale.",
        "content": "Les forêts sont les poumons de notre planète, abritant une myriade d'espèces végétales et animales essentielles à l'équilibre écologique. Cependant, la déforestation incontrôlée menace leur existence et entraîne des conséquences désastreuses pour la biodiversité. Dans cet article, nous examinerons de près les impacts de la déforestation sur les écosystèmes, des extinctions d'espèces à la perte de habitats critiques. Nous discuterons également des solutions possibles pour préserver nos forêts et protéger la richesse de la vie sur Terre."
    }
]

def home(request):
    return render(request, 'home.html', {'articles': articles})