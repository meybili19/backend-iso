import google.generativeai as genai
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# Configura Gemini API (⚠ pon tu API KEY aquí directamente solo para pruebas locales)
genai.configure(api_key="AIzaSyAzPRj2KzTa1qSmXyQgUW4qbOAW0yVEErs")

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

class SolveInput(BaseModel):
    case_study: str

class UserInput(BaseModel):
    manual_response: str
    case_study: str
    ia_solution: str

@app.get("/case")
def get_case():
    try:
        model = genai.GenerativeModel('models/gemini-pro')
        prompt = "Elabora un caso de estudio corto relacionado con la privacidad y protección de datos bajo la norma ISO/IEC 29100, sólo pon el caso de estudio, no la solución, además de que sea 1 caso de cualquier ámbito, no únicamente salud."
        response = model.generate_content(prompt)
        return {"case_study": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/solve")
def solve_case(input_data: SolveInput):
    try:
        model = genai.GenerativeModel('models/gemini-pro')
        prompt = f"Propón una solución adecuada para el siguiente caso según la norma ISO/IEC 29100:\n{input_data.case_study}"
        response = model.generate_content(prompt)
        return {"ia_solution": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/compare")
def compare_case(input_data: UserInput):
    try:
        model = genai.GenerativeModel('models/gemini-pro')
        prompt = (
            f"Compara la siguiente respuesta del usuario:\n{input_data.manual_response}\n"
            f"con la solución IA:\n{input_data.ia_solution}\n"
            "Devuelve un porcentaje de coincidencia (del 0% al 100%) y lista de coincidencias clave."
        )
        response = model.generate_content(prompt)
        return {"comparison": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
