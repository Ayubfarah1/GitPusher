document.getElementById("updateButton").addEventListener("click", async () => {
    const statusElement = document.getElementById("status");
    statusElement.textContent = "Updating...";

    try {
        let response = await fetch("http://localhost:5000/update", {
            method: "POST"
        });

        let data = await response.json();
        if (response.ok) {
            statusElement.textContent = "✅ GitHub Updated!";
        } else {
            statusElement.textContent = "❌ Error: " + data.error;
        }
    } catch (error) {
        statusElement.textContent = "❌ Failed to connect to server.";
    }
});
