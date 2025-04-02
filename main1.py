# Python 3.11
from deep_translator import GoogleTranslator

input_file = "/archivos/subtitulos_ENG.srt"
output_file = "/archivos/subtitulos_SPA.srt"

with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

traducidas = []
for linea in lines:
    if "-->" in linea or linea.strip().isdigit() or not linea.strip():
        traducidas.append(linea)
    else:
        try:
            traducida = GoogleTranslator(source='fr', target='es').translate(linea.strip())
            traducidas.append((traducida or linea.strip()) + "\n")
        except Exception as e:
            traducidas.append(linea)  # conserva original si hay error
            print("⚠️ Error traduciendo línea:", linea.strip(), "| Error:", e)

with open(output_file, "w", encoding="utf-8") as f:
    f.writelines(traducidas)

print("✅ Traducción completada:", output_file)
