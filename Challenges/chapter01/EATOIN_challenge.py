import pprint
from Practices.chapter01.EATOIN_practice import get_char_bar_chart
text_latin = "Sicut castrum in angulo suo in ludo mediaevali, gravem praevideo molestiam et hic maneo idem."
text_spanish = "Como el castillo en su rincón en un juego medieval, preveo terribles problemas y me quedo aquí igual."
pprint.pprint(get_char_bar_chart(text_spanish))
