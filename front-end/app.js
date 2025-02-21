document.addEventListener("DOMContentLoaded", function () {
    // Get the store divs
    var willys_div = document.getElementById("willys");
    var coop_div = document.getElementById("coop");
    var hemkop_div = document.getElementById("hemkop");

    // Function to create and display the table from CSV content
    function createTableFromCSV(content, parentDiv) {
        const rows = content.split("\n").map(row => row.split(","));
        const table = document.createElement("table");
        table.border = "1";
        
        // Create table headers
        const headerRow = document.createElement("tr");
        const headers = ["Product", "Price", "Quantity", "Image"];
        headers.forEach(header => {
            const th = document.createElement("th");
            th.textContent = header;
            headerRow.appendChild(th);
        });
        table.appendChild(headerRow);

        // Parse CSV and create table rows
        rows.forEach(row => {
            if (row.length >= 4) {  // Ensure there are enough columns
                const tr = document.createElement("tr");

                // Product Name
                const productTd = document.createElement("td");
                productTd.textContent = row[0];
                tr.appendChild(productTd);

                // Price
                const priceTd = document.createElement("td");
                priceTd.textContent = row[1];
                tr.appendChild(priceTd);

                // Quantity
                const quantityTd = document.createElement("td");
                quantityTd.textContent = row[2];
                tr.appendChild(quantityTd);

                // Image
                const imageTd = document.createElement("td");
                const img = document.createElement("img");
                img.src = row[3].replace(/"/g, "");  // Remove potential quotes around the image URL
                img.alt = row[0];  // Alt text as product name
                img.style.width = "100px";  // Set a consistent width for images
                imageTd.appendChild(img);
                tr.appendChild(imageTd);

                table.appendChild(tr);
            }
        });

        parentDiv.appendChild(table);
    }

    // Fetch Coop CSV
    fetch("output/coop_promos_w8.csv")
        .then(response => response.text())
        .then(content => {
            createTableFromCSV(content, coop_div);
        })
        .catch(error => console.error("Error loading Coop CSV:", error));

    // Fetch Willys CSV
    fetch("output/willys_promos_w8.csv")
        .then(response => response.text())
        .then(content => {
            createTableFromCSV(content, willys_div);
        })
        .catch(error => console.error("Error loading Willys CSV:", error));

    // Fetch Hemköp CSV (assuming you have a hemkop_promos_w8.csv file)
    fetch("output/hemkop_promos_w8.csv")
        .then(response => response.text())
        .then(content => {
            createTableFromCSV(content, hemkop_div);
        })
        .catch(error => console.error("Error loading Hemköp CSV:", error));
});
