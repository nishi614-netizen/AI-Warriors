from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate", response_class=HTMLResponse)
def generate(request: Request, task_type: str = Form(...), user_input: str = Form(...)):
    
    # 🔥 Replace this with actual AI model call
    output = f"Generated {task_type} for: {user_input}"

    return templates.TemplateResponse("index.html", {
        "request": request,
        "result": output
    })