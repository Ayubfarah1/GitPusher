document.getElementById("updateButton").addEventListener("click", async () => {
    const statusElement = document.getElementById("status");
    statusElement.textContent = "Updating...";
    console.log("Sending POST request to /update...");

    try {
        let response = await fetch("https://gitpusher.onrender.com/update", {
            method: "POST"
        });
        console.log("Response received:", response.status);
        
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
