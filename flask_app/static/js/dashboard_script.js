const construct_spell_table = (spellbook, table) => {
    console.log("Constructor is running!");
    let tableBody = table.querySelector("tbody");
    // Function to sort the table before constructing it.
    tableBody.innerHTML = "";
    for (const spell of spellbook) {
        const rowElement = document.createElement("tr");
        let nameCellElement = document.createElement("td");
        nameCellElement.textContent = spell.id;
        rowElement.appendChild(nameCellElement);

        let expirationBarElement = document.createElement("div");
        // Function to construct the status bar
        expiration_bars(expirationBarElement, spell.expiration_date);
        rowElement.appendChild(expirationBarElement);
        tableBody.appendChild(rowElement);
    }
};

const expiration_bars = (statusbar, expiration_date) => {
    let date = new Date();
    let day = date.getDate();
    let month = date.getMonth() + 1;
    if (month < 10) {
        month = "0" + month;
    }
    expiration_date = expiration_date.replaceAll("-", "");
    let year = date.getFullYear();
    let current_date = `${year}${month}${day}`;

    let days_to_expire = Math.abs(expiration_date - current_date);
    console.log(days_to_expire);

    style_box = "height: 100px;";
    if (days_to_expire > 5) {
        style_box = style_box + "background-color : green;";
    } else if (days_to_expire <= 5 && days_to_expire > 3) {
        style_box = style_box + "background-color : yellow;";
    } else if (days_to_expire <= 3) {
        style_box = style_box + "background-color : red;";
    }
    style_width = days_to_expire * 100;
    if (style_width > 600) {
        style_width = 600;
    }
    style_box = style_box + `width: ${style_width}px;`;
    statusbar.style = style_box;
};

construct_spell_table();
