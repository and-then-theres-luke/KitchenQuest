const ingredient_lookup = async (table, search_string) => {
    let tableBody = table.querySelector("tbody");
    let res = await fetch(
        `https://api.spoonacular.com/food/ingredients/search?apiKey=e5435bd9712a45208d0da9ad28db16b2&query=${search_string}`
    );
    let data = await res.json();
    let { results } = data;
    // Clear the data
    tableBody.innerHTML = "";
    for (const row of results) {
        // Note here how we are defining a variable row that gets referenced again below, we are doing something for each something for each something in a row.
        const rowElement = document.createElement("tr"); // This CREATES the row
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
        imageCellElement.appendChild(imageCellImage);
        rowElement.appendChild(imageCellElement);

        const actionsCellElement = document.createElement("td");
        const actionsAddToPantry = document.createElement("a");
        actionsAddToPantry.textContent = "Add To Pantry";
        actionsAddToPantry.href = "/recipes/show_one/" + row.id;
        // I want to make a form here to get a button to jump to the add ingredient page
        actionsCellElement.appendChild(actionsAddToPantry);
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
    // Clear the data
    tableBody.innerHTML = "";
    for (const row of results) {
        const rowElement = document.createElement("tr"); // This CREATES the row
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
        const actionsAddToPantry = document.createElement("a");
        actionsAddToPantry.textContent = "Add To Pantry";
        actionsAddToPantry.href = "/recipes/show_one/" + row.id;
        // I want to make a form here to get a button to jump to the add ingredient page
        actionsCellElement.appendChild(actionsAddToPantry);
        rowElement.appendChild(actionsCellElement);
        tableBody.appendChild(rowElement);
    }
};
