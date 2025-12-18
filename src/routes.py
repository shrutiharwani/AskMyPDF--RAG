from flask import (
    render_template,
    request,
    jsonify,
    redirect,
    url_for
)
import os

from src.services.pdf_processor import process_pdf
from src.services.llm_service import ask_llm
from src.services.history_db import (
    save_chat,
    get_all_chats,
    clear_chats
)

# --------------------
# CONFIG
# --------------------
UPLOAD_FOLDER = "uploads"

# Ensure folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# --------------------
# ROUTE REGISTRATION
# --------------------
def register_routes(app):

    # ---------- HOME ----------
    @app.route("/")
    def home():
        return render_template("home.html")

    # ---------- CHAT UI ----------
    @app.route("/chat-ui")
    def chat_ui():
        history = get_all_chats()
        return render_template("chat.html", history=history)

    # ---------- PDF UPLOAD ----------
    @app.route("/upload", methods=["POST"])
    def upload_pdf():
        if "pdf" not in request.files:
            return "No file uploaded", 400

        file = request.files["pdf"]

        if file.filename == "":
            return "No selected file", 400

        pdf_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(pdf_path)

        # ✅ Process PDF → embeddings
        process_pdf(pdf_path)

        return redirect(url_for("chat_ui"))

    # ---------- CHAT API ----------
    @app.route("/chat", methods=["POST"])
    def chat():
        data = request.get_json()
        user_query = data.get("message")

        if not user_query:
            return jsonify({"answer": "Please ask a question."})

        # ✅ RAG handled by service
        answer = ask_llm(user_query)

        # ✅ Save chat to SQLite
        save_chat(user_query, answer)

        return jsonify({"answer": answer})

    # ---------- CLEAR CHAT HISTORY ----------
    @app.route("/clear-history")
    def clear_history():
        clear_chats()
        return jsonify({"status": "cleared"})
