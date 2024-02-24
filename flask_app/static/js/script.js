const ingredient_lookup = async (table, search_string) => {
    let tableBody = table.querySelector("tbody");
    let res = await fetch(
        `https://api.spoonacular.com/food/ingredients/search?apiKey=e5435bd9712a45208d0da9ad28db16b2&query=${search_string}`
    );
    let data = await res.json();
    let { results } = data;
    tableBody.innerHTML = "";
    for (const row of results) {
        const rowElement = document.createElement("tr");
        let idCellElement = document.createElement("td");
        idCellElement.textContent = row.id;
        rowElement.appendChild(idCellElement);

        const nameCellElement = document.createElement("td");
        nameCellElement.textContent = row.name;
        rowElement.appendChild(nameCellElement);

        const imageCellElement = document.createElement("td");
        const imageCellImage = document.createElement("img");
        imageCellImage.src =
            "https://spoonacular.com/cdn/ingredients_100x100/" + row.image;
        imageCellImage.style = "width: 100px; height: auto;";
        imageCellElement.appendChild(imageCellImage);
        rowElement.appendChild(imageCellElement);

        const actionsCellElement = document.createElement("td");
        const actionsAddToSpellbook = document.createElement("a");
        actionsAddToSpellbook.textContent = "Convert to Spell";
        actionsAddToSpellbook.href = "/ingredients/show_one/" + row.id;

        actionsCellElement.appendChild(actionsAddToSpellbook);
        rowElement.appendChild(actionsCellElement);
        tableBody.appendChild(rowElement);
    }
};

const recipe_lookup = async (table, search_string) => {
    let tableBody = table.querySelector("tbody");
    let res = await fetch(
        `https://api.spoonacular.com/recipes/complexSearch?apiKey=e5435bd9712a45208d0da9ad28db16b2&query=${search_string}`
    );
    let data = await res.json();
    let { results } = data;
    tableBody.innerHTML = "";
    for (const row of results) {
        const rowElement = document.createElement("tr");
        let idCellElement = document.createElement("td");
        idCellElement.textContent = row.id;
        rowElement.appendChild(idCellElement);

        const nameCellElement = document.createElement("td");
        nameCellElement.textContent = row.title;
        rowElement.appendChild(nameCellElement);

        const imageCellElement = document.createElement("td");
        const imageCellImage = document.createElement("img");
        imageCellImage.src = row.image;
        imageCellElement.appendChild(imageCellImage);
        rowElement.appendChild(imageCellElement);

        const actionsCellElement = document.createElement("td");
        const actionsAddToBosses = document.createElement("a");
        actionsAddToBosses.textContent = "Convert to Boss";
        actionsAddToBosses.href = "/recipes/show_one/" + row.id;
        const actionsPipeElement = document.createElement("span");
        actionsPipeElement.textContent = " | ";
        const actionsAddToFavorites = document.createElement("a");
        actionsAddToFavorites.textContent = "Add to Favorites";
        actionsAddToFavorites.href = "/recipes/add_favorite/" + row.id;

        actionsCellElement.appendChild(actionsAddToBosses);
        actionsCellElement.appendChild(actionsPipeElement);
        actionsCellElement.appendChild(actionsAddToFavorites);
        rowElement.appendChild(actionsCellElement);
        tableBody.appendChild(rowElement);
    }
};

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
