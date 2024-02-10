const get_ingredient_data = async(search_string) => {
    let res = await fetch(`https://api.spoonacular.com/food/ingredients/search?apiKey=e5435bd9712a45208d0da9ad28db16b2&query=${search_string}`)
    let data = await res.json()
    let { results } = data
    for(let count = 0; count < results.length; count++) {
        ingredient_search_results.innerText += results[count]
    }
}

// https://spoonacular.com/cdn/ingredients_{SIZE}/, where {SIZE} is one of the following:

// 100x100
// 250x250
// 500x500
// So for "apple.jpg" the full path for 100x100 is https://spoonacular.com/cdn/ingredients_100x100/apple.jpg