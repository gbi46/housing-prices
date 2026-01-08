# Project Initialization

Initialize the project using Poetry:
```bash
poetry init
poetry add scikit-learn pandas
```

# Run project

```bash
poetry run python main.py
```

## What do we see in the output?

After running the program, a table appears in the console.
This table shows information about housing in different parts of California.

Each row describes one area.
Each column shows a simple fact about that area, such as income, number of people,
or average house price.

### Column meanings (in simple words)

- **MedInc** — How much money people earn on average  
- **HouseAge** — How old the houses are  
- **AveRooms** — How many rooms homes usually have  
- **AveBedrms** — How many bedrooms homes usually have  
- **Population** — How many people live there  
- **AveOccup** — How many people live in one home  
- **Latitude** — Where the area is on the map (north–south)  
- **Longitude** — Where the area is on the map (east–west)  
- **MedHouseVal** — Average house price

### Why this matters

This table helps understand how living conditions and location
are connected to house prices.
