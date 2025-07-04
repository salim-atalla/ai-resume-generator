# AI Resume Generator

A **Fullstack Python + Generative AI project** that fine-tunes GPT-2 on structured resume samples to generate professional, personalized resumes locally and for free, with a Next.js frontend for user interaction.

---

## Features

-   Fine-tune GPT-2 locally on resume data.
-   Generate structured resumes (Summary, Skills, Experience).
-   FastAPI backend with local model inference.
-   Next.js frontend for user input and preview  
    Completely offline, no OpenAI API costs.
-   Portfolio-ready for Fullstack + Generative AI applications.

---

## Tech Stack

-   **Python, FastAPI**: Backend API server.
-   **Hugging Face Transformers (GPT-2)**: Generative AI.
-   **Next.js (React)**: Frontend interface.
-   **Tailwind CSS**: Clean, responsive styling.
-   **Docker (optional)**: For containerization.

---

## Project Structure

```

ai-resume-generator/
├── backend/
│   ├── main.py                 # FastAPI server with GPT-2 generation
│   ├── train_gpt2_resume.py    # GPT-2 fine-tuning script
│   ├── test_gpt2_resume.py     # Local generation testing script
│   ├── resume_dataset.txt      # Training dataset
│   ├── gpt2_resume_finetuned/  # Fine-tuned GPT-2 model
│   └── requirements.txt        # Backend dependencies
├── frontend/
│   ├── pages/                  # Next.js pages (index.tsx, _app.tsx)
│   ├── styles/                 # Tailwind global styles
│   ├── package.json            # Frontend dependencies and scripts
│   └── ...                     # Supporting files
└── README.md

```

---

## Setup Instructions

### Clone the Repository

```bash
git clone https://github.com/salim-atalla/ai-resume-generator.git
cd ai-resume-generator
```

---

### Setup Backend

```bash
cd backend/
python -m venv venv
source venv/bin/activate      # (Linux/Mac)
venv\\Scripts\\activate       # (Windows)

pip install -r requirements.txt
```

---

### Prepare Dataset

Edit `resume_dataset.txt`:

-   Add **structured resume samples**:

```
Summary:
...

Skills:
...

Experience:
...

---
```

Use the provided 80+ samples to bootstrap your training.

---

### Fine-tune GPT-2 Locally

```bash
python train_gpt2_resume.py
```

This will save your fine-tuned model in `gpt2_resume_finetuned/`.

---

### Test Generation Locally

```bash
python test_gpt2_resume.py
```

You should see a structured resume generated in your terminal.

---

### Run FastAPI Server

```bash
uvicorn main:app --reload --port 8000
```

Your backend will be live at:

```
http://localhost:8000
```

---

### Setup Frontend (Next.js)

```bash
cd frontend/
npm install
npm run dev
```

Your frontend will be live at:

```
http://localhost:3000
```

The **frontend collects user details** and constructs a **clean structured prompt**, sending it to the backend for generation.

---

## Testing API Endpoint

Since the frontend now sends a `prompt` directly, you can test:

```bash
curl -X POST "http://localhost:8000/generate-resume" \
     -H "Content-Type: application/json" \
     -d '{"prompt": "Summary:\nName: Alice Doe\nEmail: alice@example.com\nLinkedIn: linkedin.com/in/alicedoe\nSkills: Python, FastAPI, SQL\nExperiences: Developed APIs, Managed cloud infrastructure\n\nSkills:\n-"}'
```

---

## Future Enhancements

-   PDF download of generated resumes.
-   User authentication and saved resumes.
-   Multi-language support.
-   Resume style customization.
-   Hosting on Render/Vercel for demo.

---

## Acknowledgments

-   [Hugging Face Transformers](https://huggingface.co/transformers/)
-   [FastAPI](https://fastapi.tiangolo.com/)
-   [Next.js](https://nextjs.org/)
-   [Tailwind CSS](https://tailwindcss.com/)

---

Build your **AI Resume Generator** and showcase your **Fullstack + Generative AI skills** confidently.
