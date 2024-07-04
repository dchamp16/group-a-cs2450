// JavaScript to handle color scheme changes
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
});
