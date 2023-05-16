var cities = {
    continent: "North America",
    country: "USA",
    state: "California",
    county: [
        {
            city: "LA",
            area: "LA county"
        },
        {
            city: "Anaheim",
            area: "Orange county"
        }
    ]
};

document.write(cities.county[1].city);