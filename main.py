import google.generativeai as genai
from fastapi import FastAPI, HTTPException,File, UploadFile
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import io
import pdfplumber
from docx import Document

# Configura Gemini API (⚠ pon tu API KEY aquí directamente solo para pruebas locales)
genai.configure(api_key="AIzaSyDpV3E2PEjRJRSTNanCCTriozgh8rOU0ZQ")
model = genai.GenerativeModel("gemini-2.0-flash")

app = FastAPI()

# Permitir CORS al frontend
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserSolution(BaseModel):
    case: str
    user_solution: str
    ia_solution: str

@app.get("/case")
async def generate_case():
    prompt = (
        "Elabora un caso de estudio corto con un contexto claro y una problemática concreta, "
        "relacionado con la privacidad y protección de datos según la norma ISO/IEC 29100. "
        "El caso puede ser de cualquier ámbito (educación, gobierno, finanzas, etc.) y no debe incluir la solución, solo contexto y problema."
    )
    response = model.generate_content(prompt)
    return {"case": response.text}

@app.post("/solve")
async def solve_case(data: dict):
    case = data.get("case", "")
    if not case:
        raise HTTPException(status_code=400, detail="Caso no proporcionado")
    response = model.generate_content(f"Resuelve el siguiente caso de estudio según la norma ISO/IEC 29100:\n\n{case}")
    return {"solution": response.text}

@app.post("/compare")
async def compare_solutions(data: UserSolution):
    prompt = (
        f"Compara estas dos soluciones al siguiente caso de estudio sobre privacidad de datos (ISO/IEC 29100):\n\n"
        f"Caso:\n{data.case}\n\n"
        f"Solución del usuario:\n{data.user_solution}\n\n"
        f"Solución generada por IA:\n{data.ia_solution}\n\n"
        "Evalúa si coinciden en criterios, pasos y razonamiento. Devuelve un porcentaje de coincidencia y un breve análisis en donde se mencione en qué coinciden, criterios, etc."
    )
    response = model.generate_content(prompt)
    return {"comparison": response.text}


@app.post("/upload_case")
async def upload_case(file: UploadFile = File(...)):
    try:
        content = await file.read()
        extension = file.filename.split('.')[-1].lower()

        if extension == 'txt':
            text = content.decode('utf-8')
        elif extension == 'pdf':
            with pdfplumber.open(io.BytesIO(content)) as pdf:
                text = '\n'.join([page.extract_text() for page in pdf.pages if page.extract_text()])
        elif extension == 'docx':
            doc = Document(io.BytesIO(content))
            text = '\n'.join(paragraph.text for paragraph in doc.paragraphs)
        else:
            return {"error": "Tipo de archivo no soportado"}

        return {"uploaded_case": text.strip()}
    except Exception as e:
        return {"error": str(e)}