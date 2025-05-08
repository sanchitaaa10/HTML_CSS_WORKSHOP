const toggleBtn = document.getElementById("toggleBtn");
        const body = document.body;
    
        toggleBtn.addEventListener("click", () => {
            body.classList.toggle("dark-mode");
            toggleBtn.textContent = body.classList.contains("dark-mode") ? "Toggle Light Mode" : "Toggle Dark Mode";
        });