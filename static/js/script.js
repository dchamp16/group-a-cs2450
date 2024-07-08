// JavaScript to handle color scheme changes and save content
document.addEventListener("DOMContentLoaded", function() {
    const primaryColorInput = document.getElementById("primaryColor");
    const offColorInput = document.getElementById("offColor");
    const applyButton = document.getElementById("applyColors");
    const resetButton = document.getElementById("resetColors");

    const defaultPrimaryColor = "#4C721D";
    const defaultOffColor = "#FFFFFF";

    // Load saved colors from localStorage
    const savedPrimaryColor = localStorage.getItem("primaryColor") || defaultPrimaryColor;
    const savedOffColor = localStorage.getItem("offColor") || defaultOffColor;

    document.documentElement.style.setProperty("--primary-color", savedPrimaryColor);
    document.documentElement.style.setProperty("--off-color", savedOffColor);

    primaryColorInput.value = savedPrimaryColor;
    offColorInput.value = savedOffColor;

    applyButton.addEventListener("click", function() {
        const primaryColor = primaryColorInput.value;
        const offColor = offColorInput.value;

        // Save colors to localStorage
        localStorage.setItem("primaryColor", primaryColor);
        localStorage.setItem("offColor", offColor);

        // Apply the colors
        document.documentElement.style.setProperty("--primary-color", primaryColor);
        document.documentElement.style.setProperty("--off-color", offColor);
    });

    resetButton.addEventListener("click", function() {
        // Reset to default colors
        localStorage.setItem("primaryColor", defaultPrimaryColor);
        localStorage.setItem("offColor", defaultOffColor);

        document.documentElement.style.setProperty("--primary-color", defaultPrimaryColor);
        document.documentElement.style.setProperty("--off-color", defaultOffColor);

        primaryColorInput.value = defaultPrimaryColor;
        offColorInput.value = defaultOffColor;
    });

    // Save content to a text file
    document.getElementById("saveContent").addEventListener("click", function() {
        const rows = document.querySelectorAll(".table-container table tbody tr");
        let content = "";

        rows.forEach(row => {
            const index = row.cells[0].innerText;
            const value = row.cells[1].innerText;
            content += `index: ${index} value: ${value}\n`;
        });

        const blob = new Blob([content], { type: "text/plain" });
        const link = document.createElement("a");
        link.href = URL.createObjectURL(blob);
        link.download = "content.txt";
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    });
});
