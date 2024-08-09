document.addEventListener("DOMContentLoaded", function() {
    const primaryColorInput = document.getElementById("primaryColor");
    const offColorInput = document.getElementById("offColor");
    const applyButton = document.getElementById("applyColors");
    const resetButton = document.getElementById("resetColors");
    const rerunButton = document.getElementById("rerunButton");

    const defaultPrimaryColor = "#4C721D";
    const defaultOffColor = "#FFFFFF";

    let previousValue = '';

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

    // Function to update memory slot with validation
    window.updateMemory = function(location, instruction) {
        const trimmedInstruction = instruction.trim();
        if (/^-?\d{1,6}$/.test(trimmedInstruction)) {
            fetch('/update_memory', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ memory_location: location, instruction: parseInt(trimmedInstruction) }),
            })
                .then(response => response.json())
                .then(data => {
                    if (!data.success) {
                        alert('Error: ' + data.error);
                    } else {
                        console.log('Memory updated successfully.'); // Debugging log
                        rerunButton.style.display = 'block'; // Show re-run button
                    }
                })
                .catch((error) => {
                    console.error('Error:', error);
                });
        } else {
            alert('Please enter a valid number between -999999 and 999999.');
            document.querySelector(`td[data-location="${location}"]`).innerText = previousValue;
        }
    };

    // Save the previous value when the cell is focused
    document.querySelectorAll('td[contenteditable="true"]').forEach(cell => {
        cell.addEventListener('focus', function() {
            previousValue = this.innerText.trim();
        });
    });

    // Handle re-run button click
    rerunButton.addEventListener('click', function() {
        fetch('/rerun', {
            method: 'POST',
        })
            .then(() => {
                location.reload(); // Reload to reflect changes
            })
            .catch((error) => {
                console.error('Error:', error);
            });
    });

    // Save content to a text file with a custom filename
    document.getElementById("saveContent").addEventListener("click", function() {
        const filename = prompt("Enter the filename:", "content.txt");

        if (filename) {
            const rows = document.querySelectorAll(".table-container table tbody tr");
            let content = "";

            rows.forEach(row => {
                let value = row.cells[1].innerText.trim();
                value = value.padStart(4, '0'); // Add leading zeros if less than four digits
                if (!value.startsWith('-')) {
                    value = '+' + value; // Add '+' in front of positive values
                }
                content += `${value}\n`;
            });

            const blob = new Blob([content], { type: "text/plain" });
            const link = document.createElement("a");
            link.href = URL.createObjectURL(blob);
            link.download = filename;
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        }
    });
});
