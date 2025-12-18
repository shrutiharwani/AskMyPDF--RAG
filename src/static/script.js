document.addEventListener("DOMContentLoaded", () => {
    const input = document.getElementById("chat-input");
    const chatBox = document.getElementById("chat-box");
    const sendBtn = document.getElementById("send-btn");

    if (!input || !chatBox || !sendBtn) {
        console.error("❌ Chat UI elements not found.");
        return;
    }

    input.addEventListener("keydown", (e) => {
        if (e.key === "Enter") sendMessage();
    });

    sendBtn.addEventListener("click", sendMessage);

    async function sendMessage() {
        const message = input.value.trim();
        if (!message) return;

        addMessage(message, "user");
        input.value = "";
        sendBtn.disabled = true;

        const thinkingDiv = addMessage("Thinking...", "bot thinking");

        try {
            const response = await fetch("/chat", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ message })
            });

            const data = await response.json();
            thinkingDiv.remove();

            if (data.answer) {
                // Use innerHTML for formatted response
                addMessage(formatAnswer(data.answer), "bot");
            } else {
                addMessage("No response received.", "bot");
            }
        } catch (error) {
            console.error("Error:", error);
            thinkingDiv.remove();
            addMessage("Error connecting to server.", "bot");
        }

        sendBtn.disabled = false;
        input.focus();
    }

    function addMessage(text, className) {
        const div = document.createElement("div");
        div.className = `message ${className}`;
        div.innerHTML = text; // Allows bolding and breaks
        chatBox.appendChild(div);
        
        // Smooth scroll to bottom
        chatBox.scrollTo({ top: chatBox.scrollHeight, behavior: 'smooth' });
        
        return div;
    }

    function formatAnswer(text) {
        // Clean up text for HTML display
        return text
            .replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>") // Bold Markdown
            .replace(/\n/g, "<br>"); // Line breaks
    }

    window.clearHistory = async function () {
        if(confirm("Are you sure you want to clear the chat?")) {
            await fetch("/clear-history");
            location.reload();
        }
    };
});