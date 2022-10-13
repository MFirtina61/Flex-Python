from PIL import Image,ImageFont,ImageDraw

afbeelding = Image.open("Better.png")

tekengebied = ImageDraw.Draw(afbeelding)


lettertype = ImageFont.truetype("impact.ttf", 30)

tekst = "When your code works\nWith out Error"
tekengebied.multiline_text((10,10), tekst, font=lettertype, fill=(0,0,0))




afbeelding.show()


breedte = str(afbeelding.width)
hoogte = str(afbeelding.height)



helft_breedte = afbeelding.width / 2
helft_hoogte = afbeelding.height / 2

nieuwe_afmeting = (helft_breedte, helft_hoogte)

kleinere_afbeelding = afbeelding.resize(nieuwe_afmeting)

kleinere_afbeelding.save('Better.png')