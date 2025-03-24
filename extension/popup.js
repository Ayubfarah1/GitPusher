document.getElementById("updateButton").addEventListener("click", async () => {
    const statusElement = document.getElementById("status");
    statusElement.textContent = "Updating...";

    try {
        let response = await fetch("http://127.0.0.1:5001/update", {
            method: "POST"
        });

        let data = await response.json();
        if (response.ok) {
            statusElement.textContent = "✅ GitHub Updated!";
        } else {
            statusElement.textContent = "❌ Error: " + data.error;
        }
    } catch (error) {
        console.error("Fetch failed:", error);
        statusElement.textContent = "❌ Failed to connect to server.";
    }
});
