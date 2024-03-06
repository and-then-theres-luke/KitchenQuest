expiration_bars_test = (expiration_date) => {
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
};

expiration_bars_test("2024-03-07");
