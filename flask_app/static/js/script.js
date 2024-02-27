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

// const construct_ingredient_row = (table, one_ingredient, spellbook) => {
//     // cycle through ingredients, do check
//     // let tableBody = table.querySelector("tbody");

//     //construct row
//     const rowElement = document.createElement("tr");

//     //construct name cell
//     const nameCellElement = document.createElement("td");
//     nameCellElement.innerText = one_ingredient.name;
//     rowElement.appendChild(nameCellElement);

//     let ing_found = true;
//     for (
//         spell_count = 0;
//         spell_count < one_ingredient.extendedIngredients.length - 1;
//         spell_count++
//     ) {
//         if (one_ingredient["id"] == one_ingredient.api_ingredient_id) {
//             ing_found = true;
//         }
//     }

    const chargesCellElement = document.createElement("td");

    let style_box = "color: red;";
    const actionCellElement = document.createElement("td");
    if (ing_found == true) {
        style_box = "color: black";
    } else {
        const actionCellElementAdd = document.createElement("a");
        actionCellElementAdd.src =
            "/ingredients/show_one/" + spellbook[spell_count].api_ingredient_id;
        actionCellElementAdd.innerText = "Add to Spells";
        actionCellElement.appendChild(actionCellElementAdd);
    }
    rowElement.appendChild(actionCellElement);
    tableBody.appendChild(rowElement);
};

const construct_spell_table = (spellbook, table) => {
    let tableBody = table.querySelector("tbody");
    // Function to sort the table before constructing it.
    let new_spellbook = [];
    for (let count = 0; (spellbook.length = 0); count++) {
        for (
            let inner_count = 0;
            count < spellbook.length - 1;
            inner_count++
        ) {}
    }
    tableBody.innerHTML = "";
    for (index = 0; index < spellbook.length - 1; index++) {
        const rowElement = document.createElement("tr");
        let nameCellElement = document.createElement("td");
        nameCellElement.textContent = spellbook[index].id;
        rowElement.appendChild(nameCellElement);

        let expirationBarElement = document.createElement("div");
        // Function to construct the status bar
        expiration_bars(expirationBarElement, spellbook[index].expiration_date);
        rowElement.appendChild(expirationBarElement);
        tableBody.appendChild(rowElement);
    }
};

const expiration_bars = (statusdiv, expiration_date) => {
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

    style_box = "height: 10px;";
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
    statusdiv.style = style_box;
};

const calculate_charges = (first_value, second_value, table_element) => {
    console.log(first_value.value);
    console.log(second_value);
    console.log(table_element.value);
    table_element.innerText = first_value / second_value.value;
};

const test_script = () => {};
